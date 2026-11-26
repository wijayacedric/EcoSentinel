# Comparator Audit Executive Report (Remediated)

**Project:** EcoSentinel  
**Date:** 2026-11-22 (remediated after independent scientific review)  
**Status:** Abstract/metadata-limited comparator audit. **Not a full-text audit.** Gate 2 remains **PAUSED / NOT APPROVED — Option C (Exploratory only)**.

## 1. Audit scope and major limitation

This audit reviewed priority comparators requested by the 22 Nov 2026 independent scientific review: Recknagel 2025, Fournier 2024, Rousso 2020, and Shen & Chen 2026 comment. Accessible primary evidence in-session was Crossref metadata and PubMed abstracts. Full texts/supplements/code/data were not accessible. The independent review provided additional method/validation claims; those claims are recorded as **unverified in-session** and are **not treated as conclusively demonstrated**.

The independent review itself is literature-only: it did not inspect repo dataset/code/Gate 2 records; it was targeted, not systematic; and it had mixed full-text/abstract access. Its project data-feasibility comments must be cross-checked against Gate 2 records.

## 2. Key findings

| Comparator | Verified from abstract/metadata | Reported by independent review (unverified) | Audit implication |
|---|---|---|---|
| Recknagel 2025 | 5-day-ahead hazard forecasting; 11 years hourly/daily HFISD; WT/TURB/pH/PHYCO; XGBoost/LSTM attention/HEA; training/unseen data results reported | Random 75/25 bootstrap split; only two training years reached hazard condition; no persistence baseline; no phycocyanin ablation; imputation using observations from other years; weekly biovolume interpolated to daily/hourly target resolution | Close comparator with unresolved validation/leakage concerns. Do not claim novelty or dismiss as invalid without full-text verification. |
| Fournier 2024 | 6 years incomplete HF spatio-temporal probe data; PC fluorescence proxy; 10 µg PC/L alarm; LR/RF/LSTM; 4–28 day horizons; up to 90% accuracy; positive skill 16–28 days ahead | Cuerda del Pozo reservoir, Spain; Jan 2010–Nov 2015; 4-day aggregation; temporal split 1 Jan 2013; only one major bloom in test period; interpolation before split (possible but unconfirmed leakage); no independent biological ground truth; insufficient FAR/confusion-matrix reporting; limited improvement over persistence at shorter horizons | Close comparator with proxy-target and validation-reporting cautions. Accuracy claims require careful interpretation. |
| Rousso 2020 | Systematic review of forecasting/predictive models; PB/DD taxonomy; data quality/generalizability/validation challenges noted | N/A | Landscape review; abstract retrieval discrepancy reconciled (PubMed abstract retrieved; full text not retrieved). |
| Shen & Chen 2026 comment | Four concerns: cross-year preprocessing/interpolation leakage risk; threshold-exceedance skill/lead-time/uncertainty needed; PHYCO dependence/persistence baselines/no-PHYCO ablations; mixed aggregation/single-station drivers vs multi-station/depth-integrated targets | N/A | Useful caution; no author response found in Crossref search 2026-11-22. |

## 3. Prior-art coverage corrections

The audit now explicitly records additional prior-art families/ cautions:
- **O'Brien et al. 2023** (Nat Commun, 10.1038/s41467-023-43744-8, metadata verified): early warning signals may have limited applicability to empirical lake data.
- **Multivariate resilience indicators**: Weinans et al. 2021 (Sci Rep, 10.1038/s41598-021-87839-y, metadata verified).
- **Dynamical network biomarkers**: Chen et al. 2012 (Sci Rep, 10.1038/srep00342, metadata verified).
- **Autocorrelation/generic EWS caution**: Dakos 2012 and related EWS literature remain relevant; Kehoe et al. cyanobacteria forecasting work was identified in search but publication/citation details require careful verification before use as a precise comparator claim.
- **Natural-lake vs experimentally manipulated distinction**: Pace 2017 manipulation evidence is not equivalent to observational natural-lake forecasting evidence.

## 4. Originality/positioning assessment

- **Rejected:** "EcoSentinel occupies completely unexplored territory."
- **Rejected:** "Matched-FAR alone creates novelty."
- **Supported (weak-moderate, conditional):** EcoSentinel may have a plausible methodological differentiation if it rigorously tests relationship-change indicators against simple baselines at matched FAR using independent biological labels, interval-censored onset, verified non-event exposure, and leakage-safe temporal validation.
- **Currently blocking:** Gate 2 has 0 independently reconstructed biological bloom events and 0 defensible verified non-bloom exposure intervals; confirmatory matched-FAR evaluation is not defensible.

## 5. Required next actions

1. Obtain full texts/supplements/data/code for Recknagel 2025 and Fournier 2024; verify independent-review-reported concerns against primary sources.
2. Verify Kehoe/autocorrelation cyanobacteria early-warning prior art with exact publication metadata before citing as settled comparator.
3. Maintain strict separation of verified abstract facts, unverified review claims, and EcoSentinel design aspirations.
4. Do not resume Gate 2 or change protocol/gate criteria based on this literature remediation.
