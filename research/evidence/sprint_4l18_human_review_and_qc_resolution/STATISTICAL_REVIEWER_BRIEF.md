# Statistical Reviewer Brief

**Status:** Draft for an independent reviewer — **no reviewer has been appointed**.  
**Project:** EcoSentinel  
**Date:** 2026-11-25  
**Governance:** Protocol **PROPOSED — NOT APPROVED**; Gate 2 **PAUSED / NOT APPROVED — OPTION C**; all decisions **OUTSTANDING**; analysis **NOT AUTHORISED**.

---

## 1. What is being reviewed

A descriptive, date-level measurement/comparability study using existing data:

- **Mendota:** 402 microscopy dates (1995–2020); Turner and YSI sensor eras; 128/139 same-day Turner chlorophyll/phycocyanin values; 21/22 YSI values; 0.5 m sensors vs 0–8 m biology; median 14-day biology.
- **Buffalo Pound:** 42 microscopy dates (2018–2019); 0.8 m biology and nominal 0.8 m sensors; daily 10-minute data; two seasons.

The proposed statistic is **Spearman’s rho** for P1–P4, with n and descriptive sensitivity ranges. No p-values, bootstrap interval, Pearson/log-Pearson, model, or prediction is proposed.

The original early-warning question is not the current analysis. It remains a conditional Stage 2 objective.

---

## 2. Proposed estimands

| ID | Lake / era | Sensor | Endpoint | Maximum possible n |
|---|---|---|---:|---:|
| P1 | Mendota / Turner | Chlorophyll RFU | Cyanobacteria biovolume | 128 |
| P2 | Mendota / Turner | Phycocyanin RFU | Cyanobacteria biovolume | 139 |
| P3 | Buffalo Pound / YSI | Chlorophyll RFU | Cyanobacteria biomass | 42 |
| P4 | Buffalo Pound / YSI | Phycocyanin RFU | Cyanobacteria biomass | 42 |

These are upper bounds, not actual n. No count audit has been authorised. P1/P2 share dates/endpoint; P3/P4 share dates/endpoint.

---

## 3. Proposed statistical approach

- Spearman’s rho, tie-corrected.
- n and descriptive sensitivity ranges, not confidence intervals.
- Mendota: full leave-one-year-out set as an influence diagnostic.
- Buffalo Pound: separate 2018/2019 estimates; leave-one-date-out influence values; no bootstrap interval.
- No p-values, no bootstrap, no Pearson/log-Pearson, no model.
- Seasonal stratum rho only if n ≥ 10; otherwise points and n.
- Overall minimum-estimability rule to be set before estimation, after a separately authorised count audit.
- No pooling across lakes/instruments/depths.
- All four estimates reported as equal-status exploratory; no “winner.”

---

## 4. Known statistical problems

- Date-only biology; daily sensor means; no time-of-day alignment.
- 14-day median Mendota biology; 4–16-day Buffalo Pound gaps; interval censoring.
- Serial dependence/autocorrelation; seasonal co-trending.
- Mendota 0.5 m vs 0–8 m depth mismatch; station blank for 371/402 dates.
- Turner/YSI discontinuity; no crosswalk.
- Buffalo Pound two seasons; variable daily coverage; B7/negative/above-range QC unresolved.
- Detection-conditioned population; possible selection of low/absent dates.
- Four estimates share endpoints/dates; multiple descriptive views.
- Restricted range/QC selection can attenuate or inflate rho.
- No calibration/detection limits; measurement error on both axes.

---

## 5. Current decision state

- D-01 comparability: rank association only, not approved.
- D-05 QC: unresolved; conservative interim population possible, not validated.
- D-06 daily summary: provisional Option A only (full-day means; non-equivalence stated).
- D-09 anomaly: provisional retain/flag; blocked by D-05.
- D-10 uncertainty: no bootstrap/CI; influence diagnostics only.
- D-11: n<10 principle; numeric threshold blocked pending count audit.
- D-15: **NOT APPROVED**.

---

## 6. Questions for the statistical reviewer

Please address, with reasons:

1. Is Spearman’s rho a defensible descriptive statistic for this question, given date-level co-occurrence, ties, and seasonal structure?
2. Is the proposed “descriptive sensitivity range” language honest, or does it still imply inferential uncertainty?
3. Is leave-one-year-out / leave-one-date-out sufficient as an influence diagnostic, or is another descriptive check needed?
4. Is the n<10 stratum rule defensible? What overall estimability principle should be set before the count audit?
5. Are P1–P4 appropriately described as non-independent exploratory estimates, or should some be dropped?
6. Does the detection-conditioned population introduce a bias that makes rho uninterpretable?
7. Is the Mendota 0.5 m vs 0–8 m mismatch fatal to P1/P2, or can it be reported as a bounded limitation?
8. Is the Buffalo Pound two-season design capable of supporting any descriptive rho, even exploratory?
9. Are the proposed QC exclusions (C/E/H/G/B7/negative RFU) likely to bias the rank association? What sensitivities are essential?
10. Does the study need a pre-specified tie/zero handling and a minimum distinct-value check?
11. Are there any hidden multiplicity, selection, or researcher-degree-of-freedom problems in the four estimands and nine sensitivities?
12. Is Stage 1 statistically viable as a descriptive audit, or should it be paused?

You are **not** being asked to approve D-15, endorse a result, or validate the protocol as a whole. A written opinion with reasons and conditions is sufficient.

---

## 7. Materials provided

- 4L.14 `REVISED_PROTOCOL.md` §11–§13
- 4L.14 `UNCERTAINTY_AND_SENSITIVITY_PLAN.md`
- 4L.14 `ESTIMAND_AND_SAMPLE_ELIGIBILITY_SPECIFICATION.md`
- 4L.14 statistical review
- 4L.14 addendum
- 4L.16 decision matrix/review order
- 4L.17 D-06 assessment
- 4L.18 D-05 evidence resolution
- This brief

---

## 8. Independence and conflicts

Please disclose any involvement in the datasets, the Painter/Baulch research, the NTL-LTER programme, or the project. A reviewer with a direct interest in a particular result is not independent.

**No reviewer has been appointed or contacted.** This brief is a draft for a future invitation.
