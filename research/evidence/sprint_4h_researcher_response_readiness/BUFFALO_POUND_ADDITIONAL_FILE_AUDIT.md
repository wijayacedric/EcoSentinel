# Buffalo Pound Additional File Audit

**Date:** 2026-11-23T23:27:42.541908+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Scope

Audit of the eight additional Borealis files acquired in Sprint 4F (`research/evidence/sprint_4f_buffalo_pound_stress_test/downloads/`). Existing taxonomy files are under `research/evidence/sprint4_global_bio/downloads/painter_borealis_10.5683_SP3_MPNXF/`. Hashes are in the Sprint 4F acquisition register; files were not modified.

## Findings

### 1. Phyto matrices (2018, 2019)
- 2018: 25 DOY rows × 73 species columns; 2019: 17 × 56.
- Values are species biomass (mg/m³); **row totals equal the taxonomy biomass totals exactly** (2018: 146,432.71; 2019: 155,110.32).
- **Derived duplicate representation**, not independent observations.

### 2. Group biomass (2018, 2019)
- 7 groups × 25/17 dates; group totals are aggregations of the same taxonomy rows.
- **Derived summary**, useful for descriptive composition but not new sampling occasions.

### 3. YSI profiles (2018, 2019)
- 2018: 20 dates, 388 rows, 0.2-4.0 m, temperature/conductivity/DO sat/DO mg/L/pH.
- 2019: 16 dates, 305 rows, same variables.
- 2018 includes one date not in the taxonomy file (2018-10-04); 2019 covers 16 of 17 bio dates.
- **New environmental observations at depth**, not biological observations. They improve vertical context and cross-check buoy sensors, but do not add biological events.

### 4. Heterocyte counts (2018, 2019)
- 2018: 23 dates, Dolichospermum; 2019: 17 dates, Dolichospermum and Aphanizomenon.
- Cell density/biomass of heterocytes; same sampling occasions as taxonomy.
- **Additional biological variable** (N-fixation/physiological context), not an independent occasion or additional year.

## Do they add independent biological observations?

**No.** Across all eight files, the union of biological sampling dates is still **42** (25 + 17). No file adds a new year, a non-bloom season, or higher-frequency biological sampling. The matrices/group biomass are derived; heterocytes are same-occasion variables; YSI is environmental.

## Do they resolve Sprint 4F limitations?

| 4F limitation | Resolved? |
|---|---|
| Only 2 biological seasons | No |
| No non-bloom exposure | No |
| Cadence 4-8 d / no sample times | No |
| Sensor discontinuities | Partially (YSI cross-check at depth, but no continuous QC) |
| Taxonomy/schema change | No (heterocytes use separate schema; matrices mirror 2018/2019 taxa) |
| Licence uncertainty | No (same CC BY-NC-SA 4.0) |

## Conclusion

The eight files are scientifically useful for **exploratory context** (vertical profiles, group composition, heterocytes) but do not change the confirmatory verdict. Additional years and non-bloom biological sampling are still required.
