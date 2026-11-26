# Package Version Relationship

**Date:** 2026-11-23T23:32:06.599235+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

| Package | Role | Coverage (EML) | Resolution | Relation |
|---|---|---|---|---|
| `knb-lter-ntl.88.31` | Phytoplankton microscopy | 1995-2020 | Biweekly ice-free, 4-weekly late season | Independent biological endpoint; 4 Madison lakes |
| `knb-lter-ntl.129.9` | Old HF meteo/DO/Chl/PC revision | 2006-2012 | 1-minute | Superseded by 129.42; not the modern predictor set |
| `knb-lter-ntl.129.42` | Current HF meteo/metabolism | 2006-2025 (package-level) | 1-minute; daily/hourly/HR | Same buoy as 130.29; includes Chl/PC/DO/pCO2; per-channel coverage unresolved |
| `knb-lter-ntl.130.29` | HF water temperature profile | 2006-2019 | 1-minute; 16 entities | Same buoy; temperature only; 2015 HR gap on CN |
| `knb-lter-ntl.415.2` | Microbial Observatory physico-chemical | 2006-2019 | Routine handheld profiles | Same Deep Hole; independent handheld YSI; not buoy |

## Key distinctions

- **129.9 ≠ 129.42.** 129.9 is an old revision (through 2012); 129.42 is the modern metadata revision (through 2025). Do not use 129.9 to claim modern coverage.
- **129.42 and 130.29 are complementary buoy packages**, not duplicates: 129.42 has meteo/DO/Chl/PC/pCO2; 130.29 has temperature profiles.
- **415.2 is not a buoy package**; handheld YSI Pro Plus at the Deep Hole, 2006-2019. It overlaps and can cross-check, but has different instruments/depths/QC.
- **88.31 is independent biology**; it is the endpoint, not a predictor.

## What is required to integrate

- Authorized raw access to all four.
- Sensor-list rows (129.42) to map channels to deployment periods.
- `lakeid` filter and depth definition for 88.31.
- Station/depth/timestamp audit; unit/QC harmonisation.
- No integration or transformation performed in this sprint.
