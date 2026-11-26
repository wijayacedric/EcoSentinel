# Recommended Experimental Dataset Strategy

**Date:** 2026-11-23T23:18:29.122618+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Recommendation

**Do not select a confirmatory dataset yet.** Use a two-track strategy:

### Track A — Verified exploratory work (can proceed within Option C)
**Buffalo Pound 2018-2019** is the only dataset with verified:
- independent species-level microscopy counts and biomass at 0.8 m;
- aligned 10-min multivariate buoy data at the same depth;
- all 25 (2018) and 17 (2019) biological dates matched to buoy days.

Use it for **descriptive, effort-aware exploratory analysis only**: data-quality characterization, alignment tables, predictor covariance structure, and method prototyping on synthetic/held-out-within-season data. Do **not** create bloom/non-bloom labels or claim event prediction. Two seasons are insufficient for confirmatory matched-FAR/held-out evaluation.

### Track B — Access-dependent high-value acquisition (requires human authorisation)
**Lake Mendota** is potentially the strongest candidate because of long-term (1995-2020) phytoplankton metadata plus high-frequency predictors in **129.9** (meteo/DO/chlorophyll/phycocyanin), not just temperature-only 130.29. Exact barrier: EDI PASTA requires an authorised API key (403 Public Access; no key in environment), and DataONE CN does not serve public data bytes. Obtain user authorisation and access, then perform file-level audit before any design decision.

### Not recommended as primary
- **Western Lake Erie:** discrete pigments/toxins, no cell/biovolume endpoint described, no verified HF multivariate buoy pairing, NCEI inaccessible. Keep as backup only.
- **Greifensee:** 60/60 packages are a strong environmental/exploratory resource, but the biological endpoint is classifier-derived, not independent. Exploratory only.

## Why not force a winner

Buffalo Pound has verified alignment but only two biological seasons. Mendota has the strongest potential but no verified data access. Declaring either a "winner" now would sacrifice scientific validity for convenience.

## Conditions before any Gate 2 readiness review

1. Authorised access to Mendota (or another multi-year independent biological dataset).
2. File-level verification of biological taxonomy, units, QC, cadence, missingness.
3. Verified multi-season biological–environmental alignment.
4. A defensible, protocol-compliant bloom/non-bloom exposure design (requires Gate 2 approval; not authorised now).
5. Feasibility of matched-FAR, leakage-resistant temporal/spatial validation.
6. Licence compatibility (especially Painter CC BY-NC-SA 4.0).

## Next scientifically justified action

Secure authorised EDI access for Mendota **and** complete the Buffalo Pound exploratory data-quality/alignment package. Both are legitimate within current governance; neither requires labels or modelling.
