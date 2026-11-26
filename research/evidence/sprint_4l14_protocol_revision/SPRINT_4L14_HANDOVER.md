# Sprint 4L.14 Handover

**Sprint:** 4L.14  
**Status:** PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Date:** 2026-11-24

## 1. What is complete

- Inspected `AGENTS.md`.
- Read the complete Sprint 4L.12 protocol package.
- Read the complete Sprint 4L.13 review package.
- Identified and implemented R-01–R-09.
- Produced a complete revised protocol, not just an amendment list.
- Updated all 15 human decisions with original wording, revised proposal, evidence, uncertainty, recommendation, reviewer, and status.
- Verified Buffalo Pound biomass derivation by data structure/arithmetic consistency.
- Corrected source metadata and added contradictory evidence.
- Produced a revision traceability matrix and final human review package.
- Produced source register, search log, and integrity records.

## 2. What is not complete

- No analysis, correlation, plot, derived dataset, label, event, model, hypothesis test, or threshold optimisation.
- No human decision approved.
- No D-15 authorisation.
- No Gate 2 approval.
- No external contact or data acquisition.
- No upload, publication, commit, or push.
- Actual usable n not enumerated (prohibited until D-15).
- 2019-07-17 leverage not calculated (prohibited until D-15).
- Licence/competition review not completed.
- Buffalo Pound full methods text not accessible; biomass formula inferred, not quoted.

## 3. Key findings

### 3.1 Revised question

> In Lake Mendota (2006–2020) and Buffalo Pound Lake (2018–2019), among same-day date-level co-occurrences and analysed as two separate lake-specific case studies, what are the direction and magnitude of the rank association between surface chlorophyll and phycocyanin fluorescence and independent microscopy-derived cyanobacteria biovolume (Mendota) or cyanobacteria biomass (Buffalo Pound), and how do these associations differ descriptively across seasons and sensor eras?

### 3.2 Four estimands

P1–P4 remain, but:

- 128/139/42/42 are **maximum possible n**, not actual n;
- actual n is unknown until the post-approval count audit;
- P1/P2 are suitable conditional on n/QC;
- P3/P4 are **recommended for downgrade to exploratory** pending D-02 verification of the biomass derivation, then conditional on n, B7/coverage, and two-season limits;
- if D-02 verification fails, P3/P4 are unsuitable for primary analysis.

### 3.3 Biomass derivation

`Biomass_mg_m3` is a derived microscopy quantity, consistent with:

\[
\text{Biomass}_{mg\,m^{-3}} \approx \text{Cell\_Volume}_{\mu m^3} \times \text{Cell\_Density}_{L^{-1}} \times 10^{-6}
\]

under a 1 g cm⁻³ density assumption.

- 2018: n=817 positive rows; median ratio 1.000 × 10⁻⁶; range 9.87 × 10⁻⁷–1.0366 × 10⁻⁶.
- 2019: n=405; median 1.000 × 10⁻⁶; range 9.55 × 10⁻⁷–1.0227 × 10⁻⁶.
- The variation is consistent with rounding.

This is a metadata/derivation check, not a statistical analysis. Full paper text was inaccessible; the formula is inferred and must be accepted by the data custodian.

### 3.4 Uncertainty

- Mendota: leave-one-year-out range; optional season-year block sensitivity; no primary CI.
- Buffalo Pound: no bootstrap interval; separate 2018/2019; leave-one-date-out range; state no reliable interval.
- No p-values.

### 3.5 QC

- Exact decision tree; no imputation.
- Negative RFU retained primary with exclusion sensitivity.
- B7 excluded primary with inclusion sensitivity and overlap reporting.
- H retained within bounds; strict-unflagged sensitivity.
- Undocumented flags `UNRESOLVED_FLAG`, excluded primary, sensitivity.
- Coverage rule for Buffalo Pound.

### 3.6 Two case studies

- No pooling.
- No depth-effect claim.
- No Buffalo Pound validation of Mendota.
- Confounder table retained.

### 3.7 2019-07-17

- Retain and flag primary.
- Exclusion sensitivity.
- Leverage plan: rank/leverage, full vs leave-one-date-out ρ, exact Δρ, sign/interpretation change.
- No arbitrary cutoff.
- No bloom/non-bloom interpretation.

### 3.8 R-01–R-09 status

