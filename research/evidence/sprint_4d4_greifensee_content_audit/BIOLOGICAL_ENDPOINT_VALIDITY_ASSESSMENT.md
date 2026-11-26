# Biological Endpoint Validity Assessment (Sprint 4D.4)

**Date:** 2026-11-22T23:36:45.421153+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Measurement object

The 5p0x `class_and_feat` packages contain camera-derived ROI/image-level classification outputs and SPCConvert-derived features from the Aquascope/DSPC at 3 m depth in Greifensee. They are **not** direct microscopy counts, flow cytometry cell densities, biovolume measurements, or laboratory biomass/toxin measurements.

## Candidate interpretations

| Interpretation | What it represents | Evidence supporting | Missing validation/calibration | Legitimate use now |
|---|---|---|---|---|
| Qualitative cyanobacteria presence in classified ROIs | Presence of cyano-pattern labels in classifier outputs | Cyano-pattern labels observed in 60-month outputs; Eyring 2025 describes classification pipeline | Class-definition mapping, per-class accuracy, false-positive/negative rates, ambiguous "probably" labels | Exploratory only, with caveats |
| Relative classification frequency / ROI rate | Proportion or rate of cyano-labeled ROIs among classified ROIs/images over time | Counts computable from outputs; ROI/sec proxy discussed in Merz 2021/Eyring 2025 | Observation-effort normalization, classifier drift/version harmonization, same-object duplication, field validation | Exploratory descriptive only |
| Relative ROI-level abundance proxy | Proxy for relative abundance of imaged/classified objects | DSPC ROI/sec used as proxy in prior work for selected taxa | Taxon-specific calibration, detection probability, volume sampled, turbidity/visibility effects, cyanobacteria-specific validation | Exploratory only; not calibrated abundance |
| Quantitative cell density | Cells/mL or equivalent | **None sufficient in these packages** | Independent cell-count calibration across cyanobacteria classes/conditions | Not supported |
| Biomass/biovolume | mg/L, mm3/L, etc. | **None in these packages** | Biovolume calibration, taxon-specific size/volume models, independent validation | Not supported |
| Bloom intensity / bloom-event ground truth | Ecologically/adjudicated bloom events | **None** | Independent event definition, validation, non-bloom exposure, protocol-compatible adjudication | Not supported; Gate 2 incompatible |

## Independent biological measurement distinction

Camera-derived classifications are **not independent biological measurements** of cyanobacteria abundance/biomass. They may be useful as exploratory sensor-derived signals, but EcoSentinel's confirmatory claims require independent biological endpoints/events with defensible validation.

## Bottom line

The dataset can support limited exploratory description of camera-derived cyanobacteria classification signals, subject to major caveats. It does **not** currently establish an independent, calibrated biological bloom endpoint suitable for Gate 2 confirmatory evaluation.
