# Raw File Validation

**Date:** 2026-11-24T07:22:12.805937+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## File

`research/evidence/sprint_4l_mendota_biology_audit/acquisition/88.31/North_Temperate_Lakes_LTER_-_Phytoplankton_-_Madison_Lakes_Area__f2de15b2fff6ae962a04c150c0a1c510.dat`

## Independent checks

| Check | Result | Expected / note |
|---|---|---|
| Exists | Yes | — |
| Bytes | **2,448,830** | Matches EML size |
| MD5 | **`a0363cc7fdfd6c12889750fea27bd542`** | Matches EML `a0363cc7fdfd6c12889750fea27bd542` |
| SHA-256 | **`a63d7cfa0502e3cdab6d8939f21820f305295e030d4d08bf10bfc69b22829db2`** | Independently calculated |
| Encoding | UTF-8, ASCII-only | no non-ASCII characters found |
| BOM | False | none |
| Line endings | CRLF | 18655 CRLF, 18655 LF |
| Header | 15 columns | exact match to EML |
| Data rows | **18,654** | 1 header + 18,654 data records |
| Malformed records | 0 | none |
| Blank lines | 0 | none |
| CSV parse errors | none | Python csv parsed every line |
| `sampledate` parse errors | 0 | none |
| `year4` parse errors | 0 | none |
| `year4` vs date-year mismatches | 0 | none |
| Truncation | No | last line ends with CRLF |
| Raw file modified | **No** | read-only inspection |

## Verdict

The raw file is structurally valid, complete and integrity-verified against the EML size and MD5. No silent data loss was detected in parsing.
