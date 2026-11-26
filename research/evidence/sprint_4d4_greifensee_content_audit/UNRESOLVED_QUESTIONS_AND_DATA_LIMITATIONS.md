# Unresolved Questions and Data Limitations (Sprint 4D.4)

**Date:** 2026-11-22T23:36:45.421153+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Unresolved

1. **Cyanobacteria label semantics:** The 7 cyano-pattern labels observed in outputs (e.g., `cyanobacteria_colonial_probably`, `chroococcales`, `dolichospermum`) require authoritative classifier taxonomy mapping and class definitions. "Probably" and broad group labels are ambiguous for species/genus-level claims.
2. **Classifier performance by class:** Per-class precision/recall/F1 for cyanobacteria classes in 5p0x 2018-2023 not audited. Model/version changes across time (Plankifier-era vs Plankiformer-only 2023 signature) limit comparability.
3. **Independent biological validation:** No independent microscopy/flow cytometry/biovolume ground truth in these packages. ROI/sec calibration (Merz 2021) is limited and not a cyanobacteria bloom ground truth.
4. **Observation effort / camera uptime:** Unique days/timestamps derived from features.csv provide partial coverage proxy; full camera uptime, maintenance, outages, and acquisition interruptions not fully reconstructed.
5. **Confidence/probability fields:** Feature files inspected did not expose obvious confidence/probability columns in sampled headers; classification txt outputs appear to be label assignments. This needs confirmation against full classifier output specification.
6. **ROI duplication / same-object tracking:** Repeated detections of same object across frames possible; ROI counts are not independent organism counts.
7. **Cross-schema comparability:** Four schema signatures observed across 60 months. 2023 months have only Ensemble+features (no Plankifier/chytrid/ciliates files). Direct cross-era count comparison is risky.
8. **Temporal alignment to EcoSentinel target:** Greifensee 2018-2023 is a different ecosystem than Buffalo Pound and different biological measurement modality than independent bloom labels required by Gate 2.

## Limitations

- Audit is structural/content-descriptive; not exhaustive semantic validation of every record.
- Cyano identification used heuristic regex over labels; not a validated taxonomic mapping.
- No biological event labels created. No modelling or confirmatory analysis.
