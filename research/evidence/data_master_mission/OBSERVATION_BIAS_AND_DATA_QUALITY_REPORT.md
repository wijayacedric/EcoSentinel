# Observation Bias and Data Quality Report

**Date:** 2026-11-23T23:18:29.122618+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Buffalo Pound

**Observation bias (verified file-level):**
- Biological sampling dates are approximately weekly in 2018 (25 dates over 112 days) but less regular in 2019 (17 dates with a 16-day gap). No evidence in the data files of event-triggered sampling; however, field-log confirmation is unavailable, so bias cannot be excluded.
- Sampling depth fixed at 0.8 m; single station; no station switching observed in the taxonomy files.
- Missing observations are not randomly distributed: sampling is ice-free-season only, and 2019 has a mid-season gap.

**Data quality:**
- Buoy flags exist for all variables; README documents sensor fouling, extreme winds, and corrected 2017/2018 conductivity.
- 2018 key-variable completeness ≈88%; 2021 ≈98-100%; deep pH missing 2021 and deep chlorophyll missing 2018.
- Chlorophyll/phycocyanin are RFU sensor proxies, not calibrated biomass; they cannot serve as independent biological ground truth.
- Toxins files have multi-row analytical headers (LOD/LOQ rows) and require careful parsing; not used as endpoint here.

## Lake Mendota

- Cannot assess observation bias or QC without data bytes. NTL LTER sampling is typically scheduled, but this is **not verified** for this package.
- Critical risk: if sampling frequency changed around bloom periods, event onset would be interval-censored and potentially biased.

## Western Lake Erie

- Literature indicates scheduled May-Sep sampling, COVID disruption in 2020, and opportunistic scum sampling. Opportunistic scum samples would strongly bias bloom-intensity estimates if mixed with routine samples.
- NCEI inaccessible, so QC flags/missingness unverified.

## Greifensee

- Continuous camera with maintenance gaps; classifier/schema changes across years; no independent validation. Observation effort proxies vary.

## Bottom line

Data-quality evidence is adequate only for Buffalo Pound. For every candidate, **non-bloom exposure cannot yet be defensibly established**; no labels or intervals were created.
