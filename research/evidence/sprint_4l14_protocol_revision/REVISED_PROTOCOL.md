# Revised Protocol

**Sprint:** 4L.14  
**Status:** PROPOSED — NOT APPROVED  
**Supersedes:** Sprint 4L.12 proposed protocol for human-review purposes  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Date:** 2026-11-24

> **This is a revised protocol for human review. It does not approve the protocol, any of the 15 decisions, or Gate 2. No analysis is authorised.**

## 0. Document precedence

Sprint 4L.12 and Sprint 4L.13 remain unchanged as historical records. For the revised proposal:

- this `REVISED_PROTOCOL.md` and the 4L.14 supporting documents govern;
- where the 4L.12 statistical specification, claims matrix, or question wording conflicts with 4L.14, 4L.14 governs;
- the 4L.12 files are not amended in place.

## 1. One-page summary

**Question:** In Lake Mendota (2006–2020) and Buffalo Pound Lake (2018–2019), among same-day date-level co-occurrences and analysed as two separate lake-specific case studies, what are the direction and magnitude of the rank association between surface chlorophyll and phycocyanin fluorescence and independent microscopy-derived cyanobacteria biovolume (Mendota) or cyanobacteria biomass (Buffalo Pound), and how do these associations differ descriptively across seasons and sensor eras?

**Design:** Two independent descriptive case studies; no pooling; no depth-effect claim.

**Candidate primary estimands:** P1–P4 (four sensor–endpoint pairs; not four independent quantities). P3/P4 are recommended for downgrade to exploratory pending D-02 verification.

**Primary statistic:** Spearman’s ρ, with n and a descriptive sensitivity range.

**No:** p-values, absolute agreement, calibration, prediction, bloom labels, event intervals, thresholds, early warning, matched FAR, causal depth claims.

**Sample size:** 128/139/42/42 are upper bounds under the strict 4L.10 unflagged rule; actual n is unknown and must be enumerated in a count-only audit after approval.

**Endpoints:** Mendota biovolume (µm³ mL⁻¹); Buffalo Pound biomass (mg m⁻³), a derived microscopy quantity. Not numerically equivalent; never pooled.

**QC:** Explicit decision tree; no imputation; primary/sensitivity rules; negative RFU retained primary with exclusion sensitivity; B7 excluded primary with inclusion sensitivity.

**Uncertainty:** Mendota leave-one-year-out range + optional season-year block sensitivity; Buffalo Pound no reliable interval, separate 2018/2019 and leave-one-date-out range.

**Status:** PROPOSED — NOT APPROVED. Gate 2 PAUSED / Option C. No analysis until D-15.

## 2. Background and rationale

The original EcoSentinel question asked whether persistent changes in relationships between freshwater environmental variables provide earlier warning of cyanobacterial blooms than conventional monitoring at comparable false-alarm rates. That question remains untestable with the available evidence:

- 0 independently reconstructed bloom events;
- 0 defensible non-bloom intervals;
- no approved event/non-event definition;
- no time-stamped/sub-weekly biology;
- no matched-FAR denominator.

The revised study is a **descriptive measurement audit**, not an early-warning validation. It asks whether surface pigment fluorescence ranks with independent microscopy-derived cyanobacteria abundance in two lake-specific case studies, and how the association varies descriptively across seasons and sensor eras.

## 3. Research question

### 3.1 Primary question

> In Lake Mendota (2006–2020) and Buffalo Pound Lake (2018–2019), among same-day date-level co-occurrences and analysed as two separate lake-specific case studies, what are the direction and magnitude of the rank association between surface chlorophyll and phycocyanin fluorescence and independent microscopy-derived cyanobacteria biovolume (Mendota) or cyanobacteria biomass (Buffalo Pound), and how do these associations differ descriptively across seasons and sensor eras?

### 3.2 Definitions

- **Same-day date-level co-occurrence:** biological and sensor observations share a calendar date; sample time is unknown; sensor value is a daily summary; not a paired/same-time/same-parcel measurement.
- **Rank association:** Spearman’s ρ; monotonic association; not agreement/calibration/prediction/validation.
- **Direction and magnitude:** sign and value of ρ; n; descriptive sensitivity range; no strong/weak labels.
- **Two separate case studies:** Mendota and Buffalo Pound analysed separately; no pooling; no depth-effect claim.
- **Descriptively across seasons/eras:** observational strata; no interaction tests; no causal attribution.

### 3.3 Original early-warning question

Preserved as a long-term aspiration, not the current analysis. No part of this protocol authorises an early-warning analysis.

## 4. Design: two case studies

### 4.1 Case 1 — Lake Mendota

