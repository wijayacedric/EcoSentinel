# Greifensee 2018-2023 5p0x class_and_feat Completeness Audit

**Project:** EcoSentinel  
**Date:** 2026-11-22  
**Sprint:** 4D.1 — File-completeness and provenance audit only  
**Gate 2 status:** **PAUSED / NOT APPROVED — Option C (Exploratory Only)** (unchanged)

## Direct answer

**The 20 skipped 5p0x class_and_feat tarballs are scientifically necessary for a complete/defensible temporal 5p0x series, but not all are strictly necessary before limited preliminary exploratory work.** 

- **Scientifically necessary for completeness / unbiased temporal coverage:** all 20 skipped files, because each corresponds to a unique month in the C2G 2018-2023 monthly series and no acquired 5p0x class_and_feat file covers that month. Omitting them creates systematic temporal gaps.
- **Minimum additional set for a defensible exploratory time series:** all 20 skipped files (or all months required by the intended analysis window). There is no smaller subset that removes the identified month gaps, because each skipped file is month-unique.
- **If the intended exploratory analysis can be explicitly restricted:** only the skipped months within the planned analysis window are essential; others remain important for completeness but can be deferred with explicit scope limitation. However, this requires a pre-declared window and gap-aware interpretation.

## 1. Inventory (verified)

- C2G landing package lists **60 monthly sub-DOIs** (May 2018–Jun 2023; note May 2022 DOI `10.25678/x00B8V`).
- Sprint 4D manifest contains **59** `5p0x class_and_feat` rows: **39 ok**, **20 skipped_size**, 0 err.
- Filesystem verification: all 39 ok files exist at recorded local paths. No missing/unexpected substitutions found.
- The 1 monthly DOI not represented as a 5p0x row in manifest is: **none by month gap in 60-list except May 2022 was included after resolution**; inventory CSV records the exact mapping. (See `ALL_59_TARBALL_INVENTORY.csv`.)

## 2. Acquired 39 content audit (structural)

All 39 acquired tarballs opened successfully. Observed structure: per-timestamp subfolders containing per-image ROI-level classification and/or feature files.

Observed basenames across samples/all audited files include:
- `features.csv` (present in sampled 2020/2023 packages)
- `classification_leaderabs0.txt`
- `Ensemble_models_Plankiformer_predictions_geo_mean_finetuned.txt`
- `class_CILIATES_leaderabs0.txt` (earlier packages)
- `Predictions_avg_ens_chytrid.txt` (earlier packages)

Schema/structure is **not uniform across all years** (e.g., May 2018 shows 4 classification txt types; Jun 2023 shows `features.csv` + Ensemble Plankiformer predictions). This is an important provenance/processing-version caveat; do not assume cross-month schema equivalence without explicit harmonization.

Observation unit appears to be image/ROI-level records (sample rows show image path + label/prediction; features.csv has per-image feature columns including timestamp). Temporal resolution appears high-frequency within deployment periods but not exhaustively quantified here.

## 3. Skipped 20 comparison

