# Sprint 4L.14 Review Addendum

**Addendum to:** `research/evidence/sprint_4l14_protocol_revision/REVISED_PROTOCOL.md` and the 4L.14 package  
**Status:** PROPOSED ADDENDUM — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Date:** 2026-11-25

> **This addendum does not modify the 4L.14 protocol in place.** It records proposed amendments for human review, responds to the independent review findings, and distinguishes document-level resolution from scientific resolution. No analysis is authorised. All 15 decisions remain outstanding.

---

## 1. Purpose and verdict

The independent 4L.14 review returned **ACCEPT AFTER REVISIONS**. This addendum responds to every finding in `FINDINGS_AND_SEVERITY_REGISTER.md` (F-01–F-13), the ten revision recommendations, and the review’s scientific-value concerns.

### Verdict

- **The addendum is ready for qualified human review.**
- **The protocol is not ready for approval.** Several mandatory items require data-custodian, statistical, scientific, or licence input.
- **Stage 1 remains scientifically defensible only as a modest exploratory measurement audit.** It is not an early-warning validation, sensor validation, calibration, or agreement study.
- **P3/P4 remain exploratory only.** The duplicate-row and biomass-provenance issues are not resolved by this addendum.
- **All 15 decisions remain OUTSTANDING.**

### Status key

| Status | Meaning |
|---|---|
| **Resolved in addendum** | The document-level issue is corrected; no further evidence is required for the wording/rule itself. |
| **Partially resolved** | The addendum defines the correct treatment or suspends the unsupported rule, but external evidence or a human decision is still required. |
| **Unresolved** | The issue cannot be settled without source documentation, data-custodian input, or a new decision. |

### Finding status summary

| Finding | Severity | Addendum status | Mandatory before approval? |
|---|---|---|---|
| F-01 daily coverage rule | MAJOR | **Partially resolved** — fixed 72/144 rule withdrawn; replacement needs custodian | Yes |
| F-02 duplicate/replicate semantics | MAJOR | **Unresolved** — P3/P4 exploratory only | Yes |
| F-03 taxon absence vs zero | MAJOR | **Partially resolved** — detection-conditioned population defined; source semantics unresolved | Yes |
| F-04 same-date is not synchronous | MAJOR | **Resolved in addendum** — terminology and claims corrected | No (wording) |
| F-05 fluorescence QC thresholds | MAJOR | **Partially resolved** — unsupported bounds/flags suspended; source documentation required | Yes |
| F-06 depth/station/ecological interpretation | MAJOR | **Resolved in framing; partially resolved on station rule** | Yes for station rule |
| F-07 season/era wording | MODERATE | **Resolved in addendum** — era claim limited to Mendota | No (wording) |
| F-08 block bootstrap | MODERATE | **Resolved in addendum** — removed entirely | No (wording) |
| F-09 biomass source access/formula | MODERATE | **Partially resolved** — source correction and paper citation; exact multiplier/replicates unresolved | Yes |
| F-10 prior art/originality | MODERATE | **Resolved in narrative** — Painter 2022 direct overlap added; D-13 remains | D-13 |
| F-11 multiplicity/selection | MODERATE | **Resolved in reporting rule** — all four equal-status exploratory | No (wording) |
| F-12 leverage terminology | MINOR | **Resolved in addendum** — “rank extremeness/influence” | No |
| F-13 traceability overstatement | MINOR | **Resolved by this addendum** — document vs scientific completion separated | No |

### Mandatory pre-approval checklist

The following must be completed before the protocol can be approved:

1. **F-01:** data custodian approves a date-specific coverage rule, or P3/P4 remain descriptive only.
2. **F-02:** data custodian resolves duplicate/replicate semantics, or P3/P4 remain exploratory only.
3. **F-03:** source semantics for no-cyanobacteria dates are documented, or the detection-conditioned population is explicitly accepted.
4. **F-05:** fluorescence QC rules are tied to documented instrument ranges/flags; unsupported values remain unresolved and sensitivity-only.
5. **F-06:** the Mendota station rule is reviewed and accepted.
6. **F-09:** Buffalo Pound biomass provenance is confirmed, or P3/P4 remain exploratory only.
7. **D-14:** licence/competition review is completed.
8. **Addendum re-review:** the scientific, statistical, data-custodian and licence reviewers accept this addendum and the unchanged 4L.14 protocol as amended.

