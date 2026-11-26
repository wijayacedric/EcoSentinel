# Sprint 4F Executive Report — Buffalo Pound Data Quality, Alignment & Scientific Limits Audit

**Date:** 2026-11-23T23:22:37.724583+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Verdict: **FAIL for formal Gate 2 readiness review (confirmatory); SUITABLE for exploratory work only**

This is a fitness-for-confirmatory-purpose failure, not a claim that the data are worthless. Buffalo Pound is the only candidate with verified independent biological counts and aligned high-frequency environmental data. It nonetheless cannot support the intended confirmatory early-warning evaluation because it has **two biological seasons, ~42 independent sampling dates, one station/depth, and no verified non-bloom exposure**.

## What was verified

- **Eight buoy files** exist, SHA256-verified; 68 variables; 10-min cadence (2014 15-min); 2014-06-11 to 2021-10-07; ice-free only.
- **Biological files:** 2018 = 25 dates, 817 taxon rows, 73 taxa, 170 cyanophyte rows; 2019 = 17 dates, 405 rows, 56 taxa, 78 cyanophyte rows; depth 0.8 m; species-level counts and biomass.
- **Additional biological files acquired and verified:** group biomass, heterocyte counts, YSI profiles (2018/2019). These strengthen exploratory context.
- **Alignment:** all 25 (2018) and 17 (2019) biological dates matched to buoy days; 0.8 m depth match; 121-144 records/day (2018), 42-131 (2019).
- **Licences:** buoy CC BY 4.0 (verified); Painter data CC BY-NC-SA 4.0 (verified via Borealis API).

## Why FAIL (confirmatory)

1. **Two seasons only.** At most two annual cycles; cannot hold out years or estimate stable false-alarm rates.
2. **No defensible non-bloom exposure.** Both seasons are bloom seasons with ~71% cyanophyte biomass; no winter/spring baseline; no adjudicated non-bloom intervals.
3. **Sparse biological cadence.** Median gap 4 d (2018), 8 d (2019), max 16 d; bloom onset can occur between samples. Warning lead-time and interval censoring cannot be resolved.
4. **Pseudoreplication risk.** 40k+ sensor readings and 1,222 taxon rows collapse to 42 date-level biological observations. Sensor records are repeated measurements, not independent events.
5. **Sensor discontinuities.** 2015 shallow DO only 38.5% valid; deep 6920 suite ends 2019 (2019 deep DO 2.78%, pH 6.45%, BGP 0%); 2021 deep pH 0%; conductivity calibration corrections 2017/2018; fouling B7 spikes; identical-value runs up to 216.
6. **Method/schema change between years.** 2018 uses `Sample_ID`; 2019 uses `REP` with labels on disjoint dates; 73 vs 56 taxa, only 39 shared. Harmonisation is unresolved.
7. **Prior art overlap.** Painter 2022/2023 and Baulch 2025 already describe this system and its bloom phases; no novelty claim is supportable.

## What Buffalo Pound can support (Option C)

- Descriptive data-quality and missingness characterisation.
- Verified alignment tables.
- Exploratory method development on within-season data, with explicit caveats.
- Hypothesis generation, not hypothesis testing or performance claims.

## Deliverables

All ten files in `research/evidence/sprint_4f_buffalo_pound_stress_test/`.

**Gate 2 remains PAUSED / NOT APPROVED — Option C (Exploratory Only).**
