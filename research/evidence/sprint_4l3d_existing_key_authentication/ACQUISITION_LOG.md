# Acquisition Log

**Date:** 2026-11-24T07:10:03.729185+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Target

- Package: `knb-lter-ntl.88.31`
- DOI: `10.6073/pasta/bd03330e83fc52a5442bb39e131c95e9`
- Entity: `f2de15b2fff6ae962a04c150c0a1c510`
- Object: `ntl88_v13.csv`
- Expected size: **2,448,830 B**
- Expected MD5: **`a0363cc7fdfd6c12889750fea27bd542`**
- Output directory: `research/evidence/sprint_4l_mendota_biology_audit/acquisition/88.31/`

## Timeline

| Date/step | Action | Result |
|---|---|---|
| 2026-11-23 (prior) | Existing script with `--include-data` and entity | Exit 2: `EDI_API_KEY` not set; **no network request**; no data |
| 2026-11-24 | Inspected script and prior evidence | No code change; MD5 parser gap noted |
| 2026-11-24 | Prepared secure prompt helper + auth test | Syntax checks pass; not executed with a key |
| 2026-11-24 | Existing-key authentication | **Not executed** — waiting for user local input |
| 2026-11-24 | Single-entity acquisition | **Not executed** — depends on authentication |

## Script inspection summary

- Key source: `os.environ["EDI_API_KEY"]`; stripped.
- IAM request: `POST https://auth.edirepository.org/auth/v1/key`, JSON `{"key": ...}`.
- Token: response `edi-token`, held in memory; sent as `Cookie: edi-token=...`.
- Secret output: none in normal operation; provenance has no key/token; URLs have no key.
- URL guard: data URL must start with `https://pasta.lternet.edu/package/data/`.
- Size validation: yes, when EML `<size>` is parsed.
- MD5 validation: **no** (EML uses `<authentication>`, parser looks for `<checksum>`); wrapper performs independent MD5.
- Retries: 2 for transient 429/5xx/network; none for 401/403/404.
- Resume: `.part` with Range; no overwrite; mismatch preserved.
- Timeout: 120 s for data; 60 s for IAM.

## What was not done

No key entry, no authentication request, no data request, no unrelated entity download, no script modification, no SSEC substitution.

## Next

User runs the secure helper. On success, record the actual HTTP status, size, MD5, SHA256, timestamp, and continue the raw audit.
