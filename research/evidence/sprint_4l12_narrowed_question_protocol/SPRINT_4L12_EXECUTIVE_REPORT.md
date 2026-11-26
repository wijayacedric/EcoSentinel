# Sprint 4L.12 Executive Report — Narrowed-Question Protocol and Pre-Analysis Plan

**Sprint:** 4L.12  
**Status:** **PROPOSED — NOT APPROVED**  
**Gate 2:** **PAUSED / NOT APPROVED — Option C (Exploratory Only)**  
**Date:** 2026-11-24

> **No analysis may begin until this protocol has been reviewed and explicitly approved.**

## 1. What this sprint did

This sprint converted the Sprint 4L.11 strategic decision — **CONTINUE — NARROWED RESEARCH QUESTION** — into a human-reviewable protocol and pre-analysis plan.

It:

- inspected the primary Mendota and Buffalo Pound data dictionaries, metadata, audit records, and prior evidence;
- defined the measurement question precisely, separating association, correlation, agreement, prediction, biological measurement validity, and ecological interpretation;
- defined primary and secondary endpoints, sensor variables, observational unit, target population, and scope of inference;
- defined lake-specific inclusion/exclusion rules, temporal matching, QC/missingness handling, descriptive statistics, uncertainty, sensitivity analyses, and a claims matrix;
- conducted a focused prior-art update on sensor–microscopy comparisons, chlorophyll/phycocyanin proxy validity, depth mismatch, seasonality, and multi-lake comparability;
- identified the human decisions that must be made before any analysis.

It did **not**:

- compute a correlation, plot project data, clean/transform data, or create a derived dataset;
- create bloom/non-bloom labels, event intervals, models, hypothesis tests, or thresholds;
- acquire data, contact researchers, upload, commit, or push;
- approve the protocol or begin analysis.

## 2. Bottom line

The narrowed question is **scientifically feasible as a descriptive measurement/comparability study**, but it is **not yet precisely defined in its 4L.11 wording**, and its **originality is low–moderate**.

The 4L.11 strategic decision remains **CONTINUE — NARROWED RESEARCH QUESTION**. The recommended disposition for this sprint is:

> **PROCEED TO HUMAN REVIEW — PROTOCOL NOT APPROVED.**

If human reviewers require a genuinely novel early-warning contribution, the correct decision is **PAUSE — INSUFFICIENT SCIENTIFIC FEASIBILITY**, not to stretch the measurement study into an early-warning claim.

## 3. Why the 4L.11 wording needs revision

The 4L.11 wording asked “how comparable” sensor proxies are with microscopy biovolume. That phrase conflates six different things:

| Term | Requires | Proposed? |
|---|---|---|
| Statistical association | A directional relationship | **Yes — primary** |
| Correlation | A specific linear/rank statistic | **Spearman primary; Pearson secondary** |
| Agreement | Same quantity, same scale, bias/limits | **No — not estimable** |
| Predictive performance | Calibrated model, held-out validation | **No** |
| Biological measurement validity | Unbiased, calibrated measurement across conditions | **No** |
| Ecological interpretation | Causal/mechanistic explanation | **No** |

RFU and biovolume/biomass are different quantities on different scales. There is no validated conversion, no cross-calibration between Turner and YSI, and no paired calibration experiment. Absolute agreement, Bland–Altman limits, concordance correlation, and predictive accuracy cannot be estimated.

The protocol therefore recommends:

> **Comparability = rank association + relative concordance, not absolute agreement.**

This is the single most important precision change in the sprint.

## 4. Recommended primary question

> In Lake Mendota (2006–2020) and Buffalo Pound Lake (2018–2019), among same-day paired observations and analysed separately by lake and sensor era, what are the direction, strength and descriptive uncertainty of the rank association between surface chlorophyll and phycocyanin fluorescence and independent microscopy-derived cyanobacteria biovolume (Mendota) or cyanobacteria biomass (Buffalo Pound), and how do these associations vary by season and depth-alignment setting?

This is a **descriptive measurement/comparability study**. It is not an early-warning validation, bloom-detection study, sensor calibration, or toxicity assessment.

## 5. Primary estimands

