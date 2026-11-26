#!/usr/bin/env python3
"""Controlled EDI acquisition helper for Lake Mendota packages.

Safety properties
-----------------
- Requires EDI_API_KEY in the environment. The key is never printed, logged,
  written to disk, or placed in a URL. It is exchanged once for a short-lived
  EDI token via the documented IAM endpoint.
- Metadata is fetched first; data entities are downloaded only when
  --include-data and an explicit --entity selector are supplied.
- Never overwrites an existing complete file. Interrupted downloads resume via
  HTTP Range where supported; otherwise the partial file is restarted.
- Retries only transient failures (429/5xx/network) a small number of times.
  It does not retry 401/403/404.
- Refuses any data URL outside the EDI PASTA data endpoint.
- Writes a provenance CSV with source URL (no key), timestamps, sizes, SHA256,
  EML checksum (when present), HTTP status, and status.

This script is prepared but intentionally not executed in Sprint 4K because no
authorised EDI key is available. See ../EDI_USER_ACCESS_GUIDE.md.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

PASTA = "https://pasta.lternet.edu/package"
AUTH_TOKEN_URL = "https://auth.edirepository.org/auth/v1/key"
USER_AGENT = "EcoSentinel-EDI-Acquire/1.0 (controlled research acquisition)"

PACKAGES = {
    "88.31": {"scope": "knb-lter-ntl", "identifier": "88", "revision": "31"},
    "129.42": {"scope": "knb-lter-ntl", "identifier": "129", "revision": "42"},
    "130.29": {"scope": "knb-lter-ntl", "identifier": "130", "revision": "29"},
    "415.2": {"scope": "knb-lter-ntl", "identifier": "415", "revision": "2"},
}


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


def eprint(*args) -> None:
    print(*args, file=sys.stderr)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def safe_name(text: str) -> str:
    text = re.sub(r"[^A-Za-z0-9._-]+", "_", text or "entity").strip("_")
    return text[:120] or "entity"


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def parse_eml_inventory(eml_path: Path) -> list[dict]:
    root = ET.parse(eml_path).getroot()
    entities: list[dict] = []
    for node in root.iter():
        if local_name(node.tag) != "dataTable":
            continue
        item = {
            "entity_name": "",
            "entity_id": "",
            "url": "",
            "size_bytes": "",
            "checksum": "",
            "checksum_algorithm": "",
            "format": "",
        }
        for child in node.iter():
            name = local_name(child.tag)
            text = (child.text or "").strip()
            if name == "entityName" and text and not item["entity_name"]:
                item["entity_name"] = text
            elif name == "url" and text and not item["url"]:
                item["url"] = text
            elif name == "size" and text and not item["size_bytes"]:
                item["size_bytes"] = text
            elif name == "checksum" and text and not item["checksum"]:
                item["checksum"] = text
                item["checksum_algorithm"] = (child.attrib.get("algorithm") or "").upper()
            elif name == "formatName" and text and not item["format"]:
                item["format"] = text
        if item["url"]:
            item["entity_id"] = item["url"].rstrip("/").split("/")[-1]
            entities.append(item)
    return entities


def verify_checksum(path: Path, expected: str, algorithm: str) -> tuple[bool | None, str]:
    expected = (expected or "").strip()
    algorithm = (algorithm or "").upper().replace("-", "")
    if not expected:
        return None, "no EML checksum"
    if algorithm in ("SHA256", "SHA256SUM"):
        actual = sha256_file(path)
    elif algorithm in ("SHA1",):
        h = hashlib.sha1()
        with path.open("rb") as fh:
            for chunk in iter(lambda: fh.read(1024 * 1024), b""):
                h.update(chunk)
        actual = h.hexdigest()
    elif algorithm in ("MD5",):
        h = hashlib.md5()
        with path.open("rb") as fh:
            for chunk in iter(lambda: fh.read(1024 * 1024), b""):
                h.update(chunk)
        actual = h.hexdigest()
    else:
        return None, f"unsupported EML checksum algorithm: {algorithm or 'unknown'}"
    return actual.lower() == expected.lower(), f"EML {algorithm} expected={expected} actual={actual}"


class EdiClient:
    def __init__(self, key: str, retries: int = 2):
        self._key = key
        self._token = ""
        self.retries = retries
        self._authenticate()

    def _authenticate(self) -> None:
        payload = json.dumps({"key": self._key}).encode("utf-8")
        req = urllib.request.Request(
            AUTH_TOKEN_URL,
            data=payload,
            method="POST",
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "User-Agent": USER_AGENT,
            },
        )
        with urllib.request.urlopen(req, timeout=60) as resp:
            obj = json.loads(resp.read().decode("utf-8"))
        token = obj.get("edi-token")
        if not token:
            raise RuntimeError("IAM response did not contain an edi-token")
        self._token = token

    def _open(self, url: str, accept: str, range_start: int | None = None):
        headers = {
            "User-Agent": USER_AGENT,
            "Accept": accept,
            "Cookie": f"edi-token={self._token}",
        }
        if range_start:
            headers["Range"] = f"bytes={range_start}-"
        return urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=120)

    def fetch_bytes(self, url: str, accept: str = "*/*", range_start: int | None = None) -> tuple[bytes, int, dict]:
        last_error: Exception | None = None
        for attempt in range(self.retries + 1):
            try:
                with self._open(url, accept, range_start) as resp:
                    body = resp.read()
                    return body, resp.status, dict(resp.headers)
            except urllib.error.HTTPError as exc:
                last_error = exc
                if exc.code == 401 and attempt == 0:
                    self._authenticate()
                    continue
                if exc.code in (403, 404):
                    raise RuntimeError(f"HTTP {exc.code} for {url}; not retrying") from exc
                if exc.code in (429, 500, 502, 503, 504) and attempt < self.retries:
                    time.sleep(5 * (attempt + 1))
                    continue
                raise
            except (urllib.error.URLError, TimeoutError) as exc:
                last_error = exc
                if attempt < self.retries:
                    time.sleep(5 * (attempt + 1))
                    continue
                raise
        raise RuntimeError(f"request failed after retries: {last_error}")


def append_provenance(path: Path, row: dict) -> None:
    fields = [
        "timestamp_utc", "package", "kind", "entity_name", "entity_id",
        "source_url", "local_path", "bytes", "sha256", "eml_checksum",
        "eml_checksum_algorithm", "http_status", "content_type", "resumed",
        "status", "notes",
    ]
    new = not path.exists()
    with path.open("a", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        if new:
            writer.writeheader()
        writer.writerow({k: row.get(k, "") for k in fields})


def download_entity(client: EdiClient, pkg: str, entity: dict, outdir: Path,
                    max_bytes: int, provenance: Path) -> None:
    url = entity["url"]
    if not url.startswith(PASTA + "/data/"):
        raise RuntimeError(f"refusing non-PASTA data URL: {url}")

    expected_size = int(entity["size_bytes"]) if entity["size_bytes"].isdigit() else None
    if max_bytes and expected_size and expected_size > max_bytes:
        eprint(f"SKIP {pkg} {entity['entity_id']}: expected {expected_size} B exceeds --max-bytes {max_bytes}")
        append_provenance(provenance, {
            "timestamp_utc": utcnow(), "package": pkg, "kind": "data",
            "entity_name": entity["entity_name"], "entity_id": entity["entity_id"],
            "source_url": url, "status": "skipped_size_cap",
            "notes": f"expected_bytes={expected_size}; max_bytes={max_bytes}",
        })
        return

    pkg_dir = outdir / pkg
    pkg_dir.mkdir(parents=True, exist_ok=True)
    ext = ".csv" if "csv" in (entity.get("format") or "").lower() else ".dat"
    final = pkg_dir / f"{safe_name(entity['entity_name'])}__{entity['entity_id']}{ext}"
    part = final.with_suffix(final.suffix + ".part")

    if final.exists():
        digest = sha256_file(final)
        ok, note = verify_checksum(final, entity.get("checksum", ""), entity.get("checksum_algorithm", ""))
        append_provenance(provenance, {
            "timestamp_utc": utcnow(), "package": pkg, "kind": "data",
            "entity_name": entity["entity_name"], "entity_id": entity["entity_id"],
            "source_url": url, "local_path": str(final), "bytes": final.stat().st_size,
            "sha256": digest, "eml_checksum": entity.get("checksum", ""),
            "eml_checksum_algorithm": entity.get("checksum_algorithm", ""),
            "resumed": False, "status": "skipped_exists" if ok is not False else "exists_checksum_mismatch",
            "notes": note,
        })
        return

    # A previously interrupted download may already contain the full entity.
    # Verify and finalize it before issuing another Range request (avoids 416).
    if part.exists() and expected_size and part.stat().st_size == expected_size:
        digest = sha256_file(part)
        ok, note = verify_checksum(part, entity.get("checksum", ""), entity.get("checksum_algorithm", ""))
        if ok is not False:
            part.replace(final)
            append_provenance(provenance, {
                "timestamp_utc": utcnow(), "package": pkg, "kind": "data",
                "entity_name": entity["entity_name"], "entity_id": entity["entity_id"],
                "source_url": url, "local_path": str(final), "bytes": final.stat().st_size,
                "sha256": digest, "eml_checksum": entity.get("checksum", ""),
                "eml_checksum_algorithm": entity.get("checksum_algorithm", ""),
                "resumed": True, "status": "verified_from_complete_part", "notes": note,
            })
            eprint(f"OK {pkg} {entity['entity_id']} -> {final} (recovered complete .part)")
            return

    resumed = False
    if part.exists() and part.stat().st_size > 0:
        resumed = True
        start = part.stat().st_size
        body, status, headers = client.fetch_bytes(url, range_start=start)
        if status == 206:
            with part.open("ab") as fh:
                fh.write(body)
        else:
            # Server ignored Range; restart from scratch in the .part file.
            part.write_bytes(body)
            resumed = False
    else:
        body, status, headers = client.fetch_bytes(url)
        part.write_bytes(body)

    digest = sha256_file(part)
    ok, note = verify_checksum(part, entity.get("checksum", ""), entity.get("checksum_algorithm", ""))
    if expected_size and part.stat().st_size != expected_size:
        ok = False
        note = (note + "; " if note else "") + f"size expected={expected_size} actual={part.stat().st_size}"
    if ok is False:
        mismatch = part.with_suffix(part.suffix + ".mismatch")
        if mismatch.exists():
            mismatch = part.with_suffix(part.suffix + f".mismatch.{int(time.time())}")
        part.replace(mismatch)
        append_provenance(provenance, {
            "timestamp_utc": utcnow(), "package": pkg, "kind": "data",
            "entity_name": entity["entity_name"], "entity_id": entity["entity_id"],
            "source_url": url, "local_path": str(mismatch), "bytes": mismatch.stat().st_size,
            "sha256": digest, "eml_checksum": entity.get("checksum", ""),
            "eml_checksum_algorithm": entity.get("checksum_algorithm", ""),
            "http_status": status, "content_type": headers.get("Content-Type", ""),
            "resumed": resumed, "status": "checksum_or_size_mismatch", "notes": note,
        })
        raise RuntimeError(f"integrity mismatch for {entity['entity_id']}; preserved as {mismatch}")

    part.replace(final)
    append_provenance(provenance, {
        "timestamp_utc": utcnow(), "package": pkg, "kind": "data",
        "entity_name": entity["entity_name"], "entity_id": entity["entity_id"],
        "source_url": url, "local_path": str(final), "bytes": final.stat().st_size,
        "sha256": digest, "eml_checksum": entity.get("checksum", ""),
        "eml_checksum_algorithm": entity.get("checksum_algorithm", ""),
        "http_status": status, "content_type": headers.get("Content-Type", ""),
        "resumed": resumed, "status": "verified", "notes": note,
    })
    eprint(f"OK {pkg} {entity['entity_id']} -> {final} ({final.stat().st_size} B)")


def main() -> int:
    parser = argparse.ArgumentParser(description="Controlled EDI Mendota acquisition (metadata-first).")
    parser.add_argument("--package", action="append", required=True,
                        choices=sorted(PACKAGES) + ["all"], help="Package(s) to process")
    parser.add_argument("--outdir", default="research/evidence/sprint_4k_mendota_authorised_access/acquisition")
    parser.add_argument("--include-data", action="store_true",
                        help="Permit data downloads. Requires --entity.")
    parser.add_argument("--entity", action="append", default=[],
                        help="Explicit entity ID or URL suffix to download (repeatable)")
    parser.add_argument("--list-only", action="store_true", help="Metadata + inventory only")
    parser.add_argument("--max-bytes", type=int, default=100_000_000,
                        help="Skip entities expected larger than this (0 = no cap)")
    parser.add_argument("--retries", type=int, default=2)
    args = parser.parse_args()

    key = os.environ.get("EDI_API_KEY", "").strip()
    if not key:
        eprint("EDI_API_KEY is not set. Create an authorised EDI API key and export it")
        eprint("in your own shell (do not paste it into chat or commit it). See")
        eprint("research/evidence/sprint_4k_mendota_authorised_access/EDI_USER_ACCESS_GUIDE.md")
        return 2

    packages = sorted(PACKAGES) if "all" in args.package else sorted(set(args.package))
    outdir = Path(args.outdir).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    provenance = outdir / "provenance.csv"
    client = EdiClient(key, retries=max(0, args.retries))

    for pkg in packages:
        meta = PACKAGES[pkg]
        pkg_dir = outdir / pkg
        pkg_dir.mkdir(parents=True, exist_ok=True)
        meta_url = f"{PASTA}/metadata/eml/{meta['scope']}/{meta['identifier']}/{meta['revision']}"
        eprint(f"metadata {pkg}: {meta_url}")
        body, status, headers = client.fetch_bytes(meta_url, accept="application/xml")
        meta_path = pkg_dir / f"metadata_{pkg}.xml"
        if meta_path.exists():
            eprint(f"SKIP existing metadata {meta_path} (not overwritten)")
        else:
            meta_path.write_bytes(body)
            append_provenance(provenance, {
                "timestamp_utc": utcnow(), "package": pkg, "kind": "metadata",
                "entity_name": "EML metadata", "entity_id": "",
                "source_url": meta_url, "local_path": str(meta_path),
                "bytes": len(body), "sha256": hashlib.sha256(body).hexdigest(),
                "http_status": status, "content_type": headers.get("Content-Type", ""),
                "status": "verified",
            })

        entities = parse_eml_inventory(meta_path)
        inv_path = pkg_dir / f"entity_inventory_{pkg}.csv"
        with inv_path.open("w", newline="", encoding="utf-8") as fh:
            fields = ["entity_name", "entity_id", "url", "size_bytes", "checksum",
                      "checksum_algorithm", "format"]
            writer = csv.DictWriter(fh, fieldnames=fields)
            writer.writeheader()
            writer.writerows(entities)
        eprint(f"inventory {pkg}: {len(entities)} entities -> {inv_path}")
        for ent in entities:
            eprint(f"  {ent['entity_id']}  {ent['size_bytes'] or '?'} B  {ent['entity_name'][:80]}")

        if args.list_only or not args.include_data:
            continue
        if not args.entity:
            eprint(f"REFUSING data download for {pkg}: --include-data requires explicit --entity selectors")
            continue
        selectors = set(args.entity)
        chosen = [e for e in entities if e["entity_id"] in selectors or any(s in e["url"] for s in selectors)]
        if not chosen:
            eprint(f"no entities matched --entity for {pkg}")
            continue
        for ent in chosen:
            download_entity(client, pkg, ent, outdir, args.max_bytes, provenance)

    eprint("done")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as exc:
        eprint(f"ERROR: {exc}")
        raise SystemExit(1)
