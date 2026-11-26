# Methods and Techniques Review

**Project:** EcoSentinel  
**Date:** 2026-11-22  
**Status:** Literature investigation only. No method selected/approved for confirmatory EcoSentinel evaluation. Gate 2 remains **PAUSED / NOT APPROVED — Option C (Exploratory only)**.

## 1. Evaluation criteria

Each method is assessed against EcoSentinel constraints: high-frequency autocorrelated sensors, missing data/quality flags, seasonality, sensor artefacts, sparse/interval-censored independent biological labels (currently insufficient), need for matched false-alarm-rate comparison, interpretability, and student-feasible implementation.

**Caution:** A method being mathematically capable does not mean it is scientifically valid for EcoSentinel. Predictive claims require independent labels and leakage-safe validation.

## 2. Method comparison

| Method | Mathematical idea | Ecological information it may reveal | Predictive or descriptive? | Key assumptions | Weaknesses with autocorrelated environmental time series | Sensitivity to missing data/seasonality/sensor artefacts | Computational complexity | Student-feasible? |
|---|---|---|---|---|---|---|---|---|
| **Rolling correlations / covariance** | Compute Pearson/Spearman correlation or covariance over moving windows between variable pairs. | Changing coupling among DO, pH, temp, pigments, turbidity; possible regime/coupling shifts. | **Primarily descriptive** unless validated prospectively against independent events at matched FAR. | Stationarity within window; meaningful linear/monotonic relation; sufficient complete observations. | High false-positive risk: autocorrelation and shared trends create persistent apparent correlation changes; overlapping windows inflate significance. | High. Missing data shrinks windows; seasonality drives correlation; fouling/drift can create spurious coupling. | Low | Yes, but easy to misuse. Requires pre-registration, detrending/null models, and careful uncertainty. |
| **Dynamic correlation networks** | Build time-varying networks where nodes are variables and edges are rolling correlations/MI; track network metrics (density, modularity, centrality). | System-level reorganization; which variables become central before events. | Descriptive/exploratory; predictive only with rigorous out-of-sample event validation. | Edge definition meaningful; network metrics stable; comparable windows. | Network metrics inherit autocorrelation and windowing artefacts; multiple comparisons across edges/metrics. | High. Gaps break edges; seasonality creates periodic networks; sensor artefacts can dominate topology. | Low–medium | Medium. Implementation possible; interpretation and statistical validation harder. |
| **Multivariate change-point detection** | Detect points/segments where distribution, mean, covariance, or model parameters change (e.g., CUSUM, PELT, Bayesian change point, kernel methods). | Abrupt regime shifts or structural breaks in multivariate state. | Can be used prospectively, but many formulations are retrospective/descriptive. | Change type matches model; adequate pre/post data; change points identifiable. | Autocorrelation violates i.i.d./simple assumptions; can produce spurious change points. | Medium–high. Missing data complicates segmentation; seasonality can look like change points; artefacts create false breaks. | Medium | Medium. Off-the-shelf tools exist, but correct assumptions/validation are nontrivial. |
| **Statistical process control (SPC)** | Monitor statistics (mean, variance, Mahalanobis T², MEWMA/MCUSUM) against control limits. | Deviation from "in-control" process; abnormal multivariate behavior. | Can be predictive for anomaly/alerting if control period is appropriate and validated. | Stable in-control period; known/estimable covariance; appropriate false-alarm calibration. | Autocorrelation breaks classical SPC assumptions; control limits become invalid. | Medium. Needs clean baseline; seasonality requires seasonal control charts; sensor drift contaminates baseline. | Low | Yes. Conceptually accessible; baseline selection and autocorrelation adjustment are critical. |
| **Multivariate anomaly detection** | Identify observations/windows deviating from learned normal pattern (Isolation Forest, autoencoder, one-class SVM, clustering, density models). | Unusual multivariate states, possibly including bloom precursors or artefacts. | Usually descriptive/anomaly scoring; predictive only if anomalies align with future independent events. | "Normal" can be defined; anomalies are meaningful; training data representative. | Temporal dependence can cause leakage if randomly split; anomalies may be seasonal extremes. | High. Missingness and sensor faults often look like anomalies; seasonality must be modeled. | Medium–high | Medium. Easy to run, hard to validate rigorously; interpretability often poor. |
| **State-space models** | Model latent states and observations over time (Kalman filter, dynamic linear models, particle filters, hidden Markov/state-switching models). | Latent ecological states, transitions, uncertainty, time-varying dynamics. | Can be predictive/probabilistic if properly specified and validated. | Model structure captures dynamics; noise/transition assumptions reasonable; identifiable parameters. | Better suited than many methods, but misspecification can still create false inferences. | Medium. Can handle missing observations naturally in some formulations; seasonality must be included; artefacts need explicit measurement models. | Medium–high | Medium–hard. Requires statistical maturity; implementation feasible with care. |
| **Dynamic factor models (DFM)** | Represent many observed variables through few latent dynamic factors. | Shared underlying drivers; reduced-dimension system state. | Descriptive/compressive; predictive when factor forecasts are validated. | Low-rank latent structure; linear/Gaussian or specified extensions; stable factor loadings or modeled changes. | Factors may capture common autocorrelation/seasonality rather than ecological transition. | Medium. Missing data can be handled in some implementations; seasonality may dominate factors. | Medium | Medium. Feasible with stats packages; interpretation requires care. |
| **Information-theoretic approaches** | Quantify information flow/complexity: transfer entropy, mutual information, permutation entropy, Fisher information. | Directional coupling, predictability changes, complexity loss near transitions. | Mostly descriptive; causal claims are risky without strong assumptions. | Adequate data length; discretization/embedding choices appropriate; stationarity/local stationarity assumptions. | Entropy/MI estimates biased in short/autocorrelated/noisy series; requires surrogate testing. | High. Missing data and sampling irregularity problematic; seasonality and noise affect estimates. | Medium–high | Hard. Easy to compute incorrectly; interpretation often overstated. |
| **Early-warning indicators / critical transitions (CSD)** | Rising variance, autocorrelation, skewness, spectral reddening, spatial indicators as signs of critical slowing down before bifurcations (Scheffer et al., 2009; Dakos et al., 2012). | Loss of resilience near critical transitions. | Potentially predictive in specific bifurcation-driven systems; not universal. | System approaches a critical transition with critical slowing down; adequate resolution; appropriate detrending. | Strong risk of false positives/negatives in autocorrelated ecological series; not all transitions show CSD (Dakos et al., 2012). | High. Preprocessing, bandwidth/window choice, and seasonality dominate results; sensor artefacts can mimic signals. | Low–medium | Medium. Simple metrics easy; defensible inference difficult. |
| **Machine learning (supervised)** | Learn mapping from features to labels (RF, gradient boosting, SVM, simple NN). | Predictive patterns if labels are reliable. | Predictive by design, but only as good as labels and validation. | Representative labels; no leakage; stable feature-label relationship. | Random splits leak heavily; autocorrelation inflates performance. | High. Missing labels and sparse biological ground truth are major barriers; sensor artefacts learned as shortcuts. | Medium | Medium. Implementation easy; defensible validation hard. |
| **Machine learning (deep/sequence models)** | LSTM/TCN/transformer learn temporal patterns. | Complex nonlinear temporal dependencies. | Predictive, but often opaque and data-hungry. | Large, clean, representative labeled data; careful regularization and validation. | Can memorize temporal structure; leakage and overfitting risks severe. | High. Missingness, sparse labels, and regime changes problematic. | High | Low–medium for responsible validation. Not recommended before baselines and label sufficiency. |

