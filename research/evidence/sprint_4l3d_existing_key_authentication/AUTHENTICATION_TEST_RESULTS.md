# Authentication Test Results

**Date:** 2026-11-24T07:10:03.729185+00:00  
**Status: NOT EXECUTED WITH THE EXISTING KEY.** The user must enter the key locally.

## What has and has not been tested

| Test | Result | Interpretation |
|---|---|---|
| Prepared test script with no key | `LOCAL_CONFIGURATION_FAILURE` (exit 2) | Local configuration failure; **not** evidence about key validity |
| Empty JSON POST to IAM endpoint (previous sprint) | HTTP 400, missing field `key` | IAM endpoint reachable; exchange mechanism exists |
| Anonymous PASTA metadata/data (previous sprint) | HTTP 403 Public Access | Auth required; expected |
| Existing user key exchange | **Not executed** | Cannot classify yet |
| PASTA read with existing token | **Not executed** | Cannot classify yet |

## Planned test

`scripts/test_existing_key.py` performs exactly two requests:

1. `POST https://auth.edirepository.org/auth/v1/key` with `{"key": ...}`.
2. `GET https://pasta.lternet.edu/package/metadata/eml/knb-lter-ntl/88/31` with `Cookie: edi-token=...`.

It prints only:
- `TOKEN_EXCHANGE_SUCCESS` or a safe failure category;
- `PASTA_METADATA_SUCCESS bytes_first_read=<n>` or a safe failure category;
- `AUTHENTICATION_TEST_PASSED` on success.

It never prints the key, token, cookie, request body or response body.

## Outcome classification

| Observed | Classification | Next action |
|---|---|---|
| Token exchange 200 + PASTA metadata 200 | Key authenticates; token accepted | Proceed to single-entity acquisition |
| 400/401 at token exchange | Authentication failure: formatting/expiry/validity | Inspect key entry/format; do not create a new key until official requirements checked |
| 403 at token exchange | Authorization/key-scope issue | Inspect principal/group permissions |
| 403 at PASTA | Authenticated but not authorized | Inspect package/principal permissions |
| DNS/TLS/timeout | Network failure | Retry when network is available; not a key verdict |
| Missing variable | Local configuration failure | Re-enter key in the controlled shell |
| 5xx | Server/service failure | Retry later; not a key verdict |

## No conclusion

The user's statement that the key is active is recorded as user-provided context, not as a verified test result. The key has **not** been demonstrated invalid or valid in this sprint.
