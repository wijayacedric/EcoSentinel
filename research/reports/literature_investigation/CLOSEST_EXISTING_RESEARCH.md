# Closest Existing Research

**Project:** EcoSentinel  
**Date:** 2026-11-22  
**Status:** Literature investigation only. This is not an exhaustive systematic review. Gate 2 remains **PAUSED / NOT APPROVED — Option C (Exploratory only)**.

## 1. Search scope and limitations

Searches were performed via Crossref API queries and limited web searches in-session on 2026-11-22. The web search tool returned limited/non-specific results for some queries; Crossref metadata was used to verify DOIs for key papers. **Full texts were not retrieved for most papers.** Therefore, comparisons below distinguish metadata/abstract-level information from full-text-verified findings. This report identifies *closest* studies found, but cannot guarantee all relevant studies were identified.

## 2. Closest studies

### Study C1 — Recknagel et al. 2025 (Lake Müggelsee, Germany)

| Field | Assessment |
|---|---|
| **Citation** | Recknagel, F., Shan, K., Adrian, R., & Köhler, J. (2025). Early warning of harmful cyanobacteria blooms based on high frequency in situ monitoring and intelligible machine learning modelling: The case study of Lake Müggelsee (Germany). *Water Research*, 287, 124514. https://doi.org/10.1016/j.watres.2025.124514 |
| **Location/ecosystem** | Lake Müggelsee, Germany; eutrophic shallow lake (title/abstract verified). |
| **Dataset/sampling** | 11 years of hourly and daily HFISD (abstract). Independent review (2026-11-22, unverified in-session) reported imputation using observations from other years and weekly biovolume interpolated to daily/hourly target resolution. |
| **Biological ground truth** | Total cyanobacteria / hazard-level exceedance (abstract). Target-construction independence from PHYCO is unclear from abstract. |
| **Variables** | WT, TURB, pH, PHYCO named in abstract; full predictor set unverified. |
| **Methods** | XGBoost, LSTM attention, HEA/intelligible ML (abstract). No relationship-change/coupling indicator evident from accessible evidence. |
| **Validation design** | Abstract: training vs unseen data. Independent review (2026-11-22, unverified in-session) reported random 75/25 bootstrap split; only two training years reached hazard condition; no persistence baseline; no phycocyanin ablation. **Potential leakage/validation concerns; not conclusively demonstrated in this audit.** |
| **Main findings** | Abstract: 5-day-ahead hazard forecasts; XGBoost/HEA satisfying for unseen daily/hourly data in reported settings; HEA interpretable rules. |
| **Limitations** | Full text not reviewed. Reported split/interpolation/imputation/event-support/baseline/ablation issues are unverified in-session and must be checked against primary source. |
| **Overlap with EcoSentinel** | High topical overlap: early warning, cyanobacterial blooms, high-frequency in situ monitoring. |
| **Difference from EcoSentinel** | EcoSentinel proposes relationship-change indicators and matched-FAR event-based evaluation with independent biological labels. Recknagel appears hazard-forecasting ML-focused; no evidence of relationship-change or matched-FAR design in accessible evidence. |

**Originality implication:** Close comparator. Do not claim EcoSentinel novelty against it without full-text differentiation. Do not treat Recknagel as conclusively validated strong prior art given unresolved validation concerns.

### Study C1b — Fournier et al. 2024 (Reservoir, Spain; abstract/review-informed)

| Field | Assessment |
|---|---|
| **Citation** | Fournier, C., Fernandez-Fernandez, R., Cirés, S., López-Orozco, J. A., Besada-Portas, E., & Quesada, A. (2024). LSTM networks provide efficient cyanobacterial blooms forecasting even with incomplete spatio-temporal data. *Water Research*, 267, 122553. https://doi.org/10.1016/j.watres.2024.122553 |
| **Location/ecosystem** | Cuerda del Pozo reservoir, Spain (reported by independent review, unverified in-session; abstract does not name site). |
| **Dataset/sampling** | 6 years incomplete high-frequency spatio-temporal probe data (abstract). Independent review (unverified in-session): Jan 2010–Nov 2015; 4-day aggregation. |
| **Biological ground truth** | PC fluorescence proxy; 10 µg PC/L alarm threshold (abstract). No independent biological ground truth reported by independent review (unverified in-session). |
| **Variables** | Multiparametric probes including phycocyanin (abstract). |
| **Methods** | AR and multivariate LR, RF, LSTM (abstract/review). No relationship-change/coupling indicator evident from accessible evidence. |
| **Validation design** | Horizons 4–28 days (abstract). Independent review (unverified in-session): temporal split 1 Jan 2013; only one major bloom in test period; interpolation described before split (possible but unconfirmed leakage). |
| **Main findings** | Abstract: multivariate LSTM best; up to 90% accuracy for 10 µg PC/L alarm; positive skill 16–28 days ahead. Review cautions: limited improvement over persistence at shorter horizons and insufficient FAR/confusion-matrix reporting (unverified in-session). |
| **Limitations** | Full text not reviewed. Proxy target, possible leakage, limited event count, and incomplete FAR/confusion-matrix reporting are unverified in-session concerns; ~90% accuracy requires cautious interpretation. |
| **Overlap with EcoSentinel** | High overlap: HF in situ/probe data, cyanobacteria bloom forecasting, temporal horizons, incomplete data handling. |
| **Difference from EcoSentinel** | Forecasts PC alarm exceedance with ML models; no evidence of relationship-change indicators or matched-FAR independent biological event evaluation. |

