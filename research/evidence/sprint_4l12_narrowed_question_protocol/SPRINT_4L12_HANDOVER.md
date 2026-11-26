# Sprint 4L.12 Handover

**Sprint:** 4L.12  
**Status:** **PROPOSED — NOT APPROVED**  
**Gate 2:** **PAUSED / NOT APPROVED — Option C (Exploratory Only)**  
**Date:** 2026-11-24

## 1. What is complete

- Inspected the Sprint 4L.11 decision, final recommendation, executive report, current-state record, evidence requirements, source register, and handover.
- Inspected the Sprint 4L.10 Mendota final decision, joint-coverage tables, endpoint/depth critiques, and sensor-era/QC critique.
- Inspected the Sprint 4L.9 daily sensor audit (schema, flags, era, depth, overlap).
- Inspected the Sprint 4L.5/4L.6 Mendota biology audits (endpoint, taxonomy, depth, anomalies).
- Inspected the Sprint 4F Buffalo Pound stress test, biological/environmental QC audits, and alignment verification.
- Inspected the primary dataset metadata and data dictionaries:
  - EDI `knb-lter-ntl.129.42` EML and daily CSV;
  - EDI `knb-lter-ntl.88.31` EML and phytoplankton CSV;
  - FRDR Buffalo Pound README/data flags and annual CSVs;
  - Painter et al. 2022 Borealis microscopy data;
  - Baulch et al. 2025 data paper.
- Drafted the full protocol and pre-analysis plan:
  - precise question and operational definitions;
  - four primary estimands;
  - lake-specific inclusion/exclusion rules;
  - temporal matching specification;
  - QC and missingness protocol;
  - statistical analysis specification;
  - claims and limitations matrix;
  - originality and prior-art update;
  - source register and search log.
- Identified 15 human decisions that must be resolved before analysis.
- Created the deliverables index and SHA-256 register (to be regenerated after final edits).

## 2. What is not complete

- The protocol is **not approved**.
- No analysis, correlation, plot, cleaning, transformation, derived dataset, label, event, model, hypothesis test, or threshold optimisation was performed.
- No external contact, data acquisition, upload, commit, or push was made.
- The 15 human decisions are unresolved.
- The licence/competition review is not complete.
- The final SHA-256 register/sidecar must be regenerated after the last edits.

## 3. Key conclusions to carry forward

### 3.1 Question precision

The 4L.11 wording (“how comparable/agreement”) is **not precise enough**. It conflates association, correlation, agreement, prediction, measurement validity, and ecological interpretation.

The recommended wording is:

> In Lake Mendota (2006–2020) and Buffalo Pound Lake (2018–2019), among same-day paired observations and analysed separately by lake and sensor era, what are the direction, strength and descriptive uncertainty of the rank association between surface chlorophyll and phycocyanin fluorescence and independent microscopy-derived cyanobacteria biovolume (Mendota) or cyanobacteria biomass (Buffalo Pound), and how do these associations vary by season and depth-alignment setting?

**Comparability is defined as rank association + relative concordance, not absolute agreement.**

### 3.2 Design

- Four primary estimands: Mendota Turner chlorophyll/phycocyanin vs cyanobacteria biovolume; Buffalo Pound YSI chlorophyll/phycocyanin vs cyanobacteria biomass.
- Mendota YSI is secondary (n≈21/22).
- Turner and YSI are never concatenated.
- Mendota biovolume and Buffalo Pound biomass are never pooled.
- Same-day matching primary; ±1-day sensitivity only.
- Spearman ρ primary; log-Pearson secondary; no p-values.
- No models, thresholds, labels, calibration, prediction, or early warning.

### 3.3 Originality

**LOW–MODERATE.** The measurement question is already extensively studied; the literature predicts weak/variable relationships. The two-lake depth contrast is confounded. The study is a modest measurement audit, not a novel early-warning contribution.