---

## 2. Finding-by-finding response

### F-01 — The 50% daily coverage rule is arbitrary

**Finding.** The rule “≥72 of 144 expected 10-minute values and at least one record in each half-day” assumes a 144-record day and a representative daily mean. Buffalo Pound daily counts vary (2018: 121–144; 2019: 42–131), so 144 is not a universal denominator. A 50% day can be mostly one unusual interval; one record per half is weak. Coverage selection may correlate with maintenance, fouling, weather, or high biomass.

**Addendum response.** The fixed 72/144 rule is **withdrawn from primary eligibility**. It cannot be replaced by another arbitrary percentage without date-specific evidence. P3/P4 are suspended from primary status until the data custodian documents:

- the expected logger cadence by date/deployment;
- deployment start/end and time zone;
- duplicate timestamps and missing intervals;
- within-day distribution and exposure duration;
- whether a daily mean is representative of the biological sample day.

**Proposed amendment (not applied).**

> **Buffalo Pound daily-summary eligibility (proposed).** A date-level sensor mean may enter a primary analysis only if the data custodian has approved a date-specific expected-cadence rule and the count audit reports exposure duration, number of valid records, and within-day distribution. Until that rule is approved, Buffalo Pound sensor summaries are reported descriptively only, with exposure duration and record counts; no primary P3/P4 association is estimated. The fixed 72/144 rule is withdrawn.

**Residual uncertainty.** The correct coverage rule is unknown. A date-specific rule may still select non-random days; the count audit must report included-vs-excluded biological distributions, but cannot prove missing-at-random.

**Mandatory before approval?** **Yes.** Data custodian.

---

### F-02 — Duplicate date × species rows define different endpoints

**Finding.** 2018 has 19 date–species groups with two rows and no replicate identifier; 2019 has `REP1`/`REP2` on disjoint dates. Mean-before-sum assumes replicates; sum assumes separate counts; first-row assumes a selected record. These are different ecological quantities, not interchangeable sensitivities.

**Addendum response.** The addendum does **not** choose an aggregation. It removes mean-before-sum as a primary rule for P3/P4. P3/P4 remain exploratory only. If the custodian cannot resolve the semantics, Buffalo Pound cannot supply a primary endpoint.

**Proposed amendment (not applied).**

> **Buffalo Pound replicate rule (proposed).** Mean-before-sum is not accepted as a primary endpoint. Until the source custodian documents whether duplicate date–species rows are technical replicates, split samples, separate subsamples, or distinct records, P3/P4 are exploratory only. Exploratory displays may show mean, sum, and first-row as three separately labelled endpoint definitions; they must not be presented as robustness checks of one endpoint. If the semantics cannot be resolved, Buffalo Pound is excluded from primary analysis.

**Residual uncertainty.** Source semantics; whether `REP1`/`REP2` identify samples, observers, replicates, or something else.

**Mandatory before approval?** **Yes.** Data custodian.

---

### F-03 — No cyanobacteria row does not mean zero

**Finding.** The protocol requires at least one cyanobacteria row, but the meaning of a sampled date with no such row is unresolved: true zero, no detection, taxonomic omission, not reported, or missing biology. Requiring a row conditions the sample on detected/reported cyanobacteria and may remove low/absent dates, changing the target population.

**Addendum response.** The addendum defines the primary population explicitly as **detection-conditioned**: dates with a reported cyanobacteria row. It does not treat absence as zero. It requires reporting the number and dates of no-row samples and prohibits zero/non-detection claims unless the source confirms them.

**Proposed amendment (not applied).**

