# Pre-Analysis Plan

**Sprint:** 4L.12  
**Status:** PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Date:** 2026-11-24

> **No analysis may begin until this plan has been reviewed and explicitly approved. This is a plan, not a result.**

## 1. Purpose

This pre-analysis plan (PAP) is the master specification for the narrowed descriptive measurement/comparability study. It integrates:

- `PROPOSED_RESEARCH_QUESTION.md`
- `DATASET_INCLUSION_EXCLUSION_RULES.md`
- `TEMPORAL_MATCHING_SPECIFICATION.md`
- `STATISTICAL_ANALYSIS_SPECIFICATION.md`
- `QC_AND_MISSINGNESS_PROTOCOL.md`
- `CLAIMS_AND_LIMITATIONS_MATRIX.md`

Where documents overlap, the stricter rule applies. If documents conflict, the conflict must be resolved by human review before analysis; it must not be resolved silently in code.

## 2. What is fixed and what is open

### 2.1 Fixed by the 4L.11 strategic decision

- **CONTINUE — NARROWED RESEARCH QUESTION.**
- The study is descriptive/measurement-focused, not early-warning validation.
- Mendota is retained for limited exploratory use and rejected for validation of the original question.
- Buffalo Pound is pending/exploratory only; no additional data are assumed.
- Gate 2 remains PAUSED / NOT APPROVED — Option C.

### 2.2 Fixed by this PAP (subject to approval)

- Four primary estimands: P1–P4.
- Mendota Turner era as primary; Mendota YSI as secondary.
- Buffalo Pound 2018–2019 as the only Buffalo Pound analysis window.
- Same-day matching primary; ±1-day sensitivity only.
- Spearman ρ primary; log-Pearson secondary.
- No p-values, models, thresholds, labels, or early-warning claims.
- No pooling across lakes/instruments/depths.

### 2.3 Open — requires human judgement

The decisions in Section 10 are **not** approved by this document. They must be resolved before analysis.

## 3. Research question and estimands

### 3.1 Primary question

> In Lake Mendota (2006–2020) and Buffalo Pound Lake (2018–2019), among same-day paired observations and analysed separately by lake and sensor era, what are the direction, strength and descriptive uncertainty of the rank association between surface chlorophyll and phycocyanin fluorescence and independent microscopy-derived cyanobacteria biovolume (Mendota) or cyanobacteria biomass (Buffalo Pound), and how do these associations vary by season and depth-alignment setting?

### 3.2 Primary estimands

| ID | Lake | Era | Sensor | Endpoint | Max n | Statistic |
|---|---|---|---|---|---:|---|
| P1 | Mendota | Turner | Chlorophyll RFU | Cyanobacteria biovolume | 128 | Spearman ρ |
| P2 | Mendota | Turner | Phycocyanin RFU | Cyanobacteria biovolume | 139 | Spearman ρ |
| P3 | Buffalo Pound | YSI 6600 | Chlorophyll RFU | Cyanobacteria biomass | 42 | Spearman ρ |
| P4 | Buffalo Pound | YSI 6600 | Phycocyanin RFU | Cyanobacteria biomass | 42 | Spearman ρ |

### 3.3 What is not an estimand

- Bloom/non-bloom status.
- Bloom onset/termination.
- Toxicity.
- Predictive accuracy.
- Absolute agreement.
- Calibration/conversion.
- Early-warning lead time.
- Matched false-alarm rate.
- Whole-water-column biomass.
- Causal depth effect.

## 4. Analysis populations

### 4.1 Mendota primary population

All Mendota dates from 2006-07-09 to 2020-12-10 with:

- `lakeid = ME`;
- `depth_range = 0-8m`;
- a cyanobacteria biovolume total (sum of `biovolume_conc` for `division = Cyanophyta`);
- a same-day valid Turner chlorophyll or phycocyanin value under the primary QC rule.

Maximum n: 128/139 under the strict unflagged rule; final n may differ under the approved QC rule.

### 4.2 Buffalo Pound primary population

All 42 documented dates in 2018–2019 with:

