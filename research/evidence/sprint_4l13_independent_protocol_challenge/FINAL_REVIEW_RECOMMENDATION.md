# Final Review Recommendation

**Sprint:** 4L.13  
**Status:** INDEPENDENT REVIEW — NOT APPROVAL  
**Protocol reviewed:** Sprint 4L.12, PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Date:** 2026-11-24

> **This is a review recommendation, not protocol approval. The protocol remains PROPOSED — NOT APPROVED. No analysis is authorised.**

## 1. Review outcome

# READY AFTER SPECIFIC REVISIONS — HUMAN REVIEW REQUIRED

The protocol is **not ready for approval as written**, but it is **not fundamentally unsound**. The core design — a descriptive, date-level comparison of surface pigment fluorescence with independent microscopy-derived cyanobacteria abundance in two lakes — is coherent. The main problems are precision, uncertainty, QC operationalization, endpoint documentation, and framing, not the existence of the study.

The protocol can become ready for human approval after the essential revisions in `REQUIRED_PROTOCOL_REVISIONS.md` and the 15 human decisions are recorded.

If the essential revisions are not made, the correct outcome is **NOT READY — MATERIAL METHODOLOGICAL ISSUES**.

If the team requires a genuinely novel early-warning contribution, the correct outcome is **RECOMMEND PAUSE — INSUFFICIENT SCIENTIFIC VALUE**.

## 2. Required final answers

### 2.1 Is the proposed measurement question scientifically coherent?

**Yes, conditionally.**

The question asks whether surface chlorophyll/phycocyanin fluorescence is rank-associated with microscopy-derived cyanobacteria biovolume/biomass, and how the association varies by season, sensor era, and the two lake settings. That is a coherent descriptive question.

It is not coherent as written because:

- “paired observations” implies a pairing the data cannot support;
- “strength” is undefined;
- “depth-alignment setting” implies a controlled comparison the design cannot provide;
- the actual usable n is unknown;
- Buffalo Pound biomass derivation is not documented.

After R-01, R-02, and R-06, the question becomes coherent.

### 2.2 Are the four estimands defensible?

**Conditionally.**

| Estimand | Assessment |
|---|---|
| P1 — Mendota Turner chlorophyll vs biovolume | **Defensible** as a descriptive rank association; depth/taxonomy caveats |
| P2 — Mendota Turner phycocyanin vs biovolume | **Defensible**; stronger biological rationale than chlorophyll, but taxon-dependent |
| P3 — Buffalo Pound chlorophyll vs biomass | **Conditional** on biomass derivation, actual n, B7/coverage, and two-season limitation |
| P4 — Buffalo Pound phycocyanin vs biomass | **Conditional** on the same, plus prior *Planktothrix* detection concerns |

The four are **distinct sensor–endpoint pairs**, not four independent quantities. P1/P2 share the Mendota endpoint and dates; P3/P4 share the Buffalo Pound endpoint and dates. They should not be counted as four independent confirmations.

### 2.3 Is the statistical approach appropriate?

**Partly.**

- **Spearman ρ:** appropriate for a monotonic rank association; correctly not treated as agreement.
- **No p-values:** appropriate given the descriptive goal.
- **Mendota year-cluster bootstrap:** questionable with 14 non-exchangeable years; should be replaced by a leave-one-year-out range and/or a season-year block bootstrap as a descriptive sensitivity.
- **Buffalo Pound date-level bootstrap:** **not appropriate**; two seasons and serial dependence cannot support a reliable interval. Report ρ, n, 2018/2019 separately, and a leave-one-date-out range; state “no reliable interval.”
- **Relative concordance:** under-defined and adds little; remove or demote to exploratory.
- **Log-Pearson:** secondary and arbitrary; justify or remove.

The statistical approach is appropriate in spirit (descriptive, no p-values) but not in its uncertainty method. R-03 and R-04 are essential.

### 2.4 Does the two-lake comparison add meaningful value?

**As two case studies: yes, modestly. As a depth comparison: no.**

The comparison can show whether the expected mixed/variable relationship appears in a depth-mismatched setting (Mendota) and a depth-aligned setting (Buffalo Pound), and it can document data-quality differences. That is useful.

It cannot isolate depth alignment. The lakes differ in type, morphometry, stratification, community, instrument, period, sampling frequency, sample integration, QC, and endpoint. Buffalo Pound cannot validate Mendota. The question should be reframed as two lake-specific case studies.

### 2.5 Does originality justify proceeding?

**Low–moderate originality. It justifies a modest measurement audit only if a negative/limited result is acceptable.**

The core question is already well studied. The literature contains both weak/variable results and positive results; the correct synthesis is “mixed and context-dependent.” The proposed study adds two specific lakes and a depth-mismatch contrast, but it does not add a new method, sensor, calibration, causal design, or generalisable dataset.

