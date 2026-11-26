# Adversarial Audit

**Sprint:** 4L.19  
**Purpose:** Test the proposed Stage 1 design against three hostile-but-fair perspectives before finalising the package.  
**Status:** Internal adversarial review. **Not an independent review. No decision approved.**

---

## 1. How this audit was conducted

Three reviewer personas were used:

- **Reviewer A — freshwater ecologist:** endpoint validity, biological interpretation, taxonomy, measurement independence, sampling representativeness, depth mismatch, seasonal confounding, scientific contribution.
- **Reviewer B — environmental statistician:** sampling structure, temporal dependence, QC selection bias, small samples, rank association, multiplicity, sensitivity analyses, estimand interpretation, generalisability.
- **Reviewer C — science-fair judge:** originality, student contribution, technical depth, question clarity, evidence quality, competition suitability, whether the project has a meaningful result if associations are weak or absent.

Each persona was asked to identify:

- fatal issues;
- major weaknesses;
- minor weaknesses;
- remediable issues;
- evidence needed;
- recommended response.

The audit deliberately looks for reasons the study should be reduced or paused, not reasons to proceed.

---

## 2. Reviewer A — freshwater ecologist

### 2.1 Overall judgement

“This is not really an ecological study. It is a comparison of two imperfect measurement systems, one of which (surface fluorescence) is not a measurement of cyanobacteria biomass at all. The ecological question — what controls cyanobacteria abundance — is not being asked. If the project is presented as ecology, it will overreach. If it is presented as a measurement audit, it can be honest but modest.”

### 2.2 Fatal issues

**A-F1 — The sensor is not a biomass measurement.** Chlorophyll and phycocyanin fluorescence are proxies whose relationship to biovolume depends on taxon, pigment content, physiology, light history, quenching, temperature and morphology. A rank association between a proxy and biomass is not a measurement of the proxy’s ecological meaning. **Verdict:** fatal only if the project claims validation, calibration or ecological inference. Remediable by framing as a measurement audit and prohibiting those claims.

**A-F2 — Mendota depth mismatch.** A 0.5 m sensor is compared with a 0–8 m integrated biovolume. Deep chlorophyll maxima, buoyant cyanobacteria and vertical heterogeneity can decouple the two. **Verdict:** potentially fatal for P1/P2 as a test of “surface fluorescence tracks cyanobacteria.” Remediable only by restricting the claim to “surface fluorescence vs integrated biovolume” and treating the depth difference as a bounded limitation. The reviewer may still consider it too weak.

**A-F3 — Buffalo Pound sensor non-detection.** Painter et al. (2022) already report that the autumn *Planktothrix* bloom was not detected by sensor or laboratory chlorophyll. If the proposed P3 asks whether sensor chlorophyll tracks cyanobacteria biomass, the prior evidence says the answer may be “poorly” for a biologically important taxon. **Verdict:** not fatal, but it undermines any expectation of a general positive association. Must be stated as prior context.

### 2.3 Major weaknesses

- **Taxonomic resolution and biomass derivation.** The biological endpoint is a derived wet-weight-equivalent biomass, not a direct measurement. The exact density, rounding and aggregation are unconfirmed. A change in taxonomy or counting can create apparent ecological change.
- **Detection-conditioned population.** Dates with a reported cyanobacteria row are not a random sample of the lake’s seasonal cycle. Low-biomass or non-bloom dates may be underrepresented, which can inflate or attenuate rank association.
- **Sampling representativeness.** A same-day microscopy sample is a point sample (Buffalo Pound 0.8 m) or an integrated sample (Mendota 0–8 m); the sensor is a different volume and time. Same date is not same water parcel.
- **Seasonal confounding.** Both fluorescence and cyanobacteria biomass rise in summer. A positive rank association may simply reflect season, not a useful proxy relationship.
- **Two-season Buffalo Pound.** Two seasons cannot support a generalisable association, and the 2019 anomaly shows how one date can dominate.
- **No independent ground truth.** Microscopy is independent of the sensor, but it is not a perfect reference. It has counting error, taxonomic uncertainty and detection limits.