**Originality implication:** Close comparator. Reinforces need for independent biological labels, event-based evaluation, leakage checks, and matched-FAR reporting.


### Study C2 — Pace et al. 2017 (Peter Lake, USA)

| Field | Assessment |
|---|---|
| **Citation** | Pace, M. L., Batt, R. D., Buelo, C. D., Carpenter, S. R., Cole, J. J., Kurtzweil, J. T., & Wilkinson, G. M. (2017). Reversal of a cyanobacterial bloom in response to early warnings. *PNAS*, 114(2), 352–357. https://doi.org/10.1073/pnas.1612424114 |
| **Location/ecosystem** | Peter Lake, Michigan/Wisconsin region, USA; experimental lake. |
| **Dataset/sampling** | High-frequency monitoring during nutrient enrichment experiment. |
| **Biological ground truth** | Induced cyanobacterial bloom response to enrichment; pigment/monitoring indicators. |
| **Variables** | Pigments/resilience indicators; nutrient enrichment manipulation. |
| **Methods** | Resilience indicators / early warning signals; management intervention. |
| **Validation design** | Whole-lake experimental manipulation with intervention threshold. |
| **Main findings** | Early-warning indicators detected during enrichment; halting nutrient input reversed bloom trajectory. |
| **Limitations** | Controlled experimental lake; induced bloom; not natural multi-year observational forecasting; single system. |
| **Overlap** | Cyanobacterial bloom early warning concept; high-frequency monitoring. |
| **Difference** | EcoSentinel focuses on observational Buffalo Pound data, multivariate relationship changes, and matched-FAR comparison against conventional monitoring; Pace tests EWS in controlled manipulation. |

### Study C3 — Rousso et al. 2020 (Systematic review)

| Field | Assessment |
|---|---|
| **Citation** | Rousso, B. Z., Bertone, E., Stewart, R., & Hamilton, D. P. (2020). A systematic literature review of forecasting and predictive models for cyanobacteria blooms in freshwater lakes. *Water Research*, 182, 115959. https://doi.org/10.1016/j.watres.2020.115959 |
| **Location/ecosystem** | Global synthesis; freshwater lakes. |
| **Dataset/sampling** | Review of published models (full inclusion set unverified in-session). |
| **Biological ground truth** | Varies by included study. |
| **Variables** | Nutrients, physical, chemical, meteorological, biological predictors (review-level). |
| **Methods** | Systematic review of forecasting/predictive models; abstract distinguishes process-based and data-driven models. |
| **Validation design** | Review-level assessment; abstract notes performance assessment/protocol and standardization as challenges. |
| **Main findings** | Maps forecasting model landscape; identifies predictors, model classes, and gaps including data quality, generalizability, and validation challenges. |
| **Limitations** | Full text not retrieved in-session; review conclusions depend on included studies and are time-bound. |
| **Overlap** | Defines the broader forecasting field EcoSentinel must differentiate from. |
| **Difference** | Not a primary study; useful for positioning and gap identification. |

**Reconciliation note (2026-11-22):** Earlier in-session notes inconsistently reported Rousso abstract as not retrieved. PubMed abstract (PMID 32531494) was retrieved in-session and Crossref metadata verified; full text remains not retrieved. Records have been reconciled to "metadata + PubMed abstract verified; full text not retrieved."

### Study C4 — Buffalo Pound local studies (Painter 2022, Painter 2023, Boyer 2025)

