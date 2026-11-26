# Sprint 4L.10 — Independent Mendota Feasibility Challenge and Dataset Decision

**Date:** 2026-11-24  
**Gate 2:** PAUSED / NOT APPROVED — option C (Exploratory Only)  
**Primary recommendation: RETAIN — LIMITED EXPLORATORY USE.**  
**For the original early-warning research question: REJECT Mendota as a validation dataset.**

## 1. What was independently checked

The Sprint 4L.9 audit was challenged by a fresh parser and a second SQLite calculation. **5,439 comparable values** were checked across raw structure, variable counts, missingness, annual/seasonal coverage, intervals, flags, biology overlap, windows, Turner/YSI pairs, sensor-era summaries and depth metadata.

- **Numerical mismatches versus 4L.9: 0.**
- **Numerical mismatches versus the SQLite second method: 0.**
- **Interpretive discrepancies recorded: 10.**
- Raw daily identity remains: 490,187 bytes; 38 columns; 3,996 rows; 0 duplicate dates; date range 2006-07-09 to 2025-11-18.
- Biology remains: 402 Mendota dates; 400 0–8 m composites; 2 0–2 m dates; 371/402 dates with no station value.

The 4L.9 arithmetic is reproducible. The challenge is therefore about **interpretation, qualification and dataset decision**, not correction of counts.

## 2. The decisive new calculation: common coverage with biology

4L.9 reported variable-by-variable overlap. It did not report how often a **set** of variables is jointly valid on a biology date. That changes the feasibility judgement:

| Common set | Biology dates with all variables valid |
|---|---:|
| Turner chlorophyll + phycocyanin + DO + water temperature | **64/402 (15.9%)** |
| Turner chlorophyll + phycocyanin + DO + water temp + air temp + wind | **58/402 (14.4%)** |
| Turner core + PAR above + PAR below | **23/402 (5.7%)** |
| YSI chlorophyll + phycocyanin + DO | **16/402 (4.0%)** |
| YSI chlorophyll + phycocyanin + DO + water temp + pH | **2/402 (0.5%)** |
| YSI chlorophyll + phycocyanin + pH + fDOM + turbidity + conductance | **21/402 (5.2%)** |

Only **165/402** biology dates (41.0%) have even one same-day unflagged sensor variable. That rises to **165/230** (71.7%) within 2006–2020, but the joint sets remain small.

Sensor-only multivariate coverage is much better: **939** dates for the Turner core and **306** for the YSI core. The limitation is not the sensor matrix alone; it is the **sensor–biology common support**.

## 3. Assessment of the 4L.9 verdict

4L.9 concluded: **“EXPLORATORY FEASIBILITY SUPPORTED WITH MAJOR LIMITATIONS.”**

Independent assessment: **directionally correct but insufficiently qualified.**

- **A. Seasonal descriptive analysis:** supported with major limitations.
- **B. Descriptive sensor–cyanobacteria comparison:** partially supported, but only pairwise/descriptive, not sensor validation.
- **C. Multivariate environmental relationships:** limited for sensor-only data; **not robustly supported for sensor–biology data**.
- **D. Early-warning validation:** **not supported.**

The single label is too broad if read as support for B-as-validation or C-as-biological-multivariate. It is appropriately cautious for D. It is not too pessimistic for A.

## 4. Scientific reasons

1. **The biological endpoint is abundance, not bloom status or onset.** Cyanobacteria biovolume is a defensible exploratory abundance indicator, but it does not define bloom, toxicity or onset; the record has no event labels or time of day.
2. **Same-day overlap is date availability, not temporal alignment.** The 128 Turner chlorophyll and 139 Turner phycocyanin same-day dates are day-level matches; they cannot establish lead time or intraday coincidence.
3. **The depth mismatch is first-order.** A 0.5 m point sensor is not a 0–8 m composite; stratification, vertical migration and surface scums can decouple them.
4. **Turner and YSI are different instruments.** 2019 paired medians differ by orders of magnitude (chlorophyll 1,354.7 vs 0.39 RFU; phycocyanin 802.0 vs 0.5895). No crosswalk exists.
5. **QC is incomplete.** `O` is undefined; eight flag columns use undocumented values; `C` sometimes carries numeric values; unflagged values include negative turbidity, negative YSI phycocyanin/chlorophyll and negative PAR below.
6. **Sensor-to-biovolume validation is weak in the literature.** Cotterill et al. (2019) found weak, variable phycocyanin–biovolume relationships; Levi et al. (2025) found sensor-specific calibration, composition/interference and low-concentration limitations.
7. **Mendota is not a blank early-warning testbed.** Carpenter et al. (2020, 2022) already use high-frequency Mendota phycocyanin; Beal et al. (2021, 2022) produce seasonal/sub-seasonal cyanobacteria forecasts; O'Brien et al. (2023) include Mendota in a multi-lake EWS assessment where most indicators performed poorly.

## 5. Separate verdicts

| Use | Independent verdict | Basis |
|---|---|---|
| A. Seasonal descriptive ecological analysis | **SUPPORTED WITH MAJOR LIMITATIONS** | Multi-year sensor series; sensor-only complete sets; open-water season only; era separation required |
| B. Descriptive comparison with microscopy cyanobacteria | **PARTIALLY SUPPORTED — DESCRIPTIVE ONLY** | 128/139 same-day Turner proxies; 80–88 with DO/temp; 21–22 YSI; depth and validation caveats |
| C. Multivariate environmental relationships | **LIMITED (SENSOR-ONLY); NOT ROBUSTLY SUPPORTED WITH BIOLOGY** | 939/306 sensor-only complete dates vs 58/2 biology-core dates |
| D. Early-warning validation | **NOT SUPPORTED / REJECT** | No labels/events; 14-day date-only biology; depth mismatch; proxies; prior-art EWS limitations |

## 6. Final dataset decision

**RETAIN — LIMITED EXPLORATORY USE.**

Mendota should be retained for:
- descriptive seasonal analysis of environmental variables;
- pairwise descriptive comparison of sensor conditions with cyanobacteria biovolume/cell density, with era separation and depth caveats.

Mendota should **not** be used for:
- bloom/non-bloom labels, event intervals or early-warning validation;
- confirmatory modelling, hypothesis testing or threshold optimisation;
- Turner/YSI concatenation without a documented crosswalk;
- claims that 0.5 m sensors represent 0–8 m biomass.

The alternative “RETAIN — SUPPORTING DATA ONLY” would be too restrictive because pairwise descriptive B is genuinely possible. “REJECT” would be too broad because A and pairwise B have scientific value. But **for the original early-warning question specifically, Mendota is rejected**.

## 7. What would change the decision

- Sub-weekly, time-stamped, depth-resolved microscopy or a validated biomass series with event adjudication.
- A documented Turner/YSI cross-calibration and calibration/maintenance history.
- A defined depth comparator and surface-vs-composite sensitivity analysis.
- Independent bloom/non-bloom labels and verified non-event exposure.
- A pre-specified lead-time validation with leakage control and adequate event count.

Until then, Gate 2 remains **PAUSED / NOT APPROVED — Option C**. No labels, event intervals, models, hypothesis tests, threshold optimisation, external contacts, uploads, commits or pushes were made.
