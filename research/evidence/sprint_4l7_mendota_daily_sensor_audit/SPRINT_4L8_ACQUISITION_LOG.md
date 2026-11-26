# Sprint 4L.8 Acquisition Log

**Date:** 2026-11-24T09:34:03.677381+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Target (only authorized entity)

- Package: `knb-lter-ntl.129.42`
- DOI: `10.6073/pasta/9c4b1eecf7a019c7239297b6bf4513c4`
- Entity: `cba9ed12834b8f315d6b10675bb60c5a`
- Object: `ntl129_1_v16.csv`
- Expected size: **490,187 bytes**
- Expected EML MD5: **`eb7b3a3848b27074bac4504236ccefc3`**
- Expected DataONE CN SHA-1: **`bb1d8a281a3d580cad45549551abdbaed1ae03fe`**
- Destination: `research/evidence/sprint_4l7_mendota_daily_sensor_audit/acquisition/`

## Timeline

| Step | Action | Result |
|---|---|---|
| 1 | Checked current environment/keychain | `EDI_API_KEY` absent; Keychain candidates absent |
| 2 | Ran prepared authentication test | Exit 2, `LOCAL_CONFIGURATION_FAILURE`; **no network request** |
| 3 | Prepared hidden-input helper for 129.42 daily entity | Syntax checked; **not executed** |
| 4 | Acquisition | **NOT ATTEMPTED** — blocked before network |
| 5 | Raw daily audit | **NOT PERFORMED** |

## Current destination

`acquisition/` is empty; no daily file exists. No hourly/1-minute or unrelated entity was downloaded.

## Integrity

No actual size, MD5 or SHA-256 of the daily file is available. Expected values above are metadata-derived and are **not** verification results.

## Next

User runs the hidden-input helper in a local Terminal. If authentication succeeds, it acquires only the daily entity and verifies size/MD5/SHA256.
