# 2019-07-17 Leverage Plan

**Sprint:** 4L.14  
**Status:** PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Date:** 2026-11-24

> **No analysis is authorised. This is a pre-analysis plan; the statistics are not calculated in this sprint.**

## 1. Purpose

This document implements Sprint 4L.13 revision R-08. It specifies how the 2019-07-17 Buffalo Pound anomaly will be assessed for influence on the rank association.

The existing proposal is **retain and flag**, with exclusion as a sensitivity. This document does not change that proposal; it defines the leverage assessment that must accompany it.

## 2. The anomaly

- Date: 2019-07-17 (DOY 198).
- Record: 9 taxon rows, all `REP2`.
- Total biomass: 45.81 mg m⁻³.
- Cyanobacteria biomass: 41.02 mg m⁻³ (89.5%).
- Neighbours: 2019-07-10 total 12,587.1 mg m⁻³; 2019-07-29 total 9,497.9 mg m⁻³.
- Taxonomy and group biomass agree.
- A same-date toxin sample exists but is not verified for quantitative use.
- Cause unresolved: real crash, sampling error, processing error, or replicate artifact.

## 3. Eligibility under final QC

After D-05/D-09 approval and the count audit, determine:

1. Is 2019-07-17 within the Buffalo Pound analysis window? (Yes, 2019-05-29 to 2019-10-03.)
2. Does it have a valid 0.8 m cyanobacteria biomass total?
3. Does it pass the `Group`/`Phylum` rule?
4. Does it have same-day shallow chlorophyll and phycocyanin values?
5. Do the sensor values pass the primary QC rules?
6. Does the date pass the within-day coverage rule?

If the date fails eligibility for a reason unrelated to the anomaly, it is excluded by the standard rule and the leverage assessment is moot for that estimand. Report the reason.

If it passes, it enters the primary analysis and is flagged `ANOMALY_20190717`.

## 4. Leverage assessment

For each of P3 (chlorophyll) and P4 (phycocyanin), after approval, report:

### 4.1 Rank position

- rank of the biological endpoint on 2019-07-17 among eligible dates;
- rank of the sensor value on 2019-07-17;
- whether the date is the minimum, maximum, or an interior rank.

### 4.2 Full-sample versus leave-one-date-out

- Spearman ρ on the full eligible sample;
- Spearman ρ with 2019-07-17 removed;
- exact difference Δρ = ρ_full − ρ_without;
- whether the sign changes;
- whether the descriptive interpretation changes (e.g., from positive to near-zero or negative).

### 4.3 Influence on the leave-one-date-out range

- whether 2019-07-17 is the most influential date;
- its position in the distribution of leave-one-date-out estimates;
- whether removing it moves the estimate outside the range produced by removing other dates.

### 4.4 Reporting

- report exact Δρ, not a “material/immaterial” label based on an arbitrary threshold;
- report whether the conclusion depends on the date;
- if the result changes materially, say so prominently in the abstract/results;
- do not select the version (with/without) that looks better;
- do not interpret the anomaly as bloom termination, recovery, or non-bloom.

## 5. Materiality

The protocol does **not** set a numeric cutoff for “material.” Instead:

- any sign change is material;
- any change that moves the estimate from a descriptive positive association to a near-zero/negative association (or vice versa) is material;
- any change that alters the stated conclusion is material;
- the exact Δρ is reported regardless.

This avoids an arbitrary threshold while ensuring transparency.

## 6. What must not happen

- Do not delete the date silently.
- Do not correct/impute the biomass value.
- Do not treat the date as a bloom/non-bloom event.
- Do not use the anomaly to claim the sensor failed or succeeded.
- Do not report only the version that supports a preferred conclusion.

## 7. D-09 status

D-09 remains **OUTSTANDING — NOT APPROVED**. The review recommendation is:

> Retain and flag; exclude in sensitivity; report leverage. The human data custodian/scientific reviewer must decide.

This document does not approve D-09.

## 8. Governance

- **Protocol: PROPOSED — NOT APPROVED.**
- **Gate 2: PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- No analysis is authorised until the required human decisions and explicit D-15 approval are recorded.
