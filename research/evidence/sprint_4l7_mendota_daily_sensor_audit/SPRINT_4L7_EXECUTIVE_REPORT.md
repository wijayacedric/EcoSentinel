# Sprint 4L.7 Executive Report — Mendota Daily Sensor Acquisition and Feasibility Audit

**Date:** 2026-11-24T08:45:50.090661+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Status: COMPLETE FOR PACKAGE/METADATA AUDIT; ACQUISITION BLOCKED; RAW DAILY SENSOR AUDIT NOT PERFORMED.**

## 1. What was actually acquired and inspected

- Inspected the current `knb-lter-ntl.129.42` EML, entity inventory, DOI and DataONE CN sysmeta.
- Verified the existing sensor-list file (`mendota_buoy_sensors_v3.csv`, 1,039 B, MD5 `6e5c2a9204fe7e9e15a319a0344ebff0`).
- **Did not acquire the daily entity** `ntl129_1_v16.csv` (490,187 B; EML MD5 `eb7b3a3848b27074bac4504236ccefc3`; CN SHA-1 `bb1d8a281a3d580cad45549551abdbaed1ae03fe`).
- A local authentication check returned `LOCAL_CONFIGURATION_FAILURE: EDI_API_KEY is not set` (exit 2), before any network request. No key was requested or exposed.
- No high-resolution, hourly or unrelated entities were downloaded.

## 2. Entity inventory

| entity_name | object_name | size_bytes | resolution | acquisition_recommendation | raw_status |
|---|---|---|---|---|---|
| North Temperate Lakes LTER: Daily Meteorological and Metabolism Data - Lake Mendota | ntl129_1_v16.csv | 490187 | daily | ACQUIRE (priority) | NOT ACQUIRED |
| North Temperate Lakes LTER: Hourly Meteorological and Metabolism Data - Lake Mendota | ntl129_2_v16.csv | 11380329 | hourly | DO NOT ACQUIRE this sprint | NOT ACQUIRED |
| North Temperate Lakes LTER: High Resolution Meteorological and Metabolism Data - Lake Mendota | ntl129_3_v16.csv | 682487953 | 1-minute | DO NOT ACQUIRE | NOT ACQUIRED |
| List of sensors used on the Lake Mendota buoy since 2006 | mendota_buoy_sensors_v3.csv | 1039 | inventory | ALREADY ACQUIRED | already present |

The daily entity is the smallest scientifically relevant file. Hourly and 1-minute archives were deliberately excluded. The sensor list was already verified and is not re-downloaded.

## 3. Integrity status

**No daily file was acquired, so no size/MD5/SHA-256 verification of actual observations is possible.** Expected metadata values are recorded above. No integrity check is claimed to have passed. The sensor-list hash was independently verified previously (4L.1).

## 4. Variable coverage

Raw variable-level coverage cannot be computed without the daily entity. Metadata-level expected eras:

| variable | role | documented_era | eml_unit | flag_codes | raw_status |
|---|---|---|---|---|---|
| avg_air_temp | air temperature | 2006-2025 package | celsius | C;E;H | BLOCKED_NO_DAILY_DATA |
| avg_rel_hum | relative humidity | 2006-2025 package | percent | C;E | BLOCKED_NO_DAILY_DATA |
| avg_wind_speed | wind speed | 2006-2025 package | meterPerSecond | C | BLOCKED_NO_DAILY_DATA |
| avg_wind_dir | wind direction | 2006-2025 package | degree | C;H | BLOCKED_NO_DAILY_DATA |
| avg_chlor_rfu_turner | chlorophyll proxy | 2006-2019 (documented) | RFU (unit not in EML) | C;H | BLOCKED_NO_DAILY_DATA |
| avg_chlor_rfu_ysi | chlorophyll proxy | 2019-present (documented) | RFU (unit not in EML) | C;H;E;G | BLOCKED_NO_DAILY_DATA |
| avg_phyco_rfu_turner | phycocyanin proxy | 2006-2019 (documented) | RFU (unit not in EML) | C;H | BLOCKED_NO_DAILY_DATA |
| avg_phyco_rfu_ysi | phycocyanin proxy | 2019-present (documented) | RFU (unit not in EML) | C;H;E;G | BLOCKED_NO_DAILY_DATA |
| avg_par | light | 2016-present per sensor list | micromolePerMeterSquaredPerSecond | C;H | BLOCKED_NO_DAILY_DATA |
| avg_par_below | underwater light | 2016-present per sensor list | micromolePerMeterSquaredPerSecond | C;G | BLOCKED_NO_DAILY_DATA |
| avg_do_wtemp | water temperature | 2016-present per sensor list | celsius | C;H | BLOCKED_NO_DAILY_DATA |
| avg_do_sat | DO | 2016-present per sensor list | percent | C;E;H | BLOCKED_NO_DAILY_DATA |
| avg_do_raw | DO | 2016-present per sensor list | milligramPerLiter | C;E;H | BLOCKED_NO_DAILY_DATA |
| avg_pco2_ppm | pCO2 | 2017-present per sensor list | ppm (unit not explicit in EML) | C;E | BLOCKED_NO_DAILY_DATA |
| avg_ph | pH | 2019-present per sensor list | dimensionless | C | BLOCKED_NO_DAILY_DATA |
| avg_fdom | fDOM proxy | 2019-present per sensor list | RFU/ppb QSU not explicit | C | BLOCKED_NO_DAILY_DATA |
| avg_turbidity | turbidity | 2019-present per sensor list | FNU (unit not explicit in EML) | C | BLOCKED_NO_DAILY_DATA |
| avg_spec_cond | specific conductance | 2006 only and 2019-present per sensor list | uS/cm (unit not explicit in EML) | C;H | BLOCKED_NO_DAILY_DATA |