- `Depth = 0.8`;
- a cyanobacteria biomass total (sum of `Biomass_mg_m3` for `Group = Cyanophyte`);
- a same-day valid shallow chlorophyll or phycocyanin daily mean;
- adequate within-day coverage (≥50% of expected 10-minute values; both halves of the day represented).

Maximum n: 42; final n may be lower.

### 4.3 No pooled population

Do not create a combined Mendota–Buffalo Pound dataset. Do not append rows. Do not add a lake indicator and fit a pooled model. The cross-lake synthesis is a side-by-side table.

## 5. Data flow and audit

Before estimation, produce a flow table:

| Step | Mendota | Buffalo Pound |
|---|---:|---:|
| Source biological dates | 402 | 42 |
| In analysis window | 230 (2006–2020) | 42 |
| Depth-eligible | 230 (`0-8m`) | 42 (`0.8m`) |
| With any sensor record | 165 | 42 |
| With numeric sensor value | ... | ... |
| Passing primary flag rule | ... | ... |
| Passing coverage rule | not assessable | ... |
| Final primary n (chlorophyll) | ... | ... |
| Final primary n (phycocyanin) | ... | ... |

The Mendota “230 in window” is the count of biology dates from 2006–2020; the exact same-day counts for each pigment are 128/139 under the strict rule. The table must be completed from the data, not assumed.

The audit must also list excluded dates and reasons. No correlation is computed at this stage.

## 6. Analysis sequence

### Step 1 — Verify source identity

- Recompute SHA-256 for each raw file.
- Compare to the recorded hashes in `EVIDENCE_SHA256_REGISTER.csv` and prior sprint records.
- Stop if any hash differs.

### Step 2 — Parse and validate

- Check schema, date parsing, duplicate dates, impossible values, and row counts.
- Do not modify raw files.
- Write a validation table.

### Step 3 — Build analysis populations

- Apply lake/depth/window/date rules.
- Apply taxonomy rules.
- Apply QC rules.
- Apply temporal matching.
- Apply Buffalo Pound replicate and coverage rules.
- Write the flow table and excluded-date list.
- Do not compute associations yet.

### Step 4 — Descriptive summaries

- Distributions, missingness, flag counts, sampling intervals.
- Included vs excluded comparison.
- Scatterplots and time series.
- No fitted models.

### Step 5 — Primary analysis

- P1–P4 Spearman ρ.
- Descriptive bootstrap intervals.
- Log-Pearson secondary.
- No p-values.

### Step 6 — Secondary/exploratory

- Q1–Q10, clearly labelled.
- No promotion to primary.

### Step 7 — Sensitivity

- S-A to S-J.
- Report all, not only the favourable ones.

### Step 8 — Claims check

- For every sentence in the report, check against `CLAIMS_AND_LIMITATIONS_MATRIX.md`.
- Remove prohibited phrases.
- Add the mandatory limitations paragraph.

### Step 9 — Human review

- A second reviewer checks the code, flow table, estimates, and claims.
- The report is not released until review is complete.

## 7. Primary analysis details

### 7.1 Spearman

For each P1–P4:

- compute ρ on the primary population;
- report n, ρ, and descriptive interval;
- report the number of tied ranks;
- report the number of years/seasons contributing;
- do not report a p-value.

### 7.2 Descriptive interval

- Mendota: year-cluster bootstrap, 2,000 replicates.
- Buffalo Pound: date-level bootstrap, 2,000 replicates; label naive; report 2018 and 2019 separately.
- If n < 10 or bootstrap is unstable, report n and points only.

### 7.3 Log-Pearson

- `log10(1 + x)` for non-negative endpoints.
- Report r and n.
- No p-value.
- Do not use it to claim prediction or calibration.

### 7.4 No absolute agreement

Do not compute Bland–Altman, concordance correlation, ICC, calibration slope, or conversion factors. State why.

## 8. Secondary and exploratory analyses

