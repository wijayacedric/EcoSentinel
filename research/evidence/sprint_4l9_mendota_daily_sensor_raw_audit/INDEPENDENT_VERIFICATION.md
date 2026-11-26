# Independent Verification

This is a second-method check of the Sprint 4L.9 audit. It does not import the audit script.
It parses the raw file by simple comma splitting (the data fields contain no embedded commas),
then compares key counts with the generated audit tables.

## Checksums

| Item | Value |
|---|---|
| Bytes | 490,187 |
| MD5 | `eb7b3a3848b27074bac4504236ccefc3` |
| SHA-1 | `bb1d8a281a3d580cad45549551abdbaed1ae03fe` |
| SHA-256 | `104ef1b33769bc0ad1d3e9e6dff28219b743b81ce89ee888460d2df255981343` |

## Structure

| Item | Value |
|---|---|
| Lines including header | 3,997 |
| Data rows | 3,996 |
| Bad field counts | 0 |
| Columns | 38 |
| Unique dates | 3,996 |
| Duplicate dates | 0 |
| Year mismatches | 0 |
| Exact duplicate rows | 0 |
| Date range | 2006-07-09 to 2025-11-18 |

## Reconciliation

- Variable coverage mismatches: **0**
- Biology overlap mismatches: **0**
- Percentage reconciliation issues: **0**

All independently recomputed counts and percentages reconcile with the generated audit tables.
