# Sprint 4D.4 Executive Report — Complete Greifensee 5p0x Biological Content and Consistency Audit

**Project:** EcoSentinel  
**Date:** 2026-11-22T23:37:22.944270+00:00  
**Scope:** Descriptive file-level audit of all 60 Greifensee 2018–2023 5p0x `class_and_feat` monthly packages  
**Gate 2 status:** **PAUSED / NOT APPROVED — Option C (Exploratory Only)** (unchanged)

## 1. Authoritative inventory and structural usability

- **60/60 packages present locally**; filenames/sizes/SHA256 match `COMPLETE_60_PACKAGE_MANIFEST.csv`. Coverage May 2018–June 2023. May 2022 DOI `10.25678/x00B8V` correctly represented. No missing/duplicated/misidentified months detected.
- **All 60 archives opened and were structurally inspected** via Python `tarfile`; no archive-level parse failures. Month-level parse_errors: none.
- Totals (descriptive): feature records 15,699,488; classification records 57,102,044; heuristic cyano-matched classification records 1,137,454.

## 2. Content and schema consistency

- **Four schema signatures observed** across 60 months (see `CLASSIFIER_AND_SCHEMA_VERSION_HISTORY.csv`):
  - 42 months: `Ensemble_models_Plankiformer_predictions_geo_mean_finetuned.txt | Predictions_avg_ens_chytrid.txt | class_CILIATES_leaderabs0.txt | classification_leaderabs0.txt | features.csv`
  - 8 months: `class_CILIATES_leaderabs0.txt | classification_leaderabs0.txt | features.csv` (Jan–May 2020, Oct–Dec 2020)
  - 4 months: `Ensemble_models_Plankiformer_predictions_geo_mean_finetuned.txt | class_CILIATES_leaderabs0.txt | classification_leaderabs0.txt | features.csv` (Jun–Sep 2020)
  - 6 months: `Ensemble_models_Plankiformer_predictions_geo_mean_finetuned.txt | features.csv` (Jan–Jun 2023)
- Classifier/model version metadata is **not fully explicit inside tarballs**; 000C2G readme states Plankiformer (CNN variant, Nov 2022 release) and Plankifier 2018–2022. Cross-era comparability requires documented version mapping and harmonization.

## 3. Cyanobacteria/taxonomic audit

- Heuristic regex over classification labels found **7 cyano-pattern labels**: cyanobacteria_colonial_probably (572,359), chroococcales (394,014), cyanobacteria_colonial_blue (117,085), dolichospermum (20,558), cyanobacteria_filamentous (13,610), cyanobacteria_colonial_clathrate (10,692), planktothrix (9,136).
- These are **output labels, not independently validated taxonomic ground truth**. Some are broad/ambiguous (`cyanobacteria_colonial_probably`, `chroococcales`, `cyanobacteria_colonial_blue/clathrate/filamentous`); others genus-like (`dolichospermum`, `planktothrix`). Species-level identification is **not supported** by this audit.
- Months with zero heuristic cyano-matched records: January 2020, February 2020, March 2020, April 2020, May 2020, October 2020, November 2020, December 2020. For the 2020 3-file months, absence may reflect schema/classifier-output differences, not confirmed biological absence.

## 4. Observation effort and comparability

- Observation-effort proxies (unique days/timestamps from features, timestamp folders, record counts) vary substantially by month. Camera uptime/maintenance logs not fully reconstructed from tarballs.
- **Raw monthly detection frequencies cannot be fairly compared** across all 60 months without: effort normalization, schema/classifier harmonization, label crosswalk, confidence/validation assessment, and handling of same-object repeated detections.

## 5. Independent biological validation / endpoint validity

- Packages contain **camera-derived ROI/image-level classifications and features** at 3 m depth, not independent microscopy/flow cytometry/biovolume/toxin measurements.
- Merz 2021/Eyring 2025 provide limited proxy/calibration context, but **no cyanobacteria-specific independent bloom ground truth** is established by inspected packages. 
- Therefore dataset can support **exploratory camera-signal description** only; it does **not** support Gate 2 confirmatory independent biological event evaluation.

## 6. Prior publication overlap

- Eyring et al. 2025 (Sci Data, 10.1038/s41597-025-04988-9) is the data descriptor for this dataset/system - **high overlap**.
- Ntetsika et al. 2026 (ISME Communications, web-identified) indicates toxic cyanobacteria analysis on Greifensee/Aquascope context - **high overlap risk**; full text not audited here.
- No novelty claims made.

## 7. Final questions (direct answers)

1. **Are all 60 packages structurally usable?** **Yes, structurally**. All 60 opened/readable; no archive-level parse failures. Usability for scientific comparison is constrained by schema/classifier differences and missing validation.
2. **Are cyanobacteria specifically identifiable?** **Partially/heuristically at label level, not independently validated.** Seven cyano-pattern labels observed; some broad/ambiguous, some genus-like. No species-level or validated ground-truth confirmation in this audit.
3. **Are classifications consistent across May 2018–June 2023?** **No.** Four schema signatures; 2023 months missing Plankifier/chytrid/ciliates files present in earlier periods; classifier-version mapping not fully explicit.
4. **Can monthly detection frequencies be compared fairly?** **Not without major caveats.** Raw counts are confounded by observation effort, schema/classifier changes, label ambiguity, and duplicate/same-object detections. Effort-normalized, harmonized, validation-aware comparison would be required for exploratory use only.
5. **Is there evidence of independent biological validation?** **Not sufficient for EcoSentinel confirmatory endpoint validity.** Limited proxy/calibration context exists in literature (Merz 2021/Eyring 2025), but no independent cyanobacteria-specific microscopy/biovolume bloom ground truth confirmed in packages.
6. **What biological conclusions can legitimately be drawn?** Exploratory descriptive conclusions about **camera-derived ROI/image-level classification signals** at 3 m depth, with explicit caveats. Not calibrated cell density, biomass/biovolume, or bloom-event ground truth.
7. **Can this dataset support EcoSentinel's central research question, and under what limitations?** **Not for Gate 2 confirmatory evaluation in its current audited form.** It may support **exploratory, hypothesis-generating** analysis of camera-derived signals alongside environmental data, but EcoSentinel's central confirmatory question requires independent biological event/non-event endpoints, defensible validation, and protocol-compatible evaluation. Greifensee is also a different ecosystem than Buffalo Pound.
8. **What is the single most important remaining scientific barrier?** **Lack of an independently validated, calibrated cyanobacteria biological endpoint/event ground truth compatible with EcoSentinel’s confirmatory Gate 2 design** (plus cross-era classifier harmonization/validation).

## 8. Deliverables

All 12 required files are in `research/evidence/sprint_4d4_greifensee_content_audit/`.

**Gate 2 remains PAUSED / NOT APPROVED — Option C (Exploratory Only).**
