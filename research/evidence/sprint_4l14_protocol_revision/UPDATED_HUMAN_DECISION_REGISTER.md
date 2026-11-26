# Updated Human Decision Register

**Sprint:** 4L.14  
**Status:** PROPOSED — NOT APPROVED  
**Supersedes:** Sprint 4L.12 decision table for review purposes  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Date:** 2026-11-24

> **No decision in this register is approved. All 15 decisions remain OUTSTANDING. This register preserves the original IDs and wording, records the revised proposal and evidence, and identifies the responsible reviewer. Approval status is NOT APPROVED for every decision.**

## 1. Approval separation

| Approval | Scope | Cannot substitute for |
|---|---|---|
| Scientific reviewer | Question, estimands, endpoints, inclusion, claims | Statistical, data custodian, governance, licence |
| Statistical reviewer | Spearman, dependence, sensitivity ranges, n rules | Scientific, data custodian, governance, licence |
| Data custodian | QC, missingness, anomalies, replicate handling, biomass derivation | Scientific, statistical, governance, licence |
| Gate 2 governance | Option C status, no labels/models, scope | Scientific, statistical, data custodian, licence |
| Licence/competition review | CC BY-NC-SA, attribution, share-alike, competition use | Scientific, statistical, data custodian, governance |
| D-13 continuation/pause | Whether the study is worth doing | D-15 authorisation |
| D-15 authorisation | Explicit go-ahead to begin analysis | Any of the above |

## 2. Decision-by-decision register

### D-01 — Operational definition of “comparability”

**Original wording (4L.12):**
> Operational definition of “comparability” | (a) rank association + relative concordance; (b) absolute agreement; (c) predictive performance

**Revised proposal:**
> (a) **rank association only** (direction and magnitude of Spearman’s ρ). Remove “relative concordance” from the operational definition and from the primary/secondary estimands. If a directional check is later desired, it must be formally defined, justified, and labelled exploratory.

**Evidence:**
- RFU and biovolume/biomass are different quantities/scales.
- No Turner/YSI cross-calibration; no RFU-to-biomass conversion.
- Absolute agreement and predictive performance are not estimable.
- “Relative concordance” was under-defined and added little beyond Spearman (4L.13).

**Remaining uncertainty:** Whether the team wants any directional-change descriptive statistic. It is not required for the primary question.

**Recommended human decision:** Adopt the revised (a).

**Responsible reviewer:** Scientific reviewer + statistical reviewer.

**Approval status:** **NOT APPROVED — OUTSTANDING.**

**Estimand impact:** P1–P4 unchanged as rank associations; removes an ambiguous secondary concept.

---

### D-02 — Buffalo Pound endpoint

**Original wording (4L.12):**
> Buffalo Pound endpoint | (a) supplied biomass; (b) derive biovolume from cell volume × density; (c) exclude Buffalo Pound

**Revised proposal:**
> (a) Use supplied `Biomass_mg_m3`, conditional on accepting the documented/verified derivation. Do not derive a new biovolume endpoint. **Until the data custodian verifies the derivation against the original publication/supplement, recommend downgrading P3/P4 to exploratory.** If verification succeeds, P3/P4 may be restored to primary subject to the count audit. If it fails or direct biovolume is required, P3/P4 are unsuitable and Buffalo Pound is excluded from primary analysis.

**Evidence:**
- The source supplies `Biomass_mg_m3`, `Cell_Density_L`, and `Cell_Volume_um3`, but no biovolume column.
- Arithmetic consistency check: 2018 all 817 positive rows, median ratio 1.000 × 10⁻⁶ (range 9.87 × 10⁻⁷–1.0366 × 10⁻⁶); 2019 all 405 positive rows, median 1.000 × 10⁻⁶ (range 9.55 × 10⁻⁷–1.0227 × 10⁻⁶).
- Consistent with `Biomass ≈ Cell_Volume × Cell_Density × 10⁻⁶` under 1 g cm⁻³.
- 2018/2019 use the same relationship.
- Full paper text was not accessible; local data dictionary does not state the formula/density assumption.

