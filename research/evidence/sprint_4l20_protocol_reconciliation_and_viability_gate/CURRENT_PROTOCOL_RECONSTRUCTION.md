# Current Protocol Reconstruction

**Sprint:** 4L.20  
**Date:** 2026-11-26  
**Purpose:** Reconstruct the proposed Stage 1 design exactly as it currently exists, separate current proposal from historical/review material, and identify every component that needs a disposition.  
**Status:** Reconstruction only. **PROTOCOL NOT APPROVED. D-15 NOT APPROVED. ANALYSIS NOT AUTHORISED.**

---

## 1. Document precedence

The current proposed design is not a single, internally consistent document. It is a layered record:

| Layer | Document | Role | Status |
|---|---|---|---|
| 1 | `sprint_4l12_narrowed_question_protocol/` | Original narrowed protocol | Historical; superseded for review by 4L.14 |
| 2 | `sprint_4l13_independent_protocol_challenge/` | Independent review of 4L.12 | Review evidence; not approval |
| 3 | `sprint_4l14_protocol_revision/REVISED_PROTOCOL.md` and supporting documents | Current proposed protocol | **PROPOSED — NOT APPROVED** |
| 4 | `sprint_4l14_codex_independent_review/` | Independent review of 4L.14 | Review evidence; accept-after-revisions |
| 5 | `strategic_reconciliation_and_muggelsee_enquiry_2026_11_25/SPRINT_4L14_REVIEW_ADDENDUM.md` | Proposed amendments to 4L.14 | **Not applied**; review/addendum |
| 6 | `sprint_4l16/17/18/19` | Human-review preparation, QC evidence, provenance and external engagement | Evidence; not protocol |
| 7 | `sprint_4l20` (this package) | Reconciliation and viability decision | Recommendation; not approval |

**Rule:** the 4L.14 `REVISED_PROTOCOL.md` remains the current *proposed* protocol, but it is contradicted in several places by the 4L.14 addendum and later evidence. The addendum is not the approved protocol. No document in this package silently amends the protocol.

---

## 2. Protocol inventory

