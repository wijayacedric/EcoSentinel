# Scientific Strengths and Failure Modes — Buffalo Pound Stress Test

**Date:** 2026-11-23T23:22:37.724583+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Strengths (verified)

1. **Genuine independent biological endpoint:** species-level microscopy counts and biomass, not a sensor proxy or classifier.
2. **Genuine high-frequency environmental record:** 10-min, 68 variables, eight ice-free seasons.
3. **Real alignment:** all 25 (2018) and 17 (2019) biological dates matched to buoy days; 0.8 m depth match; 93-99% valid key variables on those days.
4. **Additional context:** YSI profiles, group biomass, heterocyte counts, toxin files.
5. **Clear provenance and licences:** FRDR and Borealis DOIs, local SHA256 records.

## Failure modes (strongest disqualifiers)

1. **Two seasons / 42 date-level biological observations.** Cannot support held-out temporal validation, stable false-alarm rates, or multi-year event evaluation. This alone disqualifies confirmatory use.
2. **No defensible non-bloom exposure.** Both seasons are bloom seasons (~71% cyanophyte biomass); no winter/spring baseline; no adjudicated non-bloom intervals.
3. **Biological cadence too coarse for onset.** Median 4-8 days, max 16 days; bloom onset and warning lead time are interval-censored.
4. **Pseudoreplication.** Sensor records and taxon rows are not independent events; effective N ≈42 dates.
5. **Sensor discontinuities could mimic relationship change.** 2015 shallow DO 38.5%; deep 6920 suite ends 2019; 2021 deep pH 0%; conductivity corrections 2017/2018; fouling spikes; identical runs up to 216.
6. **Method/schema change 2018→2019.** Different replicate encoding; 73 vs 56 taxa, only 39 shared. Harmonisation unresolved.
7. **Prior art overlap.** Painter 2022/2023, Baulch 2025, and broader EWS/forecasting literature. No originality claim.

## Exploratory vs confirmatory

| Use | Suitable? | Reason |
|---|---|---|
| Data-quality/missingness audit | **Yes** | Verified files |
| Descriptive seasonal alignment | **Yes** | 42 matched dates |
| Exploratory method prototyping within season | **Yes, with caveats** | Small N; no labels |
| Hypothesis testing / performance claims | **No** | Gate 2 paused |
| Confirmatory early-warning evaluation | **No** | Two seasons, no non-bloom exposure, no held-out validation |
| Matched-FAR evaluation | **No** | Event/false-alarm rates unstable with 2 seasons |

## What would change the verdict

- Additional independent microscopy/cell-biomass across multiple years, including non-bloom seasons, with documented sampling design.
- Or a different candidate with multi-year independent biology + HF predictors (Mendota if access granted).
- Protocol-approved event/non-event adjudication (requires Gate 2, not authorised now).