No package-level 2006–2025 coverage is assumed to apply to every variable. The sensor inventory shows Turner→YSI chlorophyll/phycocyanin in 2019, pH/fDOM/turbidity/conductivity from 2019 (conductivity also 2006 only), DO from 2016, and water temperature from 2007 in the RBR era.

## 5. QC and sensor eras

- EML flag codes: **C** sensor off; **E** noisy/malfunctioning; **H** outside range; **G** suspected biofouling.
- **G** is documented for YSI chlorophyll/phycocyanin and PAR-below only; Turner chlorophyll/phycocyanin flags are C/H only.
- No calibration dates, coefficients, serial numbers or fouling/maintenance logs are in the EML/sensor list.
- 2019 is a major EXO2 suite transition; 2017/2018/2016/2013/2007 are additional sensor changes. Raw daily values cannot be concatenated across eras without documented mapping/QC.

## 6. Biology–sensor temporal compatibility

- Biology: **402 Mendota dates**, 1995–2020, median interval 14 days.
- 129.42 metadata coverage: 2006–2025. **230 biology dates fall within 2006–2020**; 172 predate 2006; none post-2020.
- **No same-day sensor record is verified** because the daily entity was not acquired. The overlap table records potential date overlap only (`daily_sensor_records_verified=0`).
- Biology has **date only**, no sample time. Sensor data are daily averages. Matching would be day-level; the microscopy date cannot be assumed to represent an exact sensor time.
- No labels, events or aggregation/model predictors were created.

## 7. Depth and spatial compatibility

| variable | documented_depth | measurement | biological_reference | classification |
|---|---|---|---|---|
| avg_do_wtemp | 0.5 m | water temperature | 0-8 m composite | Weakly comparable |
| avg_do_sat | 0.5 m | DO % saturation | 0-8 m composite | Weakly comparable |
| avg_do_raw | 0.5 m | DO mg/L | 0-8 m composite | Weakly comparable |
| avg_ph | 0.5 m | pH | 0-8 m composite | Weakly comparable |
| avg_spec_cond | 0.5 m | specific conductance | 0-8 m composite | Weakly comparable |
| avg_turbidity | 0.5 m | turbidity | 0-8 m composite | Weakly comparable |
| avg_chlor_rfu_turner | 0.5 m | chlorophyll RFU | 0-8 m composite | Weakly comparable |
| avg_chlor_rfu_ysi | 0.5 m | chlorophyll RFU | 0-8 m composite | Weakly comparable |
| avg_phyco_rfu_turner | 0.5 m | phycocyanin RFU | 0-8 m composite | Weakly comparable |
| avg_phyco_rfu_ysi | 0.5 m | phycocyanin RFU | 0-8 m composite | Weakly comparable |
| avg_pco2_ppm | 1 m | pCO2 | 0-8 m composite | Weakly comparable |
| avg_par_below | 1 m | underwater PAR | 0-8 m composite | Weakly comparable |
| avg_par | 2 m above water | above-water PAR | 0-8 m composite | Not comparable |
| meteorology | 2-3 m above water | air temp/RH/wind | 0-8 m composite | Not comparable |

- Biological Mendota samples are generally **0–8 m composites**; sensor chlorophyll/phycocyanin/DO/pH/conductance/turbidity are at **0.5 m**, pCO2 at 1 m, PAR above/below at 2/1 m.
- **No surface sensor represents the 0–8 m composite.** A future comparison requires an explicit depth comparator and sensitivity analysis.
- Site co-location is documented (buoy/Deep Hole), but biological `sta` is blank for most records and station-level linkage is weak.

## 8. Manifest discrepancy

The Sprint 4L.5 self-hash discrepancy is a **self-reference/stale-entry issue**, not evidence that the biological audit is invalid. The original register was preserved. **43/43 non-self entries match their recorded SHA-256 values**; the self entry is 7,065 B with recorded hash `480101...`, while the current register hashes to `0aeb...`. A file cannot contain its own final hash. A non-self V2 register and sidecar hash were created in this sprint.

## 9. Scientific feasibility

**Cannot yet pass a sensor-side feasibility review.** Daily observations are not available for audit, so continuity, variable-specific coverage, zero/invalid readings, flag distributions, sensor-era discontinuities and same-day overlap are unresolved.

Metadata supports a **conditional exploratory path**: the package contains relevant variables (temperature, DO, chlorophyll/phycocyanin proxies, pH, conductivity, turbidity, PAR, meteorology), and 230 biology dates fall within the 2006–2020 overlap. But no claim can be made until the daily entity is acquired and audited. More sensor observations do not solve the sparse 14-day biological ground truth.

## 10. Final verdict

**CONDITIONAL — acquisition-blocked.** The package and entity are verified; the daily observations are not. Further work requires the user-authorised EDI key and acquisition of `cba9ed12834b8f315d6b10675bb60c5a` only. Gate 2 remains PAUSED.