### 2.4 Minor weaknesses

- The project uses “biovolume” for Mendota and “biomass” for Buffalo Pound; the terms are not interchangeable, and the report must not slip between them.
- The Mendota station blanks and depth metadata are unresolved.
- The Turner/YSI eras are different instruments; the report must not imply continuity.
- The project’s own governance language is dense; it can obscure the simple ecological question.

### 2.5 What would change the verdict

- A clear, single ecological question with a bounded measurement claim.
- A Mendota-only design with an explicit “surface vs integrated” framing.
- A reviewer-accepted justification for the depth mismatch, or a restriction to dates/depths where the mismatch is smallest.
- A demonstration that the detection-conditioned population does not exclude the low-biomass range.

### 2.6 Recommended response

1. Frame the study as a measurement-comparability audit, not ecology.
2. Make Mendota the core; treat Buffalo Pound as conditional.
3. State the depth mismatch and detection-conditioned population in every summary.
4. Do not claim validation, calibration, prediction or early warning.
5. Accept that a weak/absent association is a legitimate result.

---

## 3. Reviewer B — environmental statistician

### 3.1 Overall judgement

“The proposed statistic is simple, which is good, but the data are not simple. Date-level observations are serially dependent, seasonally structured, unevenly spaced and selected by QC. A descriptive Spearman rho with a leave-one-out range is not automatically honest; it can still mislead if the dependence and selection are not shown. The four estimands and nine sensitivities are a researcher-degree-of-freedom problem unless there is a pre-specified hierarchy.”

### 3.2 Fatal issues

**B-F1 — Detection-conditioned selection.** If the analysis includes only dates with a reported cyanobacteria row, the sample is selected by the biological endpoint. This can induce collider-like bias or restrict the range. **Verdict:** potentially fatal for a claim about the lake; remediable if the population is explicitly defined and the selection is described, or if the question is restricted to “among dates with microscopy.”

**B-F2 — Serial dependence and seasonal confounding.** Same-date observations are not independent; seasonal co-trending can produce a strong rho even if the sensor is a poor short-term proxy. A descriptive rho without seasonal stratification or a within-season check may be uninterpretable. **Verdict:** potentially fatal for a general “association” claim; remediable by seasonal stratification, within-season permutation/negative control, and explicit limitation.

**B-F3 — Multiplicity and researcher degrees of freedom.** Four estimands, nine sensitivities, multiple seasons, multiple eras and optional station subsets create many possible views. Without a pre-specified hierarchy and a rule for what counts as consistent, the presentation can look like result-shopping. **Verdict:** fatal for an inferential claim; remediable by a pre-specified primary/secondary hierarchy and a limited sensitivity set.

### 3.3 Major weaknesses

- **Small n.** Buffalo Pound has 42 dates across two seasons, before QC and matching; actual n may be much smaller. Mendota has 128/139 upper-bound same-day values, but the effective independent sample is smaller due to autocorrelation.
- **No minimum estimability rule.** The protocol defers the overall minimum n until after the count audit. That is honest, but it also means the analysis plan is incomplete.
- **No uncertainty language.** “Descriptive sensitivity range” is better than a confidence interval, but it can still be read as a uncertainty interval. The report must state what it is not.
- **Ties and zeros.** Cyanobacteria biomass may have many small values and ties; Spearman’s rho with ties is computable but the interpretation changes.
- **Measurement error on both axes.** Sensor error and microscopy error are both substantial; rank association is attenuated by both.
- **QC selection bias.** Excluding H/G/B7/negative/above-range values may select a non-random subset of dates, seasons or biomass levels. The sensitivity analyses may not recover the excluded population.
- **Influence diagnostics are not a substitute for dependence modelling.** Leave-one-year-out and leave-one-date-out show influence, not whether the association is stable or meaningful.
- **Four estimands are not independent.** P1/P2 share dates and endpoint; P3/P4 share dates and endpoint. Reporting them as four “estimates” can overstate the evidence.

