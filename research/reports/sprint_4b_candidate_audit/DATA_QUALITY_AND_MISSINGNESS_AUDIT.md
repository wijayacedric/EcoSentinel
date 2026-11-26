# Data Quality and Missingness Audit (Sprint 4B)

**Date:** 2026-11-22  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Candidate A — Greifensee Dryad r4454
- **File-level audit:** Performed on user-provided zip (SHA256 recorded). 
- **2014-2015 cytobuoy:** 9366 rows, 44 cols. dens_clean/dens_euks/dens_cyanos/cyano_percent: 7235 non-null, 2131 null. High missingness: po4/no3/nh4 inflow conc/mass ~96.7%; ammonia ~93.1%; dissolved phosphate/nitrate ~93.0%; grazers_all ~92.9%. Depths 1-10m, mostly 4h intervals.
- **Long-term microscopy:** 388 rows, 36 cols. dens_phytos/dens_cyanos/dens_euks/cyano_percent: 346 non-null, 42 null. High missingness: Mg_min/max ~53.9%; thermocline_depth ~35.1%; POC ~33.0%. Monthly resolution.
- **Method/QC notes from README:** ammonia below detection limit set to 3; dissolved phosphate below detection limit set to 0.5; irradiance estimated from regression; zooplankton/grazers interpolated by GAM in some columns; long-term dates rounded to nearest month and duplicates averaged.
- **Status:** File-verified (basic audit); full QC provenance not independently audited.

## Candidate B — Greifensee 2018-2023
- **File-level audit:** Not possible (ERIC Anubis blocked).
- **Paper-indicated quality info:** Paper describes data cleaning removing technical artefacts; meteorological cleaning removed 33.58% data points (16,662,570 remaining); CTD cleaning removed 14.12% (14,068,236 remaining); DSPC acquisition changes in 2018 vs later; 1-in-6 subsampling for 0.5x magnification; diel vertical migration caveat; recommendation for daily aggregation; limitations include translucent object detection, >~10um size limit, 3m depth misses surface blooms, underestimation of species richness. 
- **Unverified:** Actual missingness by variable/taxon, classification confusion matrix details, SI tables, per-class cyanobacteria performance.
- **Status:** Partial (paper-described), file-unverified.

## Candidate C — Mendota NTL-LTER 88.31
- **File-level audit:** Not possible (PASTA/EDI access blocked in environment).
- **Status:** Unverified.

## Candidate D — Buffalo Pound Painter 2018-2019
- **File-level audit (inspected files):** 2018 phyto CSV 818 rows, 25 unique DOY; 2019 17 unique DOY. No missing-value audit performed across all columns. Toxin CSVs have complex multi-row headers and encoding (latin-1) requiring careful parsing before use.
- **Known quality concerns from project records:** 2019-07-17 anomaly unresolved; sparse interval-censored sampling; limited to 2018-2019.
- **Status:** Partial file verification; full QC audit incomplete.
