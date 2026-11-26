# Stage 2 Early-Warning Requirements Reassessment

**Sprint:** 4L.20  
**Date:** 2026-11-26  
**Question:** What would the original early-warning ambition actually require, and does any current dataset qualify?  
**Status:** Requirements reassessment. **Stage 2 remains conditional and unqualified. No event audit performed. No contact made.**

---

## 1. The original ambition

> Can persistent changes in relationships between freshwater environmental variables provide earlier warning of cyanobacterial blooms than conventional monitoring, at comparable false-alarm rates?

This is not a same-date association question. It requires:

- a future bloom outcome;
- a lead time;
- a pre-specified event definition;
- non-event exposure;
- a false-alarm denominator;
- a comparable baseline monitoring rule;
- out-of-sample evaluation;
- a leakage-safe design.

The current Stage 1 measurement audit does **not** answer this question and cannot be presented as if it does. Stage 2 is a separate programme.

---

## 2. What the current datasets provide

### 2.1 Mendota

**Strengths:**

- Long daily sensor record (2006–present), including Turner/YSI chlorophyll and phycocyanin.
- Long microscopy record (1995–present), 402 dates; 400 at 0–8 m.
- Measurement-independent microscopy; species-level biovolume.
- CC BY 4.0; well documented.

**Fatal limitations for Stage 2:**

- Biology is **biweekly** during the ice-free season, every 4 weeks in autumn, and usually once in winter; not weekly-or-better.
- Biology is **date-only**, with no sample time.
- Biology is a **0–8 m composite**; sensors are at 0.5 m; no depth-resolved biology.
- No independently defined bloom/non-bloom events; no event labels; no event count.
- No verified non-event exposure.
- No matched false-alarm denominator.
- Sensor era changes (Turner/YSI) without a crosswalk.
- No per-record calibration/maintenance history.

**Verdict:** Mendota is **not** a Stage 2 dataset for daily EWS. It may support a seasonal descriptive analysis, but not the original question.

### 2.2 Buffalo Pound

**Strengths:**

- 10-minute sensor record; 0.82 m pigments; depth-aligned biology at 0.8 m.
- Two seasons of microscopy (42 dates).
- Direct published evidence of bloom phases and sensor non-detection (Painter 2022).

**Fatal limitations for Stage 2:**

- Two seasons only; cannot support ≥10 independent events or a stable event model.
- Duplicate/`REP` semantics, biomass derivation, B7, coverage, time zone and calibration unresolved.
- No event definition or non-event exposure.
- Different licence (CC BY-NC-SA 4.0).
- No custodian confirmation.

**Verdict:** Buffalo Pound is **not** a Stage 2 dataset. It is a future context case at best.

### 2.3 Müggelsee

**Strengths:**

- FRED 867: phytoplankton 1979–ongoing, weekly growing season / biweekly ice, Utermöhl microscopy, biomass/biovolume, documented conversion.
- FRED 1: weekly multiparameter probe 1978–2019, including chlorophyll a and phycocyanin.
- FRED 1145: high-frequency station 2001–ongoing, 5-minute nominal, 1.5 m, chlorophyll a and phycocyanin.
- Long record, formal DOIs, metadata PDFs.

**Fatal/conditional limitations:**

- Data are **all rights reserved**; written permission is required.
- Sensor station M210 is not the phytoplankton stations M3/M5/M7/M8/M10; spatial offset not quantified.
- Sensor depth 1.5 m vs integrated 0–4/0–7 m samples; depth mismatch.
- No public event definition, event count, non-event exposure or calibration/QC record.
- High-frequency series has hourly gaps before 2013 and winter hourly data.
- Weekly probe ends in 2019; high-frequency series continues, but the biological series is ongoing.
- Sampling times are not verified.

**Verdict:** Müggelsee remains the **strongest public candidate**, but it is **not qualified**. It is the only current lead with a plausible weekly-or-better microscopy + high-frequency sensor combination.

---

## 3. Required Stage 2 qualification framework

The original threshold (≥5 years, ≥10 events, weekly-or-better time-stamped microscopy, co-located high-frequency sensors, non-bloom periods, calibration metadata) is necessary but insufficient. The following is the proposed strengthened framework.

### 3.1 Outcome definition

| Requirement | Why |
|---|---|
| Pre-specified bloom event definition | The outcome must exist before analysis |
| Definition independent of the candidate sensor | Avoid circularity |
| Threshold, minimum duration, separation rule | Prevent overlapping events |
| Treatment of partial/truncated events | Avoid immortal-time/interval bias |
| Event adjudication by independent biology | Prevent sensor-derived labels |

### 3.2 Biological ground truth

| Requirement | Why |
|---|---|
| Weekly or better during bloom season | Daily/weekly lead time needs resolution |
| Sample dates and times documented | Align sensor windows |
| Species/taxon-level biovolume or biomass | Community-specific pigment content |
| Consistent taxonomy/processor history | Prevent apparent regime shifts |
| Detection limits and counting error | Distinguish absence from non-detection |
| Sample depth and integration documented | Match sensor depth |
| Preservation/counting methods stable | Comparability across years |

### 3.3 Sensor data

