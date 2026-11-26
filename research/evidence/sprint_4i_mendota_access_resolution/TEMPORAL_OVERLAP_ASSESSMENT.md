# Temporal Overlap Assessment

**Date:** 2026-11-23T23:32:06.599235+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Metadata-level overlap

| Pair | Overlap | Basis |
|---|---|---|
| 88.31 biology × 129.42 HF predictors | **2006-2020** (15 years) | EML coverage; raw unverified |
| 88.31 biology × 130.29 temperature | **2006-2019** (14 years) | EML coverage; raw unverified |
| 88.31 biology × 415.2 MO | **2006-2019** (14 years) | EML coverage; raw unverified |
| 129.42 × 130.29 | 2006-2019 | Same buoy, complementary variables |
| SSEC alternative × 88.31 | **2019-2020 only** | SSEC API 2019-2025; 2006/2018 unavailable |

## Resolution

- Biological cadence: **biweekly** ice-free (late Mar/Apr-early Sep), every 4 weeks to late Nov. Environmental: 1-minute (129.42/130.29); routine handheld (415.2).
- Interval-censored onset evaluation: **feasible in principle** over 14-15 years if raw data are complete, because biweekly sampling bounds onset intervals. It is not feasible to resolve sub-biweekly onset.
- Conventional baselines: sensor chlorophyll/phycocyanin thresholds, temperature, DO, pCO2 are available in principle; they are **sensor proxies**, not independent cell/biomass ground truth.
- Depth/station: 88.31 is a 0-8 m composite at the deep hole; buoy sensors are at discrete depths (DO ~0.5 m; thermistor chain; Chl/PC at buoy depth). 415.2 handheld profiles span the water column. A defensible comparator (e.g., surface/euphotic integration) must be defined; raw verification required.
- 2015 HR temperature gap in 130.29 is bounded; 129.42 may still provide modern predictors, but 2015 cross-check is incomplete.

## What remains scientifically uncertain

- Whether 88.31 contains complete Mendota records for all 2006-2020 years and how many slides were not identified.
- Per-channel 129.42 coverage and sensor changes.
- Exact depth/time alignment and QC comparability.
- Event/non-bloom adjudication (Gate 2 governance).

**No labels, event intervals, or modelling were created.**
