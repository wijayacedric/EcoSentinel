# QC Flag Audit

**Date:** 2026-11-24T08:45:50.090661+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Documented flag codes

| code | definition | where_documented |
|---|---|---|
| C | Sensor off | all flag columns |
| E | Sensor noisy or malfunctioning | air temp, RH, YSI chlorophyll/phycocyanin, DO sat/raw, pCO2 |
| H | Outside of standard range | air temp, wind dir, Turner/YSI chlorophyll/phycocyanin, PAR, DO, spec cond |
| G | Sensor - suspected biofouling | YSI chlorophyll/phycocyanin, PAR below |

## Key observations

- **C** = sensor off; **E** = noisy/malfunctioning; **H** = outside standard range; **G** = suspected biofouling.
- **G** is documented only for YSI chlorophyll/phycocyanin and PAR-below. Turner chlorophyll/phycocyanin flags are C/H only, so biofouling may be less explicitly flagged in the Turner era.
- Every variable has a flag column in the schema, but **actual flag distributions, counts and temporal patterns are not available** (no daily file).
- The flags are not a full calibration/QA record; no calibration dates, coefficients, maintenance logs or serial numbers are in the EML.
- Missing values/non-finite values cannot be audited without the raw daily data.

## Required checks after acquisition

1. Flag distribution by variable/year/month.
2. Missingness by flag code and season.
3. Flag runs and coincidence with sensor-era transitions.
4. Whether C/E/H/G codes are used consistently across Turner and YSI eras.
5. Whether flags precede/follow site visits or fouling events.

No QC success is claimed.