| Revision | Status | Where |
|---|---|---|
| R-01 question | Fully addressed | `REVISED_RESEARCH_QUESTION.md`; `REVISED_PROTOCOL.md` §3 |
| R-02 actual n | Fully addressed as specification; counts not calculated | `ESTIMAND_AND_SAMPLE_ELIGIBILITY_SPECIFICATION.md` |
| R-03 relative concordance | Fully addressed (removed) | `REVISED_PROTOCOL.md` §11.2 |
| R-04 uncertainty | Fully addressed | `UNCERTAINTY_AND_SENSITIVITY_PLAN.md` |
| R-05 QC | Fully addressed as rules; coverage/B7 counts not calculated | `QC_AND_MISSINGNESS_RULES.md` |
| R-06 biomass | Addressed; derivation partially verified; P3/P4 downgrade recommended | `BIOLOGICAL_ENDPOINT_AND_BIOMASS_REVIEW.md` |
| R-07 two-lake framing | Fully addressed | `TWO_CASE_STUDY_DESIGN.md` |
| R-08 2019-07-17 | Fully addressed as plan; statistics not calculated | `2019_07_17_LEVERAGE_PLAN.md` |
| R-09 sources | Fully addressed; some sources abstract-only | `PRIOR_ART_AND_SOURCE_CORRECTIONS.md`; `SOURCE_REGISTER.md`/`.csv` |

### 3.9 Evidence integrity and prohibited actions

- 18 Sprint 4L.14 files registered; 0 hash mismatches.
- Raw Mendota data hashes unchanged.
- No correlations, plots, labels, event intervals, models, hypothesis tests, thresholds, derived analytical datasets, or usable-n calculations were performed.
- The only numerical check was a deterministic biomass-derivation consistency check on existing values; it is a documentary verification, not a statistical analysis.
- No external contact, dataset acquisition, upload, publication, commit, or push occurred.

### 3.10 Inaccessible or partial sources

- Painter et al. 2022 full text/supplement: RSC and ESSOAr returned 403; abstract/README/supplement metadata used. The biomass formula is inferred from data structure/arithmetic consistency, not quoted from the paper.
- Several sensor studies are abstract/metadata only (Hartmann, Bowling, Hodges, Thomson-Laing, Kovalenko, Cotterill, Rousso, Bertone 2018/2019, Rozina, Haggard).
- No systematic citation index/forward-citation database was available.
- No researcher reply or additional Buffalo Pound data are documented.
- No new dataset was acquired.

## 4. The 15 decisions

All **OUTSTANDING — NOT APPROVED**. See `UPDATED_HUMAN_DECISION_REGISTER.md`.

Approvals remain distinct: scientific, statistical, data custodian, Gate 2 governance, licence, D-13, D-15.

## 5. Blockers

1. No D-15 authorisation.
2. Actual n unknown.
3. Buffalo Pound biomass density assumption/methods text.
4. B7 overlap and negative RFU counts unknown.
5. Buffalo Pound replicate design undocumented.
6. 2019-07-17 leverage not calculated.
7. Mendota 2014–2015 C-flag coverage unknown.
8. Licence/competition review incomplete.
9. D-13 originality decision outstanding.
10. No Gate 2 approval.

## 6. Next single action

**Submit the revised protocol and updated decision register to qualified human reviewers.**

The review should:

1. accept/reject R-01–R-09;
2. record D-01–D-14;
3. decide whether D-15 authorises the count-only audit;
4. only after the audit, decide whether to authorise P1–P4 estimation.

Do not begin analysis, contact researchers, acquire data, or approve Gate 2 while the review is pending.

## 7. If approved

Sequence:

1. Count-only audit (R-02); no correlations.
2. Confirm actual n and estimand reportability.
3. Build analysis populations under the approved QC rules.
4. Descriptive summaries/flow table.
5. P1–P4 Spearman + descriptive ranges.
6. Sensitivities S-A–S-I.
7. 2019-07-17 leverage.
8. Claims-matrix check.
9. Independent review.

## 8. If not approved

- Revise the protocol again.
- Or **PAUSE — INSUFFICIENT SCIENTIFIC VALUE** if a novel early-warning result is required or the measurement audit is judged not worth doing.
- No pivot without a specific evidence-based alternative and a new protocol.

## 9. Final governance status

**RESEARCH DIRECTION: CONTINUE — NARROWED RESEARCH QUESTION.**

**PROTOCOL: PROPOSED — NOT APPROVED.**

**GATE 2: PAUSED / NOT APPROVED — OPTION C (EXPLORATORY ONLY).**

**ALL 15 HUMAN DECISIONS: OUTSTANDING.**

**D-15: NOT APPROVED.**

No analysis is authorised without the required independent approvals and explicit D-15 authorisation.