| Component | Current proposal | Evidence basis | Status | Contradiction or concern | Recommended disposition |
|---|---|---|---|---|---|
| **Research question** | “In Lake Mendota (2006–2020) and Buffalo Pound Lake (2018–2019), among same-day date-level co-occurrences and analysed as two separate lake-specific case studies, what are the direction and magnitude of the rank association between surface chlorophyll and phycocyanin fluorescence and independent microscopy-derived cyanobacteria biovolume (Mendota) or cyanobacteria biomass (Buffalo Pound), and how do these associations differ descriptively across seasons and sensor eras?” | 4L.14 §1, §3; 4L.13 R-01; 4L.14 addendum F-07 | Proposed | “Across seasons and sensor eras” overstates Buffalo Pound (one era); “2006–2020” includes YSI era; Buffalo Pound cannot support the biomass endpoint without custodian evidence | Replace with Mendota-only Turner-era question; P2 primary, P1 secondary; remove Buffalo Pound |
| **Scientific objective** | Descriptive measurement/comparability audit, not validation/EWS | 4L.14 §1–§3; 4L.13; 4L.14 addendum | Proposed | Objective is coherent, but the two-lake design implies comparison that the data cannot support | Retain measurement-audit framing; remove cross-lake comparison |
| **Interpretation** | Rank association only; no agreement/calibration/prediction/EWS | 4L.14 §1, §11, §14 | Proposed | Correct in principle; the four-estimand structure creates selective-emphasis risk | Retain and strengthen; one primary, one secondary |
| **P1 — Mendota Turner chlorophyll** | Chlorophyll RFU vs cyanobacteria biovolume, 0–8 m; maximum n 128 | 4L.14 §5; 4L.10; 4L.9 | Proposed, conditional | Depth mismatch; biweekly biology; H/negative QC unresolved; no actual n | Retain as **secondary descriptive comparator**, not co-primary |
| **P2 — Mendota Turner phycocyanin** | Phycocyanin RFU vs cyanobacteria biovolume, 0–8 m; maximum n 139 | 4L.14 §5; 4L.10; 4L.9 | Proposed, conditional | Depth mismatch; 4 negative RFU; H treatment; seasonal confounding | Retain as **primary**; Turner only |
| **P3 — Buffalo Pound YSI chlorophyll** | Chlorophyll RFU vs supplied cyanobacteria biomass, 0.8 m; maximum n 42 | 4L.14 §5; Painter 2022; Baulch 2025; 4L.19 | Proposed but recommended downgrade | Duplicate/`REP` semantics, biomass derivation, B7, coverage, time zone, two seasons, separate licence | **Remove from Stage 1**; preserve as future/Stage 2 context |
| **P4 — Buffalo Pound YSI phycocyanin** | Phycocyanin RFU vs supplied biomass, 0.8 m; maximum n 42 | 4L.14 §5; Painter 2022; 4L.19 | Proposed but recommended downgrade | Same as P3, plus *Planktothrix* detection concern | **Remove from Stage 1** |
| **Primary/secondary outcomes** | P1–P4 candidate primary; P3/P4 recommended downgrade; YSI Mendota secondary | 4L.14 §4–§5 | Ambiguous | §1 and §7.2 say P3/P4 downgrade; §4.2 says “Primary estimates: P3/P4”; §5 calls all four “candidate primary” | Replace with explicit P2 primary / P1 secondary hierarchy; no P3/P4 |
| **Matching rule** | Same calendar date; sensor daily summary; no interpolation; ±1-day exploratory | 4L.14 §9; 4L.12 temporal spec | Proposed | Date-only biology; daily mean not sample-time; ±1-day changes sample composition | Same-date only; remove ±1-day unless reviewer requires |
| **Instrument eras** | Mendota Turner 2006–2019 primary; YSI 2019–2020 secondary; Buffalo Pound YSI 6600 2018–2019 | 4L.14 §4.1–§4.2 | Proposed | YSI Mendota n≈21/22; no cross-era concatenation; “eras” plural only for Mendota | Turner-only; remove YSI era |
| **Biological endpoint — Mendota** | Total cyanobacteria biovolume (`division = Cyanophyta`), 0–8 m composite | 4L.14 §7.1; 4L.5; 4L.6; NTL EML 88.31 | Proposed | Measurement-independent but taxonomically non-stationary; no detection limits; 0–8 m composite vs 0.5 m sensor | Retain broad division-level biovolume; state limitations |
| **Biological endpoint — Buffalo Pound** | Total cyanobacteria biomass (`Group = Cyanophyte`; `Biomass_mg_m3`) | 4L.14 §7.2; 4L.19 | Proposed, unverified | Derived wet-weight-equivalent biomass; exact density/rounding/provider method unconfirmed; duplicate rows; not biovolume | **Remove from Stage 1**; do not sum by assumption |
| **QC framework — Mendota** | C/E/G/O/undocumented excluded; H retained if numeric; negative RFU retained; physical bounds | 4L.14 §10.1; `QC_AND_MISSINGNESS_RULES.md` | Proposed | H retention unsupported (no numeric range); negative retention unsupported; C-with-value; G absent for Turner; O undefined | Replace with Mendota-specific QC; H and negative require reviewer decision; both reported |
| **QC framework — Buffalo Pound** | M/C excluded; B7 excluded; negative retained; >100 retained with flag; ≥50%/both halves coverage | 4L.14 §10.2; `QC_AND_MISSINGNESS_RULES.md` §4, §8 | Proposed | B7 is caution interval; >100 outside documented range; coverage rule withdrawn; negative unresolved; duplicates/REP unresolved | **Remove from Stage 1**; preserve for future work |
| **Daily summary — Mendota** | Provider daily mean of 1-minute data | 4L.14 §9.1; D-06; 4L.9 | Provisional Option A | Within-day coverage unknown; sample time unknown; daily mean may not represent sample moment | Retain as only available daily summary, with limitation; no equivalence claim |
| **Daily summary — Buffalo Pound** | Mean of valid 10-minute values; day/night medians sensitivity | 4L.14 §9.1; D-06 | Provisional Option A | Coverage/time zone/sample time unresolved | **Remove from Stage 1** |
| **Sensitivity analyses** | S-A strict unflagged; S-B flagged-inclusive; S-C negative excluded; S-D ±1-day; S-E B7-inclusive; S-F 2019-07-17 excluded; S-G replicate sum/first; S-H station-1; S-I seasonal | 4L.14 §12.4 | Proposed | Nine sensitivities include BP-only and cross-lake items; multiplicity/selective emphasis | Reduce to Mendota-relevant set: H, negative, station, seasonal, leave-one-year-out; no BP items |
| **Uncertainty** | Mendota leave-one-year-out range; BP leave-one-date-out; no bootstrap/CI | 4L.14 §12; addendum F-08 | Proposed | Influence diagnostics are not sampling uncertainty; no p-values; descriptive range language must be precise | Retain leave-one-year-out; state it is not a CI; reviewer to accept |
| **Reporting rules** | Report all four estimates; no “best” sensor; seasonal strata n≥10 | 4L.14 §11–§12; addendum F-11 | Proposed | Four-estimand reporting creates false replication; hierarchy needed | Report P2 primary, P1 secondary; all outputs, no winner |
| **Claims matrix** | Permitted rank-association language; prohibited validation/EWS/prediction/causation | 4L.14 §14 | Proposed | Strong in principle; needs Mendota-only wording; depth mismatch limitation must be mandatory | Retain and tighten |
| **Exclusions** | Missing, C/E/G/O/undocumented, H (strict sensitivity), negative (sensitivity), BP coverage/B7 | 4L.14 §10; `QC_AND_MISSINGNESS_RULES.md` | Proposed | Some exclusions unsupported or contradictory; BP exclusions no longer relevant | Replace with Mendota-specific exclusions |
| **Limitations** | Date-only biology; 0.5 m vs 0–8 m; Turner/YSI non-comparability; biovolume vs biomass; two seasons; no calibration | 4L.14 §14.3 | Proposed | Mandatory limitations are good; need remove BP-specific items and add Mendota detection-conditioned/biweekly limitations | Rewrite for Mendota-only |
| **Governance dependencies** | D-01–D-15 outstanding; Gate 2 paused; no analysis | 4L.14 §16–§17; all later packages | Current | No decision approved; no reviewer; no count audit; no licence review | Preserve; do not approve D-15 |
| **Licence** | D-14 review; Painter data CC BY-NC-SA; Mendota/BP buoy CC BY 4.0 | 4L.14 §16; D-14 register; 4L.19 | Outstanding | Removing Buffalo Pound removes CC BY-NC-SA from Stage 1; Mendota CC BY 4.0 still needs competition review | Re-scope D-14 to Mendota CC BY 4.0; written review remains required |
| **Count audit** | Separate authorisation after D-15; enumerate actual n | 4L.14 §6.3; `ESTIMAND...` §7 | Not authorised | Actual n unknown; no count audit performed | Keep separate; authorise only after scope/protocol decision |

