# Originality Claim Stress Test

**Status:** Critical stress test based on abstract/metadata-limited evidence. Gate 2 remains **PAUSED / NOT APPROVED — Option C (Exploratory only)**.

## 1. Stress-test questions

### T1. Existing studies already perform substantially the same analysis.
- **Evidence:** Recknagel 2025 (abstract) performs HF in situ CyanoHAB early warning with ML and 5-day-ahead forecasts; Fournier 2024 performs HF probe-based cyanobacterial bloom forecasting with LSTM over 4-28 day horizons. Both are close in application domain.
- **Assessment:** **Partially supported.** They overlap on early warning/forecasting with HF in situ data. They do **not** clearly confirm the same relationship-change indicator hypothesis or matched-FAR independent-event evaluation, but full texts are needed.
- **Verdict:** **Unresolved; serious overlap risk.**

### T2. EcoSentinel's proposed relationship-change indicators are merely alternative feature engineering.
- **Evidence:** No comparator abstract mentions rolling correlation/coupling-change indicators; however, absence in abstract is not absence in paper. Many multivariate models implicitly capture relationships.
- **Assessment:** **Plausible concern.** Unless relationship changes are shown to add independent predictive value at matched FAR and be interpretable/mechanistically justified, they risk being feature engineering.
- **Verdict:** **Supported as a risk; not disproven.**

### T3. The apparent warning signal is seasonal progression.
- **Evidence:** Dakos 2012 warns about preprocessing/autocorrelation; Buffalo Pound has strong seasonality. No comparator abstract reviewed here demonstrates robust seasonal-null controls.
- **Assessment:** **Strong plausible confounder** for any EcoSentinel result.
- **Verdict:** **Supported as major risk.**

### T4. Environmental relationships change because of hydrology or weather rather than impending blooms.
- **Evidence:** Painter 2023 shows Buffalo Pound flow management/source-water changes affect water quality and bloom occurrence. Weather/mixing drive many variables.
- **Assessment:** **Strong plausible confounder**, especially in Buffalo Pound.
- **Verdict:** **Supported as major risk.**

### T5. Phycocyanin or chlorophyll measurements create circular validation.
- **Evidence:** Fournier uses PC fluorescence as alarm target/proxy; Recknagel includes PHYCO as driver and forecasts cyanobacteria state (independence unclear from abstract). Shen & Chen 2026 comment flags PHYCO reliance and requests no-PHYCO ablation/persistence baselines.
- **Assessment:** **Supported as major risk in general and relevant to comparators.** EcoSentinel correctly treats buoy RFU as non-independent ground truth.
- **Verdict:** **Supported.**

### T6. Conventional monitoring thresholds perform just as well.
- **Evidence:** Fournier includes LR/RF/LSTM comparisons and skill metric; Recknagel abstract does not show simple threshold baseline. Rousso notes metric standardization gaps.
- **Assessment:** **Unresolved.** This is exactly why EcoSentinel requires matched-FAR baselines.
- **Verdict:** **Unresolved; critical test.**

### T7. The proposed matched-FAR comparison does not create meaningful novelty.
- **Evidence:** Matched-FAR is a good evaluation practice. Many fields expect it. It is not a novel algorithm.
- **Assessment:** **Supported.** Matched-FAR is a **methodological quality requirement**, not a standalone scientific novelty claim. It can strengthen credibility but not substitute for novelty.
- **Verdict:** **Supported.**

### T8. Independent biological sampling is too sparse to validate the proposed warning claim.
- **Evidence:** EcoSentinel Gate 2 history: 0 independently reconstructed biological bloom events; no defensible non-bloom exposure. Painter 2022 has 25/17 sampling dates over 2018-2019, interval-censored and limited.
- **Assessment:** **Strongly supported for current EcoSentinel state.**
- **Verdict:** **Supported (current blocking constraint).**

## 2. Overall stress-test outcome

| Claim | Status |
|---|---|
| EcoSentinel occupies completely unexplored territory | **Rejected** |
| EcoSentinel has a plausible but unproven methodological differentiation | **Supported (weak-moderate)** |
| EcoSentinel's differentiation is currently sufficient for an originality claim | **Rejected** |
| Matched-FAR alone is novelty | **Rejected** |
| Independent biological validation is a major unresolved barrier | **Strongly supported** |
| Closest comparator risk is material | **Strongly supported** (Recknagel 2025; Fournier 2024 also relevant) |

## 3. Minimum evidence needed before any originality claim

1. Full-text comparator audit confirming exact gap (especially Recknagel 2025, Fournier 2024, Rousso-cited close studies).
2. Human-approved independent biological event labels and non-event exposure.
3. Pre-registered matched-FAR temporal/event-based evaluation.
4. Demonstrated added value over simple baselines and null controls.
5. Robustness to seasonality, hydrology, sensor artefacts, and ablations.
