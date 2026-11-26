# Environmental Data Feasibility — Mendota (Sprint 4E.1C)

**Date:** 2026-11-23T07:05:41.270436+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 130.29 High-frequency buoy temperature (knb-lter-ntl.130.29)

- **Temporal coverage:** 2006-2019 (EML range; per-year HR entities 2006-2019 listed, with 2009/2015 coverage as represented in EML).
- **Entities:** Daily, Hourly, High-resolution yearly files (2006-2019).
- **Variables:** sampledate/sampletime, depth, wtemp, flag_wtemp (+ year/month/day/hour in aggregated files).
- **Assessment:** Temperature only. Useful for thermal context but **insufficient alone** for EcoSentinel's multivariate environmental-relationship question if other predictors (DO, pH, conductivity, nutrients, etc.) are required. High-resolution potential exists, but 2015 HR entity missing on CN.

## 415.2 Microbial Observatory (knb-lter-ntl.415.2)

- **Temporal coverage:** 2006-06-15 to 2019-10-24 (EML).
- **Entities:** YSI-Poseidon 2014-2019 (temp, DO, pH, specific conductance, barometer, depth); non-Poseidon water temps; non-Poseidon dissolved oxygen.
- **Assessment:** Has relevant physico-chemical variables (temp, DO, pH, conductivity). Sampling described as routine Microbial Observatory sampling - likely discrete/low-frequency relative to buoy HF; actual cadence must be verified. Not a continuous HF multivariate buoy record.

## Overall

Environmental coverage is **fragmented across packages**: 130.29 gives HF temperature; 415.2 gives some physico-chemical variables at likely lower cadence. Neither alone clearly satisfies the "high-frequency environmental measurements" expectation for the full EcoSentinel predictor set. Alignment and variable sufficiency remain unresolved.
