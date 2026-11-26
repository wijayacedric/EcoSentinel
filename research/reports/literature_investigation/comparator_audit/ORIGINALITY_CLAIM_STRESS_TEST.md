# Originality Claim Stress Test (Remediated)

**Status:** Critical stress test based on abstract/metadata-limited evidence and independent review input (2026-11-22). Gate 2 remains **PAUSED / NOT APPROVED — Option C (Exploratory only)**.

## 1. Stress-test questions

### T1. Existing studies already perform substantially the same analysis.
- **Evidence:** Recknagel 2025 and Fournier 2024 perform HF in situ/probe cyanobacteria early warning/forecasting. Rousso 2020 reviews a broad forecasting landscape. Generic EWS, multivariate resilience indicators (Weinans 2021, metadata verified), and dynamical network biomarkers (Chen 2012, metadata verified) provide adjacent prior art.
- **Assessment:** **Partially supported.** Overlap exists in goal/data domain. The exact relationship-change + matched-FAR + independent biological event combination is not confirmed in comparator abstracts, but absence in abstract is not absence in full text.
- **Verdict:** **Unresolved; serious overlap risk.**

### T2. EcoSentinel's proposed relationship-change indicators are merely alternative feature engineering.
- **Evidence:** Multivariate resilience indicators and dynamical network biomarkers are established prior-art families. Implicit relationship capture in ML models is possible.
- **Assessment:** **Plausible concern.** Relationship changes must demonstrate added value at matched FAR, robustness, and interpretability beyond generic multivariate EWS/feature engineering.
- **Verdict:** **Supported as a risk; not disproven.**

### T3. The apparent warning signal is seasonal progression.
- **Assessment:** **Strong plausible confounder**.
- **Verdict:** **Supported as major risk.**

### T4. Environmental relationships change because of hydrology or weather rather than impending blooms.
- **Assessment:** **Strong plausible confounder**, especially in Buffalo Pound (Painter 2023 flow/source-water effects).
- **Verdict:** **Supported as major risk.**

### T5. Phycocyanin or chlorophyll measurements create circular validation.
- **Evidence:** Fournier uses PC fluorescence proxy target; Recknagel includes PHYCO and forecasts cyanobacteria state (independence unclear). Shen & Chen 2026 comment flags PHYCO reliance and requests no-PHYCO ablations/persistence baselines.
- **Assessment:** **Supported as major risk.** EcoSentinel correctly treats buoy RFU as non-independent ground truth.
- **Verdict:** **Supported.**

### T6. Conventional monitoring thresholds perform just as well.
- **Assessment:** **Unresolved.** Critical matched-FAR baseline test.
- **Verdict:** **Unresolved.**

### T7. The proposed matched-FAR comparison does not create meaningful novelty.
- **Assessment:** **Supported.** Matched-FAR is a methodological quality requirement, not a standalone scientific novelty claim.
- **Verdict:** **Supported.**

### T8. Independent biological sampling is too sparse to validate the proposed warning claim.
- **Evidence:** EcoSentinel Gate 2: 0 independently reconstructed biological bloom events; 0 defensible verified non-bloom exposure. Painter 2022 has 25/17 sampling dates over 2018–2019, interval-censored and limited.
- **Assessment:** **Strongly supported for current EcoSentinel state.**
- **Verdict:** **Supported (current blocking constraint).**

### T9. Comparator validation concerns make them easy targets for novelty claims.
- **Evidence:** Independent review raised potential leakage/validation issues for Recknagel/Fournier. These are unverified in-session and not conclusively demonstrated.
- **Assessment:** **Invalid shortcut.** EcoSentinel cannot claim novelty by attacking comparators on unverified grounds. Primary-source verification is required.
- **Verdict:** **Supported caution.**

## 2. Overall stress-test outcome

| Claim | Status |
|---|---|
| EcoSentinel occupies completely unexplored territory | **Rejected** |
| EcoSentinel has a plausible but unproven methodological differentiation | **Supported (weak-moderate)** |
| EcoSentinel's differentiation is currently sufficient for an originality claim | **Rejected** |
| Matched-FAR alone is novelty | **Rejected** |
| Independent biological validation is a major unresolved barrier | **Strongly supported** |
| Closest comparator risk is material | **Strongly supported** (Recknagel 2025; Fournier 2024 also relevant) |
| Generic multivariate EWS / DNB prior art must be addressed | **Supported** |

## 3. Minimum evidence needed before any originality claim

1. Full-text comparator audit confirming exact gap (Recknagel 2025, Fournier 2024, Rousso-cited close studies, and relevant multivariate EWS/DNB prior art).
2. Human-approved independent biological event labels and non-event exposure.
3. Pre-registered matched-FAR temporal/event-based evaluation.
4. Demonstrated added value over simple baselines and null controls.
5. Robustness to seasonality, hydrology, sensor artefacts, ablations, and autocorrelation.