> **Biological target population (proposed).** The primary Mendota and Buffalo Pound populations are dates with a reported cyanobacteria row and a valid endpoint. A sampled date with no cyanobacteria row is **not** treated as zero; it is reported separately as “no reported cyanobacteria.” The analysis is explicitly detection-conditioned. If the source custodian confirms that an empty row means a true zero/non-detection, a sensitivity analysis including zeros may be added; otherwise no zero-inclusive claim is permitted.

**Residual uncertainty.** Source semantics for empty dates; whether low/absent dates are systematically missing.

**Mandatory before approval?** **Yes.** Data custodian/scientific reviewer.

---

### F-04 — Same date is not synchronous

**Finding.** A date-only biological sample and a daily sensor summary may represent different times and water parcels. “Same-day” can be over-read as paired/synchronized validation.

**Addendum response.** Terminology is corrected throughout: **same-calendar-date co-occurrence**, not “paired,” “synchronized,” or “validation.” The addendum adds a mandatory limitation statement to every result.

**Proposed amendment (not applied).**

> **Terminology (proposed).** Replace “same-day paired observations” with “same-calendar-date co-occurrences.” A co-occurrence means only that the biological sample and sensor summary share a calendar date. It does not mean same time, same water parcel, or synchronized measurement. No result may be described as paired, simultaneous, or validated.

**Residual uncertainty.** None for wording; the scientific limitation remains.

**Mandatory before approval?** **No** (document-level), but the limitation is mandatory in every report.

---

### F-05 — Fluorescence QC thresholds are not scientifically validated

**Finding.** `C/E/G/O/H` handling is explicit but not fully evidence-based. `H` retention within broad bounds is not a quality validation; negative RFU as an ordinary rank assumes below-baseline ordering has biological meaning; Buffalo Pound >100 RFU may be saturated; undocumented flags and missing values remain.

**Addendum response.** The addendum separates **documented** from **unresolved** rules. Unsupported bounds are not called “physical/analytical.” Negative and above-range values are retained only as flagged observations with exclusion sensitivities; they are not interpreted as concentration or zero biomass. P1/P2 remain conditional; P3/P4 remain exploratory.

**Proposed amendment (not applied).**

> **Fluorescence QC (proposed).** (1) A flag is excluded from primary when the provider documents that it denotes sensor-off, malfunction, fouling, or another invalid condition. (2) `H` values are retained only if they fall within a documented instrument range; if the range is unknown, `H` is `UNRESOLVED_RANGE` and excluded from primary, with a sensitivity including numeric values. (3) Negative RFU is flagged `BELOW_BASELINE` and retained only in a sensitivity; it is not interpreted as zero or low biomass. (4) Buffalo Pound values above the documented 0–100 RFU range are `ABOVE_RANGE` and excluded from primary, with a sensitivity including them. (5) Undocumented flags are `UNRESOLVED_FLAG` and excluded from primary, with a sensitivity including numeric values where defined. (6) The QC system defines an **analysis population**, not “clean” or “true” measurements.

**Residual uncertainty.** Instrument-specific meaning of negative/above-range values; whether 0–100 is an operating range or a display scale; missingness mechanisms.

**Mandatory before approval?** **Yes.** Data custodian + statistical reviewer.

---

### F-06 — Depth, station, and ecological interpretation

**Finding.** Mendota has a 0.5 m sensor versus a 0–8 m composite, ~106 m offset, and 371/402 dates with blank station. Buffalo Pound is depth-aligned but two seasons. The lakes differ in many linked dimensions; depth is not identifiable. The station fallback (station 1 if present, otherwise blank) is deterministic but not neutral.

**Addendum response.** The two-case-study framing is retained and strengthened. No depth-effect claim. The station rule is changed: primary includes all eligible Mendota dates regardless of station, with station status reported; sensitivity restricts to station 1 and to blank. This avoids silently treating station-coded dates as the primary sample.

**Proposed amendment (not applied).**