| Month | DOI | Size (bytes) | Category | Evidence |
|---|---|---:|---|---|
| July 2018 | 10.25678/0009JA | 309276716 | A. Essential | Unique month; no acquired 5p0x class_and_feat covers this month; content not inspected |
| August 2018 | 10.25678/0009KB | 532128625 | A. Essential | Unique month; no acquired 5p0x class_and_feat covers this month; content not inspected |
| September 2018 | 10.25678/0009MC | 1475244474 | A. Essential | Unique month; no acquired 5p0x class_and_feat covers this month; content not inspected |
| October 2018 | 10.25678/0009ND | 844432447 | A. Essential | Unique month; no acquired 5p0x class_and_feat covers this month; content not inspected |
| November 2018 | 10.25678/0009QF | 217149787 | A. Essential | Unique month; no acquired 5p0x class_and_feat covers this month; content not inspected |
| June 2019 | 10.25678/0009WM | 158171800 | A. Essential | Unique month; no acquired 5p0x class_and_feat covers this month; content not inspected |
| July 2019 | 10.25678/0009XN | 215466856 | A. Essential | Unique month; no acquired 5p0x class_and_feat covers this month; content not inspected |
| August 2019 | 10.25678/0009YP | 197644782 | A. Essential | Unique month; no acquired 5p0x class_and_feat covers this month; content not inspected |
| September 2019 | 10.25678/0009ZQ | 284975202 | A. Essential | Unique month; no acquired 5p0x class_and_feat covers this month; content not inspected |
| August 2020 | 10.25678/000AG3 | 160081731 | A. Essential | Unique month; no acquired 5p0x class_and_feat covers this month; content not inspected |
| September 2020 | 10.25678/000AH4 | 173400741 | A. Essential | Unique month; no acquired 5p0x class_and_feat covers this month; content not inspected |
| March 2021 | 10.25678/000ASC | 220894134 | A. Essential | Unique month; no acquired 5p0x class_and_feat covers this month; content not inspected |
| July 2021 | 10.25678/000AXG | 158180843 | A. Essential | Unique month; no acquired 5p0x class_and_feat covers this month; content not inspected |
| August 2021 | 10.25678/000AYH | 232147308 | A. Essential | Unique month; no acquired 5p0x class_and_feat covers this month; content not inspected |
| September 2021 | 10.25678/000AZJ | 196356919 | A. Essential | Unique month; no acquired 5p0x class_and_feat covers this month; content not inspected |
| July 2022 | 10.25678/000BAX | 254864374 | A. Essential | Unique month; no acquired 5p0x class_and_feat covers this month; content not inspected |
| August 2022 | 10.25678/000BBY | 272689871 | A. Essential | Unique month; no acquired 5p0x class_and_feat covers this month; content not inspected |
| September 2022 | 10.25678/000BCZ | 396335875 | A. Essential | Unique month; no acquired 5p0x class_and_feat covers this month; content not inspected |
| October 2022 | 10.25678/000BJ0 | 156652754 | A. Essential | Unique month; no acquired 5p0x class_and_feat covers this month; content not inspected |
| March 2023 | 10.25678/000BQ5 | 156121811 | A. Essential | Unique month; no acquired 5p0x class_and_feat covers this month; content not inspected |

**All 20 are month-unique gaps.** No skipped month is covered by another acquired 5p0x class_and_feat file. Therefore none can be classified redundant on available evidence.

## 4. Scientific necessity assessment

- **A. Essential (for complete 5p0x temporal coverage):** all 20 skipped files — July 2018, August 2018, September 2018, October 2018, November 2018, June 2019, July 2019, August 2019, September 2019, August 2020, September 2020, March 2021, July 2021, August 2021, September 2021, July 2022, August 2022, September 2022, October 2022, March 2023.
- **B. Important:** n/a beyond A; if a user pre-declares a narrower analysis window, skipped months outside that window become deferrable but still important for completeness.
- **C. Redundant:** none evidenced.
- **D. Unclear:** content-level equivalence/quality remains unclear because skipped files were not downloaded/inspected; however temporal uniqueness is clear.

## 5. Gap/bias risk

Omitting the 20 skipped months creates **systematic temporal gaps** concentrated in larger-file months (many summer/high-activity months are large). This risks seasonal/biological bias if used for time-series analysis. The 39-file subset is therefore **not temporally complete** for 2018-2023.

## 6. Recommendation

- **For a scientifically defensible exploratory 5p0x time series covering the available 2018-2023 period:** acquire all 20 skipped files listed in `RECOMMENDED_ADDITIONAL_DOWNLOADS.csv`.
- **For limited preliminary exploratory work only:** a smaller pre-declared window may be used, but any omitted month must be explicitly declared as missing; do not interpret as complete.
- **Do not start downloading until this audit is reviewed.**

## 7. Restrictions confirmation

No files modified/renamed/deleted/overwritten. No Anubis/auth/CAPTCHA/access controls bypassed. No custodians contacted. No uploads/publication/commits/pushes. No biological event labels, modelling, confirmatory analysis, or Gate 2 changes.