If a novel early-warning result is required, **PAUSE**.

### 3.4 Competition

The study can be competitive at school level if framed as a rigorous measurement/negative-result study. It is unlikely to compete as a novel early-warning method. Earth Prize/GENIUS may require a stronger applied/innovation angle; ISEF/EUCYS may require stronger novelty.

## 4. Human decisions required

The full table is in `PRE_ANALYSIS_PLAN.md` §10. The most consequential:

| ID | Decision | Recommended |
|---|---|---|
| D-01 | Comparability = rank association, not absolute agreement | Accept |
| D-02 | Buffalo Pound endpoint = supplied biomass, not derived biovolume | Accept |
| D-03 | Mendota 0.5 m vs 0–8 m, no depth correction | Accept |
| D-04 | Turner/YSI separate, no cross-calibration | Accept |
| D-05 | Primary QC: retain `H`; exclude `C/E/G/O`; Buffalo Pound blank only | Accept, with strict-unflagged sensitivity |
| D-06 | Full-day means; Buffalo Pound nighttime sensitivity | Accept |
| D-07 | Same-day + ±1-day only | Accept |
| D-08 | Buffalo Pound replicate mean; sum/first sensitivity | Accept |
| D-09 | Retain 2019-07-17 with exclusion sensitivity | Accept |
| D-10 | Bootstrap/no-p-value uncertainty | Accept |
| D-11 | n<10 stratum: no ρ, show points | Accept |
| D-12 | Claims matrix | Accept |
| D-13 | Proceed vs pause based on originality | Decide |
| D-14 | Licence/competition compliance (CC BY-NC-SA) | Review |
| D-15 | Explicit approval to begin analysis | Required |

## 5. Blockers

1. **No approval.** The protocol is proposed, not approved.
2. **Originality.** Low–moderate; may be insufficient for top competitions.
3. **Mendota depth mismatch.** 0.5 m vs 0–8 m; no correction.
4. **Buffalo Pound two seasons.** 42 dates; no non-bloom baseline.
5. **Date-only biology.** No sample times; no onset/lead.
6. **Turner/YSI non-comparability.** No cross-calibration.
7. **No calibration/detection limits.** RFU is a relative signal.
8. **2019-07-17 anomaly.** Unresolved; retained and flagged.
9. **Painter licence.** CC BY-NC-SA 4.0; competition use needs review.
10. **No researcher reply/data.** Buffalo Pound remains pending/exploratory; no additional data assumed.

## 6. Next single action

**Send the protocol to human review.** The review should resolve D-01–D-14 and record D-15 explicitly.

Do not begin analysis, do not contact researchers, and do not acquire data while the review is pending.

## 7. If approved

Sequence:

1. Build and audit analysis populations (flow table, excluded-date list).
2. Produce descriptive summaries and figures.
3. Compute P1–P4 with Spearman and descriptive intervals.
4. Compute secondary/exploratory analyses.
5. Compute sensitivity analyses S-A to S-J.
6. Draft report with claims-matrix check.
7. Independent review.
8. Human sign-off.
9. Only then consider competition/communication use, subject to licence review.

## 8. If not approved

Options:

- **Revise the protocol** to address reviewer concerns, then re-review.
- **Narrow further** to a single lake or a single pigment, if that makes the question more defensible (but do not claim novelty from narrowing).
- **PAUSE — INSUFFICIENT SCIENTIFIC FEASIBILITY** if a novel early-warning result is required or the measurement study is judged too incremental.
- **PIVOT** only with a specific, evidence-based alternative and a new protocol; no pivot is proposed here.

## 9. Governance

- **Gate 2 remains PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- No labels, event intervals, confirmatory models, hypothesis tests, threshold optimisation, protocol changes, external contacts, uploads, commits or pushes were made.
- Raw data and prior evidence remain unchanged.
- No analysis may begin until the protocol is reviewed and explicitly approved.
