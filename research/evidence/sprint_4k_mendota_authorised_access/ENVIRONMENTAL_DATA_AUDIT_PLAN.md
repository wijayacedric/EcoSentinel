# Environmental Data Audit Plan — 129.42, 130.29, 415.2

**Date:** 2026-11-23T23:36:48.967538+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Inputs (after explicit authorisation)

- 129.42: daily (`cba9ed...`), hourly (`72494d...`), high-resolution (`af29c6...`), sensor list (`edddc490...`).
- 130.29: 16 entities (daily/hourly/high-resolution temperature by year).
- 415.2: three handheld-probe tables (`22da...`, `d748...`, `4c0f...`).

## 1. 129.42 sensor list first

- Columns: `parameter, sensor_mfg, sensor_model, date_began, date_ended`.
- Build a per-parameter deployment timeline; identify gaps, overlaps, replacement dates.
- Map sensor eras (e.g., Turner vs YSI chlorophyll/phycocyanin; 2019+ additions such as YSI, specific conductivity, pH, turbidity, fDOM).
- Determine per-variable coverage; do **not** assume 2006-2025 applies to every channel.

## 2. 129.42 daily/hourly/high-resolution

- Header vs EML attributes (38 daily, 39 hourly/HR expected).
- Timestamp parsing; duplicates; daylight/timezone convention; daily aggregation rules.
- Per-variable and per-year missingness; flag distributions (`flag_*`).
- Check sentinel values, out-of-range values, repeated readings, and sensor-change discontinuities.
- Compare daily vs hourly/HR for consistency; do not mix resolutions without a documented rule.
- Chlorophyll/phycocyanin: RFU proxies, Turner vs YSI; no calibrated biomass; no biological ground truth.
- DO: D-Opto at ~0.5 m; distinguish raw/saturation/water temp; check units.
- pCO2: deployment period and sensor changes.
- Do not treat sensor proxies as independent biological observations.

## 3. 130.29 temperature

- 16 entities; parse each; map year/depth coverage.
- Thermistor chain depths; changes in 2006/2007/2008; 2015 HR missing.
- Check duplicates, gaps, timestamp resolution; confirm daily/hourly/HR consistency.
- Determine whether 2015 gap is material for the intended overlap; do not assume it must be recovered.

## 4. 415.2 Microbial Observatory

- Three tables: YSI-Poseidon 2014-2019; non-Poseidon water temp; non-Poseidon DO.
- Handheld profiles at Deep Hole; depths, timestamps, instrument IDs, field notes.
- Sampling frequency: derive from dates; do not assume routine = fixed.
- Method change 2006-2014 vs 2014-2019; units; missingness; QC.
- pH/conductance only 2014-2019.

## 5. Cross-package alignment

- Station coordinates: buoy and Deep Hole (43.0995, -89.4045; 43°05'58.2"N 89°24'16.2"W) must be verified in files.
- Depth: 88.31 0-8 m composite vs buoy sensors (DO ~0.5 m; thermistor chain; chlorophyll/phycocyanin at buoy depth) vs 415.2 handheld profiles. Define a defensible comparator; do not assume surface equals composite.
- Date overlap: 2006-2020 (metadata); verify per-variable, per-year actual coverage.
- QC: compare flags/units/methods across packages; no silent harmonisation.

## 6. No substitution

SSEC/AOSS Metobs API data are not EDI 129.42/130.29 observations. If used at all, keep in a separate exploratory directory, label clearly, and do not merge into EDI files or treat as equivalent (no QC flags; 2006-2018 absent from tested API).

## 7. Outputs

- `129_42_sensor_timeline.csv`
- `129_42_variable_coverage.csv`
- `130_29_temperature_coverage.csv`
- `415_2_handheld_coverage.csv`
- `environmental_qc_notes.md`
- No labels, modelling, or event intervals.
