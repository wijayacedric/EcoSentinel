# Sprint 4L.1 Handover

**Date:** 2026-11-23T23:48:59.424593+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Verified

- Raw sensor file exists; **1,039 bytes**.
- SHA256 `255dc9a279f1acb4a3588f697e91f206c5466b9ef2c47166b9b6204002b117d5` matches acquisition provenance.
- MD5 `6e5c2a9204fe7e9e15a319a0344ebff0` matches EML `<authentication method="MD5">`.
- Format: CSV, CRLF, quoted, 5 columns, 1 header + **20 records**, **13 parameter categories**.
- EML object name: `mendota_buoy_sensors_v3.csv`.

## Key content

- Water Temp: TempLine 2006 → RBR Concerto 2007-present.
- DO: D-Opto 2016-2018, miniDOT 2018, YSI EXO2 2019-present.
- Chlor/Phyco: Turner Cyclops 2006-2019 → YSI EXO2 2019-present.
- Conductivity: YSI 2006 (model blank), YSI EXO2 2019-present; gap 2007-2018.
- pH/fDOM/Turbidity: YSI EXO2 2019-present.
- CO2: Turner C-sense 2017-present.
- Temp/RH: RM Young 41382 2006-2017 → Vaisala HMP110 2017-present.
- Wind: Vaisala 2006-2012 → RM Young 5106 2013-present.
- IR Skin Temp: Apogee SI-111 2013-present.
- PAR above/below: Apogee SQ-110/SQ-111 2016-present.

## Important caveats

- No depths, serials, calibration, accuracy, or QC in this file.
- "present" is undefined; exact transition dates are years only.
- 2019 is a major sensor-suite discontinuity; 2017/2018/2016/2013/2007 also change instruments.
- Chlorophyll/phycocyanin are proxies, not independent biological ground truth.
- 88.31 is a 0-8 m composite; depth matching must be explicit.

## Provenance note

- Acquisition provenance says "no EML checksum" because the parser looked for `<checksum>`; the EML actually uses `<authentication method="MD5">`. Independent MD5/matches prove integrity. This is a parser-field defect to fix in future acquisition tooling, not a data defect.

## Next

- If authorised, audit 129.42 daily columns/flags and map them to sensor eras; then 88.31 biology.
- Do not label, model, or change Gate 2.

## Files

`SPRINT_4L1_EXECUTIVE_REPORT.md`, `SENSOR_INVENTORY_TRANSCRIPTION.csv`, `DEPLOYMENT_TIMELINE.md`, `VARIABLE_COVERAGE_AND_LIMITATIONS.md`, `UNRESOLVED_QUESTIONS.md`, `SPRINT_4L1_HANDOVER.md`.
