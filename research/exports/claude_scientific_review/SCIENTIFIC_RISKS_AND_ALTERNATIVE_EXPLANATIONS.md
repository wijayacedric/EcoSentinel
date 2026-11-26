# Scientific Risks and Alternative Explanations

**Project:** EcoSentinel  
**Date:** 2026-11-22  
**Status:** Critical review. Gate 2 remains **PAUSED / NOT APPROVED — Option C (Exploratory only)**.

## 1. Purpose

This report stress-tests EcoSentinel's central hypothesis. It separates **scientific plausibility** from **demonstrated predictive performance**. No claim is made that the hypothesis is false or validated; the goal is to identify what could make it fail or appear true for the wrong reasons.

## 2. Central hypothesis under scrutiny

> Persistent changes in relationships between freshwater environmental variables provide earlier warning of cyanobacterial blooms than conventional monitoring, at comparable false-alarm rates.

## 3. Strongest arguments against / alternative explanations

| Risk | Why it threatens EcoSentinel | What would mitigate it | Residual status |
|---|---|---|---|
| **Seasonality confounding** | Variables co-move seasonally (temperature, light, DO, pH). Rolling relationships may change every year regardless of bloom timing. | Seasonal baselines/nulls; event-conditional evaluation; compare against seasonal naive baseline; multiple years/events. | High residual risk. |
| **Consequence, not precursor** | Detected relationship changes may occur after bloom onset or during bloom metabolism (DO/pH feedbacks). | Interval-censored onset bounds; require alert before onset_earliest; independent biological onset; negative controls. | High residual risk without independent onset labels. |
| **Univariate signals suffice** | Phycocyanin/chlorophyll/turbidity thresholds may already capture available warning. Multivariate complexity adds no value. | Matched-FAR comparison against simple univariate baselines; ablation tests. | Major unresolved challenge. |
| **Autocorrelation-induced false signals** | Rolling windows over autocorrelated series create persistent spurious correlations/alerts (Dakos et al., 2012). | Surrogate data tests; block bootstrap; pre-registered windows; minimum persistence; report false-alarm fraction. | High; core methodological risk. |
| **Sensor fouling/drift artefacts** | Fouling (B7), calibration shifts, maintenance can create apparent multivariate shifts. | Quality flags, maintenance logs, artifact-focused negative controls, sensitivity excluding flagged periods. | High in real buoy data. |
| **Hydrological/management confounding** | Buffalo Pound flow/source-water management changes alter water quality and bloom occurrence (Painter et al., 2023). | Include hydrologic covariates/regimes; stratify by management period; avoid causal overclaim. | High for Buffalo Pound specifically. |
| **Pigment proxy circularity** | Using phycocyanin/chlorophyll as both predictor-side signal and label creates circular evaluation. | Independent biological labels; exclude/handle proxy labels transparently; sensitivity analyses. | Critical; already a Gate 2 blocker. |
| **Insufficient independent biological evidence** | Cannot measure missed-event rate or defensible FAR without verified events/non-events. | Obtain/approve independent biological records; interval-censored event reconstruction. | **Current blocking risk.** |
| **Sparse event count / low power** | Few blooms over 2014-2021 may make performance estimates unstable and overfit-prone. | Event-based uncertainty; leave-one-event-out; avoid overclaiming. | High. |
| **Taxonomic/ecological heterogeneity** | Different bloom types (Dolichospermum vs Planktothrix in Buffalo Pound; Painter et al., 2022) may have different precursors. | Stratify by event type where possible; avoid one-size-fits-all claims. | Medium-high. |
| **Transferability illusion** | A pattern in Buffalo Pound may not generalize to other lakes/events. | External validation; treat cross-system transfer as hypothesis. | High. |

## 4. Strongest evidence supporting plausibility

| Supporting evidence | Why it helps | Why it is insufficient |
|---|---|---|
| Critical transitions/EWS theory suggests some systems show precursors before regime shifts (Scheffer et al., 2009; Dakos et al., 2012). | Provides theoretical motivation for monitoring change, variance, autocorrelation. | Generic theory; not cyanobacteria-specific; many transitions lack CSD; false positives common. |
| Whole-lake experiments detected early warnings before regime shifts/blooms (Carpenter et al., 2011; Pace et al., 2017). | Empirical proof-of-concept that early warnings can exist in lake/bloom contexts. | Controlled/experimental settings; different indicators; does not validate EcoSentinel's specific multivariate relationship-change method. |
| Buffalo Pound has rich high-frequency multivariate data (Baulch et al., 2025). | Makes investigation possible. | Data availability is not evidence of predictive validity. |
| Local studies show complex bloom dynamics and pigment limitations (Painter et al., 2022, 2023). | Motivates looking beyond single pigment thresholds. | Also increases confounding and label difficulty. |

## 5. Strongest evidence against current readiness

1. **No independent biological bloom-event labels approved for confirmatory evaluation (Gate 2 blocker).**  
2. **No defensible verified non-event exposure.**  
3. **Matched-FAR comparison cannot be performed credibly.**  
4. **High confounding risk in Buffalo Pound (flow management, sensor artifacts, seasonality).**  
5. **Close existing work may already cover parts of the space** (e.g., high-frequency in situ early warning / ML; Recknagel et al., 2025 - full text not reviewed here).

## 6. Bottom line

EcoSentinel's hypothesis is **scientifically plausible as an exploratory hypothesis** but **not demonstrated**. The strongest current risk is not mathematical infeasibility; it is **invalid evaluation under label scarcity and confounding**. Any future claim must survive matched-FAR, temporal, independent-label, and confounder-control scrutiny.

## References (verified in-session)

- Baulch, H. M., et al. (2025). *Data in Brief*, 63, 112290. https://doi.org/10.1016/j.dib.2025.112290
- Carpenter, S. R., et al. (2011). *Science*, 332, 1079–1082. https://doi.org/10.1126/science.1203672
- Dakos, V., et al. (2012). *PLoS ONE*, 7(7), e41010. https://doi.org/10.1371/journal.pone.0041010
- Pace, M. L., et al. (2017). *PNAS*, 114(2), 352–357. https://doi.org/10.1073/pnas.1612424114
- Painter, K. J., et al. (2022). *Environmental Science: Processes & Impacts*, 24, 1212–1227. https://doi.org/10.1039/D2EM00078D
- Painter, K. J., Venkiteswaran, J. J., & Baulch, H. M. (2023). *Ecosphere*, 14(3), e4472. https://doi.org/10.1002/ecs2.4472
- Scheffer, M., et al. (2009). *Nature*, 461, 53–59. https://doi.org/10.1038/nature08227
