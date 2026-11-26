# Sprint 4L.14 Executive Report — Protocol Revision and Human Review Preparation

**Sprint:** 4L.14  
**Status:** PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Date:** 2026-11-24

> **This sprint revised the protocol for human review. It did not approve the protocol, any of the 15 decisions, or Gate 2. No analysis was authorised or performed.**

## 1. Purpose and outcome

Sprint 4L.14 implemented the nine mandatory revisions from Sprint 4L.13 (R-01–R-09) and produced a complete revised protocol and updated human decision register.

The revised package is **ready for human review**, not approval. The protocol remains:

- **PROPOSED — NOT APPROVED**;
- **Gate 2 PAUSED / NOT APPROVED — Option C (Exploratory Only)**;
- all **15 decisions OUTSTANDING**;
- no **D-15** authorisation.

## 2. What changed

### R-01 — Research question

The question now uses:

- “same-day date-level co-occurrence” instead of “paired observations”;
- “direction and magnitude of Spearman’s ρ” instead of “strength”;
- “two separate lake-specific case studies” instead of “depth-alignment setting.”

The original early-warning question is preserved as a long-term aspiration only.

### R-02 — Actual usable n

The protocol now distinguishes:

- previously reported maximum n (128/139/42/42);
- actual primary n (unknown);
- exact eligibility rules for P1–P4;
- what the post-approval count-only audit must calculate.

No counts were invented. No correlations were calculated.

### R-03 — Relative concordance

“Relative concordance” was removed from the operational definition and from the primary/secondary estimands. Spearman’s ρ is the sole primary association statistic.

### R-04 — Uncertainty method

The bootstrap plan was replaced:

- **Mendota:** ρ, n, leave-one-year-out range; optional season-year block sensitivity as descriptive, not a CI;
- **Buffalo Pound:** no bootstrap interval; ρ, n, separate 2018/2019, leave-one-date-out range; state that two seasons cannot support a reliable interval;
- no p-values.

### R-05 — QC and missingness

The revised protocol includes:

- an exact flag decision tree;
- explicit `C/E/G/O/H` handling;
- negative RFU retained primary with exclusion sensitivity;
- Buffalo Pound `B7` excluded primary with inclusion sensitivity and overlap reporting;
- documented physical/analytical bounds;
- `UNRESOLVED` categories for undocumented flags/values;
- exclusion reason codes;
- count-audit reporting requirements.

No arbitrary ecological thresholds were introduced.

### R-06 — Buffalo Pound biomass

The biomass endpoint was investigated:

- `Biomass_mg_m3` is a derived microscopy quantity, not a direct measurement;
- data structure and arithmetic are consistent with:
  \[
  \text{Biomass}_{mg\,m^{-3}} \approx \text{Cell\_Volume}_{\mu m^3} \times \text{Cell\_Density}_{L^{-1}} \times 10^{-6}
  \]
  under a 1 g cm⁻³ density assumption;
- 2018 all 817 positive rows: median ratio 1.000 × 10⁻⁶ (range 9.87 × 10⁻⁷–1.0366 × 10⁻⁶);
- 2019 all 405 positive rows: median 1.000 × 10⁻⁶ (range 9.55 × 10⁻⁷–1.0227 × 10⁻⁶);
- 2018/2019 use the same relationship;
- full paper text was not accessible; the formula is inferred and documented as conditional.

P3/P4 are recommended for **downgrade to exploratory** pending data-custodian verification. They may be restored to primary if verification succeeds; they become unsuitable if the derivation is rejected or direct biovolume is required.

### R-07 — Two-lake framing

The design is now **two independent case studies**:

- no pooling;
- no depth-effect claim;
- no Buffalo Pound validation of Mendota;
- explicit confounder table;
- cross-case synthesis limited to side-by-side description.

### R-08 — 2019-07-17 leverage

A pre-analysis leverage plan was added:

- eligibility check;
- rank/leverage;
- full vs leave-one-date-out ρ;
- exact Δρ;
- sign/interpretation change;
- no arbitrary cutoff;
- retain-and-flag preserved pending D-09.

No leverage statistics were calculated.

### R-09 — Source corrections

Bibliographic metadata was corrected and contradictory evidence added:

- corrected volumes/pages/article numbers for Hartmann, Hodges, Cotterill, Rousso, Recknagel, Kovalenko, Carpenter, Buelo, Beal, Painter 2023, Baulch;
- added Bertone 2018/2019, Ma 2023, Rozina 2018, Haggard 2023, USGS PhytoFind 2022;
- balanced synthesis: relationships are mixed and context-dependent, not uniformly weak;
- originality remains low–moderate.

