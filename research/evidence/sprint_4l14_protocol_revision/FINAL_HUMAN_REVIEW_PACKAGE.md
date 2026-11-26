# Final Human Review Package

**Sprint:** 4L.14  
**Status:** PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Date:** 2026-11-24

> **This package is submitted for human review. It is not an approval. No analysis is authorised.**

## 1. What the reviewer is asked to do

The reviewer is asked to:

1. Confirm that the revised protocol addresses R-01–R-09.
2. Review the revised research question for precision and scope.
3. Review the four estimands and their eligibility rules.
4. Review the QC/missingness decision tree for reproducibility.
5. Review the uncertainty/sensitivity plan for honesty about dependence.
6. Review the Buffalo Pound biomass derivation and decide whether P3/P4 are suitable.
7. Review the two-case-study framing and reject any depth-effect language.
8. Review the 2019-07-17 leverage plan.
9. Review the corrected source register and balanced evidence synthesis.
10. Record decisions D-01–D-14 with names, rationales, and dates.
11. Decide whether the protocol is ready for D-15 authorisation.

The reviewer is **not** asked to approve analysis at this stage unless all decisions and D-15 are explicitly recorded.

## 2. What changed from 4L.12

| Revision | Change | Where |
|---|---|---|
| R-01 | Question rewritten: date-level co-occurrence; direction/magnitude of ρ; two case studies; no depth setting | `REVISED_RESEARCH_QUESTION.md`; `REVISED_PROTOCOL.md` §3 |
| R-02 | Max n vs actual n; eligibility rules; count-only audit | `ESTIMAND_AND_SAMPLE_ELIGIBILITY_SPECIFICATION.md`; `REVISED_PROTOCOL.md` §5–§6 |
| R-03 | Relative concordance removed | `REVISED_PROTOCOL.md` §11.2; D-01 |
| R-04 | Bootstrap replaced by descriptive ranges; no BP interval | `UNCERTAINTY_AND_SENSITIVITY_PLAN.md`; `REVISED_PROTOCOL.md` §12 |
| R-05 | QC decision tree; negative RFU retained primary; B7 sensitivity; exact bounds | `QC_AND_MISSINGNESS_RULES.md`; `REVISED_PROTOCOL.md` §10 |
| R-06 | Biomass derivation verified by arithmetic consistency; conditional endpoint | `BIOLOGICAL_ENDPOINT_AND_BIOMASS_REVIEW.md`; `REVISED_PROTOCOL.md` §7 |
| R-07 | Two independent case studies; no depth effect | `TWO_CASE_STUDY_DESIGN.md`; `REVISED_PROTOCOL.md` §4 |
| R-08 | 2019-07-17 leverage plan | `2019_07_17_LEVERAGE_PLAN.md`; `REVISED_PROTOCOL.md` §13 |
| R-09 | Source metadata corrected; contradictory evidence included | `PRIOR_ART_AND_SOURCE_CORRECTIONS.md`; `SOURCE_REGISTER.md`/`.csv` |

## 3. What remains unresolved

| Issue | Status | Blocks approval? |
|---|---|---|
| Actual usable n | Unknown until post-approval count audit | Yes |
| Buffalo Pound biomass density assumption/full methods text | Inferred/partially verified | Yes, for P3/P4 |
| P3/P4 primary status | Recommended downgrade to exploratory pending D-02 verification | Yes |
| B7 overlap with high biomass | Not yet quantified | Yes, for P3/P4 |
| Negative RFU counts in Buffalo Pound | Not yet quantified | Yes, for P3/P4 |
| Buffalo Pound replicate design | Not documented | Yes, for D-08 |
| 2019-07-17 leverage | Not yet calculated | No, but must be reported |
| Mendota 2014–2015 C-flag coverage | Known issue; exact effect on n unknown | Yes |
| Licence/competition review | Not completed | Yes, for public/competition use |
| D-13 originality decision | Outstanding | Yes |
| D-15 authorisation | Outstanding | Yes |

## 4. The 15 decisions

All 15 remain **OUTSTANDING — NOT APPROVED**. See `UPDATED_HUMAN_DECISION_REGISTER.md`.

The most consequential:

- **D-01** comparability = rank association only.
- **D-02** Buffalo Pound biomass endpoint, conditional on derivation acceptance.
- **D-05** QC decision tree; negative RFU/B7 handling.
- **D-07** same-day primary; ±1-day exploratory only.
- **D-09** 2019-07-17 retain/flag/leverage.
- **D-10** descriptive ranges; no BP interval.
- **D-13** proceed only as modest measurement audit, otherwise pause.
- **D-14** CC BY-NC-SA review.
- **D-15** do not authorise analysis yet.

## 5. Approval sequence

Recommended sequence:

1. **Scientific reviewer** — question, estimands, endpoints, two-case framing, claims.
2. **Statistical reviewer** — Spearman, descriptive ranges, no p-values, minimum n, sensitivity plan.
3. **Data custodian** — QC tree, negative RFU, B7, H, replicate rule, biomass derivation.
4. **Gate 2 governance** — Option C, no labels/models, scope.
5. **Licence/competition reviewer** — CC BY-NC-SA, attribution/share-alike, competition use.
6. **D-13** — project lead/scientific/governance proceed-vs-pause.
7. **D-15** — explicit authorisation after all above.

No step may be skipped. No approval implies another.

## 6. Review questions

1. Is the revised question precise enough to guide the analysis? If not, what wording remains ambiguous?
2. Are P1–P4 the right estimands? Should any be added, removed, or downgraded?
3. Is the actual-n audit sufficient to establish feasibility before estimation?
4. Is the QC decision tree reproducible by a second analyst?
5. Is retaining negative RFU in primary defensible, or should it be excluded?
6. Is excluding B7 from primary defensible given possible high-biomass overlap?
7. Is the Buffalo Pound biomass derivation acceptable? If not, are P3/P4 unsuitable?
8. Is the two-case-study framing sufficient to prevent depth-effect overclaiming?
9. Is the uncertainty plan honest about two-season limits?
10. Is the 2019-07-17 leverage plan sufficient?
11. Does the source register accurately reflect the balance of evidence?
12. Is the originality sufficient for the intended competition/educational goal?

## 7. Readiness statement

The package is **ready for human review** of the revised protocol and decisions.

It is **not ready for approval** until:

- the reviewer accepts R-01–R-09;
- the 15 decisions are recorded;
- actual n is enumerated after approval;
- the licence review is complete;
- D-15 is explicitly approved.

## 8. Sprint 4L.14 completion criteria

| Criterion | Status | Evidence |
|---|---|---|
| All nine revisions addressed | Met | `REVISION_TRACEABILITY_MATRIX.md` |
| Revised protocol internally consistent | Met | `REVISED_PROTOCOL.md`; cross-document checks |
| Unsupported numerical limits/statistical claims removed | Met | QC bounds documented; no arbitrary thresholds; no BP bootstrap interval; no Pearson |
| All four estimands have explicit eligibility rules | Met | `ESTIMAND_AND_SAMPLE_ELIGIBILITY_SPECIFICATION.md` |
| Maximum n distinguished from actual eligible n | Met | Same; actual n marked unknown |
| No prohibited analysis occurred | Met | No correlations/plots/labels/models/derived datasets/usable-n calculations; deterministic biomass check only |
| Unresolved evidence clearly identified | Met | Endpoint review; QC; uncertainty; handover |
| All 15 decisions available for human review | Met | `UPDATED_HUMAN_DECISION_REGISTER.md` |
| Revision traceability matrix | Met | `REVISION_TRACEABILITY_MATRIX.md` |
| Source register and search log complete | Met with access limitations | `SOURCE_REGISTER.md`/`.csv`; `EXTERNAL_SEARCH_LOG.md` |
| Final package suitable for human review | Met | This package |
| Evidence integrity checks pass | Met | SHA-256 register; 0 mismatches |

**Access limitation:** some key sources are abstract/metadata only; Painter 2022 full methods text was inaccessible (RSC/ESSOAr 403). These are recorded, not hidden.

## 9. Final governance status

**RESEARCH DIRECTION: CONTINUE — NARROWED RESEARCH QUESTION.**

**PROTOCOL: PROPOSED — NOT APPROVED.**

**GATE 2: PAUSED / NOT APPROVED — OPTION C (EXPLORATORY ONLY).**

**ALL 15 HUMAN DECISIONS: OUTSTANDING.**

**D-15: NOT APPROVED.**

No analysis is authorised without the required independent approvals and explicit D-15 authorisation.