**Remaining uncertainty:** Density assumption; rounding; full methods text; replicate design; detection limits.

**Recommended human decision:** (a) conditional on data-custodian verification. Until then, **downgrade P3/P4 to exploratory**; do not treat them as primary.

**Responsible reviewer:** Data custodian + scientific reviewer.

**Approval status:** **NOT APPROVED — OUTSTANDING.**

**Estimand impact:** P3/P4 recommended downgrade to exploratory pending verification; unsuitable for primary if the derivation is rejected.

---

### D-03 — Mendota depth comparator

**Original wording (4L.12):**
> Mendota depth comparator | (a) 0.5 m vs 0–8 m, no correction; (b) attempt a depth correction; (c) exclude Mendota

**Revised proposal:**
> (a) 0.5 m vs 0–8 m, no correction, explicitly framed as a **depth-mismatched case-study limitation**, not a depth comparison. No depth correction; no whole-column claim.

**Evidence:**
- Sensor variables at 0.5 m; biology 0–8 m tube composite.
- No depth-resolved paired profiles at the buoy.
- No validated correction.
- ~105.7 m spatial offset; station metadata mostly blank.

**Remaining uncertainty:** How much of any association is due to depth/sample integration vs sensor performance. The design cannot separate them.

**Recommended human decision:** (a).

**Responsible reviewer:** Scientific reviewer + data custodian.

**Approval status:** **NOT APPROVED — OUTSTANDING.**

**Estimand impact:** P1/P2 remain suitable with caveats; no depth-effect claim.

---

### D-04 — Turner/YSI handling

**Original wording (4L.12):**
> Turner/YSI handling | (a) separate eras; (b) concatenate; (c) convert

**Revised proposal:**
> (a) Separate eras; never concatenate. 2019 transition year analysed separately by instrument; no averaging/choosing. No conversion.

**Evidence:**
- Both output RFU but differ by orders of magnitude.
- 2019 paired medians: Turner chlorophyll 1,354.74 vs YSI 0.39; Turner phycocyanin 802.01 vs YSI 0.59.
- No cross-calibration.
- EML: “significant magnitude differences.”

**Remaining uncertainty:** None for separation; YSI n is small.

**Recommended human decision:** (a).

**Responsible reviewer:** Data custodian + statistical reviewer.

**Approval status:** **NOT APPROVED — OUTSTANDING.**

**Estimand impact:** P1/P2 Turner primary; YSI secondary; no concatenation.

---

### D-05 — Primary QC rule

**Original wording (4L.12):**
> Primary QC rule | (a) retain H, exclude C/E/G/O; (b) strict unflagged; (c) include all numeric

**Revised proposal:**
> (a) revised with an exact decision tree:
> - `C/E/G/O`: exclude primary; sensitivity include numeric where defined.
> - `H`: retain primary if numeric, finite, non-negative/within broad bounds; strict sensitivity excludes all H.
> - Undocumented flags: `UNRESOLVED_FLAG`; exclude primary; sensitivity include numeric if within bounds.
> - Negative RFU: retain primary as observed; `SENS_NEG` excludes.
> - Buffalo Pound `B7`: exclude primary; `SENS_B7` includes.
> - Coverage: ≥50% and both halves; otherwise exclude primary; `SENS_COVERAGE`.
> - Missing: exclude; no imputation.

**Evidence:**
- `C` often has numeric values; `H` means outside standard range, not invalid.
- Turner chlorophyll 2014–2015 has many `C` flags.
- B7 is an interval fouling flag.
- Negative RFU can be baseline/noise; no blank threshold documented.
- 4L.13 found “plausible” non-operational and negative exclusion potentially biasing.

**Remaining uncertainty:** B7 overlap with high biomass; negative RFU counts in Buffalo Pound; exact effect on n.

**Recommended human decision:** (a) revised.

**Responsible reviewer:** Data custodian + statistical reviewer.

**Approval status:** **NOT APPROVED — OUTSTANDING.**

**Estimand impact:** All estimands; determines actual n and bias.