### 3.4 Minor weaknesses

- The protocol does not specify tie handling or minimum distinct values.
- The ±1-day sensitivity is described as exploratory, but it may still be over-interpreted.
- The 2019-07-17 leverage plan is sensible but depends on D-05.
- The Mendota YSI era has very small n (21/22) and should not be presented as a parallel estimate.

### 3.5 What would change the verdict

- A pre-specified primary estimand and a limited secondary set.
- A minimum n and minimum distinct-value rule set before analysis.
- A seasonal stratification or within-season negative control.
- A clear statement that the rho is a descriptive summary of the included dates, not an estimate of a population parameter.
- A reviewer-accepted plan for QC selection bias.

### 3.6 Recommended response

1. Pre-specify P1/P2 as the core and P3/P4 as conditional exploratory appendices.
2. Set a minimum n and minimum distinct-value rule before the count audit.
3. Add a seasonal/within-season descriptive check, not just pooled rho.
4. Limit sensitivities to a justified set; report all, not the best.
5. State that the rho is not a validation, agreement or predictive statistic.
6. Consider Mendota-only if Buffalo Pound n or QC is inadequate.

---

## 4. Reviewer C — science-fair judge

### 4.1 Overall judgement

“The project is careful, well documented and scientifically honest. But a judge will ask: what did you discover? If the answer is ‘the sensor sometimes correlates with biomass, and we cannot validate it,’ that is a modest result. The governance trail is impressive, but it is not a substitute for a clear scientific question and a clear finding. The project risks looking like a data-management exercise rather than a piece of ecological research.”

### 4.2 Fatal issues

**C-F1 — No clear discovery narrative.** The project’s originality is low–moderate; the core association is established. If the entry depends on “we found a new sensor relationship,” it will fail. **Verdict:** fatal for a novelty-based entry; remediable by framing the contribution as a measurement audit with a negative/weak-result possibility.

**C-F2 — Student contribution unclear.** The project uses public data, external datasets, AI-assisted documentation and possibly supervisor input. If the student cannot clearly explain what they did, the entry risks plagiarism/ownership concerns. **Verdict:** potentially fatal for competition eligibility; remediable by a clear contribution statement and acknowledgement.

### 4.3 Major weaknesses

- **Complexity.** The governance/QC trail is too detailed for a short poster; the audience may lose the question.
- **Weak visual story.** “Rank association between RFU and biovolume” is not inherently gripping; the poster needs a clear before/after or “what the sensor sees vs what the microscope sees” visual.
- **Null-result risk.** A weak or absent association is legitimate but harder to present; the project must explain why the question is still worth asking.
- **Two-lake asymmetry.** The Buffalo Pound story is more complicated and less resolved than Mendota; it may weaken the narrative.
- **No new data.** The project reuses existing data; that is acceptable, but the student must show genuine analysis/interpretation, not just data wrangling.
- **Competition rules.** Eligibility, venue, report book, display, plagiarism, external supervision and media release must be handled; D-14 is unresolved.

### 4.4 Minor weaknesses

- The title “EcoSentinel” suggests a monitoring system/AI, but the study is a descriptive audit; the title may overpromise.
- The project’s claims matrix is strong, but the poster may not reflect it.
- The report book may be too long; the judge needs a clear one-page summary.

### 4.5 What would change the verdict

- A single, vivid question and a clear result (even a negative one).
- A simple visual explanation of RFU, biovolume and depth mismatch.
- A contribution statement that distinguishes student work from dataset authors’ work and AI assistance.
- A Mendota-core narrative with Buffalo Pound as a contrast, not a second validation.
- A completed licence/competition review.

### 4.6 Recommended response

