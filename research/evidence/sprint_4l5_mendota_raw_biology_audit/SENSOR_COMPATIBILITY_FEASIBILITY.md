# Sensor Compatibility Feasibility

**Date:** 2026-11-24T07:23:09.883291+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Existing sensor evidence reviewed (no new downloads)

- **129.42 metadata:** package-level coverage 2006–2025; 1-minute data; daily/hourly/high-resolution + sensor-list tables; variables include air temp, RH, wind, PAR, chlorophyll (Turner/YSI), phycocyanin (Turner/YSI), DO, pCO2.
- **129.42 sensor list:** 20 records / 13 parameter categories; shallow sonde 6600 (2014–2021), deep sonde 6920 (2014–2019), Turner→YSI chlorophyll/phycocyanin transition in 2019, pH/fDOM/turbidity/conductivity only from 2019 (conductivity also 2006 only).
- **130.29:** temperature-only, 2006–2019, 16 tables; 2015 HR entity missing on CN.
- **415.2:** handheld YSI Pro Plus, 2006–2019, routine profiles at the Deep Hole; pH/conductance only 2014–2019.
- No 129.42 daily/hourly/high-resolution observations were downloaded or inspected in this sprint; no sensor–biology integration was performed.

## Compatibility questions

| Issue | Status | Evidence/limitation |
|---|---|---|
| Date overlap | **Metadata-level yes, 2006–2020** | Biology 1995–2020; 129.42 2006–2025; 130.29 2006–2019. Raw sensor observations not audited. |
| Sampling frequency | **Mismatch** | Biology median 14 days; sensor 1 minute. Need daily aggregation and avoid treating sensor records as independent. |
| Measurement depth | **Major mismatch** | Biology 0–8 m composite (Mendota); sensor chlorophyll/phycocyanin/DO documented at ~0.5 m; thermistor chain at discrete depths. |
| Station correspondence | **Unresolved** | Buoy and Deep Hole coordinates are the same general site, but biological `sta` is blank for most rows (only 2011–2012 has `sta=1`). |
| Sensor deployment changes | **Known but unmapped** | 2019 EXO2 transition; 2017 Temp/RH; 2016 DO/PAR; 2013 wind/IR; 2007 water temp; per-channel periods unresolved. |
| Sensor QC/calibration | **Not audited** | EML flags exist; no raw sensor data or calibration logs inspected. |
| Temporal mismatch | **Unresolved** | Biology has date only, no sample time; sensors are 1-minute. Day-level matching only. |
| Depth-structure anomalies | **Present in biology** | 40 ME 0–2m records (2002) and 310 MO 0–8m records (1995/2002–2004) contradict metadata depth assignments. |

## What is needed before alignment

1. Acquire 129.42 daily/hourly/high-resolution data and the sensor-list rows; map per-channel start/end.
2. Acquire 130.29 temperature profile and 415.2 handheld profiles; audit depths, timestamps, QC.
3. Define the biological comparator for a 0–8m composite (surface layer, euphotic-zone integration, or whole-column biomass) and test sensitivity.
4. Obtain sample times or document that only day-level matching is possible.
5. Resolve station IDs/coordinates and depth anomalies.
6. Account for sensor-era changes and calibration/fouling flags; do not compute multivariate relationships across eras without stratification.

## Prohibition

No sensor–biology integration, labels, event intervals or confirmatory analysis was performed. SSEC/Metobs data were not substituted for EDI observations.