---

### D-06 — Primary daily summary

**Original wording (4L.12):**
> Primary daily summary | (a) full-day mean for both lakes; (b) nighttime for BP only; (c) daytime for both

**Revised proposal:**
> (a) full-day mean for both lakes; Buffalo Pound nighttime/daytime medians as sensitivity. State the asymmetry: Mendota provider daily mean (unknown within-day coverage) vs Buffalo Pound computed 10-minute mean (known coverage).

**Evidence:**
- Mendota daily file has no within-day counts; no nighttime reconstruction.
- Buffalo Pound 10-minute data allow nighttime/daytime summaries.
- Quenching can reduce chlorophyll up to 79% and PC up to 59%.

**Remaining uncertainty:** Diel bias cannot be removed from Mendota.

**Recommended human decision:** (a), with BP nighttime sensitivity.

**Responsible reviewer:** Scientific reviewer + statistical reviewer.

**Approval status:** **NOT APPROVED — OUTSTANDING.**

**Estimand impact:** All; Mendota P1/P2 include unknown diel quenching.

---

### D-07 — Temporal window

**Original wording (4L.12):**
> Temporal window | (a) same-day primary + ±1-day sensitivity; (b) ±3/±7/±14; (c) same-day only, no sensitivity

**Revised proposal:**
> (a) same-day primary + ±1-day **exploratory date-window co-occurrence** only. Do not use ±1-day as a robustness/agreement claim. No ±3/±7/±14. No lag/lead/onset.

**Evidence:**
- Date-only biology; ±1 day changes sample composition.
- Wider windows can span bloom phases.
- 4L.13 found ±1 ambiguous as a sensitivity.

**Remaining uncertainty:** Whether ±1-day is worth reporting at all.

**Recommended human decision:** (a) revised; consider dropping ±1-day if the reviewers want the cleanest design.

**Responsible reviewer:** Scientific reviewer + statistical reviewer.

**Approval status:** **NOT APPROVED — OUTSTANDING.**

**Estimand impact:** Primary P1–P4 unaffected; ±1-day exploratory only.

---

### D-08 — Buffalo Pound replicate handling

**Original wording (4L.12):**
> Buffalo Pound replicate handling | (a) mean before summing; (b) sum; (c) first row

**Revised proposal:**
> (a) mean before summing as an explicit **replicate assumption**; sum and first-row as sensitivity. Verify the source method; if duplicates are split samples rather than replicates, mean may be wrong.

**Evidence:**
- 2018: 19 date–species groups with two rows; no replicate ID.
- 2019: REP1/REP2 on disjoint dates; not paired.
- 1,222 taxon rows; 248 cyanophyte rows; not independent.

**Remaining uncertainty:** Whether duplicates are replicate counts or split samples.

**Recommended human decision:** (a), with sensitivity; data custodian to verify source method.

**Responsible reviewer:** Data custodian.

**Approval status:** **NOT APPROVED — OUTSTANDING.**

**Estimand impact:** P3/P4 totals.

---

### D-09 — 2019-07-17 anomaly

**Original wording (4L.12):**
> 2019-07-17 anomaly | (a) retain and flag, exclude in sensitivity; (b) exclude from primary; (c) correct

**Revised proposal:**
> (a) Retain and flag primary; exclude in sensitivity; **mandatory leverage report**: eligibility, rank/leverage, full vs leave-one-date-out ρ, exact Δρ, sign/interpretation change. No correction; no bloom/non-bloom interpretation.

**Evidence:**
- 45.81 mg m⁻³ total; 41.02 cyanobacteria; 9 rows all REP2.
- Neighbours 12,587.1 and 9,497.9.
- Taxonomy/group biomass agree; cause unresolved.
- At n=42, single date could dominate.

**Remaining uncertainty:** Cause; whether result depends on it.

**Recommended human decision:** (a) with leverage report.

**Responsible reviewer:** Data custodian + scientific reviewer.

**Approval status:** **NOT APPROVED — OUTSTANDING.**