> **Mendota station rule (proposed).** The primary population includes all eligible Mendota dates with `depth_range = 0-8m`, regardless of station value. Station status (`1`, blank, other) is reported descriptively. Sensitivity analyses restrict to station 1 and to blank-station dates. No station is treated as the default sampling location. The comparison remains two separate case studies; no depth, station, or lake effect is identified.

**Residual uncertainty.** Whether station-coded and blank dates represent the same location/composition; source documentation may resolve.

**Mandatory before approval?** **Yes** for the station rule; scientific reviewer + data custodian.

---

### F-07 — “Across seasons and sensor eras” overstates Buffalo Pound

**Finding.** Buffalo Pound has one documented YSI era across 2018–2019; only Mendota has Turner/YSI eras. Seasonal strata may be sparse and confounded by year.

**Addendum response.** The question is revised to limit sensor-era language to Mendota and to label all seasonal/era summaries as descriptive.

**Proposed amendment (not applied).**

> **Revised question (proposed).** “In Lake Mendota (2006–2020) and Buffalo Pound Lake (2018–2019), among same-calendar-date co-occurrences and analysed as two separate lake-specific case studies, what are the direction and magnitude of the rank association between surface chlorophyll and phycocyanin fluorescence and independent microscopy-derived cyanobacteria biovolume (Mendota) or cyanobacteria biomass (Buffalo Pound), and how do these associations differ descriptively across seasonal strata, with Mendota’s Turner and YSI eras analysed separately?”

**Residual uncertainty.** Seasonal strata may be too sparse; report n and points, no stratum ρ if n < 10.

**Mandatory before approval?** **No** (wording), but the revised wording must replace the 4L.14 wording in the approved protocol.

---

### F-08 — The optional block bootstrap is not justified

**Finding.** The 2,000-resample season-year block bootstrap lacks a defined target, exchangeability assumptions, sparse-block rules, and a valid-resample justification. Percentiles may look like confidence intervals.

**Addendum response.** The optional block bootstrap is **removed entirely**. Retain leave-one-year-out (Mendota) and leave-one-date-out (Buffalo Pound) as influence diagnostics only. No percentiles, no confidence intervals, no p-values.

**Proposed amendment (not applied).**

> **Uncertainty (proposed).** Mendota: ρ, n, and the full leave-one-year-out set (not only min/max), labelled an influence diagnostic. Buffalo Pound: ρ, n, separate 2018/2019 estimates, and leave-one-date-out influence values, with the statement that two seasons cannot support a reliable interval. No bootstrap, no percentile interval, no confidence interval, no p-values.

**Residual uncertainty.** Influence diagnostics do not quantify sampling uncertainty. That limitation must be stated.

**Mandatory before approval?** **No** (wording), but statistical reviewer must accept the replacement.

---

### F-09 — Biomass source access and exact derivation

**Finding.** 4L.14 stated the Painter full text was inaccessible; the independent review accessed the publisher article. The article verifies microscopy, species identification, cell counts, and shape-based cell-volume conversion to wet-weight biomass, but does not state the exact universal density multiplier or explain duplicate rows. The arithmetic is consistent with a 1 g/cm³ assumption but does not prove the exact field provenance.

**Addendum response.** Correct the stale access claim; cite the article methods; distinguish **broad derivation verified** from **exact multiplier/replicates unresolved**. P3/P4 remain exploratory. Do not describe the conversion as fully verified.

**Proposed amendment (not applied).**

> **Buffalo Pound endpoint (proposed).** `Biomass_mg_m3` is a microscopy-derived wet-weight-equivalent quantity. Painter et al. (2022) describes species-level inverted microscopy, cell-volume measurement, and shape-specific geometric conversion to wet-weight biomass. The local arithmetic is consistent with `Cell_Volume_um3 × Cell_Density_L × 10^-6` under a 1 g cm⁻³ assumption, but the exact universal multiplier, density treatment, and duplicate-row semantics are not verified from the accessible text. P3/P4 remain exploratory until the data custodian confirms the field provenance and aggregation. The endpoint is not biovolume, not dry mass, not carbon biomass, and not numerically equivalent to Mendota biovolume.