| Requirement | Why |
|---|---|
| Co-located with biological station | Same water parcel |
| Depth matched or quantified | Surface vs integrated mismatch |
| High-frequency (sub-hourly) | Capture blooms/onsets |
| Calibration/maintenance/QC records | Sensor drift/fouling |
| Range/saturation/fouling flags | Avoid artefacts |
| Consistent instrument configuration | No hidden era effects |
| Missingness documented | Avoid coverage bias |

### 3.4 Temporal alignment

| Requirement | Why |
|---|---|
| Sample times known or bounded | Match sensor window |
| Date/time zone convention documented | Avoid date-boundary errors |
| Bloom window pre-specified | No post-hoc windows |
| Lead time pre-specified | No lead-time search |
| Lag/lead analysis limited to pre-specified lags | Avoid researcher degrees of freedom |
| Interval censoring acknowledged | Biweekly biology cannot resolve daily onset |

### 3.5 Non-event exposure and false alarms

| Requirement | Why |
|---|---|
| Non-bloom periods sampled at comparable resolution | Otherwise the model learns season |
| False-alarm rate defined | Comparable monitoring claim |
| Baseline monitoring rule defined | “Earlier than conventional” comparison |
| Matched false-alarm denominator | Avoid unfair comparison |
| Alert threshold pre-specified | No threshold optimisation |
| Consequence of false positives/negatives stated | Decision relevance |

### 3.6 Evaluation design

| Requirement | Why |
|---|---|
| Temporal holdout or rolling-origin evaluation | Out-of-sample test |
| No leakage from future to past | Avoid optimistic performance |
| Event-level, not sample-level, reporting | Avoid pseudo-replication |
| Performance by year/event | Stability |
| Null/seasonal benchmark | Show added value |
| Alternative explanations tested | Season, autocorrelation, sampling |
| Uncertainty reported | Decision relevance |
| Pre-registered analysis plan | Prevent outcome switching |

### 3.7 Data governance

| Requirement | Why |
|---|---|
| DOI/version/correction history | Reproducibility |
| Written licence/permission | Legal use |
| Data dictionary | Variable meanings |
| Custodian confirmation | Provenance |
| Redistribution terms | Competition/publication |
| Fixed analysis version and hashes | Reproducibility |

---

## 4. Müggelsee assessment against the framework

| Requirement | Status | Evidence |
|---|---|---|
| ≥5 years | **Pass** | Phytoplankton 1979–; sensors 2001– |
| ≥10 independent events | **Unknown** | No event definition/count |
| Weekly-or-better microscopy | **Pass/Conditional** | Weekly growing season, biweekly ice; sample times not verified |
| Co-located high-frequency sensors | **Conditional/Fail** | Station M210 vs M3/M5/M7/M8/M10; offset not quantified |
| Depth matching | **Fail/Conditional** | 1.5 m sensor vs integrated 0–4/0–7 m |
| Non-bloom exposure | **Unknown** | Likely sampled; no classification |
| Calibration/QC | **Unknown** | Not public |
| Event definition independent of sensor | **Fail** | No public definition |
| False-alarm denominator | **Fail** | No baseline/alert rule |
| Holdout/leakage design | **Not yet specified** | Requires Stage 2 protocol |
| Licence/access | **Fail/Unknown** | All rights reserved; permission required |
| Data dictionary | **Conditional** | Metadata PDFs; full dictionary/code not public |

**Result:** Müggelsee is **not qualified**. It is a candidate for a future access/qualification process.

---

## 5. What would justify resuming Stage 2

A Stage 2 resumption would require **all** of:

1. Written permission/licence for the intended use.
2. A complete data dictionary and calibration/QC record.
3. A pre-specified, sensor-independent bloom event definition.
4. At least ten independent events after QC and matching.
5. Non-event exposure at comparable resolution.
6. Sample times/depths documented or bounded.
7. Spatial co-location or a quantified offset.
8. A pre-specified false-alarm/alert rule and baseline monitoring comparison.
9. A temporal holdout/rolling-origin design with leakage prevention.
10. Independent scientific/statistical review of the Stage 2 protocol.

No current dataset meets these conditions.

---

## 6. What not to do

- Do not call the Stage 1 same-date audit “early warning.”
- Do not use Painter et al. (2022) as proof that a sensor can warn earlier; it shows the opposite for one bloom phase.
- Do not use Müggelsee data without permission.
- Do not define blooms from the same sensor used as the predictor.
- Do not count overlapping samples as independent events.
- Do not search over lead times/thresholds and report the best.
- Do not claim “matched false-alarm rate” without a denominator.
- Do not treat a weekly biology series as daily ground truth.

---

## 7. Verdict

**The original early-warning ambition remains scientifically important but currently unachievable.** Mendota and Buffalo Pound fail the biological/temporal requirements. Müggelsee is the strongest candidate but is unqualified on access, event definition, co-location, depth and calibration/QC.

Stage 2 should remain a **future, evidence-gated programme**, not a label attached to the Stage 1 measurement audit. No Stage 2 dataset is qualified. No contact was made in this sprint.

**No event audit was performed. No analysis was authorised.**