- Sensor: 0.5 m; Turner chlorophyll/phycocyanin 2006–2019; YSI 2019–2020 secondary.
- Biology: 0–8 m composite; 402 dates total; 400 at 0–8 m; 2 at 0–2 m (excluded).
- Cadence: median 14 days; date-only.
- Primary estimates: P1/P2 (Turner).
- Secondary: YSI era (P1/P2 analogue), with n ≈ 21/22 maximum.

### 4.2 Case 2 — Buffalo Pound Lake

- Sensor: 0.82 m shallow sonde; 10-minute data; 2018–2019.
- Biology: 0.8 m; 42 dates (25 in 2018, 17 in 2019); median 4/8 days; date-only.
- Primary estimates: P3/P4.
- No deep sensors, YSI profiles, thermistors, toxins, nutrients, or heterocytes in primary/secondary estimands.

### 4.3 No pooling

- No pooled Mendota–Buffalo Pound correlation/regression.
- No biomass-to-biovolume conversion.
- No RFU-to-biomass conversion.
- No Turner/YSI concatenation.
- No claim that Buffalo Pound validates Mendota.
- No claim that lake differences identify a depth effect.

## 5. Candidate primary estimands

| ID | Lake / era | Sensor | Biological endpoint | Maximum possible n | Actual n known? |
|---|---|---|---|---:|---|
| P1 | Mendota / Turner 2006–2019 | Chlorophyll RFU | Cyanobacteria biovolume (0–8 m) | 128 | No |
| P2 | Mendota / Turner 2006–2019 | Phycocyanin RFU | Cyanobacteria biovolume (0–8 m) | 139 | No |
| P3 | Buffalo Pound / YSI 6600 2018–2019 | Chlorophyll RFU | Cyanobacteria biomass (0.8 m) | 42 | No |
| P4 | Buffalo Pound / YSI 6600 2018–2019 | Phycocyanin RFU | Cyanobacteria biomass (0.8 m) | 42 | No |

The n values are upper bounds under the strict 4L.10 “unflagged only” rule. They are not actual primary n. Actual n must be enumerated after approval under the revised QC rules. P1/P2 share the Mendota endpoint/dates; P3/P4 share the Buffalo Pound endpoint/dates; they are not independent quantities.

**P3/P4 status:** recommended **downgrade to exploratory** pending D-02 verification of the Buffalo Pound biomass derivation. Until the data custodian accepts the derivation, P3/P4 are not approved as primary estimands. If verification succeeds, they may be restored to primary subject to the count audit; if it fails, they are unsuitable for primary analysis.

## 6. Eligibility and sample size

Full rules: `ESTIMAND_AND_SAMPLE_ELIGIBILITY_SPECIFICATION.md`.

### 6.1 Mendota

- `lakeid = ME`;
- `depth_range = 0-8m`;
- 2006-07-09 to 2020-12-10;
- cyanobacteria biovolume total (sum of `biovolume_conc` for `division = Cyanophyta`);
- same-day Turner chlorophyll or phycocyanin value passing the QC rules;
- station rule: station 1 if present, otherwise blank; multiple other stations → `UNRESOLVED_STATION` primary, sensitivity all stations.

### 6.2 Buffalo Pound

- one of the 42 documented dates in 2018–2019;
- `Depth = 0.8`;
- cyanobacteria biomass total (sum of `Biomass_mg_m3` for `Group = Cyanophyte`; `Phylum = Cyanophyta` consistency check);
- same-day shallow chlorophyll or phycocyanin daily mean;
- ≥50% of expected 10-minute values and both halves of the day represented;
- replicate rule: mean before summing primary; sum/first-row sensitivity.

### 6.3 Count-only audit

After D-15 approval and before any correlation:

- enumerate total dates → window → depth → any sensor → numeric sensor → QC pass → station/group/replicate → coverage → final n;
- report n by year/season;
- report excluded dates with reason codes;
- report included vs excluded biological endpoint distributions (descriptive only);
- report B7 overlap, negative RFU counts, H counts, coverage failures.

This is not a correlation analysis and does not create a cleaned dataset.

### 6.4 Minimum n

No minimum is set in this sprint because actual n is unknown. The statistical reviewer must set an overall minimum n after the count audit and before estimation, justified by precision/dependence, not by the result. Seasonal strata: n < 10 → no stratum ρ; show points and n.

## 7. Biological endpoints

Full review: `BIOLOGICAL_ENDPOINT_AND_BIOMASS_REVIEW.md`.

### 7.1 Mendota

- Total cyanobacteria biovolume, µm³ mL⁻¹;
- broad `Cyanophyta` total;
- no species-level primary;
- 0–8 m composite;
- taxonomy non-stationarity, repeated rows, anomalies, no detection limits;
- measurement-independent of sensor; not independent of lake processes.

### 7.2 Buffalo Pound

