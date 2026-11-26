# Acquisition and Integrity Report

**Date:** 2026-11-24T08:45:50.090661+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Target

- Package: `knb-lter-ntl.129.42`
- DOI: `10.6073/pasta/9c4b1eecf7a019c7239297b6bf4513c4`
- Daily entity: `cba9ed12834b8f315d6b10675bb60c5a`
- Object: `ntl129_1_v16.csv`
- Expected size: **490,187 bytes**
- EML authentication: **MD5 `eb7b3a3848b27074bac4504236ccefc3`**
- DataONE CN sysmeta: size 490,187; SHA-1 `bb1d8a281a3d580cad45549551abdbaed1ae03fe`; replica only `urn:node:LTER`.

## Acquisition attempt

The local authentication check returned:

`LOCAL_CONFIGURATION_FAILURE: EDI_API_KEY is not set in this process` (exit 2).

No network request was made; no file was created. The prior 4L.3C investigation documented PASTA 403 without a key, CN 404 for data bytes, and a host/path-level 403 on the LTER member-node `/mn/v2` route. No bypass was attempted.

## Integrity status

- Actual size: **not measured**
- Actual MD5: **not measured**
- Actual SHA-256: **not measured**
- EML checksum comparison: **not performed**
- CSV parse/header: **not performed**

**No integrity success is claimed.** The expected values are metadata-derived.

## What was acquired

- Sensor inventory already present: 1,039 B, MD5 `6e5c2a9204fe7e9e15a319a0344ebff0` (verified in 4L.1).
- No daily, hourly, high-resolution or unrelated entity was downloaded.

## Required acquisition command (user-authorised key)

```bash
python3 research/evidence/sprint_4k_mendota_authorised_access/scripts/edi_mendota_acquire.py \
  --package 129.42 --include-data \
  --entity cba9ed12834b8f315d6b10675bb60c5a \
  --max-bytes 600000 \
  --outdir research/evidence/sprint_4l7_mendota_daily_sensor_audit/acquisition
```

Do not paste the key into chat or repository files.
