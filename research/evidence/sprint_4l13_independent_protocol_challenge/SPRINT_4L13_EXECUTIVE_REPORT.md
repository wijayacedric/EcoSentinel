# Sprint 4L.13 Executive Report — Independent Protocol Challenge and Approval Preparation

**Sprint:** 4L.13  
**Status:** INDEPENDENT REVIEW — NOT APPROVAL  
**Protocol reviewed:** Sprint 4L.12, PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Date:** 2026-11-24

> **This sprint is an independent review only. It does not authorise data analysis or approve the protocol. The protocol remains PROPOSED — NOT APPROVED.**

## 1. Review outcome

# READY AFTER SPECIFIC REVISIONS — HUMAN REVIEW REQUIRED

The proposed two-lake descriptive measurement study is **scientifically coherent in its broad design**, but the 4L.12 protocol is **not ready for approval as written**.

The core design is sound enough to justify revision:

- it asks a descriptive question, not an early-warning or validation question;
- it separates association from agreement;
- it separates Turner and YSI;
- it separates Mendota and Buffalo Pound;
- it uses the date as the unit of analysis;
- it refuses labels, models, thresholds, prediction, and early warning;
- it has an explicit QC/missingness protocol and claims matrix.

The protocol has **material methodological issues** that must be fixed before approval:

1. the actual usable sample size is unknown;
2. “paired observations” overstates the date-level design;
3. “relative concordance” is under-defined and adds little;
4. the Buffalo Pound bootstrap cannot support a reliable interval;
5. the Mendota year-cluster bootstrap is questionable;
6. the QC rule depends on unstated “plausibility” judgement;
7. Buffalo Pound biomass derivation is undocumented;
8. the two-lake “depth-alignment” contrast is confounded;
9. the 2019-07-17 anomaly could dominate the Buffalo Pound result;
10. source metadata and contradictory evidence need correction.

All are fixable without new data. If they are not fixed, the outcome becomes **NOT READY — MATERIAL METHODOLOGICAL ISSUES**. If the team requires a genuinely novel early-warning contribution, the outcome becomes **RECOMMEND PAUSE — INSUFFICIENT SCIENTIFIC VALUE**.

## 2. What was inspected

The review read:

- all 14 Sprint 4L.12 deliverables;
- the 4L.12 index, SHA-256 register and README;
- the 4L.11 final recommendation, executive report and handover;
- the 4L.10 Mendota final decision, coverage tables and critiques;
- the 4L.9 sensor audit, QC tables, depth/era critiques;
- the 4L.5/4L.6 biology audits;
- the 4F Buffalo Pound stress test and alignment audit;
- the Gate 2F/G/H institutional/anomaly/limitations reports;
- the primary dataset metadata and data dictionaries;
- the 4L.12 source register and search log;
- the focused sensor–microscopy, phycocyanin, depth, seasonal, Mendota/Buffalo Pound, and bootstrap/dependence literature.

It did not:

- compute correlations from project data;
- generate plots or descriptive result tables from raw observations;
- create cleaned or derived analytical datasets;
- create labels or event intervals;
- run models, hypothesis tests, or threshold optimisation;
- change the research question or protocol;
- approve any of the 15 decisions;
- approve Gate 2;
- contact researchers or institutions;
- acquire additional data;
- upload, publish, commit, or push.

## 3. Area-by-area findings

### 3.1 Research question and estimands

**Finding: coherent but imprecise (Major).**

The question asks a legitimate descriptive question, but four phrases overstate the design:

- “paired observations” — the data are date-level co-occurrences, not paired measurements;
- “strength” — not a defined statistical quantity;
- “descriptive uncertainty” — Buffalo Pound cannot support a reliable interval;
- “depth-alignment setting” — implies a controlled contrast that the two-lake design cannot provide.

The four estimands are distinct sensor–endpoint pairs, but they are not independent: P1/P2 share the Mendota endpoint/dates; P3/P4 share the Buffalo Pound endpoint/dates. They should not be counted as four independent confirmations.

The maximum n values (128/139/42/42) are upper bounds under the strict 4L.10 unflagged rule, not actual primary n under the 4L.12 QC rule. Actual n is unknown and must be enumerated before estimation.

### 3.2 Association versus agreement

**Finding: mostly correct, with one weak concept (Major).**

The protocol correctly:

- refuses absolute agreement, Bland–Altman, concordance correlation, ICC, calibration, and prediction;
- distinguishes association from agreement;
- uses Spearman ρ for monotonic association;
- keeps Pearson as secondary.

The problem is **“relative concordance.”** It appears in the operational definition of comparability but is defined only in the statistical specification, as the proportion of consecutive-date pairs with the same sign of change. It adds little beyond Spearman, is sensitive to irregular sampling intervals, and can be inflated by seasonal co-trend. It should be removed from the operational definition or formally defined and demoted to exploratory.

“Strength” should be replaced by “direction and magnitude of Spearman’s ρ.” No strong/weak labels without a justified benchmark.

### 3.3 Bootstrap and temporal dependence