- Total cyanobacteria biomass, mg m⁻³;
- `Biomass_mg_m3` is a **derived microscopy quantity**, consistent with:
  \[
  \text{Biomass}_{mg\,m^{-3}} \approx \text{Cell\_Volume}_{\mu m^3} \times \text{Cell\_Density}_{L^{-1}} \times 10^{-6}
  \]
  under a 1 g cm⁻³ density assumption; this is a volume-derived, wet-weight-equivalent biomass proxy, not dry weight, carbon biomass, or a direct gravimetric measurement;
- verification check: 2018 all 817 positive rows median ratio 1.000 × 10⁻⁶ (range 9.87 × 10⁻⁷–1.0366 × 10⁻⁶); 2019 all 405 positive rows median 1.000 × 10⁻⁶ (range 9.55 × 10⁻⁷–1.0227 × 10⁻⁶); consistent with rounding;
- not a direct measurement; not biovolume; not numerically equivalent to Mendota;
- 2018/2019 schema/taxonomy differences; replicates unresolved; 2019-07-17 unresolved;
- P3/P4 recommended **downgrade to exploratory** pending data-custodian verification of the inferred formula and density assumption; restored to primary only if verification succeeds.

### 7.3 No pooling

Do not pool biovolume and biomass; do not convert; do not treat them as the same endpoint.

## 8. Sensor variables

### 8.1 Primary

- P1: `avg_chlor_rfu_turner`;
- P2: `avg_phyco_rfu_turner`;
- P3: `ChlRFUShallow_RFU`;
- P4: `BGPCShallowRFU_RFU`.

### 8.2 Secondary/contextual

- Mendota YSI chlorophyll/phycocyanin (2019–2020), separate era;
- DO mg/L and % saturation, water temperature (contextual);
- Buffalo Pound temperature/DO (contextual).

### 8.3 Excluded from biological comparison

- Mendota pH, fDOM, turbidity, specific conductance (short 2019–2020 overlap; ancillary only);
- PAR above/below water (light context; not biomass proxy);
- pCO2, weather;
- Buffalo Pound deep sensors, thermistors, YSI profiles, toxins, nutrients, heterocytes.

## 9. Temporal matching

Full rules: `TEMPORAL_MATCHING_SPECIFICATION.md` (4L.12, unchanged except terminology).

### 9.1 Primary

- same calendar date only;
- Mendota: provider daily mean of 1-minute data; no nighttime reconstruction;
- Buffalo Pound: mean of valid 10-minute values; coverage rule;
- no interpolation/carry-forward/zero-fill;
- no substitution across instruments/depths.

### 9.2 Sensitivity

- ±1-day date-window co-occurrence: **exploratory only**; not a robustness/agreement claim. Where the 4L.12 matching specification calls this a “sensitivity,” this revised protocol demotes it to exploratory.
- no ±3/±7/±14-day windows;
- no lag/lead/onset analysis.

### 9.3 What same-day means

A same-day match is not a same-time or same-parcel measurement. Diel cycles, quenching, and sample-time uncertainty remain.

## 10. QC and missingness

Full rules: `QC_AND_MISSINGNESS_RULES.md`.

### 10.1 Mendota

- `C`, `E`, `G`, `O`: exclude primary; sensitivity include numeric where defined;
- `H`: retain primary if numeric, finite, non-negative; strict sensitivity excludes;
- undocumented flags: `UNRESOLVED_FLAG`; exclude primary; sensitivity include numeric if within bounds;
- negative RFU: retain primary as observed; `SENS_NEG` excludes;
- missing: exclude; no imputation;
- physical bounds: RFU finite; DO 0–50 mg/L; DO sat 0–500%; temp −5–50°C; pH 0–14.

### 10.2 Buffalo Pound

- `M`, `C`: exclude primary; sensitivity where defined;
- `B7`: exclude primary; `SENS_B7` includes;
- Chl/BGPC: 0–100 RFU documented; negative retained as observed; >100 `ABOVE_RANGE` retained primary with flag, `SENS_ABOVE` excludes;
- coverage: ≥50% and both halves; otherwise `EXCLUDED_COVERAGE`; `SENS_COVERAGE`;
- DO 0–50 mg/L; DO sat 0–500%; temp −5–50°C; pH 0–14.

### 10.3 No silent exclusion

Every exclusion has a reason code. Every unresolved value is reported. The count audit must show coverage effects and B7 overlap. No imputation.

## 11. Statistical analysis

This section supersedes the Sprint 4L.12 `STATISTICAL_ANALYSIS_SPECIFICATION.md` where they differ.

### 11.1 Primary statistic

Spearman’s ρ for each of P1–P4, with n and descriptive sensitivity range. Tie-corrected. No p-values.

### 11.2 No relative concordance

“Relative concordance” is **removed** from the operational definition of comparability and from the primary/secondary estimands. It is not computed. Spearman ρ is the sole primary association statistic.