## 3. Methods most relevant to EcoSentinel's current question

### Tier 1 — Worth investigating first (interpretable, feasible, aligned with scope)

1. **Rolling correlation/covariance change with null models**  
   - Directly matches the research question.  
   - Must be framed as candidate indicator, not proof.  
   - Needs detrending/seasonal controls, surrogate/autocorrelation-aware nulls, pre-registered windows/thresholds.

2. **Simple multivariate SPC/change scores (Mahalanobis distance, MEWMA)**  
   - Good baseline comparator against relationship-change claims.  
   - Interpretable and computationally light.  
   - Requires careful "in-control" definition and temporal validation.

3. **State-space/dynamic linear models (simple forms)**  
   - Can represent time-varying relationships and uncertainty more explicitly.  
   - More work, but scientifically defensible if kept simple.

### Tier 2 — Exploratory only after Tier 1

4. **Dynamic correlation networks** — useful visualization/exploration; high multiple-comparison risk.  
5. **Dynamic factor models** — useful for shared latent drivers/confounding.  
6. **CSD indicators** — relevant theory, but should not be assumed applicable without testing transition type.

### Tier 3 — Not priority under current constraints

7. **Information-theoretic directionality (transfer entropy)** — interesting but fragile with noisy, gapped, autocorrelated sensor data; easy to overinterpret.  
8. **Deep learning** — premature given label scarcity, interpretability needs, and Gate 2 constraints.

## 4. Key methodological risks

- **Autocorrelation-induced false discovery:** most alarming risk for rolling-window methods (Dakos et al., 2012).
- **Seasonality masquerading as precursor:** spring warm-up or autumn turnover can produce repeatable multivariate shifts.
- **Sensor artefacts masquerading as ecology:** fouling, calibration shifts, maintenance, and RFU quirks.
- **Leakage:** future windows, normalization, threshold tuning, or label-informed preprocessing.
- **Label insufficiency:** without independent biological events and non-event exposure, predictive performance cannot be credibly estimated.

## 5. Recommendation for EcoSentinel (non-binding)

The most defensible next methodological investigation is a **comparison of simple, interpretable relationship-change indicators against simple univariate and multivariate baselines**, under explicit matched-FAR and temporal validation rules, using only synthetic or human-approved biological labels. No method should be treated as validated by literature plausibility alone.

## References (verified in-session)

- Dakos, V., Carpenter, S. R., Brock, W. A., Ellison, A. M., Guttal, V., Ives, A. R., ... & Scheffer, M. (2012). Methods for detecting early warnings of critical transitions in time series illustrated using simulated ecological data. *PLoS ONE*, 7(7), e41010. https://doi.org/10.1371/journal.pone.0041010
- Scheffer, M., Bascompte, J., Brock, W. A., Brovkin, V., Carpenter, S. R., Dakos, V., ... & Sugihara, G. (2009). Early-warning signals for critical transitions. *Nature*, 461(7260), 53–59. https://doi.org/10.1038/nature08227
- Rousso, B. Z., Bertone, E., Stewart, R., & Hamilton, D. P. (2020). A systematic literature review of forecasting and predictive models for cyanobacteria blooms in freshwater lakes. *Water Research*, 182, 115959. https://doi.org/10.1016/j.watres.2020.115959