**Finding: Buffalo Pound interval is not defensible (Critical); Mendota interval is questionable (Major).**

- Mendota has 14 Turner-era years, but years are not exchangeable; sampling, sensor era, seasonal coverage, and n vary. A year-cluster bootstrap with 14 clusters is coarse and may not target a meaningful parameter.
- Buffalo Pound has two seasons. Date-level resampling ignores serial dependence and is anti-conservative; year-cluster resampling with two clusters is degenerate. There is no reliable interval.

Recommended replacement:

- Mendota: ρ, n, leave-one-year-out range; optional season-year block bootstrap as a descriptive sensitivity; no primary confidence interval.
- Buffalo Pound: ρ, n, separate 2018/2019 estimates, leave-one-date-out range; state “no reliable interval”; no bootstrap interval.
- No p-values.

### 3.4 Biological endpoints

**Finding: Mendota documented; Buffalo Pound conditional (Major).**

Mendota biovolume is microscopy-based, geometry-derived, measurement-independent of the sensor, and documented in the EML. It has taxonomy non-stationarity, repeated rows, anomalies, no detection limits, and a 0–8 m composite vs 0.5 m sensor.

Buffalo Pound `Biomass_mg_m3` is a derived microscopy quantity, not a direct measurement. The exact formula and 2018/2019 consistency are not documented in the local metadata. The source has `Cell_Volume_um3` and `Cell_Density_L` but no biovolume column. Before primary analysis, the biomass derivation must be verified; if not, Buffalo Pound should be downgraded to exploratory or excluded.

Biomass and biovolume are not numerically equivalent and must not be pooled.

### 3.5 Matching and temporal sensitivity

**Finding: conservative in intent, overclaimed in wording (Major).**

Same-day matching is the right primary rule given date-only biology. But it is not a paired measurement; the sensor daily mean integrates a full day, the biological sample time is unknown, and the sample is not the same water parcel.

The ±1-day sensitivity changes both the matching rule and the sample composition. It should be labelled exploratory, not a robustness check. No lag/lead/onset analysis is possible.

### 3.6 QC and missingness

**Finding: thoughtful taxonomy, incomplete operationalization (Major).**

The protocol correctly distinguishes missing, flagged, excluded, and usable observations; preserves raw data; forbids imputation; and requires flag counts and a flow table.

Problems:

- “retain H if plausible” is not numerically defined;
- negative pigment values are excluded from primary without a clear justification; this may truncate low signal and inflate ρ;
- B7 is an interval fouling flag; excluding it may remove high-biomass dates;
- C flags in 2014–2015 may make the Turner record uneven;
- the coverage rule has not been applied; actual n is unknown;
- the flow table is incomplete.

A second analyst could apply different rules. The protocol needs an exact decision tree and numeric bounds.

### 3.7 Two-lake comparison

**Finding: illustrative as two case studies; not a depth comparison (Major).**

The lakes differ in type, morphometry, stratification, community, instrument, period, sampling frequency, sample integration, QC, and endpoint. Depth alignment is one difference among many. The design cannot isolate depth.

The comparison can still be valuable as two case studies: a depth-mismatched Mendota case and a depth-aligned Buffalo Pound case. It cannot support “depth alignment improves agreement,” “Buffalo Pound validates Mendota,” or a generalisable multi-lake relationship.

### 3.8 2019-07-17

**Finding: retention is defensible, but leverage must be reported (Major).**

The anomaly is a documented observation: 45.81 mg m⁻³ total, 41.02 cyanobacteria, 9 rows all REP2, between neighbours 12,587.1 and 9,497.9. Cause unresolved. Retaining it and excluding it in sensitivity is a reasonable compromise, but at n=42 it could dominate ρ.

The protocol must report its rank/leverage, ρ with and without it, and whether the conclusion depends on it. It must not interpret it as bloom termination/non-bloom.

## 4. Prior-art and originality findings

The 4L.12 review correctly concluded that the measurement question is not novel. The independent review adds contradictory positive evidence that 4L.12 under-represented:

- Rozina et al. 2018: high CHL/PC–biovolume correlation in two small water bodies; PC false positives up to 1% of CHL.
- Ma et al. 2023: 2-h moving-average PC vs total cyanobacterial biovolume R=0.73 (p=0.098) at a high-risk plant; no meaningful correlation at low-risk plants.
- Thomson-Laing et al. 2020: strong overall relationships (r²≥0.78), but lake-specific 0.06–0.90.
- Rogora et al. 2023: total biovolume R²=0.72.
- Hartmann et al. 2019: good total chlorophyll–total biovolume agreement, with group bias.
- Haggard et al. 2023: raw fluorescence thresholds vs microcystin, an applied positive result.

The correct synthesis is **mixed and context-dependent**, not uniformly weak. The proposed study remains a modest measurement audit, not a novel contribution.

**Originality: LOW–MODERATE.** It is sufficient for a rigorous educational/competition measurement study if a negative/limited result is acceptable. It is not sufficient for a genuinely novel early-warning claim. If novelty is required, **PAUSE**.