If a future protocol wants a directional check, it must define it formally and justify its added value; it is not part of this protocol.

### 11.3 No Pearson/log-Pearson

Pearson and log-Pearson are **not used**. The protocol relies on Spearman + scatterplots. This avoids an arbitrary transformation and reinforces that the question is rank association, not linear agreement.

### 11.4 No agreement/calibration/prediction

Do not compute Bland–Altman, concordance correlation, ICC, calibration slope/intercept, conversion factors, predictive R²/RMSE/MAE/accuracy, or matched FAR. State why: different quantities/scales, no calibration.

### 11.5 Seasonal/era analysis

- seasonal ρ only if n ≥ 10; otherwise points/n;
- no interaction test;
- Mendota Turner/YSI separate; no concatenation;
- Buffalo Pound single shallow era; 2018/2019 separate descriptive estimates.

## 12. Uncertainty and sensitivity

Full plan: `UNCERTAINTY_AND_SENSITIVITY_PLAN.md`.

### 12.1 Mendota

- ρ, n;
- leave-one-year-out range (min/max/median);
- optional season-year block bootstrap as descriptive sensitivity, not a CI;
- 14 non-exchangeable years; no claim that resampling solves limited temporal coverage.

### 12.2 Buffalo Pound

- ρ, n;
- separate 2018/2019;
- leave-one-date-out range;
- **no bootstrap interval**; state two seasons cannot support a reliable interval.

### 12.3 Descriptive vs inferential

Use “descriptive sensitivity range,” not “confidence interval.” No standard errors, no p-values, no significance.

### 12.4 Sensitivity list

- S-A strict unflagged (H excluded);
- S-B flagged-inclusive;
- S-C negative RFU excluded;
- S-D ±1-day exploratory;
- S-E B7-inclusive;
- S-F 2019-07-17 excluded;
- S-G replicate sum/first;
- S-H station-1 subset;
- S-I lake-specific open-water season.

Pearson/log-Pearson is not part of the protocol (removed; R-11), so there is no log-scale sensitivity.

## 13. 2019-07-17 leverage

Full plan: `2019_07_17_LEVERAGE_PLAN.md`.

- retain and flag primary;
- exclusion sensitivity;
- report rank/leverage, full vs leave-one-date-out ρ, exact Δρ;
- any sign/interpretation change is material;
- no arbitrary cutoff;
- no bloom/non-bloom interpretation.

## 14. Claims and limitations

### 14.1 Permitted

- “In the included dates, [pigment] showed a [direction] rank association with [endpoint] (Spearman ρ = ..., n = ...).”
- “The descriptive pattern was [similar/different] across seasons/eras/cases, with [n] and [confounders].”
- “The two cases differ in depth alignment, but also in lake, instrument, period, community, sampling, QC, and endpoint; the comparison cannot isolate depth.”
- “The result is a date-level association, not agreement or validation.”

### 14.2 Prohibited

- validation/accuracy/prediction/forecast;
- early warning/lead time;
- bloom detection/bloom-non-bloom classification;
- toxicity;
- whole-water-column biomass;
- absolute agreement/limits of agreement/concordance;
- Turner/YSI interchangeability;
- causal depth effect;
- generalisation to other lakes.

### 14.3 Mandatory limitations

Every report must state:

- date-only biology; no sample times;
- sensor daily summary vs unknown sample time;
- Mendota 0.5 m vs 0–8 m; Buffalo Pound 0.82 m vs 0.8 m;
- Turner/YSI non-comparability;
- biovolume vs biomass non-equivalence;
- taxonomy/detection-limit limitations;
- two-season Buffalo Pound;
- no calibration/detection limits;
- no labels/events/early warning.

## 15. Analysis sequence after approval

1. Verify source hashes.
2. Parse/validate; no raw edits.
3. Count-only audit (R-02); no correlations.
4. Descriptive summaries/flow table.
5. P1–P4 Spearman; descriptive ranges.
6. Secondary/exploratory (if any).
7. Sensitivities S-A–S-I.
8. 2019-07-17 leverage.
9. Claims-matrix check.
10. Independent review.

No step may skip the count audit or claims check.

## 16. Human decisions and approval

All 15 decisions remain **OUTSTANDING — NOT APPROVED**. See `UPDATED_HUMAN_DECISION_REGISTER.md`.

Approvals remain distinct:

- scientific reviewer;
- statistical reviewer;
- data custodian;
- Gate 2 governance;
- licence/competition review;
- D-13 continuation/pause;
- D-15 authorisation to begin analysis.

No decision is approved by this protocol.

## 17. Governance

- **Protocol: PROPOSED — NOT APPROVED.**
- **Gate 2: PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- No analysis is authorised until the required human decisions and explicit D-15 approval are recorded.