| ID | Lake / era | Sensor | Biological endpoint | Max n |
|---|---|---|---|---|
| P1 | Mendota / Turner 2006–2019 | Chlorophyll RFU | Cyanobacteria biovolume (0–8 m) | 128 |
| P2 | Mendota / Turner 2006–2019 | Phycocyanin RFU | Cyanobacteria biovolume (0–8 m) | 139 |
| P3 | Buffalo Pound / YSI 6600 2018–2019 | Chlorophyll RFU | Cyanobacteria biomass (0.8 m) | 42 |
| P4 | Buffalo Pound / YSI 6600 2018–2019 | Phycocyanin RFU | Cyanobacteria biomass (0.8 m) | 42 |

The n values are upper bounds under the strict 4L.10 “unflagged only” rule. The protocol’s primary QC rule retains some `H`-flagged numeric values, so the final n may be larger; it must be enumerated before estimation.

**Mendota biovolume and Buffalo Pound biomass are not numerically equivalent and are never pooled.** Buffalo Pound supplies biomass, not biovolume; deriving biovolume from cell volume × density would be a new derived endpoint and is not authorised.

## 6. Design summary

### 6.1 Mendota

- Sensor: 0.5 m; Turner chlorophyll/phycocyanin 2006–2019; YSI 2019–2020.
- Biology: 402 dates, 400 at 0–8 m, 2 at 0–2 m; median 14-day interval; date-only.
- Same-day overlap: 128 Turner chlorophyll, 139 Turner phycocyanin, 21 YSI chlorophyll, 22 YSI phycocyanin under the strict unflagged rule.
- Primary: Turner era; YSI is secondary due small n.
- Depth: 0.5 m sensor vs 0–8 m composite; no depth correction.
- Turner and YSI are never concatenated.

### 6.2 Buffalo Pound

- Sensor: 0.82 m shallow sonde; 10-minute data; 2018–2019.
- Biology: 42 dates (25 in 2018, 17 in 2019); 0.8 m; median 4/8-day intervals; date-only.
- Same-day overlap: all 42 dates, subject to QC and coverage.
- Depth: 0.82 m sensor vs 0.8 m sample — the closest alignment in the project.
- Two seasons only; no non-bloom baseline; 2019-07-17 anomaly retained and flagged.

### 6.3 Temporal matching

- Primary: same calendar date only.
- Mendota: provider daily mean of 1-minute data; no nighttime reconstruction.
- Buffalo Pound: mean of valid 10-minute values; ≥50% of expected values and both halves of the day represented.
- Sensitivity: ±1-day window only; no ±3/±7/±14-day windows; no lag/lead analysis.
- Date-only biology means same-day is not same-time.

### 6.4 Statistics

- Primary: Spearman’s ρ, with n and a descriptive bootstrap interval.
- Mendota: year-cluster bootstrap; Buffalo Pound: naive date-level bootstrap plus separate 2018/2019 estimates.
- Secondary: Pearson r on log10(1+x) as a scale check.
- No p-values, hypothesis tests, models, thresholds, calibration, Bland–Altman, concordance, prediction, or matched FAR.
- Seasonal strata with n<10: no stratum ρ; show points and n.

## 7. What the primary data show (evidence inspection only)

No analysis was performed. The following are verified counts from prior audits, not results:

- Mendota daily sensor file: 3,996 rows, 38 columns, 2006-07-09 to 2025-11-18, 0 duplicate dates.
- Mendota biology: 402 dates, 1995-01-24 to 2020-12-10; 400 0–8 m composites; 2 0–2 m; 371/402 dates have blank station.
- Mendota same-day strict-unflagged overlap: Turner chlorophyll 128; Turner phycocyanin 139; YSI chlorophyll 21; YSI phycocyanin 22; DO raw 99; water temperature 94.
- Mendota joint coverage: 58/402 for a 7-variable Turner core; 2/402 for an 11-variable YSI core; 165/402 with any sensor.
- Buffalo Pound biology: 42 dates; 25 in 2018, 17 in 2019; 0.8 m; median gap 4/8 days; maximum 12/16 days.
- Buffalo Pound buoy: 142,760 records; 68 columns; 10-minute (2014: 15-minute); ice-free 2014–2021.
- Buffalo Pound same-day alignment: 25/25 (2018), 17/17 (2019); 121–144 records/day (2018), 42–131 (2019).
- Buffalo Pound 2019-07-17: total biomass 45.81 mg m⁻³, cyanobacteria 41.02 mg m⁻³, between neighbours 12,587.1 and 9,497.9 mg m⁻³; unresolved.

These counts define the feasible sample. They do not support labels, events, early warning, or validation.

## 8. Prior-art pressure

The measurement question is **not novel**. Key prior findings:

