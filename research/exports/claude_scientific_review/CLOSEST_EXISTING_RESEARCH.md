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
| **Location/ecosystem** | Lake Müggelsee, Germany; eutrophic shallow lake (from title/metadata). |
| **Dataset/sampling** | High-frequency in situ monitoring (details require full text). |
| **Biological ground truth** | Harmful cyanobacteria blooms (definition/independence requires full text). |
| **Variables** | High-frequency in situ variables (full text required). |
| **Methods** | Intelligible machine learning modelling; early warning (full text required). |
| **Validation design** | Not verified in-session. |
| **Main findings** | Metadata/title indicate early warning of harmful cyanobacteria blooms using high-frequency in situ monitoring and intelligible ML. |
| **Limitations** | Full text not reviewed; cannot assess false-alarm matching, independence of labels, temporal leakage controls, or comparison to simple baselines. |
| **Overlap with EcoSentinel** | Very high topical overlap: early warning, cyanobacterial blooms, high-frequency in situ monitoring. |
| **Difference from EcoSentinel** | EcoSentinel proposes *relationship-change* (multivariate coupling) as precursor signal and emphasizes matched FAR, missed-event rate, and independent biological validation; Recknagel appears ML-focused (title-level). Full-text review required before claiming distinction. |

**Originality implication:** This is a close comparator. Any EcoSentinel originality claim must be carefully scoped and only after full-text review.

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
| **Dataset/sampling** | Review of published models. |
| **Biological ground truth** | Varies by included study. |
| **Variables** | Nutrients, physical, chemical, meteorological, biological predictors. |
| **Methods** | Systematic review of statistical, process-based, ML models. |
| **Validation design** | Review-level assessment. |
| **Main findings** | Maps forecasting model landscape; identifies predictors, model classes, performance reporting, and gaps. |
| **Limitations** | Review only; field evolves rapidly; full text not retrieved in-session. |
| **Overlap** | Defines the broader forecasting field EcoSentinel must differentiate from. |
| **Difference** | Not a primary study; useful for positioning and gap identification. |

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

## 3. Originality assessment (preliminary, cautious)

| Candidate claim | Status | Evidence |
|---|---|---|
| "No one has studied cyanobacterial blooms with sensors" | **False/unsupported** | Many studies exist; Rousso 2020 reviews field. |
| "High-frequency in situ early warning for cyanobacteria is unexplored" | **Likely false** | Recknagel 2025 title/metadata indicates close work; full review needed. |
| "Multivariate relationship-change (rolling correlation/coupling) as early warning, evaluated at matched FAR against conventional monitoring with independent biological labels" | **Potentially underexplored, not proven original** | Closest identified studies do not clearly match this exact combination from metadata; but full-text review of Recknagel 2025 and others is required. |
| "Buffalo Pound-specific application of this exact protocol" | **Possibly novel as local application**, but novelty of application is weaker than methodological originality. | Local studies exist; no identical confirmed study found in-session. |

## 4. Required next step before any originality claim

Conduct full-text review of at least: Recknagel et al. 2025; Rousso et al. 2020; other high-frequency HAB early warning papers (including ML/change-detection papers not fully captured by this limited search). Compare on: label independence, matched FAR, event-based evaluation, relationship-change indicators, temporal leakage controls, and baseline comparison.

## References

See `LITERATURE_EVIDENCE_REGISTER.csv` for full verified list.
