# Environmental Data Quality Audit — Buffalo Pound

**Date:** 2026-11-23T23:22:37.724583+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. Foundation

- 8 annual CSVs, 68 columns, SHA256 verified; 2014 15-min (8,015 rows), 2015-2021 10-min (16,836-22,023 rows).
- Coverage is ice-free only: 2014-06-11 to 2021-10-07.
- Sensors (Data in Brief Table 7): shallow YSI Sonde 6600 (0.82 m) active 2014-2021; deep YSI Sonde 6920 (2.8 m) active **2014-2019 only**. Deep temperature reappears 2020-2021 but the full deep suite does not.

## 2. Missingness by year (key variables)

| Variable | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| TempShallow | 99.8 | 84.6 | 98.6 | 100.0 | 87.9 | 99.1 | 94.9 | 99.9 |
| pHShallow | 99.8 | 84.6 | 98.7 | 100.0 | 87.9 | 99.1 | 95.0 | 99.9 |
| ODOShallow | 99.8 | **38.5** | 98.6 | 99.8 | 87.9 | 99.1 | 94.9 | 97.8 |
| SpCondShallow | 99.8 | 84.6 | 96.7 | 98.5 | 87.9 | 99.1 | 94.8 | 99.9 |
| TurbShallow | 99.8 | 78.7 | 98.6 | 96.0 | 87.9 | 99.1 | 95.0 | 97.8 |
| ChlRFUShallow | 99.8 | 84.6 | 98.6 | 99.6 | 87.9 | 99.1 | 95.0 | 97.7 |
| BGPCShallow | 99.8 | 84.6 | 98.6 | 99.9 | 87.9 | 99.0 | 95.0 | 97.6 |
| TempDeep | 99.8 | 99.5 | 100.0 | 100.0 | 87.9 | **6.5** | 100.0 | 100.0 |
| pHDeep | 99.8 | 99.5 | 99.9 | **56.0** | 87.9 | **6.5** | 100.0 | **0.0** |
| ODODeep | 99.8 | 99.5 | 98.8 | 99.5 | 87.6 | **2.8** | 99.7 | 100.0 |
| BGPCDeep | 99.8 | 99.5 | 100.0 | **44.2** | 87.9 | **0.0** | 100.0 | 100.0 |
| ChlorophyllRFUDeep | **0.0** | **0.0** | **0.0** | **0.0** | **0.0** | **0.0** | 99.9 | **33.7** |

## 3. Flags

- **M** = missing/sensor removed/failure/logging error.
- **C** = deemed faulty/unrealistic.
- **A2** = PAR below factory range adjusted to 0 (common at low light).
- **A3/A4** = inverted/shaded underwater PAR; A4 warns 2015 PAR sensors should not be compared for attenuation.
- **A6/B6** = specific conductivity calibration corrections (2017 shallow+deep; 2018 deep).
- **B7** = spike then decrease following site visit (fouling): 604 flags in 2014 and 803 in 2020 for turbidity/chlorophyll.

## 4. Repeated readings / sensor resolution

Long runs of identical consecutive values (10-min data):
- SpCondShallow max run **216** (2018; ~36 h), 170 (2017), 137 (2016), 133 (2018 deep).
- pHShallow max run 33 (2019; ~5.5 h), 30 (2017), 27 (2015).
- PAR/air runs are expected at night/constant light.
These may reflect sensor resolution, stuck readings, or stable conditions; they are a QC caution for relationship-change detection.

## 5. Discontinuities

- Deep suite ends 2019; 2020/2021 deep variables are not equivalent to 2014-2019.
- Shallow DO 2015 collapse (38.5% valid).
- pHDeep 2021 all invalid.
- Conductivity calibration corrections 2017/2018 create step changes (documented flags).
- Annual median SpCondShallow shifts from 923 µS/cm (2015/2017) to 454-615 µS/cm (2018-2021), partly environmental and partly calibration/QA. This could create artificial multivariate relationship shifts.

## 6. Implications

A multivariate relationship-change signal computed across these years could be driven by **sensor suite changes, calibration corrections, fouling, and missingness**, not only lake ecology. Any exploratory analysis must stratify by sensor era and QC, and must not treat the 10-min records as independent biological observations.

## 7. Data-quality visualisation

Not produced: no plotting dependency was used; the tabular audit is sufficient for the verdict. The audit can be reproduced from `MISSINGNESS_AND_QC_SUMMARY.csv`.