- **Hartmann et al. 2019:** total chlorophyll vs total biovolume correlated well, but cyanobacteria were often underestimated, including at high *Microcystis*.
- **Bowling et al. 2016:** phycocyanin correlated with cyanobacterial biovolume in two of three ponds; poor with picoplankton; chlorophyll was a poor cyanobacteria measure; taxon-dependent.
- **Hodges et al. 2018:** field phycocyanin vs biovolume R² = 0.22–0.29 for two sensors and non-significant for a third; manufacturer/temperature/morphology effects.
- **Thomson-Laing et al. 2020:** strong overall relationships, but lake-specific r² = 0.06–0.90.
- **Rogora et al. 2023:** total biovolume R² = 0.72 for Cyclops7 vs 0–20 m microscopy, but community composition mattered and cyanobacteria/picocyanobacteria were underestimated.
- **USGS SIR 2024-5010:** chlorophyll vs lab chlorophyll moderate; relations with total biovolume weaker; phycocyanin vs cyanobacterial biovolume **not significant**; temperature strongest; turbidity more informative than dual-channel phycocyanin.
- **Kovalenko et al. 2026:** chlorophyll vs total biovolume significant; spring > summer; deep chlorophyll layer weakest; cyanobacteria/green/crypto weak; diatoms strongest.
- **Cotterill et al. 2019:** weak/variable phycocyanin–biovolume relationships (<R² 0.4).
- **Levi et al. 2025:** calibration, biofouling, composition, nighttime, and high-frequency events affect performance.
- **Rousso et al. 2021:** light quenching can reduce chlorophyll by up to 79% and phycocyanin by up to 59%.
- **Painter et al. 2022:** Buffalo Pound autumn *Planktothrix* >60% biomass was not detected by sensor or laboratory chlorophyll-a.
- **Carpenter et al. 2020/2022:** Mendota high-frequency phycocyanin is already studied; stochastic states, variable lags/extremes, and sensor regime changes.

**Implication:** The proposed study can produce a useful local measurement audit, but it is testing known weaknesses, not discovering them. Combining two lakes or using Spearman does not create novelty.

## 9. Originality verdict

**LOW–MODERATE.**

What is distinctive:

- a two-case contrast between a depth-mismatched setting (Mendota 0.5 m vs 0–8 m) and a depth-aligned setting (Buffalo Pound 0.82 m vs 0.8 m);
- a long Mendota record with separate Turner/YSI eras;
- explicit QC, anomaly, and sensitivity reporting;
- a deliberate refusal of absolute-agreement/validation language.

What is not distinctive:

- the core sensor–microscopy question;
- chlorophyll/phycocyanin proxy testing;
- depth-mismatch awareness;
- seasonal/community stratification;
- Spearman correlation;
- using public data;
- reporting a negative result.

The two-lake depth contrast is **confounded** by lake type, community, instrument, period, sampling, QC, and endpoint. It cannot isolate depth alignment.

**Conclusion:** The study is sufficient for a rigorous school-level measurement project if framed honestly as a modest/negative measurement audit. It is not sufficient for a top-tier novelty or early-warning claim. If a novel early-warning result is required, **PAUSE**.

## 10. Human decisions required

The protocol is not approved until these are resolved:

1. Accept rank association (not absolute agreement) as “comparability.”
2. Accept Buffalo Pound biomass as the endpoint; no derived biovolume.
3. Accept Mendota 0.5 m vs 0–8 m with no depth correction.
4. Keep Turner/YSI separate; no cross-calibration.
5. Approve the primary QC rule (retain `H`; exclude `C/E/G/O`; Buffalo Pound blank only).
6. Approve full-day means, with Buffalo Pound nighttime as sensitivity.
7. Approve same-day + ±1-day sensitivity only.
8. Approve Buffalo Pound replicate mean, with sum/first-row sensitivity.
9. Approve retaining 2019-07-17 with exclusion sensitivity.
10. Approve the bootstrap/no-p-value uncertainty method.
11. Approve the n<10 stratum reporting rule.
12. Approve the claims matrix.
13. Decide whether a modest/negative measurement study is sufficient; if not, **PAUSE**.
14. Complete the licence/competition review (Painter data are CC BY-NC-SA 4.0).
15. Record explicit approval to begin analysis.

## 11. Final answers to the required questions

### 11.1 Is the narrowed question precisely defined?

**Conditionally yes — but not in the 4L.11 wording.**

