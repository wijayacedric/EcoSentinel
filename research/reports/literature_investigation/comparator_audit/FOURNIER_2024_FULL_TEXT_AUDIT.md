# Fournier et al. (2024) — Full-Text Audit (Remediated)

## Citation (verified)
- Fournier, C., Fernandez-Fernandez, R., Cirés, S., López-Orozco, J. A., Besada-Portas, E., & Quesada, A. (2024). LSTM networks provide efficient cyanobacterial blooms forecasting even with incomplete spatio-temporal data. *Water Research*, 267, 122553. https://doi.org/10.1016/j.watres.2024.122553
- PubMed PMID: 39388977. Crossref verified 2026-11-22.

## Access status
- **Full text/supplementary/data:** NOT accessible in-session.
- **Accessible primary evidence:** Crossref metadata + PubMed abstract (PMID 39388977).
- **Secondary evidence incorporated:** Independent scientific review (22 Nov 2026, literature-only; not full-text-verified in this session). Review-reported claims are labeled accordingly.
- **Audit limitation:** Abstract/metadata + independent-review-informed audit, not direct full-text audit.

## 1. Research objective
- **Abstract evidence (verified):** Effective EWS for cyanobacterial bloom forecasting using incomplete high-frequency spatio-temporal data and PC fluorescence as proxy for cyanobacteria.
- **Type:** Forecasting / early warning (regression + classification metrics reported in abstract).

## 2. Data
| Item | Evidence | Verification status |
|---|---|---|
| Location/ecosystem | Independent review reports Cuerda del Pozo reservoir, Spain. Abstract does not name site. | **Unverified in-session; reported by independent review.** |
| Sampling frequency/period | "6 years of incomplete high-frequency spatio-temporal data..." (abstract). Independent review reports January 2010–November 2015. | Abstract verified; exact dates unverified in-session |
| Aggregation | Independent review reports four-day aggregation. | **Unverified in-session; reported by independent review.** |
| Variables | Multiparametric probes including phycocyanin (PC) fluorescence as proxy (abstract) | Abstract verified; full list unverified |
| Biological measurements / target | PC fluorescence proxy; alarm level 10 µg PC/L proposed (abstract) | Abstract verified |
| Independence / ground truth | Target is PC fluorescence proxy. Independent review: no independent biological ground truth. | Abstract supports proxy target; independent-ground-truth absence reported by review, unverified in-session |
| Missing data | "incomplete spatio-temporal data"; probe-agnostic pre-processing (abstract) | Abstract verified; imputation details unverified |
| Events/non-events | Alarm level exceedances evaluated (abstract). Independent review: only one major bloom in the test period. | **Unverified in-session; reported by independent review.** |

## 3. Analytical methods
| Item | Evidence | Verification status |
|---|---|---|
| Models | Autoregressive and multivariate Linear Regression, Random Forest, LSTM (6 models) (abstract). Independent review confirms AR and multivariate LR/RF/LSTM approaches. | Abstract verified; details unverified |
| Temporal relationships | LSTM captures temporal patterns; multivariate versions used | Abstract verified |
| Rolling correlation/coupling indicators | Not mentioned in abstract or review summary | No evidence of relationship-change indicators; full text unverified |
| Preprocessing | Probe-agnostic pre-processing (abstract). Independent review: interpolation described before the split, with possible but unconfirmed leakage. | **Possible leakage risk reported by independent review; not conclusively demonstrated in this audit.** |

## 4. Validation
| Item | Evidence | Verification status |
|---|---|---|
| Train/test separation | Independent review: temporal split at 1 January 2013. | **Unverified in-session; reported by independent review.** |
| Temporal validation | Forecast horizons 4-28 days evaluated (abstract) | Abstract verified |
| Event-based validation | Not stated in abstract. Independent review: only one major bloom in test period. | **Unverified in-session; reported by independent review.** |
| Leakage risks | Not addressed in abstract. Independent review: interpolation described before split, possible but unconfirmed leakage. | **Possible but unconfirmed leakage risk.** |
| Baselines | 6 models compared incl. LR/RF/LSTM; skill vs displaced signal (abstract). Independent review: limited improvement over persistence at shorter forecast horizons. | Skill metric verified; persistence/short-horizon limitation reported by review, unverified in-session |
| False-alarm evaluation | Accuracy, F1, Kappa reported (abstract). Independent review: lack of sufficiently informative false-alarm and confusion-matrix reporting. | Metrics verified; completeness concern reported by review, unverified in-session |
| Missed-event evaluation | Not explicitly reported in abstract | Unverified |
| Lead-time calculations | Horizons 4-28 days; positive skill 16-28 days ahead (abstract) | Abstract verified |
| Uncertainty | Not stated in abstract | Unverified |

## 5. Results and limitations
- **Abstract-reported (verified):** Multivariate LSTM best across horizons/metrics; accuracies up to 90% for 10 µg PC/L alarm level; positive skill 16-28 days ahead.
- **Independent review findings (unverified in-session):** Cuerda del Pozo reservoir, Spain; Jan 2010–Nov 2015; 4-day aggregation; temporal split 1 Jan 2013; only one major bloom in test period; interpolation before split with possible but unconfirmed leakage; no independent biological ground truth; insufficient false-alarm/confusion-matrix reporting; ~90% accuracy requires cautious interpretation; limited improvement over persistence at shorter horizons.
- **Critical examiner notes:** PC fluorescence proxy target creates circularity/independence concerns for EcoSentinel-style ground truth; high accuracy can be misleading under class imbalance and limited event count; event-based and matched-FAR evaluation not demonstrated in abstract.

## 6. Relevance to EcoSentinel
- **Overlap:** High-frequency probe data, cyanobacteria bloom forecasting, LSTM/multivariate models, incomplete data handling.
- **Difference:** Forecasts PC alarm exceedance (proxy target) with ML model comparison; no evidence of relationship-change/coupling indicators or matched-FAR independent-event evaluation.
- **Caution:** Do not overstate positive forecasting skill; interpret 90% accuracy and short-horizon improvement cautiously given review-reported limitations.

## Required follow-up
Full text/supplement needed to verify site, dates, aggregation, split, interpolation order, event count, baselines, confusion matrices/FAR, and biological ground truth.
