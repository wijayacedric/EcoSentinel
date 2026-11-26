# Required Protocol Revisions

**Sprint:** 4L.13  
**Status:** INDEPENDENT REVIEW — NOT APPROVAL  
**Protocol reviewed:** Sprint 4L.12, PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

> **This document specifies required revisions, not approvals. The protocol remains PROPOSED — NOT APPROVED until a revised version is reviewed and all human decisions are recorded.**

## 1. Priority definitions

| Priority | Meaning | Consequence |
|---|---|---|
| **Essential** | Must be incorporated before any human approval | Without it, the protocol is not ready |
| **Required** | Must be incorporated before analysis | Without it, analysis may be ambiguous or non-reproducible |
| **Recommended** | Should be incorporated for quality/clarity | Not necessarily blocking |

## 2. Revision list

### R-01 — Rewrite the primary question (Essential)

**Location:** `PROPOSED_RESEARCH_QUESTION.md` §3; `ONE_PAGE_PROTOCOL.md` Question; `PRE_ANALYSIS_PLAN.md` §3.1; `SPRINT_4L12_EXECUTIVE_REPORT.md` §4.

**Current:**

> ...among same-day paired observations... what are the direction, strength and descriptive uncertainty... and how do these associations vary by season and depth-alignment setting?

**Required:**

> ...among same-day date-level co-occurrences... what are the direction and magnitude of the rank association... and how do the two lake-specific associations differ descriptively across seasons and sensor eras, acknowledging that the lakes differ in depth alignment and many other respects?

**Acceptance criteria:**
- “paired observations” removed or replaced with “same-day date-level co-occurrence”;
- “strength” removed or replaced with “direction and magnitude of Spearman’s ρ”;
- “depth-alignment setting” removed as an explanatory variable;
- the question matches the claims matrix and scope.

**Rationale:** Date-only biology and daily sensor summaries cannot support a paired measurement design or a controlled depth comparison.

---

### R-02 — Enumerate actual usable n before estimation (Essential)

**Location:** `PRE_ANALYSIS_PLAN.md` §5; `DATASET_INCLUSION_EXCLUSION_RULES.md` §4.6, §6.5; all estimand tables.

**Current:** Maximum n 128/139/42/42 presented as if it defines feasibility.

**Required:**
- Add a count-only audit after QC approval and before any correlation.
- Report final n per estimand, by year and season.
- Report exclusions by reason and the biological endpoint distribution of included vs excluded dates.
- If n is too small for a stable rank estimate, return to human review.
- Replace “maximum n” with “maximum possible n under the strict unflagged rule” and “actual primary n (to be enumerated).”

**Acceptance criteria:**
- flow table completed;
- actual n reported for P1–P4;
- no correlation computed during the audit;
- decision rule for insufficient n recorded.

**Rationale:** The protocol’s own QC rule can change n; feasibility is not established by upper bounds.

---

### R-03 — Remove or formally define “relative concordance” (Essential)

**Location:** `PROPOSED_RESEARCH_QUESTION.md` §3.1; `STATISTICAL_ANALYSIS_SPECIFICATION.md` §11.1; `CLAIMS_AND_LIMITATIONS_MATRIX.md`; `ONE_PAGE_PROTOCOL.md`.

**Current:** “Comparability = rank association + relative concordance”; formula only in statistical specification.

**Required (preferred):**
- Remove “relative concordance” from the operational definition.
- Define comparability as rank association only.
- If a directional check is desired, retain sign concordance as an **exploratory secondary** analysis with a formal definition.

**If retained, specify:**
- formula for sign concordance;
- zero/tie handling;
- seasonal stratification;
- irregular-interval limitation;
- n pairs and descriptive range;
- why it adds information beyond Spearman;
- prohibition on “agreement”/“tracking” language.

**Acceptance criteria:**
- no undefined term in the primary question;
- if retained, a single canonical definition appears in the question document;
- it is labelled exploratory.

**Rationale:** The term is under-defined and adds little beyond Spearman; irregular intervals make sign concordance ambiguous.

---

### R-04 — Replace the bootstrap/uncertainty method (Essential)

**Location:** `STATISTICAL_ANALYSIS_SPECIFICATION.md` §8; `PRE_ANALYSIS_PLAN.md` §7.2; `ONE_PAGE_PROTOCOL.md` Statistics; D-10.