**Estimand impact:** P3/P4; potential influence.

---

### D-10 — Uncertainty method

**Original wording (4L.12):**
> Uncertainty method | (a) Mendota year-cluster bootstrap; BP naive date bootstrap + year separation; (b) p-values; (c) no intervals

**Revised proposal:**
> Revised (a): **descriptive sensitivity ranges, not confidence intervals.**
> - Mendota: ρ, n, leave-one-year-out range; optional season-year block bootstrap as descriptive sensitivity; no primary CI.
> - Buffalo Pound: ρ, n, separate 2018/2019, leave-one-date-out range; **no bootstrap interval**; state two seasons cannot support a reliable interval.
> - No p-values.

**Evidence:**
- 14 non-exchangeable years; few clusters.
- Two seasons; serial dependence; date-level bootstrap anti-conservative.
- 4L.13 critical finding.

**Remaining uncertainty:** No reliable interval for BP; Mendota range is descriptive only.

**Recommended human decision:** Revised (a).

**Responsible reviewer:** Statistical reviewer.

**Approval status:** **NOT APPROVED — OUTSTANDING.**

**Estimand impact:** All; changes uncertainty reporting.

---

### D-11 — Small-n reporting

**Original wording (4L.12):**
> Small-n reporting | (a) no stratum ρ if n<10; show points; (b) compute all; (c) pool strata

**Revised proposal:**
> (a) no stratum ρ if n<10; show points and n. Add an **overall minimum n** set by the statistical reviewer after the count audit, before estimation; if not met, show points only and return to review.

**Evidence:**
- Seasonal strata often 10–20; winter near zero.
- n=10 still unstable.
- 4L.13 recommended overall-n rule.

**Remaining uncertainty:** Exact minimum n; depends on count audit.

**Recommended human decision:** (a) plus overall-n rule.

**Responsible reviewer:** Statistical reviewer.

**Approval status:** **NOT APPROVED — OUTSTANDING.**

**Estimand impact:** All; may determine whether an estimand is reportable.

---

### D-12 — Claims matrix

**Original wording (4L.12):**
> Claims matrix | (a) adopt as written; (b) soften prohibitions; (c) reject

**Revised proposal:**
> (a) Adopt with updates for the revised question:
> - rank association only; no relative concordance;
> - two case studies; no depth-effect claim;
> - no Pearson/log-Pearson;
> - no validation/prediction/early warning/bloom/toxicity/whole-column/agreement.

**Evidence:**
- 4L.13 found the matrix strong but needing alignment with the revised question.

**Remaining uncertainty:** Wording updates only.

**Recommended human decision:** (a) with updates.

**Responsible reviewer:** Scientific reviewer + Gate 2 governance.

**Approval status:** **NOT APPROVED — OUTSTANDING.**

**Estimand impact:** All; governs claims.

---

### D-13 — Originality sufficiency

**Original wording (4L.12):**
> Originality sufficiency | (a) proceed as a modest measurement study; (b) pause; (c) pivot

**Revised proposal:**
> (a) Proceed **only if** a modest/negative measurement audit is acceptable to the team and competition framing. Otherwise (b) pause. No (c) pivot without a specific, evidence-based alternative and a new protocol.

**Evidence:**
- Measurement question well studied; mixed/variable literature.
- Two-case depth contrast confounded.
- No new method/sensor/calibration.
- 4L.13 low–moderate originality.

**Remaining uncertainty:** Competition requirements; team goals.

**Recommended human decision:** Conditional (a) or (b).

**Responsible reviewer:** Project lead + scientific reviewer + Gate 2 governance.

**Approval status:** **NOT APPROVED — OUTSTANDING.**

**Estimand impact:** None directly; go/no-go.

---

### D-14 — Licence/competition compliance

**Original wording (4L.12):**
> Licence/competition compliance | (a) use Painter data under CC BY-NC-SA with attribution/share-alike; (b) exclude Painter data; (c) seek permission

