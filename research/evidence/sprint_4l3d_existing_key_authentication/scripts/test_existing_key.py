#!/usr/bin/env python3
"""Minimal, secret-safe EDI authentication test for an existing API key.

Reads EDI_API_KEY from the process environment only. It never prints, logs,
stores or transmits the key anywhere except the official EDI IAM endpoint.
It exchanges the key for a short-lived token, then makes one small PASTA
metadata request to verify that the token is accepted.

Exit codes:
  0  token exchange succeeded and PASTA metadata read succeeded
  2  local configuration failure (no EDI_API_KEY)
  3  authentication failure (HTTP 400/401, missing token, malformed response)
  4  authorization failure (PASTA 403)
  5  networking/TLS/timeout failure
  6  unexpected server/service failure
"""

from __future__ import annotations

import json
import os
import ssl
import sys
import urllib.error
import urllib.request

AUTH_URL = "https://auth.edirepository.org/auth/v1/key"
META_URL = "https://pasta.lternet.edu/package/metadata/eml/knb-lter-ntl/88/31"
UA = "EcoSentinel-AuthTest/1.0 (controlled research authentication check)"
CTX = ssl.create_default_context()


def fail(code: int, label: str, detail: str = "") -> None:
    print(f"{label}" + (f": {detail}" if detail else ""))
    raise SystemExit(code)


def main() -> int:
    key = os.environ.get("EDI_API_KEY", "").strip()
    if not key:
        fail(2, "LOCAL_CONFIGURATION_FAILURE", "EDI_API_KEY is not set in this process")

    payload = json.dumps({"key": key}).encode("utf-8")
    req = urllib.request.Request(
        AUTH_URL,
        data=payload,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": UA,
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60, context=CTX) as resp:
            status = resp.status
            body = resp.read()
    except urllib.error.HTTPError as exc:
        if exc.code in (400, 401):
            fail(3, "AUTHENTICATION_FAILURE", f"HTTP {exc.code}")
        if exc.code == 403:
            fail(4, "AUTHORIZATION_FAILURE", "HTTP 403 at token exchange")
        fail(6, "AUTH_SERVICE_FAILURE", f"HTTP {exc.code}")
    except (urllib.error.URLError, TimeoutError) as exc:
        reason = getattr(exc, "reason", exc)
        fail(5, "NETWORK_OR_TLS_FAILURE", str(reason)[:160])

    if status != 200:
        fail(6, "AUTH_SERVICE_FAILURE", f"unexpected HTTP {status}")

    try:
        obj = json.loads(body.decode("utf-8"))
    except (ValueError, UnicodeDecodeError):
        fail(3, "AUTHENTICATION_FAILURE", "token response was not valid JSON")

    token = obj.get("edi-token") if isinstance(obj, dict) else None
    if not token:
        fail(3, "AUTHENTICATION_FAILURE", "token response did not contain edi-token")

    # Token is kept in memory only; never print it.
    print("TOKEN_EXCHANGE_SUCCESS")

    req = urllib.request.Request(
        META_URL,
        headers={
            "User-Agent": UA,
            "Accept": "application/xml",
            "Cookie": f"edi-token={token}",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60, context=CTX) as resp:
            meta_status = resp.status
            meta = resp.read(1024)
    except urllib.error.HTTPError as exc:
        if exc.code == 403:
            fail(4, "PASTA_AUTHORIZATION_FAILURE", "HTTP 403 for metadata read")
        if exc.code in (401,):
            fail(3, "PASTA_AUTHENTICATION_FAILURE", "HTTP 401 for metadata read")
        fail(6, "PASTA_SERVICE_FAILURE", f"HTTP {exc.code}")
    except (urllib.error.URLError, TimeoutError) as exc:
        reason = getattr(exc, "reason", exc)
        fail(5, "NETWORK_OR_TLS_FAILURE", str(reason)[:160])

    if meta_status != 200:
        fail(6, "PASTA_SERVICE_FAILURE", f"unexpected HTTP {meta_status}")

    print(f"PASTA_METADATA_SUCCESS bytes_first_read={len(meta)}")
    print("AUTHENTICATION_TEST_PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
