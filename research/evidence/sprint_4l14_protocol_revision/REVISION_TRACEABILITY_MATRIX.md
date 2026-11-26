# Revision Traceability Matrix

**Sprint:** 4L.14  
**Status:** PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Date:** 2026-11-24

> **This matrix demonstrates where each Sprint 4L.13 finding was addressed. It does not approve the protocol.**

## 1. Summary

| Revision | Finding | Status | Primary file(s) | Residual uncertainty |
|---|---|---|---|---|
| R-01 | Question wording | **Addressed** | `REVISED_RESEARCH_QUESTION.md`; `REVISED_PROTOCOL.md` §3 | Human approval of wording |
| R-02 | Actual usable n | **Addressed as specification; counts not calculated** | `ESTIMAND_AND_SAMPLE_ELIGIBILITY_SPECIFICATION.md`; `REVISED_PROTOCOL.md` §6 | Actual n unknown until post-approval audit |
| R-03 | Relative concordance | **Removed** | `REVISED_RESEARCH_QUESTION.md`; `REVISED_PROTOCOL.md` §11; `UPDATED_HUMAN_DECISION_REGISTER.md` D-01 | None; decision remains outstanding |
| R-04 | Uncertainty method | **Addressed** | `UNCERTAINTY_AND_SENSITIVITY_PLAN.md`; `REVISED_PROTOCOL.md` §12 | No reliable BP interval; Mendota range descriptive |
| R-05 | QC/missingness | **Addressed as exact rules** | `QC_AND_MISSINGNESS_RULES.md`; `REVISED_PROTOCOL.md` §10 | B7/negative/H counts not yet enumerated |
| R-06 | Buffalo Pound biomass | **Addressed; derivation partially verified; P3/P4 downgrade recommended pending D-02** | `BIOLOGICAL_ENDPOINT_AND_BIOMASS_REVIEW.md`; `REVISED_PROTOCOL.md` §7 | Full paper text inaccessible; density assumption |
| R-07 | Two-lake framing | **Addressed** | `TWO_CASE_STUDY_DESIGN.md`; `REVISED_PROTOCOL.md` §4 | Human approval of framing |
| R-08 | 2019-07-17 leverage | **Addressed as plan; not calculated** | `2019_07_17_LEVERAGE_PLAN.md`; `REVISED_PROTOCOL.md` §13 | Leverage results unknown until post-approval |
| R-09 | Source metadata/contradictory evidence | **Addressed** | `PRIOR_ART_AND_SOURCE_CORRECTIONS.md`; `SOURCE_REGISTER.md`/`.csv` | Some sources abstract-only |
| R-10 | Index status | **Addressed** | This package has no stale index; 4L.12 index remains prior record | — |
| R-11 | Log-Pearson | **Removed** | `REVISED_PROTOCOL.md` §11.3 | None |
| R-12 | Overall-n rule | **Specified; number to be set after audit** | `ESTIMAND_AND_SAMPLE_ELIGIBILITY_SPECIFICATION.md` §8; `REVISED_PROTOCOL.md` §6.4 | Exact minimum n not set |

## 2. Detailed traceability

### R-01 — Rewrite the question

**Original finding:** “paired observations,” “strength,” and “depth-alignment setting” overstate the design.

**Addressed in:**
- `REVISED_RESEARCH_QUESTION.md` §2–§3;
- `REVISED_PROTOCOL.md` §1, §3;
- `UPDATED_HUMAN_DECISION_REGISTER.md` D-01, D-03, D-07.

**Acceptance criteria:**
- [x] “paired observations” removed/replaced with “same-day date-level co-occurrence”;
- [x] “strength” removed/replaced with “direction and magnitude of Spearman’s ρ”;
- [x] “depth-alignment setting” removed as explanatory variable;
- [x] two separate lake-specific case studies;
- [x] original early-warning question preserved as long-term aspiration only.

**Evidence:** 4L.13 `ESTIMAND_AND_MEASUREMENT_REVIEW.md`, `MATCHING_AND_TEMPORAL_REVIEW.md`, `TWO_LAKE_COMPARABILITY_REVIEW.md`.

**Residual uncertainty:** Human reviewers must accept the wording.

---

### R-02 — Actual usable n

**Original finding:** 128/139/42/42 are upper bounds, not actual n.

**Addressed in:**
- `ESTIMAND_AND_SAMPLE_ELIGIBILITY_SPECIFICATION.md` §2–§8;
- `REVISED_PROTOCOL.md` §5–§6;
- `UPDATED_HUMAN_DECISION_REGISTER.md` D-11.

