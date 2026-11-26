# EcoSentinel Prior Art Comparison

**Status:** Abstract/metadata-limited comparison. No full texts accessible. Gate 2 remains **PAUSED / NOT APPROVED — Option C (Exploratory only)**.

## 1. Direct comparison

| Dimension | Existing research (abstract-level evidence) | EcoSentinel proposal | Assessment |
|---|---|---|---|
| **Research objective** | Recknagel 2025: intelligible ML early warning of CyanoHAB hazard exceedance. Fournier 2024: LSTM EWS forecasting PC alarm exceedance. Rousso 2020: review of forecasting/predictive models. | Test whether persistent multivariate relationship changes provide earlier warning than conventional monitoring at comparable FAR. | **Partially overlapping objective (early warning)**. EcoSentinel's specific hypothesis (relationship-change + matched FAR) is not clearly stated in comparator abstracts, but full texts needed. |
| **Prediction target** | Recknagel: total cyanobacteria / hazard-level exceedance; Fournier: 10 µg PC/L alarm. | Independently adjudicated biological bloom events with interval-censored onset. | **Potentially meaningful difference** if EcoSentinel uses independent biological labels; currently aspirational because Gate 2 has no approved labels. |
| **Biological ground truth** | Recknagel: in situ cyanobacteria state (independence unclear); Fournier: PC fluorescence proxy. | Independent biological evidence required; no buoy RFU as ground truth. | **Meaningful in principle, currently unmet in practice**. |
| **Environmental predictors** | HF in situ water quality/probes; Recknagel names WT, TURB, pH, PHYCO. | Similar buoy/met variables; no nutrients. | **Largely overlapping data type**. |
| **Relationship-change indicators** | Not mentioned in abstracts. | Core proposed indicator family. | **Possibly different**, but cannot confirm absence in full texts. |
| **Conventional baselines** | Fournier compares multiple ML/LR models and skill; Recknagel baselines not stated in abstract. | Requires persistence/univariate thresholds/simple multivariate baselines. | **Unresolved**. |
| **False-alarm evaluation** | Not explicit in abstracts; Fournier reports Accuracy/F1/Kappa. | Primary matched-FAR comparison. | **Potentially meaningful evaluation difference**, if comparators truly lack it; unverified. |
| **Missed-event evaluation** | Not explicit. | Required. | **Potentially meaningful**, unverified. |
| **Lead-time evaluation** | Recknagel fixed 5-day horizon; Fournier 4-28 day horizons. | Interval-censored lead-time bounds relative to independent onset. | **Partially overlapping** (lead time/horizon concept exists); EcoSentinel framing more event-onset specific. |
| **Temporal validation** | Implied/training-unseen mentioned; details unverified. | Required temporal/event-based, leakage-safe. | **Unresolved**. |
| **Independent event validation** | Unverified. | Required. | **Aspirational difference**. |
| **Confounding controls** | Unverified. | Seasonality, hydrology, sensor artefacts, autocorrelation nulls required. | **Aspirational difference**. |

## 2. What EcoSentinel has already been anticipated by prior research

- **High-frequency in-situ early warning for cyanobacterial blooms is not novel.** Recknagel 2025 and Fournier 2024 directly demonstrate this space (abstract-level).
- **Multivariate predictors and ML/temporal models for bloom forecasting are established.** Rousso 2020 reviews this landscape.
- **Lead-time/horizon forecasting is established.** Fournier reports 4-28 day horizons; Recknagel uses 5-day-ahead.
- **Interpretability/operability concerns are already recognized.** Recknagel abstract emphasizes intelligibility; Shen & Chen 2026 comment raises robustness concerns.

## 3. What is methodologically different (candidate)

- **Relationship-change/coupling-change as the central indicator hypothesis** (rolling correlation/covariance/network changes) — not mentioned in accessible comparator abstracts, but full-text confirmation required.
- **Matched-FAR as primary comparison rule** — emphasized in EcoSentinel protocol; not explicit in comparator abstracts.
- **Independent biological event adjudication with interval-censored onset and verified non-event exposure** — EcoSentinel design principle; currently unmet by Gate 2 but methodologically central.
- **Explicit separation of proxy predictor from independent biological label** — central EcoSentinel constraint.

## 4. Superficial vs meaningful differences

| Difference | Superficial or meaningful? | Why |
|---|---|---|
| Using a different lake (Buffalo Pound) | Mostly superficial as novelty; meaningful for local validation | Site novelty is weak unless it tests transferability or unique constraints. |
| Using rolling correlation instead of LSTM | Potentially superficial | Could be just alternative feature engineering unless it yields interpretable, validated, matched-FAR advantage. |
| Matched-FAR comparison | **Meaningful methodological requirement**, not by itself a scientific novelty claim | Good evaluation practice; necessary but not sufficient for originality. |
| Independent biological labels + non-event exposure | **Meaningful** | Directly addresses circularity and evaluation validity. |
| Relationship-change hypothesis with rigorous negative controls | **Potentially meaningful** if tested and differentiated | Requires evidence, not assertion. |

## 5. Elements that might constitute a genuine contribution (conditional)

1. A rigorously validated demonstration that coupling/relationship-change indicators provide added early-warning value over univariate and simple multivariate baselines at matched FAR.
2. Independent biological event-based evaluation with interval-censored onset and verified non-event exposure.
3. Clear negative-control evidence ruling out seasonality/autocorrelation/sensor artefacts as explanations.

## 6. Evidence required to substantiate contribution

- Full-text comparator review confirming no equivalent prior test.
- Human-approved independent biological labels and exposure.
- Pre-registered evaluation protocol.
- Temporal/event-based validation with matched FAR, missed-event rate, lead-time bounds, uncertainty.
- Ablations: no-phyco/no-chl, univariate baselines, seasonal/autocorrelation nulls.

## Bottom line

EcoSentinel's **goal** overlaps substantially with existing early-warning work. Its **candidate differentiators** are methodological rigor and relationship-change framing, but these are **unverified as novel and unproven as effective**.