| ID | Analysis | Status | Reporting rule |
|---|---|---|---|
| Q1 | Mendota YSI era | Secondary | Separate from Turner; small n |
| Q2 | Cell density | Secondary | Compare with biovolume/biomass |
| Q3 | Total phytoplankton | Secondary | Tests chlorophyll specificity |
| Q4 | Non-cyanobacteria | Secondary | Discriminant |
| Q5 | Phycocyanin vs chlorophyll | Secondary | Side-by-side; no formal test |
| Q6 | Seasonal | Secondary | n ≥ 10 per stratum |
| Q7 | Turner vs YSI 2019 | Secondary | Descriptive ratios/ranks; no calibration |
| Q8 | Genus subsets | Exploratory | Only with approved crosswalk |
| Q9 | Relative concordance | Exploratory | Sign of change; n pairs |
| Q10 | Cross-lake | Exploratory | Side-by-side; no pooled statistic |

## 9. Sensitivity analyses

| ID | Sensitivity | Primary question |
|---|---|---|
| S-A | Strict unflagged (exclude H) | Does H retention change the pattern? |
| S-B | Flagged-inclusive (C/E/G numeric) | Does flag exclusion drive the result? |
| S-C | Negative-inclusive | Stress test only |
| S-D | ±1-day window | Does date matching matter? |
| S-E | BP B7-inclusive | Does fouling exclusion matter? |
| S-F | BP 2019-07-17 excluded | Does one date dominate? |
| S-G | BP replicate sum/first | Does replicate handling matter? |
| S-H | Mendota station-1 subset | Does station metadata matter? |
| S-I | Lake-specific open-water season | Do calendar boundaries matter? |
| S-J | Log-Pearson | Is the pattern scale-dependent? |

Every sensitivity is reported, even if it contradicts the primary.

## 10. Human decisions required before analysis

The following decisions are **not approved**. Each must be resolved explicitly, with a name/date and a recorded rationale.

| ID | Decision | Options | Recommended | Why it matters |
|---|---|---|---|---|
| D-01 | Operational definition of “comparability” | (a) rank association + relative concordance; (b) absolute agreement; (c) predictive performance | **(a)** | (b) and (c) are not estimable with RFU vs biovolume/biomass and no calibration |
| D-02 | Buffalo Pound endpoint | (a) supplied biomass; (b) derive biovolume from cell volume × density; (c) exclude Buffalo Pound | **(a)** | (b) creates a new derived endpoint and is not authorised; (c) loses the depth-aligned case |
| D-03 | Mendota depth comparator | (a) 0.5 m vs 0–8 m, no correction; (b) attempt a depth correction; (c) exclude Mendota | **(a)** | (b) has no validated correction; (c) loses the long record |
| D-04 | Turner/YSI handling | (a) separate eras; (b) concatenate; (c) convert | **(a)** | (b)/(c) would create an artificial step; no cross-calibration |
| D-05 | Primary QC rule | (a) retain H, exclude C/E/G/O; (b) strict unflagged; (c) include all numeric | **(a)** | (b) truncates high values; (c) includes faulty values; (a) balances |
| D-06 | Primary daily summary | (a) full-day mean for both lakes; (b) nighttime for BP only; (c) daytime for both | **(a)**, with (b) as sensitivity | Mendota cannot do nighttime; full-day mean is the only structurally comparable summary |
| D-07 | Temporal window | (a) same-day primary + ±1-day sensitivity; (b) ±3/±7/±14; (c) same-day only, no sensitivity | **(a)** | Wider windows can span bloom phases; ±1 day is a bounded mismatch check |
| D-08 | Buffalo Pound replicate handling | (a) mean before summing; (b) sum; (c) first row | **(a)**, with (b)/(c) sensitivity | No replicate ID; mean is the least biased assumption for replicate counts |
| D-09 | 2019-07-17 anomaly | (a) retain and flag, exclude in sensitivity; (b) exclude from primary; (c) correct | **(a)** | (b) deletes a documented observation; (c) has no basis; (a) preserves and tests |
| D-10 | Uncertainty method | (a) Mendota year-cluster bootstrap; BP naive date bootstrap + year separation; (b) p-values; (c) no intervals | **(a)** | (b) violates the no-hypothesis-test rule; (c) hides uncertainty |
| D-11 | Small-n reporting | (a) no stratum ρ if n<10; show points; (b) compute all; (c) pool strata | **(a)** | (b) unstable; (c) obscures seasonal structure |
| D-12 | Claims matrix | (a) adopt as written; (b) soften prohibitions; (c) reject | **(a)** | (b) risks early-warning/validation overclaims |
| D-13 | Originality sufficiency | (a) proceed as a modest measurement study; (b) pause; (c) pivot | **(a) only if** a modest/negative measurement result is acceptable; otherwise **(b)** | The study is low–moderate originality; it is not a novel early-warning contribution |
| D-14 | Licence/competition compliance | (a) use Painter data under CC BY-NC-SA with attribution/share-alike; (b) exclude Painter data; (c) seek permission | **(a)** with legal check | Non-commercial/share-alike terms may constrain competition entry |
| D-15 | Approval to begin analysis | (a) approve; (b) approve with changes; (c) do not approve | **(c) until D-01–D-14 are resolved** | No analysis without explicit approval |