**Acceptance criteria:**
- [x] maximum n distinguished from actual n;
- [x] exact eligibility rules for P1–P4;
- [x] actual n marked unknown;
- [x] count-only audit specified as post-approval step;
- [x] no counts invented;
- [x] minimum-n rule deferred to statistical reviewer after audit;
- [x] no correlations calculated.

**Evidence:** 4L.12 `PRE_ANALYSIS_PLAN.md`; 4L.13 `ESTIMAND_AND_MEASUREMENT_REVIEW.md`.

**Residual uncertainty:** Actual n and whether each estimand is reportable.

---

### R-03 — Relative concordance

**Original finding:** under-defined; adds little beyond Spearman.

**Addressed in:**
- `REVISED_RESEARCH_QUESTION.md` §3.2;
- `REVISED_PROTOCOL.md` §11.2;
- `UPDATED_HUMAN_DECISION_REGISTER.md` D-01.

**Acceptance criteria:**
- [x] removed from operational definition;
- [x] removed from primary/secondary estimands;
- [x] explicitly not computed;
- [x] no undefined term in the question;
- [x] no arbitrary replacement statistic introduced.

**Evidence:** 4L.13 `ASSOCIATION_AND_CONCORDANCE_REVIEW.md`.

**Residual uncertainty:** None; decision remains for human approval.

---

### R-04 — Uncertainty method

**Original finding:** BP bootstrap invalid; Mendota year-cluster bootstrap questionable.

**Addressed in:**
- `UNCERTAINTY_AND_SENSITIVITY_PLAN.md`;
- `REVISED_PROTOCOL.md` §12;
- `UPDATED_HUMAN_DECISION_REGISTER.md` D-10.

**Acceptance criteria:**
- [x] no BP bootstrap interval;
- [x] BP separate 2018/2019 + leave-one-date-out range;
- [x] Mendota leave-one-year-out range;
- [x] optional season-year block bootstrap as descriptive sensitivity;
- [x] 14 non-exchangeable clusters acknowledged;
- [x] descriptive ranges vs confidence intervals distinguished;
- [x] no p-values.

**Evidence:** 4L.13 `BOOTSTRAP_AND_DEPENDENCE_REVIEW.md`; methodological sources S64–S72.

**Residual uncertainty:** No reliable interval for BP; Mendota range is descriptive.

---

### R-05 — QC and missingness

**Original finding:** “retain H if plausible” not operational; negatives/B7 issues.

**Addressed in:**
- `QC_AND_MISSINGNESS_RULES.md`;
- `REVISED_PROTOCOL.md` §10;
- `UPDATED_HUMAN_DECISION_REGISTER.md` D-05.

**Acceptance criteria:**
- [x] every relevant flag code defined;
- [x] exact treatment of flagged numeric values;
- [x] undocumented flags classified `UNRESOLVED_FLAG`;
- [x] negative RFU retained primary with exclusion sensitivity;
- [x] physical/document bounds with evidence;
- [x] no arbitrary ecological limits;
- [x] B7 exclusion + inclusion sensitivity + overlap reporting;
- [x] missingness taxonomy;
- [x] exclusion reason codes;
- [x] effects on coverage/B7 to be reported in count audit;
- [x] no new analytical results.

**Evidence:** 4L.9/4L.10 QC audits; 4L.13 `QC_AND_MISSINGNESS_REVIEW.md`; BP data paper.

**Residual uncertainty:** B7/negative/H counts; effect on n.

---

### R-06 — Buffalo Pound biomass derivation

**Original finding:** derivation undocumented locally.

**Addressed in:**
- `BIOLOGICAL_ENDPOINT_AND_BIOMASS_REVIEW.md`;
- `REVISED_PROTOCOL.md` §7;
- `UPDATED_HUMAN_DECISION_REGISTER.md` D-02.

**Acceptance criteria:**
- [x] what biomass represents;
- [x] units;
- [x] derivation inferred and checked;
- [x] direct vs derived stated;
- [x] 2018/2019 consistency checked;
- [x] reproducibility assessed;
- [x] no assumed formula substitution without evidence;
- [x] P3/P4 conditional status stated;
- [x] P3/P4 recommended downgrade to exploratory pending D-02 verification.

**Evidence:**
- local `BP_PhytoTax_2018/2019` columns;
- arithmetic consistency check (2018 n=817; 2019 n=405; median ratio 1.000 × 10⁻⁶);
- GitHub repo/data structure;
- Painter et al. 2022 DOI/supplement metadata.

