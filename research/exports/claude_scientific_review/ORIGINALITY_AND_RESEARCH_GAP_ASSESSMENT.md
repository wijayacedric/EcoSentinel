# Originality and Research Gap Assessment

**Project:** EcoSentinel  
**Date:** 2026-11-22  
**Status:** Critical literature assessment. **No originality claim is established by this report.** Gate 2 remains **PAUSED / NOT APPROVED — Option C (Exploratory only)**.

## 1. Assessment question

Is EcoSentinel's proposed direction — persistent changes in relationships between freshwater environmental variables as earlier warning of cyanobacterial blooms than conventional monitoring, at comparable false-alarm rates — genuinely distinct, incremental, or already substantially covered?

## 2. What is already well covered

| Area | Evidence | Implication for EcoSentinel |
|---|---|---|
| Cyanobacterial bloom ecology and drivers | Large literature; Visser et al. 2016 review; local Buffalo Pound studies (Painter 2022/2023, Boyer 2025). | Mechanistic foundations exist; EcoSentinel must not re-claim them as novel. |
| Cyanobacterial bloom forecasting/prediction models | Rousso et al. 2020 systematic review (metadata verified). | Field is active and crowded; novelty claims require precise positioning. |
| High-frequency in situ monitoring for HAB/cyanobacteria management | Multiple studies/reviews; Recknagel et al. 2025 is a close recent example. | "Using high-frequency sensors" is not novel by itself. |
| Early warning signals / critical transitions theory | Scheffer 2009, Dakos 2012, Carpenter 2011, Pace 2017. | Generic EWS concept is established; application requires careful validation. |

## 3. What may be underexplored (candidate gaps)

| Candidate gap | Why plausible | Confidence | What could falsify gap |
|---|---|---|---|
| **Relationship-change indicators (rolling correlation/coupling) evaluated specifically as early-warning signals for cyanobacterial blooms** | EWS literature often uses variance/autocorrelation of state variables; HAB forecasting often uses ML/thresholds; coupling-change focus may be less common. | **Low–Medium** | Full-text review finds prior studies using rolling correlation/network coupling for cyanobacterial bloom early warning with similar evaluation. |
| **Matched-FAR comparison as primary criterion** in cyanobacteria early-warning studies | Many studies report accuracy/AUC/RMSE; matched false-alarm operating-point comparison is less consistently central. | **Low–Medium** | Review of Recknagel 2025/Rousso-included studies shows matched-FAR event-based evaluation is common. |
| **Independent biological validation with interval-censored onset and verified non-event exposure** | Sparse biological sampling makes this hard; many studies use pigment proxies. | **Medium** | Existing studies already use rigorous independent biological event adjudication with exposure denominators. |
| **Buffalo Pound-specific test of relationship-change warning** | Local studies exist but not this exact framing. | **Medium** (application novelty only) | Prior Buffalo Pound work already tests this exact hypothesis. |

## 4. Strongest defensible originality claim (candidate, not approved)

> *If* supported by rigorous evidence, EcoSentinel could potentially contribute an **evaluation-focused test** of whether persistent multivariate relationship changes in high-frequency buoy data provide earlier cyanobacterial bloom warning than conventional univariate monitoring at matched false-alarm rates, using independently adjudicated biological events with interval-censored onset and explicit non-event exposure.

**This claim is conditional.** It is not currently supported by results. It requires: (a) full-text differentiation from close comparators, especially Recknagel 2025 and studies in Rousso 2020; (b) independent biological labels; (c) defensible non-event exposure; (d) matched-FAR temporal evaluation.

## 5. What would invalidate or weaken the claim

1. **Prior art:** a published study already tests the same relationship-change indicator family, with independent biological events, matched FAR, and temporal validation.
2. **Negative result:** relationship-change indicators perform no better than simple univariate baselines at matched FAR.
3. **Confounding explanation:** apparent signals are driven by seasonality, hydrology, or sensor artefacts.
4. **Label circularity:** performance depends on proxy labels derived from predictor signals.
5. **Insufficient power:** too few independent events to estimate performance reliably.

## 6. Competing/overlapping claim risks

- **"Intelligible ML early warning"** (Recknagel 2025) may overlap substantially in goal and data type. Without full-text review, cannot claim distinction.
- **Generic EWS papers** may be cited as prior art for "relationship/change before transition."
- **Cyanobacteria forecasting reviews** may show many similar predictors; novelty must be in the specific hypothesis + evaluation discipline, not in using common sensors.

## 7. Assessment

**Overall originality status:** **Unproven / potentially incremental.** The project has a plausible, disciplined framing, but the current evidence base is insufficient to claim a clear research gap. The most defensible near-term contribution is methodological rigor (independent labels, matched FAR, interval-censored onset, exposure honesty) rather than algorithmic novelty.

## References

- Dakos et al. 2012, https://doi.org/10.1371/journal.pone.0041010
- Pace et al. 2017, https://doi.org/10.1073/pnas.1612424114
- Painter et al. 2022, https://doi.org/10.1039/D2EM00078D
- Painter et al. 2023, https://doi.org/10.1002/ecs2.4472
- Recknagel et al. 2025, https://doi.org/10.1016/j.watres.2025.124514
- Rousso et al. 2020, https://doi.org/10.1016/j.watres.2020.115959
- Scheffer et al. 2009, https://doi.org/10.1038/nature08227
- Visser et al. 2016, https://doi.org/10.1016/j.hal.2015.12.006