**Current:** Mendota year-cluster bootstrap; Buffalo Pound naive date-level bootstrap.

**Required:**
- **Buffalo Pound:** do not report a bootstrap interval. Report ρ, n, separate 2018/2019 estimates, and a leave-one-date-out sensitivity range. State that two seasons cannot support a reliable interval.
- **Mendota:** report ρ, n, and a leave-one-year-out range. Optionally report a season-year block bootstrap as a **descriptive sensitivity**, not a confidence interval. Do not present the year-cluster bootstrap as the primary interval.
- Label all ranges as descriptive, not inferential.
- Keep the no-p-values rule.

**Acceptance criteria:**
- no BP bootstrap interval;
- Mendota interval replaced or clearly demoted;
- text states “no reliable interval” for BP;
- D-10 revised accordingly.

**Rationale:** Temporal dependence, few clusters, and two seasons make the proposed intervals unreliable.

---

### R-05 — Operationalize QC with an exact decision tree (Essential)

**Location:** `QC_AND_MISSINGNESS_PROTOCOL.md` §3–§5; `DATASET_INCLUSION_EXCLUSION_RULES.md` §3.2, §5.2.

**Current:** “Retain H if plausible”; negative pigments excluded; B7 excluded; coverage rule.

**Required:**
- Provide exact numeric bounds for each variable.
- Provide a decision tree for every flag combination and value type (missing, flag, numeric, negative, above-range).
- Define “plausible” numerically, not by judgement.
- Justify or reverse the negative-value exclusion; report its effect on n and ρ.
- Quantify B7 overlap with biomass; report ρ with/without.
- Report n by year/season; flag sparse years.
- Complete the flow table.

**Acceptance criteria:**
- a second analyst can apply the rules without subjective judgement;
- every exclusion has a reason code;
- negative and B7 sensitivity analyses are pre-specified.

**Rationale:** The current rules are directionally sensible but not fully reproducible; exclusions may bias the association.

---

### R-06 — Verify and document Buffalo Pound biomass derivation (Essential)

**Location:** `BIOLOGICAL_ENDPOINT_REVIEW.md` (this sprint); `DATASET_INCLUSION_EXCLUSION_RULES.md` §6; `PROPOSED_RESEARCH_QUESTION.md` §4.2.

**Current:** Biomass is used as supplied; derivation not documented locally.

**Required:**
- Verify the `Biomass_mg_m3` formula from Painter et al. methods/data documentation.
- Confirm 2018/2019 consistency.
- State that biomass is a derived microscopy quantity, not a direct measurement.
- State that it is not numerically equivalent to Mendota biovolume.
- If unverifiable, downgrade Buffalo Pound to exploratory or exclude.

**Acceptance criteria:**
- formula and units documented;
- 2018/2019 consistency confirmed or flagged;
- D-02 decision updated with the evidence.

**Rationale:** The endpoint’s interpretation and cross-season comparability depend on the derivation.

---

### R-07 — Reframe the two-lake comparison (Essential)

**Location:** `TWO_LAKE_COMPARABILITY_REVIEW.md` (this sprint); `PROPOSED_RESEARCH_QUESTION.md` §3; `PRE_ANALYSIS_PLAN.md` §3.1; `CLAIMS_AND_LIMITATIONS_MATRIX.md` C07.

**Current:** “depth-alignment setting” in the question; “natural contrast” language in prior documents.

**Required:**
- Call the design “two lake-specific case studies.”
- State that depth alignment is one of many differences.
- Remove any implication that the comparison isolates depth.
- Keep the prohibition on causal depth claims.
- Do not use Buffalo Pound to validate Mendota.

**Acceptance criteria:**
- question and claims matrix use case-study language;
- no “depth causes/improves” phrasing;
- confounder table retained.

**Rationale:** The design is severely confounded; depth is not identifiable.

---

### R-08 — Add a mandatory 2019-07-17 leverage report (Required)

**Location:** `SPECIAL_DECISIONS_REVIEW.md` (this sprint); `STATISTICAL_ANALYSIS_SPECIFICATION.md`; `PRE_ANALYSIS_PLAN.md` D-09.

**Required:**
- report the rank/leverage of 2019-07-17;
- report ρ with and without the date;
- state whether the conclusion depends on it;
- retain + flag + sensitivity, as proposed;
- do not interpret as bloom/non-bloom.

