# Data Volume and Observation-Effort Report — Greifensee 5p0x (Sprint 4D.2)

**Date:** 2026-11-22T23:14:01.070201+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Scope:** Descriptive audit of 40 acquired 5p0x class_and_feat tarballs. No downloads of remaining 20. No bloom labels, modelling, or confirmatory analysis.

## 1. Inventory reconciliation

Authoritative inventory: **60** C2G monthly 5p0x class_and_feat packages total; **40 acquired**, **20 skipped**. May 2022 discrepancy resolved (race condition in Sprint 4D download script; file later acquired and verified). See `INVENTORY_RECONCILIATION.md`.

## 2. Acquired 40-package summary

| Metric | Value |
|---|---:|
| Tarballs audited | 40 |
| Total compressed bytes | 2,742,610,413 |
| Total extracted bytes | 7,938,903,212 |
| Total feature records | 4,656,714 |
| Total classification records | 14,619,408 |
| Total cyanobacteria classification records (label-pattern match) | 169,534 |
| Overall cyano rate per 1,000 class records | 11.597 |

**Cyanobacteria identification method:** case-insensitive regex over classification labels: `cyano|microcyst|dolichosperm|anabaena|aphanizomen|planktothrix|woronichinia|nostoc`. This is a label-pattern heuristic over available classification files; it is not a validated taxonomic audit.

## 3. Does larger package size correspond to more observations?

**Partly, but not reliably as a sole proxy.** Pearson correlations across 40 months:

| Pair | r |
|---|---:|
| compressed bytes vs extracted bytes | 0.986 |
| compressed bytes vs feature records | 0.997 |
| compressed bytes vs classification records | 0.826 |
| compressed bytes vs timestamp folders | 0.341 |
| compressed bytes vs unique days (from features) | 0.400 |
| compressed bytes vs cyano classification records | 0.510 |

Bytes-per-feature-record varies widely by month/schema (see `PACKAGE_SIZE_VS_OBSERVATION_ANALYSIS.csv`), indicating format/schema/compression differences affect size. **Do not use file size alone as observation-effort proxy.**

## 4. Does larger size correspond to more cyanobacteria detections?

**Weakly/moderately and confounded.** Compressed size vs cyano classification records r=0.510; feature records vs cyano records r=0.491. Raw cyano counts are confounded by observation effort (number of images/ROIs/class records) and schema differences. High cyano months by raw count: October 2019 (48065), October 2021 (15363), June 2022 (10839), July 2020 (10795), November 2022 (10415). These are **not** calibrated biomass/cell-density or bloom labels.

## 5. Effort adjustment

`CYANOBACTERIA_CLASSIFICATION_SUMMARY.csv` includes descriptive rates: cyano per 1,000 classification records and per 1,000 feature records. These are effort-normalizing **descriptors only**, not bloom thresholds, not calibrated abundance, and not confirmatory evidence. Schema differences (different classifier basenames/file sets across years) limit comparability.

## 6. Observation coverage (acquired 40)

Top months by feature records: June 2023 (248,172), July 2020 (248,071), March 2022 (233,142), October 2021 (230,651), April 2021 (215,442).  
Top months by unique days (from features): May 2019 (31), October 2019 (31), December 2019 (31), March 2020 (31), May 2020 (31).

Coverage is uneven across years and seasons in the acquired subset; missing 20 months further bias coverage.

## 7. Schema/classifier differences

Observed basenames differ across periods (e.g., early packages include `class_CILIATES_leaderabs0.txt` and `Predictions_avg_ens_chytrid.txt`; later packages often include `features.csv` + `Ensemble_models_Plankiformer_predictions_geo_mean_finetuned.txt`). See `SCHEMA_AND_CLASSIFIER_VERSION_COMPARISON.csv`. Cross-month comparisons require harmonization and classifier-version awareness.

## 8. Remaining 20 packages

All 20 skipped months remain month-unique temporal gaps. Given observation-effort variability and seasonal concentration of gaps, acquiring all 20 strengthens completeness and reduces seasonal bias risk. Contents remain uninspected; do not assume similar structure. See `REMAINING_20_ACQUISITION_ASSESSMENT.md`.

## 9. Answers to final questions

1. **Does larger package size actually correspond to more observations?** Partly. Positive correlations exist with feature/classification records and folders, but bytes-per-record varies by schema/format; size is an imperfect proxy.
2. **Does it correspond to more cyanobacteria detections?** Only weakly/moderately and confounded by effort and schema; raw cyano counts should not be interpreted as biological intensity without effort normalization and validation.
3. **Are those detections adjusted for observation effort?** Descriptive per-1,000-record rates are provided in CSV; they are not calibrated, not bloom labels, and not confirmatory.
4. **Which seasonal months have the greatest observation coverage?** In the acquired subset, highest feature-record coverage includes June 2023, July 2020, March 2022; highest unique-day coverage includes May 2019, October 2019, December 2019. The full seasonal picture is incomplete due 20 missing months.
5. **Does the evidence strengthen the case for acquiring all 20 missing packages?** Yes. They are month-unique gaps, concentrated in seasonally important months, and acquired data shows substantial month-to-month effort/volume variability, so omission risks temporal/seasonal bias.

## Caveats

- ROI/image-level classification outputs are not calibrated biomass/cell density.
- No bloom/non-bloom labels assigned. No confirmatory analysis.
- Cyanobacteria label-pattern matching is heuristic; classifier taxonomy/validation not exhaustively audited.
- Measurements unavailable were reported as unavailable/empty, not zero where appropriate.
