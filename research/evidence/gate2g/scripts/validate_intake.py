#!/usr/bin/env python3
"""Validate an incoming biological/environmental data file against Gate 2G intake expectations.

Read-only with respect to source files. Writes a JSON report to --out.
Supports CSV and XLSX (xlsx requires openpyxl; if unavailable, reports limitation).

This tool performs data-integrity checks only. It NEVER modifies source files,
NEVER infers biological meaning, NEVER creates bloom labels, and NEVER treats
missing/unsampled records as absence of blooms.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REQUIRED_BIO_FIELDS = ["sample_date", "location", "depth_m"]
RECOMMENDED_BIO_FIELDS = [
    "sample_time", "latitude", "longitude", "sample_id", "replicate_id", "taxon_name",
    "taxon_rank", "cell_count", "cell_count_unit", "biovolume", "biovolume_unit",
    "biomass", "biomass_unit", "chlorophyll_a", "chlorophyll_a_unit", "microcystin",
    "microcystin_unit", "toxin_method", "detection_limit", "detection_limit_unit",
    "qualifier", "method", "qa_flag", "notes",
]
NUMERIC_FIELDS = [
    "latitude", "longitude", "depth_m", "cell_count", "biovolume", "biomass",
    "chlorophyll_a", "microcystin", "detection_limit",
]
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_table(path: Path):
    suf = path.suffix.lower()
    if suf == ".csv":
        with path.open(newline="", encoding="utf-8-sig", errors="replace") as f:
            reader = csv.DictReader(f)
            headers = list(reader.fieldnames or [])
            rows = list(reader)
        return rows, headers
    if suf in {".xlsx", ".xlsm"}:
        try:
            import openpyxl  # type: ignore
        except Exception as e:
            raise RuntimeError(f"XLSX support requires openpyxl: {e}")
        wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
        ws = wb[wb.sheetnames[0]]
        it = ws.iter_rows(values_only=True)
        headers = [str(h).strip() if h is not None else "" for h in next(it, [])]
        rows = []
        for r in it:
            row = {headers[i]: ("" if v is None else v) for i in range(min(len(headers), len(r)))}
            if any(str(v).strip() != "" for v in row.values()):
                rows.append(row)
        wb.close()
        return rows, headers
    raise RuntimeError(f"Unsupported file type: {suf}")


def is_missing(v: Any) -> bool:
    if v is None:
        return True
    if isinstance(v, str):
        s = v.strip()
        return s == "" or s.lower() in {"na", "n/a", "nan", "null", "none"}
    return False


def parse_float_maybe(v: Any):
    if is_missing(v):
        return None
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        return float(v)
    s = str(v).strip()
    try:
        return float(s)
    except Exception:
        return "INVALID"


def validate_rows(rows, headers, kind: str):
    errors = []
    warnings = []
    lower = {h.strip().lower(): h for h in headers if h is not None}
    dup_cols = len([h for h in headers if h]) - len(set(h.strip().lower() for h in headers if h))
    empty_rows = sum(1 for r in rows if all(is_missing(v) for v in r.values()))

    missing_required = [f for f in REQUIRED_BIO_FIELDS if f not in lower] if kind == "biological" else []
    missing_recommended = [f for f in RECOMMENDED_BIO_FIELDS if f not in lower] if kind == "biological" else []

    if dup_cols:
        warnings.append("Duplicate column names detected (case-insensitive)")
    if kind == "biological" and missing_required:
        warnings.append("Missing required biological fields; file may need mapping/template")

    # row-level checks
    invalid_dates = []
    invalid_numeric = {}
    qualifier_without_limit = 0
    detection_limit_without_qualifier_or_value = 0
    duplicate_keys = 0
    seen_keys = set()

    for i, r in enumerate(rows, start=2):  # header is line 1
        if kind == "biological" and "sample_date" in lower:
            dv = r.get(lower["sample_date"], "")
            if not is_missing(dv):
                s = str(dv).strip()
                if DATE_RE.match(s):
                    try:
                        datetime.strptime(s, "%Y-%m-%d")
                    except Exception:
                        invalid_dates.append(i)
                else:
                    try:
                        # allow datetime parse but warn non-ISO
                        datetime.fromisoformat(s.replace("Z", "+00:00"))
                        warnings.append(f"Row {i}: sample_date not YYYY-MM-DD format: {s!r}")
                    except Exception:
                        invalid_dates.append(i)
        for nf in NUMERIC_FIELDS:
            if nf in lower:
                pv = parse_float_maybe(r.get(lower[nf], ""))
                if pv == "INVALID":
                    invalid_numeric.setdefault(nf, []).append(i)
        # qualifier/detection limit consistency (warnings only)
        qual = str(r.get(lower.get("qualifier", ""), "")).strip() if "qualifier" in lower else ""
        dl = r.get(lower.get("detection_limit", ""), "") if "detection_limit" in lower else ""
        meas_fields = ["microcystin", "chlorophyll_a", "cell_count", "biovolume", "biomass"]
        has_meas = any(not is_missing(r.get(lower.get(m, ""), "")) for m in meas_fields if m in lower)
        if qual and is_missing(dl) and ("<" in qual or "lod" in qual.lower() or "nd" in qual.lower()):
            qualifier_without_limit += 1
        if (not is_missing(dl)) and (not qual) and (not has_meas):
            detection_limit_without_qualifier_or_value += 1

        # duplicate key heuristic
        if kind == "biological":
            key_parts = []
            for k in ["sample_date", "location", "depth_m", "sample_id", "taxon_name", "replicate_id"]:
                key_parts.append(str(r.get(lower.get(k, ""), "")).strip().lower())
            key = tuple(key_parts)
            if any(key_parts):
                if key in seen_keys:
                    duplicate_keys += 1
                else:
                    seen_keys.add(key)

    if invalid_dates:
        errors.append(f"Invalid sample_date values at rows: {invalid_dates[:20]}{'...' if len(invalid_dates)>20 else ''}")
    for nf, rows_bad in invalid_numeric.items():
        errors.append(f"Invalid numeric values in {nf} at rows: {rows_bad[:20]}{'...' if len(rows_bad)>20 else ''}")
    if qualifier_without_limit:
        warnings.append(f"{qualifier_without_limit} rows have qualifier suggesting <LOD/ND but no detection_limit")
    if detection_limit_without_qualifier_or_value:
        warnings.append(f"{detection_limit_without_qualifier_or_value} rows have detection_limit but no qualifier/value")
    if duplicate_keys:
        warnings.append(f"{duplicate_keys} potential duplicate biological rows by key heuristic (date/location/depth/sample/taxon/replicate)")

    # fields that look like measurements but missing units
    unit_pairs = [("cell_count","cell_count_unit"),("biovolume","biovolume_unit"),("biomass","biomass_unit"),("chlorophyll_a","chlorophyll_a_unit"),("microcystin","microcystin_unit")]
    for meas, unit in unit_pairs:
        if meas in lower and unit not in lower:
            warnings.append(f"Measurement field {meas} present but {unit} missing")
        if meas in lower and unit in lower:
            missing_unit = 0
            for r in rows:
                if not is_missing(r.get(lower[meas], "")) and is_missing(r.get(lower[unit], "")):
                    missing_unit += 1
            if missing_unit:
                warnings.append(f"{missing_unit} rows have {meas} value but missing {unit}")

    summary = {
        "rows": len(rows),
        "columns": headers,
        "duplicate_column_names_case_insensitive": dup_cols,
        "empty_rows": empty_rows,
        "missing_required_biological_fields": missing_required,
        "missing_recommended_biological_fields": missing_recommended,
        "invalid_sample_date_rows": len(invalid_dates),
        "invalid_numeric_fields": {k: len(v) for k, v in invalid_numeric.items()},
        "potential_duplicate_rows": duplicate_keys,
    }
    if kind == "biological" and "sample_date" in lower:
        sample_dates = [str(r.get(lower["sample_date"], "")).strip() for r in rows]
        summary["sample_date_nonempty_count"] = sum(1 for d in sample_dates if d)
    return summary, errors, warnings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", help="Input CSV/XLSX file (read-only)")
    ap.add_argument("--out", required=True, help="JSON report output path")
    ap.add_argument("--kind", choices=["biological", "environmental", "unknown"], default="unknown")
    args = ap.parse_args()
    p = Path(args.input)
    report = {
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "input": str(p),
        "kind": args.kind,
        "exists": p.exists(),
        "sha256": sha256(p) if p.exists() and p.is_file() else None,
        "size_bytes": p.stat().st_size if p.exists() and p.is_file() else None,
        "status": "ok",
        "errors": [],
        "warnings": [],
        "summary": {},
        "provenance_note": "Source file not modified. This report is intake-validation only; no biological interpretation or labels generated.",
    }
    if not p.exists():
        report["status"] = "error"
        report["errors"].append("Input file not found")
    else:
        try:
            rows, headers = read_table(p)
            summary, errors, warnings = validate_rows(rows, headers, args.kind)
            report["summary"] = summary
            report["errors"].extend(errors)
            report["warnings"].extend(warnings)
            if errors:
                report["status"] = "error"
        except Exception as e:
            report["status"] = "error"
            report["errors"].append(str(e))

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({"status": report["status"], "out": str(out), "errors": report["errors"], "warnings": report["warnings"]}))
    return 0 if report["status"] == "ok" else 2


if __name__ == "__main__":
    raise SystemExit(main())
