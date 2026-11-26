# Recknagel et al. (2025) — Full-Text Audit

## Citation (verified)
- Recknagel, F., Shan, K., Adrian, R., & Köhler, J. (2025). Early warning of harmful cyanobacteria blooms based on high frequency in situ monitoring and intelligible machine learning modelling: The case study of Lake Müggelsee (Germany). *Water Research*, 287, 124514. https://doi.org/10.1016/j.watres.2025.124514
- PubMed PMID: 40925059. Crossref verified 2026-11-22.

## Access status
- **Full text:** NOT accessible in-session (Elsevier paywall; DOI webfetch returned citation only; Semantic Scholar rate-limited; Unpaywall returned 422; direct HTML scrape returned no abstract/body).
- **Supplementary/data availability:** NOT accessible.
- **Accessible evidence:** Crossref metadata + PubMed abstract (PMID 40925059). 
- **Audit limitation:** This is an **abstract/metadata audit**, not a full-text audit. All findings below are limited to what the abstract states; claims not in abstract are marked unverified.

## 1. Research objective
- **Abstract evidence:** "Early warning enables precautional control measures of CyanoHABs..." and case study demonstrates "intelligible modelling of CyanoHABs..." for "5-day-ahead forecasts of total cyanobacteria..." (PubMed abstract).
- **Interpretation:** Objective appears to be **short-horizon early warning/forecasting** of CyanoHAB hazard exceedance, with emphasis on model interpretability/generalizability/operability.
- **Unverified:** Exact research question wording, whether framed as classification/regression/both in final operational terms, and whether comparable-FAR early warning was a primary objective.

## 2. Data
| Item | Abstract/metadata evidence | Unverified |
|---|---|---|
| Location/ecosystem | Lake Müggelsee, Germany (title/abstract). | Morphometry, trophic details, management context. |
| Sampling frequency/period | "11 years of hourly and daily HFISD" (abstract). | Exact years, missingness rate, sensor maintenance, QA/QC. |
| Environmental variables | Drivers named: water temperature (WT), turbidity (TURB), pH, phycocyanin (PHYCO) (abstract). | Full predictor set, lags, meteorology, nutrients, hydrology. |
| Biological measurements | "State variables for cyanobacteria require in situ measured data to be comparable with 'high hazard level'"; total cyanobacteria forecast; hazard level exceedance mentioned (abstract). | Whether biological ground truth is independent lab taxonomy/biovolume or sensor-derived; sampling frequency; observation method. |
| Independence of biological observations | Abstract states "State variables for cyanobacteria require in situ measured data..." but does not clarify independence from PHYCO predictor. | **Critical unverified:** independence between PHYCO driver and cyanobacteria target/label. |
| Missing data/sensor quality | Not described in abstract. | Imputation, flag handling, sensor drift/fouling. |
| Independent events/non-event periods | "Predicted CyanoHAB events exceeding the 'high hazard level'..." (abstract). | Number of events, non-event exposure definition, event independence. |

## 3. Analytical methods
| Item | Abstract/metadata evidence | Unverified |
|---|---|---|
| Models | XGBoost (decision trees), LSTM with attention (deep learning neural networks), HEA (causally inferred rules) (abstract). | Hyperparameters, architectures, training details, software. |
| Temporal relationships between variables explicitly modeled? | LSTM with attention models time series; XGBoost/HEA unclear from abstract. | Whether lagged cross-variable relationships/coupling changes modeled. |
| Rolling correlation/covariance/dynamic networks/coupling indicators? | Not mentioned in abstract. | Full feature set. |
| Relationship-change vs combining predictors | Abstract suggests multivariate predictors combined for forecasting; no mention of relationship-change indicators. | Feature engineering details. |
| Preprocessing/feature engineering/thresholds | "5-day-ahead forecasts of total cyanobacteria..." "high hazard level" exceedance (abstract). | Threshold definition, preprocessing, interpolation, aggregation, normalization. |

## 4. Validation
| Item | Abstract/metadata evidence | Unverified |
|---|---|---|
| Training/testing separation | "training data..." and "unseen data" mentioned (abstract). | Exact split design, temporal ordering, leakage controls. |
| Temporal validation | Implied by time-series forecasting; not detailed. | Blocked/rolling CV, year holdout. |
| Independent event validation | Not stated. | Event-level evaluation. |
| Cross-year/site validation | 11 years used; unseen data mentioned. | Cross-year/site design. |
| Leakage risks | Not addressed in abstract. | Preprocessing leakage, interpolation, scaling, label leakage. |
| Baseline comparisons | Not stated in abstract. | Persistence, univariate threshold, simple baselines. |
| False-alarm evaluation | Not stated in abstract. | FAR, specificity, false alarm rate at operating point. |
| Missed-event evaluation | "Predicted CyanoHAB events exceeding..." implies event detection; missed events not stated. | Missed-event rate, event sensitivity. |
| Lead-time calculations | 5-day-ahead forecast horizon fixed (abstract). | Alert lead-time distribution, onset definition. |
| Uncertainty reporting | Not stated. | Confidence intervals, calibration, ensemble spread. |

## 5. Results and limitations
- **Abstract-reported findings:** Daily data: HEA and LSTM predicted hazard-level exceedances in training; only XGBoost and HEA satisfying for unseen data. Hourly data: all three predicted training exceedances; only XGBoost and HEA satisfying for unseen data. HEA provided interpretable IF-THEN-ELSE rules; XGBoost/LSTM not explicitly interpretable in same way (abstract).
- **Performance metrics:** Not reported in abstract (no R2/RMSE/FAR/lead-time values).
- **Author limitations:** Abstract lists intelligibility principles; does not clearly list study limitations.
- **Critical examiner limitations (abstract-level):** Potential target/predictor independence ambiguity (PHYCO driver vs cyanobacteria state); no FAR/missed-event/lead-time/uncertainty metrics in abstract; validation details unknown.

## 6. Relevance to EcoSentinel
- **Overlap:** High-frequency in situ early warning for cyanobacterial blooms; interpretable ML; Lake case study.
- **Potential difference:** EcoSentinel proposes relationship-change indicators and matched-FAR event-based evaluation; Recknagel abstract emphasizes intelligible ML forecasting and hazard exceedance, no relationship-change/coupling indicator mentioned.
- **Cannot conclude:** Superiority, novelty, or equivalence without full text.

## Required follow-up (inaccessible)
Obtain full text, supplementary materials, data availability statement, code repository, and any correction/response. Extract exact hazard threshold definition, target variable, PHYCO role, split design, metrics, and baselines.