- **Educational/competition investigation:** yes, if framed honestly.
- **Defensible scientific contribution:** modest.
- **Genuinely novel research contribution:** no.

If the team requires a novel early-warning result, **PAUSE**.

### 2.6 Which protocol changes are essential?

**R-01 to R-07 are essential:**

1. Rewrite the question (remove “paired,” “strength,” “depth-alignment setting”).
2. Enumerate actual usable n before estimation.
3. Remove or formally define/demote “relative concordance.”
4. Replace the bootstrap/uncertainty method (no BP interval; revise Mendota).
5. Operationalize QC with an exact decision tree and numeric bounds; reconsider negative-value exclusion.
6. Verify and document Buffalo Pound biomass derivation.
7. Reframe the two-lake comparison as two case studies.

**R-08 is required before analysis:** 2019-07-17 leverage report.

**R-09 to R-12 are required/recommended for quality:** source metadata/contradictory evidence, index fix, log-Pearson justification, overall-n rule.

### 2.7 Which decisions require human judgement?

All 15 decisions in `HUMAN_DECISION_REGISTER.md`. The most consequential:

- **D-01** comparability definition;
- **D-02** Buffalo Pound endpoint;
- **D-05** QC rule;
- **D-07** temporal window;
- **D-09** 2019-07-17 handling;
- **D-13** proceed vs pause;
- **D-14** licence/competition compliance;
- **D-15** authorisation to begin analysis.

The approvals are distinct: scientific, statistical, data custodian, Gate 2 governance, licence, D-13, D-15. One does not imply another.

### 2.8 Is the protocol ready to be submitted for human review?

**Yes — after the essential revisions are incorporated.** It is not ready for approval today.

The protocol should be revised, re-reviewed, and then submitted to the qualified reviewers with the decision register. The review outcome would then be re-evaluated.

## 3. What passed independent review

1. Refusal of absolute agreement and predictive/validation claims.
2. Separation of Turner and YSI.
3. Separation of Mendota and Buffalo Pound.
4. Date as the unit of analysis.
5. No imputation; raw data preserved.
6. Explicit matching rule (same-day; no interpolation).
7. QC/missingness taxonomy (conceptually).
8. 2019-07-17 transparency.
9. Claims matrix with prohibited phrases.
10. Honest low–moderate originality assessment.
11. Governance alignment (Gate 2 paused; no labels/models).

## 4. What failed or remains uncertain

| Issue | Status | Severity |
|---|---|---|
| Actual n unknown | Unresolved | Major |
| “Paired” wording | Unresolved | Major |
| “Relative concordance” under-defined | Unresolved | Major |
| Buffalo Pound bootstrap invalid | Unresolved | Critical |
| Mendota bootstrap questionable | Unresolved | Major |
| QC “plausible” not operational | Unresolved | Major |
| Negative-value exclusion | Unresolved | Major |
| B7 overlap not quantified | Unresolved | Major |
| Buffalo Pound biomass derivation | Unresolved | Major |
| Depth comparison confounded | Unresolved | Major |
| 2019-07-17 leverage | Unresolved | Moderate |
| Source metadata/contradictory evidence | Partly resolved in 4L.13 | Minor–Moderate |
| Originality low | Confirmed | Major for D-13 |

## 5. Single next milestone

**Revise the Sprint 4L.12 protocol in response to R-01–R-09, then submit the revised protocol and the completed human decision register for qualified human review.**

Do not begin analysis. Do not contact researchers. Do not acquire data. Do not approve Gate 2.

## 6. What would change the outcome

The outcome would become **READY FOR HUMAN REVIEW — NO MATERIAL METHODOLOGICAL OBJECTIONS** if:

- R-01–R-07 are incorporated;
- actual n is enumerated and adequate;
- the BP uncertainty statement is honest;
- QC is fully reproducible;
- BP biomass is documented;
- the question is reframed as two case studies;
- the human decisions are recorded.

The outcome would become **NOT READY — MATERIAL METHODOLOGICAL ISSUES** if:

- the BP bootstrap interval is retained as a primary uncertainty statement;
- “relative concordance” remains undefined;
- actual n remains unknown;
- QC remains judgement-dependent;
- the depth contrast is presented as isolated.

The outcome would become **RECOMMEND PAUSE — INSUFFICIENT SCIENTIFIC VALUE** if:

- the team requires a novel early-warning contribution;
- the measurement audit cannot be framed as a legitimate modest contribution;
- the reviewers conclude that reproducing known mixed/variable relationships is not worth the effort.

## 7. Governance

- **Protocol: PROPOSED — NOT APPROVED.**
- **Gate 2: PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- No analysis is authorised until the required human decisions and explicit D-15 approval are recorded.
- This document is a review recommendation, not an approval.