---

## 3. Ambiguities that must not be resolved by assumption

### 3.1 “Primary” vs “candidate primary” vs “exploratory”

The protocol uses three labels:

- §1: “Candidate primary estimands: P1–P4.”
- §4.2: “Primary estimates: P3/P4.”
- §5 table: “Candidate primary estimands.”
- §7.2: “P3/P4 recommended downgrade to exploratory.”
- `ESTIMAND...` §10: P3/P4 “Recommended downgrade to exploratory.”
- `REVISED_RESEARCH_QUESTION.md` §4: P3/P4 “Recommended downgrade to exploratory.”

This is a **documentary inconsistency**. The later documents (4L.14 addendum, 4L.18, 4L.19) support downgrade/removal. The current protocol text should not be read as approving P3/P4 as primary.

### 3.2 “H retained” vs “H unresolved”

The protocol says H is retained if numeric; the addendum says H is retained only within a documented range, and the EML provides no numeric range. The later evidence supports the addendum, not the protocol. The exact treatment remains a reviewer decision.

### 3.3 “B7 excluded” vs “B7 caution”

The protocol excludes B7; the *Data in Brief* paper defines B7 as a caution interval covering the entire period between maintenance visits. The evidence does not support automatic exclusion. If Buffalo Pound is removed from Stage 1, this becomes a future-work issue, not a Stage 1 blocker.