**Acceptance criteria:**
- leverage table included;
- sensitivity result reported alongside primary;
- no silent deletion/correction.

**Rationale:** A single extreme date can dominate a rank correlation at n=42.

---

### R-09 — Correct source metadata and add contradictory evidence (Required)

**Location:** `SOURCE_REGISTER.md`/`.csv`; `ORIGINALITY_AND_PRIOR_ART_UPDATE.md`; `EXTERNAL_SEARCH_LOG.md`.

**Required:**
- Correct volume/pages/article numbers where verified (Hodges, Beal, Cotterill, Rousso, Recknagel, Kovalenko, Hartmann, Carpenter, Buelo, Painter 2023, Baulch).
- Add Bertone 2018 review, Bertone 2019, Ma 2023, Rozina 2018, Haggard 2023, USGS PhytoFind 2022.
- Represent contradictory positive results, not only weak/variable findings.
- Keep access labels accurate (abstract vs full text).
- Add methodological sources for bootstrap/dependence.

**Acceptance criteria:**
- source register matches Crossref metadata where available;
- contradictory evidence is discussed;
- access status is accurate.

**Rationale:** The prior-art base should be balanced and verifiable.

---

### R-10 — Fix the deliverables index and status text (Recommended)

**Location:** `DELIVERABLES_INDEX.md`.

**Current:** Says SHA register “To be generated after final edits” although it exists.

**Required:** Update status to “Complete” and ensure all files are listed.

**Acceptance criteria:** index matches the directory.

---

### R-11 — Justify or remove the log-Pearson secondary analysis (Recommended)

**Location:** `STATISTICAL_ANALYSIS_SPECIFICATION.md` §6.

**Current:** Pearson on log10(1+x), no p-values.

**Required:** Either justify the transform as a pre-specified variance-stabilising scale check, or remove it. Do not try multiple transformations.

**Acceptance criteria:** one pre-specified transform or none; labelled secondary; no inference.

---

### R-12 — Add an overall-n estimability rule (Recommended)

**Location:** `STATISTICAL_ANALYSIS_SPECIFICATION.md` §15; `PRE_ANALYSIS_PLAN.md` D-11.

**Current:** n<10 rule for strata only.

**Required:** Add a rule for the overall estimand, set by the statistical reviewer after the count audit; show points only if not met; return to review if the design cannot support a stable estimate.

**Acceptance criteria:** rule recorded before estimation; no post hoc threshold.

---

## 3. Revision matrix

| ID | Revision | Priority | Blocks approval? | Blocks analysis? |
|---|---|---|---|---|
| R-01 | Rewrite question | Essential | Yes | Yes |
| R-02 | Enumerate actual n | Essential | Yes | Yes |
| R-03 | Remove/define relative concordance | Essential | Yes | Yes |
| R-04 | Replace bootstrap | Essential | Yes | Yes |
| R-05 | Operationalize QC | Essential | Yes | Yes |
| R-06 | Verify BP biomass | Essential | Yes | Yes |
| R-07 | Reframe two-lake comparison | Essential | Yes | Yes |
| R-08 | 2019-07-17 leverage | Required | No | Yes |
| R-09 | Source metadata/contradictory evidence | Required | No | No (before release) |
| R-10 | Fix index | Recommended | No | No |
| R-11 | Justify/remove log-Pearson | Recommended | No | No |
| R-12 | Overall-n rule | Recommended | No | Yes |

## 4. What does not need to change

- The refusal of absolute agreement and predictive/validation claims.
- The separation of Turner and YSI.
- The separation of Mendota and Buffalo Pound.
- The date-level unit of analysis.
- The no-imputation rule.
- The claims matrix’s prohibited phrases.
- The 2019-07-17 retention + flag + sensitivity approach (with leverage report).
- The no-p-values rule.

## 5. Acceptance statement

The protocol may be considered for human approval only when:

1. R-01–R-07 are incorporated;
2. R-08 is incorporated before analysis;
3. D-01–D-14 are recorded by qualified reviewers;
4. D-15 is explicitly approved;
5. The revised protocol is re-reviewed.

Until then:

**Protocol: PROPOSED — NOT APPROVED.**  
**Gate 2: PAUSED / NOT APPROVED — Option C (Exploratory Only).**
