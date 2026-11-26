# Fournier et al. (2024) — Full-Text Audit

## Citation (verified)
- Fournier, C., Fernandez-Fernandez, R., Cirés, S., López-Orozco, J. A., Besada-Portas, E., & Quesada, A. (2024). LSTM networks provide efficient cyanobacterial blooms forecasting even with incomplete spatio-temporal data. *Water Research*, 267, 122553. https://doi.org/10.1016/j.watres.2024.122553
- PubMed PMID: 39388977. Crossref verified 2026-11-22.

## Access status
- **Full text/supplementary/data:** NOT accessible in-session.
- **Accessible evidence:** Crossref metadata + PubMed abstract (PMID 39388977).

## 1. Research objective
- **Abstract evidence:** "propose an effective EWS for cyanobacterial bloom forecasting..." using incomplete high-frequency spatio-temporal data and PC fluorescence as proxy for cyanobacteria (PubMed abstract).
- **Type:** Forecasting / early warning classification-regression hybrid (abstract reports both regression and classification metrics).
- **Unverified:** Exact problem formulation, operational deployment intent.

## 2. Data
| Item | Abstract/metadata evidence | Unverified |
|---|---|---|
| Location/ecosystem | Not named in abstract; inland waters context. | Exact lake/reservoir, geography, trophic state. |
| Sampling frequency/period | "6 years of incomplete high-frequency spatio-temporal data from multiparametric probes" (abstract). | Exact years, frequency, stations, depths. |
| Variables | Multiparametric probes including phycocyanin (PC) fluorescence as proxy for cyanobacteria (abstract). | Full variable list, meteorology, nutrients. |
| Biological measurements | PC fluorescence as proxy for cyanobacteria; alarm level 10 µg PC/L proposed (abstract). | Independent biological validation (taxonomy/biovolume/toxin); calibration of PC to µg/L. |
| Independence | Target appears PC-based/proxy-based. | Whether any independent biological ground truth used. |
| Missing data | "incomplete spatio-temporal data"; "probe agnostic and replicable method... to pre-process..." (abstract). | Imputation strategy, bias, missingness mechanism. |
| Events/non-events | Alarm level exceedance of 10 µg PC/L evaluated; horizons 4-28 days (abstract). | Number of independent events, non-event exposure. |

## 3. Analytical methods
| Item | Abstract/metadata evidence | Unverified |
|---|---|---|
| Models | Autoregressive and multivariate Linear Regression, Random Forest, LSTM (6 models) (abstract). | Architectures, hyperparameters, features/lags. |
| Temporal relationships | LSTM captures temporal patterns; multivariate versions used. | Explicit modeling of inter-variable relationship changes/coupling. |
| Rolling correlation/coupling indicators | Not mentioned in abstract. | Feature engineering. |
| Preprocessing | Probe-agnostic replicable pre-processing; time series specific for bloom forecasting (abstract). | Exact steps, leakage controls. |

## 4. Validation
| Item | Abstract/metadata evidence | Unverified |
|---|---|---|
| Train/test separation | Not specified. | Temporal split design. |
| Temporal validation | Forecast horizons 4-28 days evaluated (abstract). | Rolling origin, blocked CV. |
| Independent event validation | Not stated. | Event-level evaluation. |
| Cross-year/site validation | Not stated. | Generalizability across sites/years. |
| Leakage risks | Not addressed. | Scaling/imputation/leakage. |
| Baselines | Compared 6 models; includes linear regression/RF; "prediction improvement over the displaced signal (skill)" (abstract). | Persistence/univariate threshold baselines. |
| False-alarm evaluation | Classification metrics include Accuracy, F1, Kappa (abstract). | False-alarm rate, specificity, matched FAR. |
| Missed-event evaluation | Recall/sensitivity not explicitly named; F1 reported. | Missed-event rate. |
| Lead-time calculations | Forecast horizons 4-28 days; "16 to 28 days in advance" (abstract). | Onset definition, event-based lead time. |
| Uncertainty | Not stated. | Confidence intervals/probabilistic forecasts. |

## 5. Results and limitations
- **Abstract-reported:** Multivariate LSTM best across horizons/metrics; accuracies up to 90% for 10 µg PC/L alarm level; positive skill 16-28 days ahead.
- **Limitations (abstract):** Not detailed; incomplete data acknowledged as handled.
- **Critical examiner notes:** PC fluorescence proxy as target may create proxy/circularity issues depending on predictors; "accuracy 90%" without FAR/missed-event/event definition is incomplete for EcoSentinel's criteria; independence of biological events unclear.

## 6. Relevance to EcoSentinel
- **Overlap:** High-frequency probe data, cyanobacteria bloom forecasting, LSTM/multivariate models, incomplete data handling.
- **Difference:** Forecasts PC alarm exceedance (proxy target) with ML model comparison; does not appear to test relationship-change/coupling indicators or matched-FAR event-based evaluation as primary claim (abstract-level).
- **Unverified:** Full validation rigor, label independence, event-based metrics.

## Required follow-up
Full text/supplement needed for data site, label construction, split/leakage controls, event definitions, and full metric reporting.