### 10.1 Decision record

For each decision, record:

- decision ID;
- chosen option;
- rationale;
- person/role approving;
- date;
- any conditions.

A decision is not approved because it is “recommended” in this table. It requires an explicit human sign-off.

## 11. Approval checklist

Before analysis, all boxes must be checked:

- [ ] D-01 comparability definition approved.
- [ ] D-02 Buffalo Pound endpoint approved.
- [ ] D-03 Mendota depth comparator approved.
- [ ] D-04 Turner/YSI separation approved.
- [ ] D-05 QC rule approved.
- [ ] D-06 daily summary approved.
- [ ] D-07 temporal window approved.
- [ ] D-08 Buffalo Pound replicate rule approved.
- [ ] D-09 2019-07-17 handling approved.
- [ ] D-10 uncertainty method approved.
- [ ] D-11 small-n rule approved.
- [ ] D-12 claims matrix approved.
- [ ] D-13 originality/continuation decision approved.
- [ ] D-14 licence/competition compliance approved.
- [ ] D-15 explicit approval to begin analysis recorded.
- [ ] Scientific reviewer sign-off.
- [ ] Statistical reviewer sign-off.
- [ ] Data custodian sign-off.
- [ ] Gate 2 governance sign-off (remains Option C).
- [ ] No outstanding protocol conflicts.

If any box is unchecked, the status remains **PROPOSED — NOT APPROVED**.

## 12. What would change the plan

A change to any of the following requires a new protocol and human approval:

- the primary question or estimands;
- the biological endpoint;
- the sensor variables;
- the lake/window inclusion;
- the matching rule;
- the primary statistic;
- the QC rule;
- the claims matrix;
- the licence/compliance position.

A change to a figure style, table layout, or script organisation does not require a new protocol, but must be recorded.

## 13. Deviations and analysis lock

- After approval, the protocol and scripts are locked.
- Any deviation is recorded in `DEVIATIONS_LOG.md` before the affected analysis is run, or immediately after discovery if unforeseen.
- The log records: date, protocol section, deviation, reason, impact on estimands/n, and whether human approval was obtained.
- The final report includes a “deviations from protocol” section, even if empty.
- A deviation that changes an estimand or inclusion rule invalidates the pre-specification and requires renewed approval.

## 14. Reporting and release

- The analysis report is internal until human review is complete.
- No upload, publication, commit, or push is authorised by this sprint.
- The report must include the mandatory limitations paragraph and the claims-matrix compliance check.
- The report must not use any prohibited phrase from `CLAIMS_AND_LIMITATIONS_MATRIX.md`.
- The report must state that Gate 2 remains PAUSED / NOT APPROVED — Option C.

## 15. Sequence after approval

1. Build and audit analysis populations.
2. Produce descriptive summaries and flow table.
3. Compute P1–P4.
4. Compute secondary/exploratory analyses.
5. Compute sensitivity analyses.
6. Draft report with claims check.
7. Independent review.
8. Human sign-off.
9. Only then consider competition/communication use, subject to licence review.

No step may be skipped to save time.

## 16. Governance

- **Gate 2 remains PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- This PAP does not create labels, events, models, derived datasets, or results.
- No analysis may begin until the approval checklist is complete and explicitly recorded.
