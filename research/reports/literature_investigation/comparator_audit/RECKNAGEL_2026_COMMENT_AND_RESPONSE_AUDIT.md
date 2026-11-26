# Recknagel 2026 Comment and Response Audit

## Citation (verified)
- Comment: Shen, F., & Chen, Z. (2026). Comment on “Early warning of harmful cyanobacteria blooms based on high frequency in situ monitoring and intelligible machine learning modelling: The case study of Lake Müggelsee (Germany)” by Recknagel et al. (Water Research 287 2025 124,514). *Water Research*, 293, 125406. https://doi.org/10.1016/j.watres.2026.125406
- PubMed PMID: 41619426. Crossref verified 2026-11-22.
- Original article: Recknagel et al. (2025), *Water Research*, 287, 124514. https://doi.org/10.1016/j.watres.2025.124514

## Access status
- **Comment full text:** NOT accessible in-session. Accessible: Crossref metadata + PubMed abstract (PMID 41619426).
- **Author response/reply/correction:** NOT found in Crossref search (2026-11-22). Existence unconfirmed.
- **Audit limitation:** Based on comment abstract only. Criticisms are reported as stated in abstract; support/validity cannot be fully adjudicated without comment full text and original full text.

## 1. Methodological criticisms (as stated in PubMed abstract)

| # | Criticism (abstract wording/paraphrase) | Exact original method/result targeted | Evidence support (available) | Status |
|---|---|---|---|---|
| C1 | **Cross-year preprocessing and interpolation of weekly biovolume to hourly/daily resolution** may introduce temporal leakage and smooth bloom dynamics. | Recknagel abstract does not mention weekly biovolume interpolation; states "11 years of hourly and daily HFISD" and "total cyanobacteria" forecasts. | **Unresolved from available evidence.** Comment abstract asserts this; original full text needed to confirm whether weekly biovolume was interpolated to hourly/daily and how used. | **Reasonable concern, unverified.** |
| C2 | **Evaluation emphasizing R2/RMSE rather than threshold-exceedance skill and lead-time distributions** at 4 mm3/L hazard level, with limited uncertainty communication. | Recknagel abstract mentions "hazard level" exceedance and "satisfying results" but no R2/RMSE values. | **Unresolved.** Comment claims R2/RMSE emphasis and 4 mm3/L threshold; original full text needed. | **Reasonable concern, unverified.** |
| C3 | **Strong reliance on phycocyanin (PHYCO)** warrants PHYCO-persistence baselines and no-PHYCO ablations to quantify incremental forecasting value and sensor dependence. | Recknagel abstract lists PHYCO as a driver variable and discusses interpretability/operability principles. | **Partially plausible from abstract.** PHYCO is named as driver; dependence/ablation not mentioned in abstract. | **Reasonable concern, partially supported by abstract-level model description.** |
| C4 | **Mixed aggregation choices and single-station drivers paired with multi-station/depth-integrated targets** can bias learned relationships. | Not described in Recknagel abstract. | **Unresolved.** Requires full text. | **Reasonable concern, unverified.** |

## 2. Author response

- No author response/reply identified in Crossref query on 2026-11-22. This does **not** prove none exists; it may be unpublished, not indexed, or differently titled.

## 3. Implications for EcoSentinel

| Comment concern | Implication for EcoSentinel |
|---|---|
| Interpolation/leakage (C1) | **High relevance.** EcoSentinel must avoid interpolating sparse biological labels into high-frequency "truth" and must audit all preprocessing for temporal leakage. |
| Threshold-exceedance/lead-time/FAR/uncertainty metrics (C2) | **High relevance.** Directly aligns with EcoSentinel's matched-FAR, missed-event, lead-time, uncertainty requirements. |
| Sensor-dependence/ablation baselines (C3) | **High relevance.** EcoSentinel should include no-PHYCO/no-pigment ablations and persistence baselines; avoid circularity. |
| Spatial/aggregation mismatch (C4) | **Medium relevance.** Buffalo Pound is a single-site buoy study but still must align predictor/label spatial-temporal support. |

## 4. Assessment

The comment abstract raises **credible, EcoSentinel-relevant methodological concerns**, especially around leakage, event-based evaluation, and sensor dependence. However, because neither full text nor author response was accessible, these criticisms are classified as **reasonable concerns pending full-text adjudication**, not demonstrated defects.

## Evidence locations
- Shen & Chen 2026: PubMed PMID 41619426, abstract. Crossref DOI 10.1016/j.watres.2026.125406.
- Recknagel 2025: PubMed PMID 40925059, abstract. Crossref DOI 10.1016/j.watres.2025.124514.
