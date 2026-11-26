# EcoSentinel Prior Art Comparison (Remediated)

**Status:** Abstract/metadata-limited comparison, remediated 2026-11-22. Independent review (literature-only) incorporated as unverified input where labeled. Gate 2 remains **PAUSED / NOT APPROVED — Option C (Exploratory only)**.

## 1. Direct comparison

| Dimension | Existing research (accessible evidence) | EcoSentinel proposal | Assessment |
|---|---|---|---|
| **Research objective** | Recknagel 2025: 5-day-ahead CyanoHAB hazard forecasting with intelligible ML. Fournier 2024: HF probe-based cyanobacterial bloom forecasting with AR/LR/RF/LSTM. Rousso 2020: review of forecasting/predictive models. | Test whether persistent multivariate relationship changes provide earlier warning than conventional monitoring at comparable FAR. | **Partially overlapping objective (early warning)**. EcoSentinel's specific relationship-change + matched-FAR + independent-event hypothesis is not clearly stated in comparator abstracts, but full texts needed. |
| **Prediction target** | Recknagel: total cyanobacteria / hazard-level exceedance. Fournier: 10 µg PC/L alarm. | Independently adjudicated biological bloom events with interval-censored onset. | **Potentially meaningful difference** if EcoSentinel uses independent biological labels; currently aspirational because Gate 2 has no approved labels. |
| **Biological ground truth** | Recknagel: cyanobacteria state target; independence from PHYCO unclear. Fournier: PC fluorescence proxy. | Independent biological evidence required; no buoy RFU as ground truth. | **Meaningful in principle, currently unmet in practice**. |
| **Environmental predictors** | HF in situ water quality/probes. | Similar buoy/met variables; no nutrients. | **Largely overlapping data type**. |
| **Relationship-change indicators** | Not evident in accessible comparator abstracts/review summaries. | Core proposed indicator family. | **Possibly different**, but cannot confirm absence in full texts. |
| **Conventional baselines** | Fournier compares LR/RF/LSTM and skill; Recknagel baselines not stated in abstract; independent review reports no persistence baseline (unverified). | Requires persistence/univariate thresholds/simple multivariate baselines. | **Unresolved; important differentiation point if rigorously implemented.** |
| **False-alarm evaluation** | Fournier reports Accuracy/F1/Kappa (abstract); FAR completeness questioned by independent review (unverified). | Primary matched-FAR comparison. | **Potentially meaningful evaluation difference**, if comparators truly lack it; unverified. |
| **Missed-event evaluation** | Not explicit in abstracts. | Required. | **Potentially meaningful**, unverified. |
| **Lead-time evaluation** | Recknagel fixed 5-day horizon; Fournier 4-28 day horizons. | Interval-censored lead-time bounds relative to independent onset. | **Partially overlapping**; EcoSentinel framing more event-onset specific. |
| **Temporal validation** | Recknagel: training/unseen mentioned; independent review reports random 75/25 bootstrap split (unverified, potential leakage concern). Fournier: temporal horizons; independent review reports split/interpolation concerns (unverified, possible leakage). | Required temporal/event-based, leakage-safe. | **Potentially meaningful** if EcoSentinel enforces strict temporal evaluation; unproven. |
| **Independent event validation** | Independent review reports limited event support in Recknagel/Fournier (unverified). | Required. | **Aspirational difference**. |
| **Confounding controls** | Unverified. | Seasonality, hydrology, sensor artefacts, autocorrelation nulls required. | **Aspirational difference**. |

## 2. What prior research already covers

- **HF in-situ cyanobacteria early warning/forecasting is not novel.** Recknagel 2025 and Fournier 2024 directly occupy this space.
- **Multivariate predictors and ML/temporal models for bloom forecasting are established.** Rousso 2020 reviews this landscape.
- **Lead-time/horizon forecasting exists.** Fournier 4–28 days; Recknagel 5-day-ahead.
- **Generic early warning signals/critical transitions are established.** Scheffer 2009, Dakos 2012, Carpenter 2011; but O'Brien et al. 2023 (Nat Commun, 10.1038/s41467-023-43744-8, metadata verified) cautions that EWS applicability to empirical lake data may be limited.
- **Multivariate resilience indicators and dynamical network biomarkers exist as prior method families.** Weinans et al. 2021 (Sci Rep, 10.1038/s41598-021-87839-y, metadata verified) and Chen et al. 2012 (Sci Rep, 10.1038/srep00342, metadata verified) are relevant prior art; EcoSentinel must distinguish any relationship-change indicator from these generic families, not ignore them.
- **Natural-lake vs experimentally manipulated evidence must be distinguished.** Pace 2017 is a whole-lake manipulation; Buffalo Pound observational inference carries different confounding and external-validity constraints.

## 3. Candidate methodological differences (unproven)

- Relationship-change/coupling-change as the central indicator hypothesis (not evident in accessible comparator abstracts; full-text confirmation required).
- Matched-FAR as primary comparison rule (good practice; not novelty by itself).
- Independent biological event adjudication with interval-censored onset and verified non-event exposure (central design principle; currently unmet).
- Explicit separation of proxy predictor from independent biological label.

## 4. Superficial vs meaningful differences

| Difference | Superficial or meaningful? | Why |
|---|---|---|
| Different lake (Buffalo Pound) | Mostly superficial as novelty; meaningful for local validation | Site novelty is weak unless it tests transferability or unique constraints. |
| Using rolling correlation instead of LSTM | Potentially superficial | Alternative feature engineering unless it yields validated matched-FAR added value. |
| Matched-FAR comparison | **Meaningful quality requirement**, not standalone novelty | Necessary but not sufficient for originality. |
| Independent biological labels + non-event exposure | **Meaningful** | Addresses circularity and evaluation validity. |
| Relationship-change hypothesis with negative controls | **Potentially meaningful** if tested and differentiated | Requires evidence, not assertion. |

## 5. Bottom line

EcoSentinel's **goal** overlaps substantially with existing early-warning work. Its **candidate differentiators** are methodological rigor and relationship-change framing, but these are **unverified as novel and unproven as effective**. The 22 Nov 2026 independent review strengthens caution around comparator validation claims and prior-art coverage; it does not establish EcoSentinel novelty.
