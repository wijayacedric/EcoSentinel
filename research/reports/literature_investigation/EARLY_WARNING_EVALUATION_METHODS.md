# Early Warning Evaluation Methods

**Project:** EcoSentinel  
**Date:** 2026-11-22  
**Status:** Literature investigation only. No evaluation rule is selected/approved by this report. Gate 2 remains **PAUSED / NOT APPROVED — Option C (Exploratory only)**.

## 1. Why conventional evaluation is misleading

| Common practice | Why misleading for EcoSentinel |
|---|---|
| Random train/test split by row/window | Leaks temporal structure; adjacent windows highly autocorrelated; inflates performance. |
| Accuracy as primary metric | Class imbalance and asymmetric costs: a model can predict "no bloom" often and score well while missing rare blooms. |
| AUC/ROC without operating point | Hides false-alarm burden and operational threshold; early warning utility depends on chosen alert threshold. |
| Precision/recall without event definition | Window-level metrics can count many windows in same event as separate successes/failures. |
| Lead time without false-alarm constraint | "Earlier" is meaningless if system alarms constantly. |
| Using proxy labels derived from predictor signal | Circularity; overestimates performance and invalidates causal/independence claims. |

## 2. Recommended evaluation dimensions (for future human decision)

### 2.1 Event-based framing

- **Unit of analysis:** biological bloom event (independently defined), not arbitrary time window. 
- **Event-level sensitivity/recall:** fraction of independent events with at least one qualified early warning in allowed horizon.
- **Missed-event rate:** 1 - event-level sensitivity (with explicit event definition).
- **False alarms:** must be defined carefully - per alert episode, per unit non-event exposure, or per season - and never use unverified non-bloom periods as negative ground truth.

### 2.2 Lead time

- **Lead time:** time from qualified alert to event onset (or onset interval). 
- For sparse biological sampling, onset is interval-censored; report bounds (earliest/latest plausible onset), not a fake precise timestamp.
- Distinguish confirmed early warning, onset-overlapping ambiguous detection, and post-onset detection.

### 2.3 False-alarm fraction / FAR

- **Matched-FAR comparison:** compare detectors at same false-alarm rate/fraction, or report full operating curve with selected operating points. 
- **Exposure denominator:** must be defensible verified non-event exposure. Unknown periods excluded from denominator, not treated as non-event.
- **Episode vs observation:** report both only with explicit units; do not label episodes/observation as episode rate.

### 2.4 Time-dependent / event-based ROC or PR

- **Time-dependent ROC:** can be useful when event timing and censoring matter, but requires careful definition of horizon and censoring.
- **PR curves:** informative under class imbalance, but still need event-based interpretation and temporal validation.
- **Not sufficient alone:** curves without matched operating-point reporting and event definitions can obscure operational utility.

## 3. Validation designs

| Design | Use | Cautions |
|---|---|---|
| **Temporal split (train earlier, test later)** | Baseline requirement for time series. | Single split may be lucky/unlucky; regime shifts over years matter. |
| **Rolling/blocked temporal cross-validation** | Multiple temporal folds respecting order. | Must include gaps/buffers to avoid leakage; folds not independent. |
| **Leave-one-event-out / leave-one-season-out** | Tests generalization across events/seasons. | Needs enough independent events; sparse events limit power. |
| **Event-based holdout** | Evaluate on held-out bloom events and verified non-event exposure. | Requires defensible event and exposure labels - currently a Gate 2 blocker. |
| **Spatial/external-site validation** | Tests transferability. | Different lake dynamics; domain shift expected. |

**Random CV is inappropriate** for this problem. Any CV must be temporal/block-aware and leakage-safe.

## 4. Handling sparse biological sampling and interval censoring

- Biological sampling may be weekly/biweekly; bloom onset is bracketed, not observed exactly.
- Use interval-censored onset/termination bounds; report detection as early/ambiguous/post-onset relative to bounds.
- Do not interpolate biological labels into daily "truth" without explicit uncertainty.
- Use high-frequency sensors for candidate alerts, but evaluate against independent biological observations only.

## 5. Autocorrelation, seasonality, and confounding

- **Autocorrelation:** inflates apparent skill and narrows confidence intervals. Use block bootstrap, temporal buffers, or autocorrelation-aware nulls.
- **Seasonality:** stratify or model seasonal baselines; avoid claiming novelty when detector follows seasonal calendar.
- **Confounding:** flow management, sensor maintenance, weather events. Report sensitivity analyses.
- **Sensor drift/fouling:** can create both false alarms and missed events; quality flags and maintenance logs must be integrated.

## 6. Uncertainty estimation

- Report confidence intervals for event-level sensitivity, FAR, and lead time where feasible.
- With few events, uncertainty will be large; acknowledge limited statistical power.
- Use bootstrap methods appropriate for dependent time series (block bootstrap), not i.i.d. bootstrap.
- Avoid overconfident claims from single-year or few-event evaluations.

## 7. Minimum defensible evaluation package (future, if Gate 2 unblocks)

1. Independently defined biological events with interval-censored bounds and provenance.
2. Defensible verified non-event exposure denominator.
3. Temporal/event-based splits; no random leakage.
4. Baselines: persistence, univariate thresholds, simple multivariate baselines.
5. Primary comparison at matched FAR.
6. Event-level sensitivity, missed-event rate, FAR, lead-time bounds, uncertainty.
7. Sensitivity analyses: label definition, horizon, persistence, missing-data handling, sensor flags, seasonality.
8. Full reporting of negative/ambiguous results.

## 8. Current EcoSentinel implication

EcoSentinel currently lacks item 1 and 2. Therefore no matched-FAR confirmatory evaluation is defensible. The Gate 2H prototype correctly treats this as synthetic-only software testing.

## References (verified in-session)

- Dakos, V., Carpenter, S. R., Brock, W. A., et al. (2012). Methods for detecting early warnings of critical transitions in time series illustrated using simulated ecological data. *PLoS ONE*, 7(7), e41010. https://doi.org/10.1371/journal.pone.0041010
- Rousso, B. Z., Bertone, E., Stewart, R., & Hamilton, D. P. (2020). A systematic literature review of forecasting and predictive models for cyanobacteria blooms in freshwater lakes. *Water Research*, 182, 115959. https://doi.org/10.1016/j.watres.2020.115959
- Scheffer, M., et al. (2009). Early-warning signals for critical transitions. *Nature*, 461, 53–59. https://doi.org/10.1038/nature08227