| Study | Citation | Overlap | Difference |
|---|---|---|---|
| Painter 2022 | https://doi.org/10.1039/D2EM00078D | Same lake; cyanobacterial bloom dynamics; pigment limitations. | Observational taxonomy/metabolite study, not predictive early warning. |
| Painter 2023 | https://doi.org/10.1002/ecs2.4472 | Same lake; high-frequency monitoring; bloom occurrence drivers. | Uses phycocyanin/GAM analysis of flow management; not independent-label early-warning evaluation. |
| Boyer 2025 | https://doi.org/10.1111/fwb.70131 | Same lake; bloom development, N2 fixation, community change. | Mechanistic/observational ecology; not early-warning system evaluation. |

These are essential local context, not competing early-warning models.

### Study C5 — Critical transition / EWS methods (Scheffer 2009, Dakos 2012, Carpenter 2011)

| Study | Citation | Overlap | Difference |
|---|---|---|---|
| Scheffer 2009 | https://doi.org/10.1038/nature08227 | Generic early-warning theory. | Not cyanobacteria-specific; not multivariate relationship-change forecasting system. |
| Dakos 2012 | https://doi.org/10.1371/journal.pone.0041010 | EWS method limitations and detection methods. | Simulated data; methodological, not Buffalo Pound application. |
| Carpenter 2011 | https://doi.org/10.1126/science.1203672 | Lake early warning before regime shift. | Whole-ecosystem food-web manipulation; different system/target. |

## 3. Additional prior-art cautions (Sprint 3 remediation)

| Prior art / family | Citation (verification) | Why it matters |
|---|---|---|
| EWS limited applicability to empirical lake data | O'Brien, D.A. et al. 2023. *Nat Commun*. https://doi.org/10.1038/s41467-023-43744-8 (Crossref metadata verified; full text not retrieved) | Generic EWS transfer to empirical lake data cannot be assumed; strengthens need for matched-FAR, nulls, and independent validation. |
| Multivariate resilience indicators | Weinans, E. et al. 2021. *Sci Rep*. https://doi.org/10.1038/s41598-021-87839-y (metadata verified; full text not retrieved) | Prior art for multivariate indicator families; EcoSentinel must distinguish its specific relationship-change indicators and evaluation design. |
| Dynamical network biomarkers | Chen, L. et al. 2012. *Sci Rep*. https://doi.org/10.1038/srep00342 (metadata verified; full text not retrieved) | Prior art for network/relationship-change precursor concepts; applicability to cyanobacteria bloom early warning requires careful scoping. |
| Autocorrelation/cyanobacteria early warning | Kehoe et al. related work identified in search (biorxiv 10.1101/674325 surfaced) but peer-reviewed citation/DOI not fully verified in this sprint | Do not cite as settled prior art until exact publication metadata is verified. |
| Natural-lake vs experimentally manipulated evidence | Pace et al. 2017 is a whole-lake manipulation (https://doi.org/10.1073/pnas.1612424114) | Manipulation evidence is not equivalent to observational natural-lake forecasting evidence. |

## 4. Originality assessment (preliminary, cautious)

| Candidate claim | Status | Evidence |
|---|---|---|
| "No one has studied cyanobacterial blooms with sensors" | **False/unsupported** | Many studies exist; Rousso 2020 reviews field. |
| "High-frequency in situ early warning for cyanobacteria is unexplored" | **Likely false** | Recknagel 2025 and Fournier 2024 are close HF in situ/probe comparators. |
| "Multivariate relationship-change (rolling correlation/coupling) as early warning, evaluated at matched FAR against conventional monitoring with independent biological labels" | **Potentially underexplored, not proven original** | Closest identified studies do not clearly match this exact combination from accessible evidence; but full-text review of Recknagel 2025, Fournier 2024, Rousso-cited studies, and multivariate EWS/DNB prior art is required. |
| "Buffalo Pound-specific application of this exact protocol" | **Possibly novel as local application**, but novelty of application is weaker than methodological originality. | Local studies exist; no identical confirmed study found in-session. |

## 5. Required next step before any originality claim

Conduct full-text review of at least: Recknagel et al. 2025; Fournier et al. 2024; Rousso et al. 2020; O'Brien et al. 2023; Weinans et al. 2021; Chen et al. 2012; and other high-frequency HAB early warning / multivariate EWS / network-biomarker papers not captured by this limited search. Compare on: label independence, matched FAR, event-based evaluation, relationship-change indicators, temporal leakage controls, baselines, and confounding/null controls. Verify any independent-review-reported comparator leakage concerns against primary sources before using them in positioning.

## 6. References

See `LITERATURE_EVIDENCE_REGISTER.csv` for full verified list.
