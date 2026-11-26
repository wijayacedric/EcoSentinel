# Comparator Audit Executive Report

**Project:** EcoSentinel  
**Date:** 2026-11-22  
**Status:** Abstract/metadata-limited comparator audit. **Gate 2 PAUSED / NOT APPROVED — Option C (Exploratory only).** No experimental work resumed.

## 1. Scope and limitation

This audit examined priority comparators: Recknagel et al. 2025 (10.1016/j.watres.2025.124514), Shen & Chen 2026 comment (10.1016/j.watres.2026.125406), Fournier et al. 2024 (10.1016/j.watres.2024.122553), and Rousso et al. 2020 (10.1016/j.watres.2020.115959). 

**Critical limitation:** Full texts, supplements, data availability statements, and author response to the 2026 comment were **not accessible** in-session despite attempts (Crossref, DOI webfetch, PubMed E-utilities, Semantic Scholar rate limits, Unpaywall 422, direct HTML scrape). Findings are based on verified Crossref metadata and PubMed abstracts. This report does **not** claim full-text-confirmed absence of methods/metrics.

## 2. Required verdicts

### Q1. Which study is the closest existing competitor to EcoSentinel?
**Answer:** **Recknagel et al. 2025** is the closest topical competitor found (HF in situ CyanoHAB early warning in a lake, intelligible ML, 5-day-ahead hazard forecasts). **Fournier et al. 2024** is also close (HF probe-based cyanobacterial bloom forecasting, 4-28 day horizons, LSTM).  
**Confidence: Medium.** Based on title/abstract/metadata; full texts required.

### Q2. Does any study already test substantially the same hypothesis?
**Answer:** **Not confirmed from accessible evidence.** No accessible abstract explicitly tests "persistent multivariate relationship changes provide earlier warning than conventional monitoring at comparable FAR" with independent biological event adjudication. But this is **not evidence of absence**; full-text review is required.  
**Confidence: Low.**

### Q3. Is the proposed relationship-change approach meaningfully different from existing multivariate forecasting?
**Answer:** **Potentially, but unproven.** Rolling correlation/coupling-change indicators are not mentioned in comparator abstracts, but multivariate models can implicitly capture relationships. The difference is meaningful only if it adds validated, interpretable, matched-FAR value beyond simple baselines and is not just alternative feature engineering.  
**Confidence: Low–Medium.**

### Q4. Is matched false-alarm-rate evaluation itself a novel contribution, or primarily a methodological quality requirement?
**Answer:** **Primarily a methodological quality requirement, not a standalone novelty claim.** It is necessary for credible early-warning evaluation but not sufficient for scientific originality.  
**Confidence: High.**

### Q5. What is the strongest defensible originality claim?
**Answer (conditional):** A rigorously evaluated claim that persistent multivariate relationship-change indicators provide added early-warning value over conventional/univariate baselines at matched FAR, using independently adjudicated biological events, interval-censored onset, verified non-event exposure, and confounder/null controls.  
**Confidence: Low–Medium.** Conditional on full-text differentiation and future evidence.

### Q6. What is the strongest argument that EcoSentinel is not sufficiently original?
**Answer:** HF in situ cyanobacterial bloom early warning/forecasting already exists (Recknagel 2025, Fournier 2024; reviewed field in Rousso 2020). EcoSentinel's relationship-change framing may be alternative feature engineering, matched FAR is not novelty, and the project currently lacks independent labels to test any claim.  
**Confidence: High.**

### Q7. What must be demonstrated before any originality claim can be made?
**Answer:** (1) Full-text comparator review confirming exact gap; (2) human-approved independent biological labels and non-event exposure; (3) pre-registered matched-FAR temporal/event-based evaluation; (4) added value over simple baselines and seasonal/autocorrelation/sensor/hydrology nulls; (5) transparent uncertainty and negative results.  
**Confidence: High.**

### Q8. Has the literature changed the scientific feasibility assessment?
**Answer:** **It reinforces caution, not feasibility.** The comparators show the problem is actively studied, making novelty harder and evaluation standards more important. Shen & Chen 2026 highlights leakage, threshold/FAR/lead-time/uncertainty, PHYCO dependence, and aggregation concerns - all directly relevant to EcoSentinel. Gate 2 evidence insufficiency remains the dominant feasibility blocker.  
**Confidence: High.**

## 3. 2026 comment implications (Shen & Chen 2026, abstract-level)

Reasonable concerns raised: preprocessing/interpolation leakage; R2/RMSE over threshold-exceedance/lead-time/FAR; PHYCO dependence needing ablation/persistence baselines; aggregation/spatial mismatch. These are **highly relevant** to EcoSentinel design. They are treated as **reasonable concerns pending full-text adjudication**, not proven defects, because original/comment full texts and any response were inaccessible.

## 4. Final classification

- **Established findings:** HF in situ cyanobacteria early warning/forecasting is an active research area; comparators exist.
- **Evidence-supported interpretations:** EcoSentinel overlaps topically with Recknagel 2025 and Fournier 2024; matched FAR is quality requirement, not novelty; Gate 2 label scarcity is blocking.
- **Unresolved questions:** Full-text method/validation details of comparators; whether any study already tests relationship-change + matched-FAR + independent-event design; author response to Shen & Chen 2026.
- **Speculative opportunities:** Relationship-change indicators may provide interpretable added value if rigorously validated - currently untested.

**No Gate 2 approval. No model training. No scope change.**