### 3.4 “Negative RFU retained” vs “negative RFU unresolved”

The protocol retains negative RFU as observed; the addendum and D-05 say negative RFU has no documented biological meaning and should be excluded primary with sensitivity. The protocol is not supported by the evidence.

### 3.5 “>100 RFU retained” vs “outside full scale”

The protocol retains >100 RFU with a flag; the documented 0–100 RFU full scale and D-05 say >100 cannot be assumed quantitative. The protocol is not supported. If Buffalo Pound is removed, this is not a Stage 1 issue.

### 3.6 “≥50% coverage” vs “fixed rule withdrawn”

The protocol uses ≥50%/both halves; the 4L.14 addendum F-01 withdrew the fixed 72/144 rule, and 4L.18/19 found no date-specific expectation. The protocol is not supported. If Buffalo Pound is removed, this is not a Stage 1 issue.

### 3.7 “Station 1 if present” vs “all eligible dates”

The protocol §6.1 uses station 1 if present, otherwise blank; the addendum F-06 proposes all eligible 0–8 m dates regardless of station, with station sensitivity. The addendum rationale is stronger because station is blank for 371/402 dates. This is a methodological choice, not a factual contradiction; it requires reviewer acceptance.

### 3.8 “2006–2020” vs Turner 2006–2019

The question window includes 2020, but the Turner era ends in 2019; 2020 is YSI. The Mendota-only Turner study should use 2006–2019. The 2020 date is a documentary overreach.

---

## 4. What the protocol actually proposes

Stripped of inconsistencies, the current proposal is:

1. **Two separate lake case studies**, not pooled.
2. **Mendota:** Turner chlorophyll/phycocyanin 2006–2019 primary; YSI 2019–2020 secondary; 0.5 m sensor vs 0–8 m composite; 128/139 same-day upper bounds.
3. **Buffalo Pound:** YSI 6600 chlorophyll/phycocyanin 2018–2019; 0.82 m sensor vs 0.8 m biology; 42 dates; derived biomass; P3/P4 recommended downgrade.
4. **Statistic:** Spearman rho, n, descriptive sensitivity range; no p-values, no agreement, no prediction.
5. **QC:** explicit decision tree, no imputation; but several rules contradicted by later evidence.
6. **Claims:** rank association only; no validation/EWS/calibration/prediction.
7. **Governance:** all decisions outstanding; D-15 not approved; no analysis.

The design is coherent in spirit but not in its current documentary details.

---

## 5. Reconstruction verdict

**The current protocol cannot be approved as written.** It contains:

- an internal P3/P4 status contradiction;
- QC rules contradicted by the provider documentation and later evidence;
- a station rule contradicted by the review addendum;
- a sensor-era clause that overstates Buffalo Pound;
- a 2020 window that includes a different instrument era;
- a two-lake comparison that cannot isolate depth or lake effects;
- a four-estimand structure that creates a false impression of replication.

The defensible reconstruction is a **Mendota-only, Turner-era, P2-primary/P1-secondary descriptive audit**, with a revised QC section and a reduced sensitivity set. That reconstruction is a recommendation, not an approval.

**No protocol file was modified. No decision was approved.**
