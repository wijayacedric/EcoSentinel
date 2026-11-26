# Sprint 4L.8 External Search Log

**Date:** 2026-11-24T09:34:03.677381+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Sources inspected

| # | Source | Access | What it establishes |
|---:|---|---|---|
| 1 | `AGENTS.md` | read | Mandatory search/evidence standards; no reduction of scope |
| 2 | `edi_mendota_acquire.py` | full file | Reads `EDI_API_KEY`; IAM POST; cookie token; no secret logging; URL guard; size/checksum handling |
| 3 | Sprint 4L.3D auth test/helper | full files | Secure hidden-input flow; local failure when key absent |
| 4 | Sprint 4L.3C access investigation | full report | PASTA 403 without key; CN no data replica; LTER GMN 403 |
| 5 | Sprint 4L.7 metadata audit | full reports | Daily entity size/MD5/SHA-1; 38-field schema; eras/depth/overlap |
| 6 | EDI IAM/token documentation | prior inspected | `POST /auth/v1/key`, free profile/API key, `edi-token` cookie |
| 7 | DataONE CN sysmeta | current | Daily size 490,187; SHA-1; replica LTER only |
| 8 | EDI Data Portal | prior | Login required; no anonymous daily data |
| 9 | NTL high-frequency page | prior | 129/130 links; buoy context |
| 10 | YSI EXO2 / Turner Cyclops pages | prior | Sensor capabilities/limitations; 2019 era relevance |

## Current local diagnostic commands

- Presence check of `EDI_API_KEY` (no value printed).
- `launchctl getenv` presence checks (no value printed).
- Keychain service existence checks (no secret read).
- Prepared auth test run: exit 2, local configuration failure.

## Inaccessible / not attempted

- No secret entry on user's behalf.
- No keychain creation or key rotation.
- No authentication bypass/alternate endpoints.
- No daily file download.
- No hourly/1-minute download.

## Why stopped

The exact blocker is local credential configuration. More searching cannot replace the user entering the existing key through the secure method.