## 3. What remains unresolved

| Issue | Status |
|---|---|
| Actual usable n | Unknown until post-approval count audit |
| Buffalo Pound biomass full methods/density assumption | Inferred; conditional |
| P3/P4 primary status | Recommended downgrade to exploratory pending D-02 verification |
| B7 overlap with high biomass | Not yet quantified |
| Negative RFU counts in Buffalo Pound | Not yet quantified |
| Buffalo Pound replicate design | Not documented |
| 2019-07-17 leverage | Plan only; not calculated |
| Mendota 2014–2015 C-flag coverage | Known issue; effect on n unknown |
| Licence/competition review | Not completed |
| D-13 originality decision | Outstanding |
| D-15 authorisation | Outstanding |

These are explicitly reported, not hidden.

## 4. The 15 decisions

All 15 remain **OUTSTANDING — NOT APPROVED**. The updated register preserves the original IDs and wording and adds:

- revised proposal;
- evidence;
- remaining uncertainty;
- recommended human decision;
- responsible reviewer;
- approval status.

Most consequential:

- D-01 comparability = rank association only;
- D-02 Buffalo Pound biomass endpoint, conditional;
- D-05 QC decision tree;
- D-07 same-day primary; ±1-day exploratory;
- D-09 2019-07-17 leverage;
- D-10 descriptive ranges; no BP interval;
- D-13 proceed only as modest measurement audit, otherwise pause;
- D-14 CC BY-NC-SA review;
- D-15 do not authorise analysis yet.

## 5. Estimand status after revisions

| Estimand | Status |
|---|---|
| P1 | Suitable, conditional on actual n/QC |
| P2 | Suitable, conditional on actual n/QC |
| P3 | Recommended downgrade to exploratory pending D-02 verification; then conditional on actual n, B7/coverage, two seasons |
| P4 | Recommended downgrade to exploratory pending D-02 verification; same + *Planktothrix* caveat |

No estimand is categorically unsuitable at this stage. P3/P4 are the most conditional.

## 6. Is the package ready for human review?

**Yes.** The package is ready for qualified human review of the revised protocol and decisions.

It is **not ready for approval** until:

- the reviewer accepts R-01–R-09;
- all 15 decisions are recorded;
- actual n is enumerated after approval;
- the licence review is complete;
- D-15 is explicitly approved.

## 7. Single next milestone

**Submit the revised protocol and updated decision register to qualified human reviewers, then record D-01–D-14 and decide whether to authorise the count-only audit/D-15.**

Do not begin analysis. Do not contact researchers. Do not acquire data. Do not approve Gate 2.

## 8. Deliverables

`research/evidence/sprint_4l14_protocol_revision/`

- `SPRINT_4L14_EXECUTIVE_REPORT.md`
- `REVISED_RESEARCH_QUESTION.md`
- `REVISED_PROTOCOL.md`
- `ESTIMAND_AND_SAMPLE_ELIGIBILITY_SPECIFICATION.md`
- `QC_AND_MISSINGNESS_RULES.md`
- `UNCERTAINTY_AND_SENSITIVITY_PLAN.md`
- `BIOLOGICAL_ENDPOINT_AND_BIOMASS_REVIEW.md`
- `TWO_CASE_STUDY_DESIGN.md`
- `2019_07_17_LEVERAGE_PLAN.md`
- `PRIOR_ART_AND_SOURCE_CORRECTIONS.md`
- `UPDATED_HUMAN_DECISION_REGISTER.md`
- `REVISION_TRACEABILITY_MATRIX.md`
- `FINAL_HUMAN_REVIEW_PACKAGE.md`
- `SOURCE_REGISTER.md` / `.csv`
- `EXTERNAL_SEARCH_LOG.md`
- `SPRINT_4L14_HANDOVER.md`
- `EVIDENCE_SHA256_REGISTER.csv` + sidecar
- `EVIDENCE_SHA256_REGISTER_README.md`

## 9. Final governance status

**RESEARCH DIRECTION: CONTINUE — NARROWED RESEARCH QUESTION.**

**PROTOCOL: PROPOSED — NOT APPROVED.**

**GATE 2: PAUSED / NOT APPROVED — OPTION C (EXPLORATORY ONLY).**

**ALL 15 HUMAN DECISIONS: OUTSTANDING.**

**D-15: NOT APPROVED.**

No analysis is authorised without the required independent approvals and explicit D-15 authorisation.
