# Recknagel et al. (2025) — Full-Text Audit (Remediated)

## Citation (verified)
- Recknagel, F., Shan, K., Adrian, R., & Köhler, J. (2025). Early warning of harmful cyanobacteria blooms based on high frequency in situ monitoring and intelligible machine learning modelling: The case study of Lake Müggelsee (Germany). *Water Research*, 287, 124514. https://doi.org/10.1016/j.watres.2025.124514
- PubMed PMID: 40925059. Crossref verified 2026-11-22.

## Access status
- **Full text:** NOT accessible in-session (Elsevier paywall; DOI webfetch returned citation only; Semantic Scholar rate-limited; Unpaywall returned 422; direct HTML scrape returned no abstract/body).
- **Supplementary/data availability:** NOT accessible in-session.
- **Accessible primary evidence:** Crossref metadata + PubMed abstract (PMID 40925059).
- **Secondary evidence incorporated:** Independent scientific review (22 Nov 2026, literature-only; reviewer inspected project reports, not repo dataset/code/Gate 2 records; targeted not systematic; mixed full-text/abstract-level access). Claims below attributed to that review are **not independently full-text-verified in this session** unless otherwise stated.
- **Audit limitation:** This remains an **abstract/metadata + independent-review-informed audit**, not a direct full-text audit. Unverified claims are explicitly labeled.

## 1. Research objective
- **Abstract evidence (verified):** 5-day-ahead forecasts of total cyanobacteria / CyanoHAB hazard exceedance; intelligible ML modelling (PubMed abstract).
- **Independent review (unverified in-session):** Five-day-ahead cyanobacteria biovolume hazard prediction.
- **Interpretation:** Short-horizon early warning/forecasting of hazard exceedance. Not the same hypothesis as EcoSentinel's relationship-change + matched-FAR + independent biological event evaluation.

## 2. Data
| Item | Evidence | Verification status |
|---|---|---|
| Location/ecosystem | Lake Müggelsee, Germany (title/abstract) | Verified (metadata/abstract) |
| Sampling frequency/period | "11 years of hourly and daily HFISD" (abstract). Independent review states approximately 11 years of hourly/daily observations. | Abstract verified; exact years unverified in-session |
| Environmental variables | WT, TURB, pH, PHYCO named in abstract | Abstract verified; full predictor set unverified |
| Biological measurements / target | Total cyanobacteria / hazard-level exceedance (abstract). Independent review states cyanobacteria biovolume hazard prediction. | Abstract verified; target construction unverified |
| Independence of biological observations | Abstract does not clarify independence from PHYCO predictor | Unverified; critical concern |
| Missing data / preprocessing | Independent review reports imputation using observations from other years; weekly biovolume interpolated to daily/hourly target resolution. | **Unverified in-session; reported by independent review. Potential leakage risk, not conclusively demonstrated here.** |
| Independent events/non-event periods | Hazard exceedance events implied; counts not in abstract. Independent review reports only two training years reached the hazard condition. | **Unverified in-session; reported by independent review.** |

## 3. Analytical methods
| Item | Evidence | Verification status |
|---|---|---|
| Models | XGBoost (decision trees), LSTM with attention (deep learning neural networks), HEA (causally inferred rules) (abstract). Independent review also reports XGBoost, LSTM attention and hybrid modelling. | Abstract verified; hybrid/model details unverified |
| Temporal relationships between variables | LSTM captures time series; XGBoost/HEA unclear | Unverified |
| Rolling correlation/covariance/dynamic networks/coupling indicators | Not mentioned in abstract or independent review summary | No evidence of relationship-change indicators; full text unverified |
| Preprocessing/feature engineering/thresholds | 5-day-ahead horizon, hazard-level exceedance (abstract). Independent review: weekly biovolume interpolated to daily/hourly target resolution; imputation using observations from other years. | Horizon verified; preprocessing details unverified in-session |

## 4. Validation
| Item | Evidence | Verification status |
|---|---|---|
| Training/testing separation | "training data" and "unseen data" (abstract). Independent review reports random 75/25 bootstrap split. | **Split design unverified in-session; reported by independent review.** |
| Temporal validation | Implied by time-series forecasting; details not in abstract. Random 75/25 bootstrap split (if confirmed) would raise temporal leakage/independence concerns. | **Potential leakage risk, not conclusively demonstrated in this audit.** |
| Event-based validation | Not stated in abstract. Independent review: only two training years reached hazard condition. | **Unverified in-session; reported by independent review.** |
| Baselines | Not stated in abstract. Independent review: no persistence baseline. | **Unverified in-session; reported by independent review.** |
| PHYCO dependence / ablation | PHYCO named as driver (abstract). Independent review: no phycocyanin ablation. | Driver verified from abstract; ablation absence unverified in-session |
| False-alarm evaluation | Not stated in abstract | Unverified |
| Missed-event evaluation | Not stated in abstract | Unverified |
| Lead-time calculations | Fixed 5-day-ahead horizon (abstract) | Verified |
| Uncertainty reporting | Not stated in abstract | Unverified |

## 5. Results and limitations
- **Abstract-reported findings (verified):** HEA/LSTM predicted hazard exceedances in training on daily data; only XGBoost and HEA satisfying for unseen daily data. Hourly data: all three predicted training exceedances; only XGBoost and HEA satisfying for unseen data. HEA interpretable via IF-THEN-ELSE rules.
- **Performance metrics:** Not reported in abstract.
- **Independent review findings (unverified in-session):** random 75/25 bootstrap split; only two training years reached hazard condition; no persistence baseline; no phycocyanin ablation; imputation using observations from other years; weekly biovolume interpolated to daily/hourly target resolution. These raise **potential methodological/leakage concerns** but are **not conclusively demonstrated** by this audit.
- **Critical examiner limitations:** Target/predictor independence ambiguity (PHYCO vs cyanobacteria state); possible leakage from interpolation/imputation/split design (if review findings confirmed); limited event support (if confirmed); no matched-FAR/missed-event/lead-time distribution evidence in abstract.

## 6. Relevance to EcoSentinel
- **Overlap:** High-frequency in situ early warning for cyanobacterial blooms; interpretable ML; lake case study.
- **Difference:** EcoSentinel proposes relationship-change indicators and matched-FAR event-based evaluation with independent biological labels. Recknagel does not appear (from accessible evidence) to test this hypothesis.
- **Caution:** If independent review findings are accurate, Recknagel's validation design is weaker than abstract-level impression; this strengthens caution against overclaiming comparator strength but does not make EcoSentinel novel.

## Required follow-up
Obtain full text, supplementary materials, data availability statement, code, and any author response/correction. Verify the independent-review-reported split, interpolation, imputation, event count, baseline, and ablation claims against primary source.