**Residual uncertainty.** Exact density factor, rounding chain, replicate semantics, detection limits.

**Mandatory before approval?** **Yes** for P3/P4; data custodian.

---

### F-10 — Prior art and originality

**Finding.** The review found directly relevant primary studies and a critical Buffalo Pound result: Painter et al. (2022) already compares cyanobacterial taxon biomass with laboratory chlorophyll and shows taxon/phase-dependent relationships, including an autumn *Planktothrix* phase poorly indicated by chlorophyll. The project’s local RFU reanalysis can be distinct, but must state the overlap.

**Addendum response.** Add Painter 2022 as direct prior art; add the chlorophyll/*Planktothrix* caveat; retain low–moderate originality. D-13 remains the decision.

**Proposed amendment (not applied).**

> **Prior-art statement (proposed).** Painter et al. (2022) already paired microscopy cyanobacteria biomass with laboratory chlorophyll in Buffalo Pound 2018–2019 and reported taxon- and phase-dependent relationships, including a *Planktothrix* phase not tracked by chlorophyll. EcoSentinel’s question is narrower and different — in-situ YSI chlorophyll/phycocyanin RFU versus total cyanobacteria biomass at date level — but it is a local reanalysis, not a new method or validation. Originality is low–moderate.

**Residual uncertainty.** Whether the competition framing accepts a modest local reanalysis (D-13).

**Mandatory before approval?** **D-13.**

---

### F-11 — Four estimates and multiplicity

**Finding.** P1/P2 share the Mendota endpoint/dates; P3/P4 share the Buffalo Pound endpoint/dates. Four “primary” estimates plus seasonal/QC sensitivities create selective-reporting risk even without p-values.

**Addendum response.** Label all four as **equal-status exploratory estimates**, report all, and prohibit a “winner” or “best sensor” selection. P1/P2 and P3/P4 are not independent confirmations.

**Proposed amendment (not applied).**

> **Reporting rule (proposed).** P1–P4 are four paired proxy/endpoint questions, not four independent confirmations. All four are reported with n and descriptive sensitivity ranges. No estimate is selected as the “best” or “primary” result after seeing the data. P1/P2 and P3/P4 are explicitly described as sharing biological dates/endpoints. Seasonal and QC sensitivities are reported in full, not only when favourable.

**Residual uncertainty.** None for the rule; the scientific limitation remains.

**Mandatory before approval?** **No** (wording), but statistical reviewer must accept.

---

### F-12 — “Leverage” is regression terminology

**Finding.** “Rank/leverage” mixes Spearman rank position with regression leverage.

**Addendum response.** Replace with **rank extremeness** and **influence on ρ**. Report rank position on each variable, full vs leave-one-date-out ρ, exact Δρ, and whether sign/interpretation changes. No cutoff.

**Proposed amendment (not applied).**

> **2019-07-17 report (proposed).** Report the date’s rank extremeness on each variable, its influence on ρ (full vs leave-one-date-out), exact Δρ, and whether the sign or interpretation changes. Do not call this “leverage.” Do not correct or remove the value solely because it changes the association.

**Residual uncertainty.** Cause of the anomaly remains unresolved.

**Mandatory before approval?** **No** (wording).

---

### F-13 — Traceability overstates scientific resolution

**Finding.** The 4L.14 handover marks revisions “fully addressed” while key evidence rules remain unresolved, which may lead reviewers to read the specification as validation.

**Addendum response.** This addendum explicitly separates **document completion** from **scientific resolution**. It preserves 4L.14 as history and does not overwrite it. It adds a status key and a mandatory-revision list.

**Proposed amendment (not applied).**

> **Status statement (proposed).** “Addressed in the addendum” means the document now states the correct treatment or suspends an unsupported rule. It does not mean the underlying scientific question is resolved. Items marked partially resolved or unresolved require the named reviewer/custodian before approval.

**Residual uncertainty.** None.

**Mandatory before approval?** **No** (document-level).

---

## 3. Response to the ten review recommendations

| Recommendation | Addendum response | Status |
|---|---|---|
| 1. Biology record semantics | F-03 defines detection-conditioned population; source confirmation required | Partially resolved |
| 2. Buffalo Pound duplicates | F-02 suspends mean-before-sum; P3/P4 exploratory | Unresolved |
| 3. Coverage | F-01 withdraws fixed 72/144; date-specific rule required | Partially resolved |
| 4. Fluorescence QC | F-05 separates documented/unresolved; negative/above-range sensitivities | Partially resolved |
| 5. Mendota station/depth | F-06 changes station rule; depth limitation retained | Resolved in framing; station rule for review |
| 6. Question wording | F-07 limits era language to Mendota | Resolved in wording |
| 7. Uncertainty | F-08 removes block bootstrap; LOYO/leave-date only | Resolved in wording |
| 8. Prior art/biomass | F-09/F-10 correct source and add Painter overlap | Partially resolved |
| 9. Scope/student story | Sections 4–6; Stage 1 is not EWS | Resolved in narrative |
| 10. Governance | All decisions remain open; no approval | Preserved |

---

## 4. Is the narrowed study scientifically defensible?

**Yes, conditionally, as a modest exploratory measurement audit.**

It is defensible if:

- the question is described as same-calendar-date rank association, not agreement/validation;
- the target population is explicitly detection-conditioned;
- P3/P4 remain exploratory until duplicate/biomass issues are resolved;
- the fixed coverage rule is withdrawn and replaced only with custodian-approved date-specific rules;
- negative/above-range RFU are treated as unresolved, not as biological zeros;
- the station rule does not silently select one location;
- all four estimates are reported as equal-status exploratory;
- no depth, lake, sensor, or calibration effect is claimed;
- the limitations are stated in every result.

It is **not** defensible if:

- P3/P4 are treated as primary without duplicate resolution;
- a rank association is called validation, agreement, or calibration;
- `H`, negative, or above-range values are treated as validated measurements;
- the fixed 72/144 rule is retained without date-specific evidence;
- the station fallback is treated as a neutral sampling design;
- the two lakes are pooled or used to identify a depth effect;
- the result is framed as early warning.

**Scientific value:** modest. The study can produce a useful local negative/limited result and a transparent data-quality audit. It is not a new method, a sensor validation, or a general cross-lake finding.

---

## 5. Reconciliation with the Sprint 4L.15 criticism

No Sprint 4L.15 package exists in the repository, and no externally supplied 4L.15 report file was provided in the workspace. The field-study proposal is known only from the task brief; it is an external proposal, not verified project state.

Its substance is assessed in `FIELD_STUDY_ROLE_ASSESSMENT.md`:

- It would test a **calibration/community-composition** question, not early warning.
- It is scientifically coherent but incremental relative to Bastien, Cotterill, Thomson-Laing, Ma, and Painter.
- It requires a field season, sonar/sonde, microscopy lab, taxonomist, permits, and supervision.
- A summer 2027 field season cannot produce results before the April–May 2027 SciFest fairs.
- It could be a Stage 1b add-on only if fully resourced and tightly scoped, or a future-year project.

**Conclusion:** The field study does not resolve the 4L.14 findings and does not replace Stage 1. It is not adopted as the primary project.

---

## 6. Claims the project must not make

### Prohibited

- validation, accuracy, calibration, or agreement;
- sensor validation or “the sensor measures biomass”;
- prediction, forecast, early warning, lead time;
- bloom detection, bloom/non-bloom classification, toxicity;
- whole-water-column biomass;
- Turner/YSI interchangeability;
- causal depth, station, lake, or sensor-era effect;
- generalisation to other lakes;
- “the two lakes validate each other”;
- “the result shows phycocyanin is a reliable proxy”;
- “the result is robust” based on a sensitivity that changes the endpoint definition.

### Permitted

- “In the included dates, [pigment] showed a [direction] rank association with [endpoint] (Spearman ρ = ..., n = ...).”
- “The descriptive pattern was [similar/different] across seasonal strata, with [n] and [confounders].”
- “The two cases differ in depth alignment, but also in lake, instrument, period, community, sampling, QC, and endpoint; the comparison cannot isolate depth.”
- “The result is a same-calendar-date association, not agreement or validation.”
- “P3/P4 are exploratory because the Buffalo Pound replicate and biomass provenance are unresolved.”

### Mandatory limitations in every report

- date-only biology; no sample times;
- sensor daily summary vs unknown sample time;
- Mendota 0.5 m vs 0–8 m; Buffalo Pound 0.82 m vs 0.8 m;
- Turner/YSI non-comparability;
- biovolume vs biomass non-equivalence;
- detection-conditioned population;
- taxonomy/detection-limit limitations;
- two-season Buffalo Pound;
- no calibration/detection limits;
- no labels/events/early warning.

---

## 7. Remaining human decisions and reviewers

All D-01–D-15 remain **OUTSTANDING**. The addendum does not approve any.

### Decisions that can be considered now

| Decision | Why now | Reviewer |
|---|---|---|
| D-01 comparability | Wording is mature; rank association only | Scientific + statistical |
| D-02 Buffalo Pound endpoint | Evidence corrected; P3/P4 exploratory proposed | Data custodian + scientific |
| D-03 Mendota depth | No correction; limitation clear | Scientific + data custodian |
| D-04 Turner/YSI | Separation is clear | Data custodian + statistical |
| D-05 QC | Decision tree proposed; unresolved values flagged | Data custodian + statistical |
| D-06 daily summary | Asymmetry documented | Scientific + statistical |
| D-07 temporal window | Same-date + ±1 exploratory | Scientific + statistical |
| D-08 replicates | Cannot be decided without custodian | Data custodian |
| D-09 2019-07-17 | Retain/flag/rank-extremeness plan | Data custodian + scientific |
| D-10 uncertainty | No bootstrap; influence only | Statistical |
| D-11 small-n | Overall minimum after count audit | Statistical |
| D-12 claims | Updated matrix | Scientific + Gate 2 |
| D-13 originality | Stage 1 modest; proceed/pause | Project lead + scientific + Gate 2 |
| D-14 licence | CC BY-NC-SA review | Licence/competition |
| D-15 analysis | **Do not approve yet** | All approvers |

### Decisions that are not ready

- **D-08** and **P3/P4 primary status** require the data custodian’s duplicate/biomass evidence.
- **D-11** requires the count audit, which itself requires separate authorisation.
- **D-15** requires D-01–D-14 recorded and the addendum re-reviewed.

### Required reviewers

- **Scientific reviewer:** question, estimands, endpoints, two-case framing, claims.
- **Statistical reviewer:** Spearman, dependence, influence diagnostics, n rule, no p-values.
- **Data custodian:** coverage, duplicates, biomass provenance, QC, station semantics.
- **Gate 2 governance:** Option C, no labels/models, scope.
- **Licence/competition reviewer:** CC BY-NC-SA and competition use.
- **Project lead:** D-13 continuation/pause.
- **All approvers:** D-15.

---

## 8. Addendum readiness

| Question | Answer |
|---|---|
| Does the addendum address every F-01–F-13 finding? | **Yes**, with explicit status. |
| Does it distinguish resolved/partial/unresolved? | **Yes.** |
| Does it identify mandatory pre-approval revisions? | **Yes** (F-01, F-02, F-03, F-05, F-06 station rule, F-09). |
| Does it preserve the 4L.14 protocol? | **Yes** — no in-place edits; proposed amendments only. |
| Is the narrowed study defensible? | **Conditionally**, as a modest exploratory measurement audit. |
| Is it ready for human review? | **Yes.** |
| Is it ready for approval? | **No.** |
| Are any decisions approved? | **No.** |

**Addendum verdict: READY FOR QUALIFIED HUMAN REVIEW — NOT APPROVED.**