1. Simplify the public question to one sentence.
2. Build the poster around one visual: “what the sensor sees” vs “what the microscope sees.”
3. State the contribution plainly: measurement audit, not validation/EWS.
4. Put governance/QC detail in the report book, not the poster.
5. Document the student’s contribution and external supervision.
6. Complete D-14 before any public display.

---

## 5. Consolidated issue register

| ID | Issue | Reviewer | Severity | Fatal? | Remediable? | Evidence needed | Response |
|---|---|---|---|---|---|---|---|
| A-F1 | Sensor is not a biomass measurement | A | Major | Only if validation claimed | Yes | Claims matrix; reviewer acceptance | Frame as measurement audit; prohibit validation |
| A-F2 | Mendota depth mismatch | A | Major | Potentially for P1/P2 | Partly | Station/depth metadata; reviewer judgement | Restrict claim; bounded limitation; Mendota-only option |
| A-F3 | Buffalo Pound sensor non-detection | A | Major | No | Yes | Painter 2022; prior context | State prior evidence; no positive-association assumption |
| B-F1 | Detection-conditioned selection | B | Major | Potentially | Yes | Population definition; selection description | Define population; describe selection; reviewer acceptance |
| B-F2 | Serial dependence/seasonal confounding | B | Major | Potentially | Yes | Seasonal stratification/negative control | Add descriptive seasonal check; limit claims |
| B-F3 | Multiplicity/degrees of freedom | B | Major | For inference | Yes | Pre-specified hierarchy | P1/P2 core; P3/P4 conditional; limited sensitivities |
| C-F1 | Low originality | C | Major | For novelty entry | Yes | Prior-art review | Reframe as measurement audit; no novelty claim |
| C-F2 | Student contribution unclear | C | Major | For competition | Yes | Contribution statement | Document student work; acknowledge supervision/AI |
| A-M1 | Taxonomy/biomass derivation | A | Major | No | Partly | Custodian evidence | P3/P4 exploratory; state derivation |
| A-M2 | Sampling representativeness | A | Major | No | Partly | Sample times/coverage | State same-date ≠ same parcel; BP daytime sensitivity |
| B-M1 | Small n | B | Major | For BP | Partly | Count audit | Minimum n; Mendota-only fallback |
| B-M2 | QC selection bias | B | Major | Potentially | Partly | Custodian evidence; sensitivity | Conservative population; report exclusions |
| C-M1 | Complexity/presentation | C | Minor | No | Yes | None | Simplify poster; report book detail |
| C-M2 | Null-result framing | C | Minor | No | Yes | None | Explain why question matters |
| C-M3 | Title overpromise | C | Minor | No | Yes | None | Consider subtitle/reframing |

---

## 6. What the adversarial audit changes

The audit does **not** change the governance status. It changes the recommended emphasis:

1. **Do not present the study as ecology or validation.** Present it as a measurement-comparability audit.
2. **Make Mendota the core; Buffalo Pound conditional.** The two-lake symmetry is not defensible while P3/P4 provenance is unresolved.
3. **Pre-specify the estimand hierarchy and minimum n.** Four equal-status estimands invite multiplicity criticism.
4. **Add a seasonal/within-season descriptive check.** A pooled rho alone is vulnerable to seasonal confounding.
5. **Simplify the competition narrative.** One question, one visual, one honest result.
6. **State the student contribution and AI/supervision role.** This is both a competition and integrity requirement.

---

## 7. Verdict

The design survives adversarial review **only as a reduced, exploratory measurement audit**. It does not survive as:

- a validation or calibration study;
- an early-warning study;
- a four-estimand equal-status primary analysis;
- a claim of ecological discovery;
- a competition entry built on novelty.

The strongest defensible version is:

> **Mendota-core, same-date, descriptive rank audit of surface fluorescence versus integrated cyanobacteria biovolume, with Buffalo Pound as a conditional exploratory contrast and a genuine possibility of a null result.**

That is not a spectacular study. It is an honest one. The project owner must decide whether that is enough for the project’s goals.

**No analysis was performed. No decision was approved.**