The 4L.11 wording (“how comparable/agreement”) is not precise. The recommended wording is precise **only if**:

- comparability is defined as rank association + relative concordance;
- Mendota biovolume and Buffalo Pound biomass remain separate;
- Turner and YSI remain separate;
- the cross-lake depth contrast is descriptive, not causal;
- no predictive/validation/early-warning claims are permitted.

If those conditions are not accepted, the question remains ambiguous and should not proceed.

### 11.2 Is the proposed measurement design defensible?

**Yes, as a descriptive two-case measurement/comparability study with major limitations. No, as validation or early warning.**

It is defensible because:

- the endpoints and sensor variables are defined;
- the inclusion/exclusion and QC rules are explicit;
- the matching is conservative (same-day; ±1-day sensitivity only);
- the statistics are descriptive and do not overclaim;
- the claims matrix prohibits validation/early-warning language;
- the analysis can produce a negative or limited result honestly.

It is limited because:

- Mendota is 0.5 m vs 0–8 m;
- Buffalo Pound has only two seasons;
- both have date-only biology;
- Turner/YSI are not comparable;
- no calibration/detection limits;
- the two-lake depth contrast is confounded;
- the literature already predicts weak/variable relationships.

### 11.3 Which decisions still require human judgement?

The 15 decisions in Section 10. The most consequential are:

- D-01 comparability definition;
- D-02 Buffalo Pound endpoint;
- D-05 QC rule;
- D-07 temporal window;
- D-09 2019-07-17 handling;
- D-13 originality/continuation;
- D-14 licence/competition compliance;
- D-15 approval to begin.

### 11.4 Is the originality sufficient to justify proceeding?

**Low–moderate; not sufficient for a strong novelty claim.**

It is sufficient to justify a **modest, rigorous measurement audit** if:

- the team accepts a negative/limited result;
- the competition framing values measurement quality and critical thinking;
- the study is not sold as early warning or sensor validation.

It is **not** sufficient if:

- the competition requires a novel early-warning method;
- the team needs a positive, management-ready sensor claim;
- the study would be presented as a generalisable multi-lake result.

In those cases, **PAUSE — INSUFFICIENT SCIENTIFIC FEASIBILITY** is more honest than stretching the study.

### 11.5 What are the exact outstanding approval requirements?

1. Scientific reviewer sign-off on the question, estimands, endpoints, and inclusion rules.
2. Statistical reviewer sign-off on Spearman, bootstrap, no-p-values, and small-n rules.
3. Data custodian sign-off on QC/missingness/anomaly handling.
4. Gate 2 governance sign-off that the study remains Option C (Exploratory Only).
5. Licence/competition review for Painter data (CC BY-NC-SA 4.0) and all datasets.
6. Explicit decision on D-13 (proceed vs pause).
7. Explicit approval to begin analysis (D-15).
8. No outstanding protocol conflicts.

Until all are recorded, the status is **PROPOSED — NOT APPROVED**.

## 12. Deliverables

`research/evidence/sprint_4l12_narrowed_question_protocol/`

- `SPRINT_4L12_EXECUTIVE_REPORT.md`
- `PROPOSED_RESEARCH_QUESTION.md`
- `ONE_PAGE_PROTOCOL.md`
- `PRE_ANALYSIS_PLAN.md`
- `DATASET_INCLUSION_EXCLUSION_RULES.md`
- `TEMPORAL_MATCHING_SPECIFICATION.md`
- `STATISTICAL_ANALYSIS_SPECIFICATION.md`
- `QC_AND_MISSINGNESS_PROTOCOL.md`
- `CLAIMS_AND_LIMITATIONS_MATRIX.md`
- `ORIGINALITY_AND_PRIOR_ART_UPDATE.md`
- `SOURCE_REGISTER.md` / `.csv`
- `EXTERNAL_SEARCH_LOG.md`
- `SPRINT_4L12_HANDOVER.md`
- `EVIDENCE_SHA256_REGISTER.csv` + sidecar
- `EVIDENCE_SHA256_REGISTER_README.md`
- `DELIVERABLES_INDEX.md`

## 13. Governance

- **Gate 2 remains PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- No bloom/non-bloom labels, event intervals, confirmatory models, hypothesis tests, threshold optimisation, protocol changes, external contacts, uploads, commits or pushes were made.
- Raw data and prior evidence remain unchanged.
- No analysis may begin until the protocol is reviewed and explicitly approved.