## 5. The 15 human decisions

The exact decisions are reproduced in `HUMAN_DECISION_REGISTER.md`. None is approved.

| ID | Topic | Review recommendation (not approval) |
|---|---|---|
| D-01 | Comparability definition | Rank association only; remove/demote relative concordance |
| D-02 | Buffalo Pound endpoint | Supplied biomass, conditional on verifying derivation |
| D-03 | Mendota depth comparator | 0.5 m vs 0–8 m as case-study limitation; no correction |
| D-04 | Turner/YSI | Separate eras; no concatenation |
| D-05 | QC rule | Revised with exact decision tree; reconsider negatives |
| D-06 | Daily summary | Full-day mean; BP nighttime sensitivity |
| D-07 | Temporal window | Same-day primary; ±1-day exploratory only |
| D-08 | BP replicates | Mean as stated assumption; verify source |
| D-09 | 2019-07-17 | Retain + flag + sensitivity + leverage report |
| D-10 | Uncertainty | No BP interval; Mendota range/season-year sensitivity |
| D-11 | Small-n | n<10 stratum rule + overall-n rule |
| D-12 | Claims matrix | Adopt with updates |
| D-13 | Originality | Proceed only as modest audit; otherwise pause |
| D-14 | Licence | CC BY-NC-SA review; otherwise exclude BP |
| D-15 | Begin analysis | Do not approve until revisions/decisions |

The approvals remain distinct: scientific, statistical, data custodian, Gate 2 governance, licence, D-13, D-15.

## 6. Essential revisions

1. **R-01** — Rewrite the question: date-level co-occurrence, direction/magnitude of ρ, two case studies, no “depth-alignment setting.”
2. **R-02** — Enumerate actual usable n before estimation.
3. **R-03** — Remove or formally define/demote relative concordance.
4. **R-04** — Replace the bootstrap/uncertainty method; no BP interval.
5. **R-05** — Operationalize QC with an exact decision tree and numeric bounds; reconsider negatives.
6. **R-06** — Verify and document Buffalo Pound biomass derivation.
7. **R-07** — Reframe the two-lake comparison as two case studies.
8. **R-08** — Add a 2019-07-17 leverage report before analysis.
9. **R-09** — Correct source metadata and add contradictory evidence.

R-10–R-12 are recommended/required quality fixes.

## 7. What passed independent review

- Refusal of absolute agreement and predictive/validation claims.
- Turner/YSI separation.
- Mendota/Buffalo Pound separation.
- Date as the unit of analysis.
- No imputation; raw data preserved.
- Explicit matching rule.
- QC/missingness taxonomy (conceptually).
- 2019-07-17 transparency.
- Claims matrix.
- Honest low–moderate originality assessment.
- Governance alignment.

## 8. What failed or remains uncertain

- Actual n unknown.
- “Paired” wording.
- “Relative concordance” under-defined.
- Buffalo Pound bootstrap invalid.
- Mendota bootstrap questionable.
- QC “plausible” not operational.
- Negative-value exclusion.
- B7 overlap not quantified.
- Buffalo Pound biomass derivation.
- Depth comparison confounded.
- 2019-07-17 leverage.
- Source metadata/contradictory evidence.
- Originality low.

## 9. Single next milestone

**Revise the 4L.12 protocol in response to R-01–R-09, then submit the revised protocol and the completed human decision register for qualified human review.**

Do not begin analysis. Do not contact researchers. Do not acquire data. Do not approve Gate 2.

## 10. Deliverables

`research/evidence/sprint_4l13_independent_protocol_challenge/`

- `SPRINT_4L13_EXECUTIVE_REPORT.md`
- `PROTOCOL_METHODS_CHALLENGE.md`
- `ESTIMAND_AND_MEASUREMENT_REVIEW.md`
- `ASSOCIATION_AND_CONCORDANCE_REVIEW.md`
- `BOOTSTRAP_AND_DEPENDENCE_REVIEW.md`
- `BIOLOGICAL_ENDPOINT_REVIEW.md`
- `MATCHING_AND_TEMPORAL_REVIEW.md`
- `QC_AND_MISSINGNESS_REVIEW.md`
- `TWO_LAKE_COMPARABILITY_REVIEW.md`
- `SPECIAL_DECISIONS_REVIEW.md`
- `PRIOR_ART_AND_ORIGINALITY_CHALLENGE.md`
- `HUMAN_DECISION_REGISTER.md`
- `REQUIRED_PROTOCOL_REVISIONS.md`
- `FINAL_REVIEW_RECOMMENDATION.md`
- `SOURCE_REGISTER.md` / `.csv`
- `EXTERNAL_SEARCH_LOG.md`
- `SPRINT_4L13_HANDOVER.md`
- `EVIDENCE_SHA256_REGISTER.csv` + sidecar

## 11. Governance

- **Protocol: PROPOSED — NOT APPROVED.**
- **Gate 2: PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- No analysis is authorised until the required human decisions and explicit D-15 approval are recorded.
- This report is a review recommendation, not an approval.
