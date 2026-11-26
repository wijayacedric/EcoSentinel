# Raw File Integrity Report

**Date:** 2026-11-24T07:10:03.729185+00:00  
**Status: NOT ACQUIRED — no integrity verdict possible.**

## Expected values (metadata-verified)

- Entity: `f2de15b2fff6ae962a04c150c0a1c510`
- Object: `ntl88_v13.csv`
- Size: **2,448,830 bytes**
- MD5: **`a0363cc7fdfd6c12889750fea27bd542`**
- EML source: `knb-lter-ntl.88.31`; DataONE CN sysmeta size 2,448,830, format text/csv.

## Actual values

- File: **not present** in the acquisition directory.
- Size: **not measured**
- MD5: **not measured**
- SHA256: **not measured**
- EML checksum comparison: **not performed**
- Acquisition provenance: no successful acquisition row for 88.31.

## Verification performed

Only the expected metadata values and the absence of a local file were verified. No check is claimed to have passed.

## Required post-acquisition checks

1. `stat -f '%z'` equals 2,448,830.
2. `md5 -q` equals `a0363cc7fdfd6c12889750fea27bd542`.
3. `shasum -a 256` recorded.
4. Header/row readability.
5. Provenance row with source URL, timestamp, bytes, SHA256, HTTP status.
6. Raw file preserved unchanged.

If any check fails, stop and preserve the file; do not overwrite or repair silently.