**Residual uncertainty:** Full paper text inaccessible; density assumption; replicate design; detection limits.

---

### R-07 — Two-lake framing

**Original finding:** depth contrast confounded; “depth-alignment setting” overclaims.

**Addressed in:**
- `TWO_CASE_STUDY_DESIGN.md`;
- `REVISED_RESEARCH_QUESTION.md` §3.4;
- `REVISED_PROTOCOL.md` §4;
- `UPDATED_HUMAN_DECISION_REGISTER.md` D-03.

**Acceptance criteria:**
- [x] two independent case studies;
- [x] confounder table;
- [x] no pooling;
- [x] no depth causal claim;
- [x] no Buffalo Pound validation of Mendota;
- [x] cross-case synthesis rules.

**Evidence:** 4L.13 `TWO_LAKE_COMPARABILITY_REVIEW.md`.

**Residual uncertainty:** Human acceptance of case-study framing.

---

### R-08 — 2019-07-17 leverage

**Original finding:** single date could dominate; retain + sensitivity needs leverage report.

**Addressed in:**
- `2019_07_17_LEVERAGE_PLAN.md`;
- `REVISED_PROTOCOL.md` §13;
- `UPDATED_HUMAN_DECISION_REGISTER.md` D-09.

**Acceptance criteria:**
- [x] eligibility check;
- [x] rank/leverage;
- [x] full vs leave-one-date-out ρ;
- [x] exact Δρ reporting;
- [x] materiality defined without arbitrary cutoff;
- [x] no calculation now;
- [x] retain-and-flag preserved pending D-09.

**Evidence:** 4L.12 `SPECIAL_DECISIONS_REVIEW.md`; 4L.10/4L.13 anomaly records.

**Residual uncertainty:** Leverage results; cause of anomaly.

---

### R-09 — Source metadata and contradictory evidence

**Original finding:** metadata errors; contradictory positive results under-represented.

**Addressed in:**
- `PRIOR_ART_AND_SOURCE_CORRECTIONS.md`;
- `SOURCE_REGISTER.md`/`.csv`;
- `EXTERNAL_SEARCH_LOG.md`.

**Acceptance criteria:**
- [x] corrected volume/pages/article numbers;
- [x] added Bertone 2018/2019, Ma 2023, Rozina 2018, Haggard 2023, USGS PhytoFind 2022;
- [x] contradictory positive/negative/inconclusive evidence;
- [x] access labels accurate;
- [x] methodological sources added;
- [x] originality remains low–moderate.

**Evidence:** Crossref metadata; abstracts/full text where accessible; 4L.13 prior art challenge.

**Residual uncertainty:** Some sources abstract-only; no systematic citation index.

---

### R-10 — Deliverables index

**Status:** Addressed in 4L.13/4L.14 packages; 4L.12 index remains a historical record. This package has no stale index claim.

### R-11 — Log-Pearson

**Status:** Removed. `REVISED_PROTOCOL.md` §11.3 states Pearson/log-Pearson not used. This avoids an arbitrary transformation.

### R-12 — Overall-n rule

**Status:** Specified. `ESTIMAND_AND_SAMPLE_ELIGIBILITY_SPECIFICATION.md` §8 and `REVISED_PROTOCOL.md` §6.4 require the statistical reviewer to set the minimum after the count audit; no arbitrary number is set now.

## 3. Cross-document consistency checks

| Check | Status |
|---|---|
| “Paired” removed from revised question/protocol | Pass |
| “Relative concordance” removed | Pass |
| “Depth-alignment setting” removed as explanatory | Pass |
| Two case studies language consistent | Pass |
| Max n vs actual n consistent | Pass |
| No pooling Turner/YSI | Pass |
| No pooling Mendota/BP | Pass |
| No biovolume/biomass conversion | Pass |
| No p-values | Pass |
| No BP bootstrap interval | Pass |
| No Pearson/log-Pearson | Pass |
| Claims matrix aligns with revised question | Pass |
| All 15 decision IDs preserved | Pass |
| All decisions marked NOT APPROVED | Pass |
| Governance status consistent | Pass |

## 4. Residual conflicts

None identified between the revised documents. The prior 4L.12 protocol remains unchanged as a historical record; where it conflicts with 4L.14, 4L.14 governs for the revised proposal.

## 5. Governance

- **Protocol: PROPOSED — NOT APPROVED.**
- **Gate 2: PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- No analysis is authorised until the required human decisions and explicit D-15 approval are recorded.
