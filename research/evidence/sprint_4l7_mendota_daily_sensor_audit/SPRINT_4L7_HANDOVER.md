# Sprint 4L.7 Handover

**Date:** 2026-11-24T08:45:50.090661+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Status: COMPLETE FOR PACKAGE/METADATA AUDIT; ACQUISITION BLOCKED; RAW DAILY SENSOR AUDIT NOT PERFORMED.**

## What is ready

- Package/entity inventory for 129.42, including exact daily entity ID/size/MD5 and the deliberately excluded hourly/HR entities.
- Sensor-list/era audit (20 records; 2019 EXO2 transition; Turner/YSI split).
- Metadata-level schema, QC flag, depth and measurement-quality audits.
- Biology–sensor metadata overlap (230/402 dates within 2006–2020) and explicit statement that **zero same-day records are verified**.
- Manifest self-hash clarification: 43/43 non-self entries match; self-reference issue documented; original preserved.

## Exact blocker

No `EDI_API_KEY` in the environment; the daily EDI entity is not on CN (404; replica only LTER); LTER member-node path was previously documented as 403. No bypass attempted. No daily file acquired.

## Next action

User-authorised EDI access, then acquire only:

```bash
python3 research/evidence/sprint_4k_mendota_authorised_access/scripts/edi_mendota_acquire.py \
  --package 129.42 --include-data \
  --entity cba9ed12834b8f315d6b10675bb60c5a \
  --max-bytes 600000 \
  --outdir research/evidence/sprint_4l7_mendota_daily_sensor_audit/acquisition
```

Verify size **490,187 B**, MD5 **`eb7b3a3848b27074bac4504236ccefc3`**, and SHA-256. Then complete:
1. Raw header/encoding/parse audit.
2. Variable-specific coverage/missingness/intervals by year/season.
3. Flag distributions and sensor-era discontinuities.
4. Same-day/preceding/following biology-date availability.
5. Depth-comparator sensitivity.

## Not done

- No daily acquisition.
- No actual variable coverage, QC distribution, gap or overlap counts.
- No labels, event intervals, modelling, hypothesis tests, protocol changes, commits or pushes.