**Revised proposal:**
> (a) Use Painter data under CC BY-NC-SA 4.0 with attribution/share-alike, subject to a documented licence/competition review. If the competition cannot accommodate the licence, (b) exclude Buffalo Pound or (c) seek permission through the proper channel (not authorised in this sprint).

**Evidence:**
- Painter data CC BY-NC-SA 4.0.
- Mendota/BP buoy data CC BY 4.0.
- Competition rules may restrict non-commercial/share-alike use.

**Remaining uncertainty:** Specific competition terms; legal review.

**Recommended human decision:** (a) conditional on review; otherwise (b).

**Responsible reviewer:** Licence/competition reviewer.

**Approval status:** **NOT APPROVED — OUTSTANDING.**

**Estimand impact:** P3/P4 unavailable if Painter data excluded.

---

### D-15 — Approval to begin analysis

**Original wording (4L.12):**
> Approval to begin analysis | (a) approve; (b) approve with changes; (c) do not approve

**Revised proposal:**
> (c) Do not approve until D-01–D-14 are recorded and the revised protocol is re-reviewed. Then reconsider (b) or (a).

**Evidence:**
- Protocol revised but not approved.
- Actual n unknown.
- Several decisions unresolved.
- Licence review incomplete.

**Remaining uncertainty:** All preceding decisions.

**Recommended human decision:** (c) at this time.

**Responsible reviewer:** All required approvers.

**Approval status:** **NOT APPROVED — OUTSTANDING.**

**Estimand impact:** None until analysis is authorised.

## 3. Estimand suitability after revisions

| Estimand | Suitability | Conditions | Could become unsuitable? |
|---|---|---|---|
| P1 | Suitable, conditional | actual n; QC; no depth correction | Yes, if n inadequate |
| P2 | Suitable, conditional | actual n; QC; taxon dependence | Yes, if n inadequate |
| P3 | Recommended downgrade to exploratory pending D-02 verification | biomass derivation verified; actual n; B7/coverage; two seasons | Yes, if derivation rejected or n inadequate |
| P4 | Recommended downgrade to exploratory pending D-02 verification | same + *Planktothrix* caveat | Yes, if derivation rejected or n inadequate |

No estimand is categorically unsuitable at this stage. P3/P4 are the most conditional.

## 4. Decision status matrix

| ID | Topic | Revised proposal | Status |
|---|---|---|---|
| D-01 | Comparability | Rank association only | OUTSTANDING |
| D-02 | BP endpoint | Supplied biomass, conditional | OUTSTANDING |
| D-03 | Mendota depth | 0.5 vs 0–8, no correction | OUTSTANDING |
| D-04 | Turner/YSI | Separate | OUTSTANDING |
| D-05 | QC | Exact decision tree | OUTSTANDING |
| D-06 | Daily summary | Full-day mean | OUTSTANDING |
| D-07 | Temporal window | Same-day + ±1 exploratory | OUTSTANDING |
| D-08 | BP replicates | Mean + sensitivity | OUTSTANDING |
| D-09 | 2019-07-17 | Retain/flag/leverage | OUTSTANDING |
| D-10 | Uncertainty | Descriptive ranges; no BP interval | OUTSTANDING |
| D-11 | Small-n | n<10 + overall minimum | OUTSTANDING |
| D-12 | Claims | Adopt with updates | OUTSTANDING |
| D-13 | Originality | Conditional proceed/pause | OUTSTANDING |
| D-14 | Licence | CC BY-NC-SA review | OUTSTANDING |
| D-15 | Begin analysis | Do not approve yet | OUTSTANDING |

## 5. What must not be inferred

- A recommendation is not an approval.
- Scientific approval does not imply statistical approval.
- Statistical approval does not imply data-custodian approval.
- Data-custodian approval does not imply Gate 2 governance approval.
- Licence review does not imply D-13 or D-15.
- D-13 proceeding does not imply D-15 authorisation.

## 6. Governance

- **Protocol: PROPOSED — NOT APPROVED.**
- **Gate 2: PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- All 15 decisions remain outstanding.
- No analysis is authorised until the required human decisions and explicit D-15 approval are recorded.
