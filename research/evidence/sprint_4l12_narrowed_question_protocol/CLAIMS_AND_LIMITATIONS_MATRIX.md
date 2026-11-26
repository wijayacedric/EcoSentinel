# Claims and Limitations Matrix

**Sprint:** 4L.12  
**Status:** PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Date:** 2026-11-24

> **No analysis may begin until this protocol has been reviewed and explicitly approved. This matrix governs what may be written after analysis, not what has been found.**

## 1. Purpose

This document defines the boundary between permissible descriptive statements and prohibited overclaims.

Every proposed conclusion must pass three tests:

1. **Evidence test:** Is there a pre-specified analysis that could support it?
2. **Confounder test:** Are the remaining confounders stated?
3. **Wording test:** Is the sentence calibrated to a descriptive association rather than agreement, validation, prediction, causation, or early warning?

If a sentence fails any test, it is not permitted.

## 2. Claim hierarchy

| Level | Permitted? | Example | Reason |
|---|---|---|---|
| **D1. Descriptive univariate** | Yes | “Median cyanobacteria biovolume was X in the included Mendota dates.” | Direct summary of observed data |
| **D2. Descriptive bivariate association** | Yes, with caveats | “Turner chlorophyll rank-associated positively with cyanobacteria biovolume (Spearman ρ = ..., n = ...).” | Pre-specified descriptive statistic |
| **D3. Descriptive comparison** | Yes, with caveats | “The descriptive ρ was higher in summer than in spring in this sample.” | Observational strata; no causal claim |
| **D4. Measurement comparability** | Only as “relative rank concordance” | “The sensor and microscopy ranked dates similarly in this sample.” | Not agreement, not validation |
| **M1. Mechanistic/causal** | **No** | “Depth alignment causes better agreement.” | Confounded; no experiment |
| **M2. Predictive/validation** | **No** | “The sensor predicts biovolume with X% accuracy.” | No calibration/holdout |
| **A1. Applied/management** | **No** | “The sensor is fit for bloom early warning.” | No event/label/FAR evaluation |

## 3. Claims matrix

### C01 — Chlorophyll rank association with cyanobacteria biovolume (Mendota, Turner)

| Element | Specification |
|---|---|
| **Candidate claim** | In Lake Mendota during the Turner era, same-day chlorophyll fluorescence is positively rank-associated with microscopy-derived cyanobacteria biovolume. |
| **Evidence that would support** | A positive Spearman ρ with n reported; a consistent positive direction across the primary, strict-unflagged, and ±1-day sensitivity analyses; no single year dominating the estimate. |
| **Evidence that would not support** | Sign reversal across pre-specified sensitivities; an interval spanning a wide range from negative to positive; the estimate driven by one year or one extreme date. |
| **Remaining confounders** | 0.5 m sensor vs 0–8 m composite; date-only biology; 14-day median sampling; diel quenching in the daily average; community composition; taxonomy changes; sensor fouling/calibration; spatial offset ~106 m. |
| **Acceptable wording** | “In the included Mendota Turner-era dates, chlorophyll fluorescence showed a [positive/negative/near-zero] rank association with cyanobacteria biovolume (Spearman ρ = ..., n = ...; descriptive interval ...). This is a date-level association, not agreement or validation.” |
| **Prohibited wording** | “Chlorophyll validates cyanobacteria biovolume”; “the sensor measures cyanobacteria biomass”; “chlorophyll predicts biovolume”; “the sensor is accurate.” |

### C02 — Phycocyanin rank association with cyanobacteria biovolume (Mendota, Turner)

| Element | Specification |
|---|---|
| **Candidate claim** | In Lake Mendota during the Turner era, same-day phycocyanin fluorescence is positively rank-associated with microscopy-derived cyanobacteria biovolume. |
| **Evidence that would support** | As C01, for phycocyanin. |
| **Evidence that would not support** | As C01; additionally, a phycocyanin association that disappears when cyanobacteria cell density is used instead of biovolume would indicate endpoint sensitivity. |
| **Remaining confounders** | As C01, plus phycocyanin content varies by taxon, morphology, light history, and temperature; colonial *Microcystis* and picocyanobacteria can decouple fluorescence from biovolume. |
| **Acceptable wording** | “In the included Mendota Turner-era dates, phycocyanin fluorescence showed a [direction] rank association with cyanobacteria biovolume (Spearman ρ = ..., n = ...). This does not establish a calibrated phycocyanin–biovolume relationship.” |
| **Prohibited wording** | “Phycocyanin is a validated proxy for cyanobacteria biomass”; “phycocyanin accurately tracks biovolume”; “the sensor can be used as a biomass monitor.” |

### C03 — Chlorophyll rank association with cyanobacteria biomass (Buffalo Pound)

| Element | Specification |
|---|---|
| **Candidate claim** | In Buffalo Pound Lake in 2018–2019, same-day chlorophyll fluorescence is positively rank-associated with microscopy-derived cyanobacteria biomass at 0.8 m. |
| **Evidence that would support** | A positive Spearman ρ with n reported; consistency across 2018 and 2019 separately; robustness to B7 and 2019-07-17 sensitivity analyses. |
| **Evidence that would not support** | A positive pooled ρ driven entirely by one year; sign reversal when B7 is included; dependence on the 2019-07-17 anomaly. |
| **Remaining confounders** | Only 42 dates/two seasons; bloom-season sampling only; no non-bloom baseline; date-only biology; 10-minute daily mean includes diel quenching; community shifts (Dolichospermum vs Planktothrix); B7 fouling; RFU not concentration; no detection limit. |
| **Acceptable wording** | “Across the 42 Buffalo Pound dates (41–42 depending on QC), chlorophyll fluorescence showed a [direction] rank association with cyanobacteria biomass (Spearman ρ = ..., n = ...). The two-season design and bloom-season sampling limit inference.” |
| **Prohibited wording** | “Chlorophyll detects Buffalo Pound blooms”; “the sensor is a validated biomass monitor in Buffalo Pound”; “the relationship is stable across seasons/years.” |

### C04 — Phycocyanin rank association with cyanobacteria biomass (Buffalo Pound)

| Element | Specification |
|---|---|
| **Candidate claim** | In Buffalo Pound Lake in 2018–2019, same-day phycocyanin fluorescence is positively rank-associated with microscopy-derived cyanobacteria biomass at 0.8 m. |
| **Evidence that would support** | As C03, for phycocyanin; consistency with the known *Planktothrix* autumn phase would need to be examined, not assumed. |
| **Evidence that would not support** | A positive pooled ρ driven by the mid-summer *Dolichospermum* phase only; a near-zero autumn association; dependence on B7 or the 2019-07-17 anomaly. |
| **Remaining confounders** | As C03, plus phycocyanin per biovolume differs among *Dolichospermum*, *Planktothrix*, *Microcystis*, and picocyanobacteria; prior work reported an autumn *Planktothrix* bloom that was not detected by sensor or laboratory chlorophyll-a. |
| **Acceptable wording** | “In the included Buffalo Pound dates, phycocyanin fluorescence showed a [direction] rank association with cyanobacteria biomass (Spearman ρ = ..., n = ...). Prior work reported taxon-specific detection limits; this study does not test them directly.” |
| **Prohibited wording** | “Phycocyanin detects all cyanobacteria”; “the sensor captures the autumn Planktothrix bloom”; “phycocyanin is a validated biomass proxy.” |

### C05 — Seasonal difference

| Element | Specification |
|---|---|
| **Candidate claim** | The rank association differs by season in one or both lakes. |
| **Evidence that would support** | Pre-specified seasonal ρ values with n ≥ 10 per stratum; a consistent ordering across sensitivity analyses; not driven by one year or one outlier. |
| **Evidence that would not support** | Seasonal strata with n < 10; an ordering that reverses when one year is removed; a difference driven solely by the 2019-07-17 anomaly or a single bloom phase. |
| **Remaining confounders** | Season is confounded with community composition, stratification, sampling frequency, sensor fouling, and biology timing; seasons are observational; sample sizes are small. |
| **Acceptable wording** | “In this sample, the descriptive ρ was higher in summer than in spring (n = ... vs ...). The strata are observational and small; this is not evidence of a seasonal effect.” |
| **Prohibited wording** | “Season significantly moderates the sensor–biomass relationship”; “the sensor is more accurate in summer”; “seasonal validation.” |

### C06 — Sensor-era difference (Mendota Turner vs YSI)

| Element | Specification |
|---|---|
| **Candidate claim** | The Turner and YSI eras show different descriptive associations with cyanobacteria biovolume. |
| **Evidence that would support** | Separate era-specific ρ values with n reported; the Turner era has 128/139 dates, the YSI era 21/22; the difference is described, not tested. |
| **Evidence that would not support** | Treating the eras as comparable; concatenating them; interpreting the difference as an instrument effect when the periods and sampling differ. |
| **Remaining confounders** | Different periods, instruments, calibration, optical geometry, RFU scales, sampling frequency, community composition, and biology dates; YSI n is very small. |
| **Acceptable wording** | “The Turner-era and YSI-era descriptive associations were [similar/different] in direction/magnitude (Turner ρ = ..., n = ...; YSI ρ = ..., n = ...). The eras are not calibrated to each other and the periods differ.” |
| **Prohibited wording** | “Turner and YSI are interchangeable”; “the YSI sensor is more accurate”; “the era difference is caused by the instrument.” |

### C07 — Cross-lake depth-alignment contrast

| Element | Specification |
|---|---|
| **Candidate claim** | The depth-aligned Buffalo Pound setting shows a stronger association than the depth-mismatched Mendota setting, consistent with a depth-alignment effect. |
| **Evidence that would support** | A side-by-side descriptive difference that is large and consistent across sensitivity analyses, with all confounders stated. |
| **Evidence that would not support** | Any causal language; a difference explained equally well by lake type, community, instrument, period, sampling, or endpoint; a difference that reverses under sensitivity. |
| **Remaining confounders** | Lake type/morphometry, trophic state, community composition, sensor instrument, RFU scale, period, sampling frequency, biology depth, taxonomy, QC, endpoint (biovolume vs biomass), spatial setting. Depth is fully confounded with lake identity. |
| **Acceptable wording** | “The Buffalo Pound setting (0.82 m sensor vs 0.8 m sample) showed a [direction/size] descriptive association, while the Mendota setting (0.5 m sensor vs 0–8 m composite) showed [direction/size]. This is consistent with, but does not test, a depth-alignment hypothesis; the lakes differ in many other respects.” |
| **Prohibited wording** | “Depth alignment improves agreement”; “the two-lake comparison shows that depth matters”; “Buffalo Pound validates the Mendota sensor”; “the difference is due to depth.” |

### C08 — Sensor validation / biological measurement validity

| Element | Specification |
|---|---|
| **Candidate claim** | Chlorophyll or phycocyanin fluorescence is a validated measure of cyanobacteria biomass. |
| **Evidence that would support** | A dedicated calibration experiment with independent concentrations, replicated across taxa, temperatures, morphologies, and ranges; documented accuracy, bias, detection limits, and uncertainty; external validation. |
| **Evidence that would not support** | A rank correlation; a descriptive regression; a single lake; a single season; no calibration; no detection limits; no external validation. |
| **Remaining confounders** | RFU is instrument-specific; pigment content varies; quenching; fouling; community composition; no concentration conversion. |
| **Acceptable wording** | “The analysis describes a rank association; it does not validate the sensor as a biomass measurement.” |
| **Prohibited wording** | “Validated proxy”; “validated sensor”; “accurate biomass measurement”; “measurement validation.” |

### C09 — Predictive performance

| Element | Specification |
|---|---|
| **Candidate claim** | The sensor predicts cyanobacteria biovolume/biomass with a stated accuracy. |
| **Evidence that would support** | A pre-specified predictive model trained and tested on independent data, with error metrics, calibration, and external validation. |
| **Evidence that would not support** | Any in-sample correlation; any R² from the same data; any descriptive regression. |
| **Remaining confounders** | No train/test split; no independent events; no calibration; small n; temporal autocorrelation; lake-specific relationships. |
| **Acceptable wording** | “No predictive model is proposed; the study does not estimate predictive accuracy.” |
| **Prohibited wording** | “Predicts with X% accuracy”; “forecast skill”; “predictive R²”; “the sensor can forecast biomass.” |

### C10 — Bloom detection / bloom/non-bloom classification

| Element | Specification |
|---|---|
| **Candidate claim** | The sensor detects blooms or classifies bloom/non-bloom dates. |
| **Evidence that would support** | An approved, independent bloom/non-bloom definition; adequate events and non-events; a pre-specified classifier; sensitivity/specificity/PPV/NPV with uncertainty; external validation. |
| **Evidence that would not support** | No event definition; no non-bloom exposure; no independent labels; a correlation with biovolume; a threshold chosen post hoc. |
| **Remaining confounders** | Bloom definition absent; non-bloom baseline absent; two seasons in Buffalo Pound; Mendota rejected for validation; taxonomic and depth mismatch. |
| **Acceptable wording** | “The study does not define or detect blooms; it compares sensor fluorescence with a continuous abundance endpoint.” |
| **Prohibited wording** | “Bloom detection”; “bloom accuracy”; “true positive/false positive”; “the sensor identifies blooms”; “bloom/non-bloom classification.” |

### C11 — Early warning / lead time

| Element | Specification |
|---|---|
| **Candidate claim** | The sensor provides earlier warning of cyanobacterial blooms than conventional monitoring. |
| **Evidence that would support** | A defined bloom onset with time-stamped, sub-weekly biology; a pre-specified warning horizon; a leakage-resistant evaluation; matched false-alarm rates; adequate events/non-events. |
| **Evidence that would not support** | Date-only biology; 14-day Mendota sampling; 4–16-day Buffalo Pound gaps; no event definition; no non-bloom exposure; no matched-FAR denominator. |
| **Remaining confounders** | All of the above; no onset; no lead time; no alarm evaluation. |
| **Acceptable wording** | “The study is not an early-warning evaluation and cannot estimate lead time or false-alarm rates.” |
| **Prohibited wording** | “Early warning”; “lead time”; “warns X days before a bloom”; “matched false-alarm rate”; “alarm performance.” |

### C12 — Whole-water-column representation

| Element | Specification |
|---|---|
| **Candidate claim** | A surface sensor represents whole-water-column cyanobacteria biomass. |
| **Evidence that would support** | Depth-resolved paired profiles; a validated depth-integration model; stratification-stratified validation. |
| **Evidence that would not support** | A 0.5 m sensor vs 0–8 m composite; a 0.82 m sensor vs 0.8 m sample; no depth profiles at the sensor. |
| **Remaining confounders** | Vertical heterogeneity, stratification, surface scums, buoyancy regulation, light acclimation, grazing. |
| **Acceptable wording** | “The sensor measures a near-surface signal; it is not a whole-column measurement.” |
| **Prohibited wording** | “Represents whole-water-column biomass”; “captures the 0–8 m community”; “surface sensor equals column biomass.” |

### C13 — Taxon-specific detection (e.g., *Planktothrix*)

| Element | Specification |
|---|---|
| **Candidate claim** | The sensor misses *Planktothrix* or other specific taxa. |
| **Evidence that would support** | A pre-specified taxon-specific comparison with adequate counts; a documented taxonomic crosswalk; a consistent pattern across dates/years. |
| **Evidence that would not support** | A broad cyanobacteria total; a single date; an unapproved species mapping; prior literature alone. |
| **Remaining confounders** | Pigment content differs by taxon; morphology/colony size; taxonomy; depth; sensor optics; prior work already reported a *Planktothrix* bloom not detected by sensor/lab chlorophyll-a in Buffalo Pound. |
| **Acceptable wording** | “Prior work in Buffalo Pound reported an autumn *Planktothrix* bloom that was not detected by sensor or laboratory chlorophyll-a (Painter et al. 2022). This study does not directly test taxon-specific detection unless an approved crosswalk is added.” |
| **Prohibited wording** | “Our results prove the sensor misses *Planktothrix*”; “the sensor cannot detect cyanobacteria”; “taxon-specific validation.” |

### C14 — Toxicity / toxin risk

| Element | Specification |
|---|---|
| **Candidate claim** | The sensor indicates toxicity or toxin risk. |
| **Evidence that would support** | Paired toxin measurements with verified units, fractions, and sample identity; a pre-specified toxicity endpoint; independent validation. |
| **Evidence that would not support** | Pigment fluorescence; genus names; unverified toxin files; no toxin endpoint in the primary analysis. |
| **Remaining confounders** | Toxin production varies by strain, gene presence, nutrients, and growth phase; pigment is not toxin. |
| **Acceptable wording** | “The study does not measure toxicity or toxin risk.” |
| **Prohibited wording** | “Toxic bloom”; “toxin risk”; “the sensor detects toxicity”; “harmful algal bloom alert.” |

### C15 — No association / sensor unusable

| Element | Specification |
|---|---|
| **Candidate claim** | There is no association, or the sensor is unusable. |
| **Evidence that would support** | A pre-specified ρ near zero with a descriptive interval that excludes a strong positive association, consistent across sensitivities; adequate n; no evidence of range restriction. |
| **Evidence that would not support** | Small n; range restriction; depth mismatch; date-only biology; a near-zero ρ that is compatible with a moderate positive association; one lake/season. |
| **Remaining confounders** | As C01–C04; “no association” is not “no value.” |
| **Acceptable wording** | “No monotonic association was detected in this sample (Spearman ρ = ..., n = ...; descriptive interval ...). This does not establish that the sensor is unrelated to biomass under other conditions.” |
| **Prohibited wording** | “The sensor is useless”; “sensors cannot measure biomass”; “there is no relationship in nature.” |

### C16 — Data-quality limitation

| Element | Specification |
|---|---|
| **Candidate claim** | Data quality limits the interpretation. |
| **Evidence that would support** | Documented flags, missingness, anomalies, calibration gaps, detection-limit gaps, and sensitivity analyses showing material dependence. |
| **Evidence that would not support** | Asserting unusability without quantifying the limitation; ignoring the sensitivity analyses. |
| **Remaining confounders** | All measurement and sampling limitations. |
| **Acceptable wording** | “Interpretation is limited by [specific flags/missingness/anomalies/calibration gaps]; the sensitivity analysis shows [direction of change].” |
| **Prohibited wording** | “The data are unusable”; “the results are invalid”; “no conclusion is possible” (unless the specific analysis truly cannot be computed). |

### C17 — Turner/YSI interchangeability

| Element | Specification |
|---|---|
| **Candidate claim** | Turner and YSI chlorophyll/phycocyanin can be used interchangeably or converted. |
| **Evidence that would support** | A documented cross-calibration with independent paired data across the full range, uncertainty, and external validation. |
| **Evidence that would not support** | The observed orders-of-magnitude difference; no conversion equation; different optical systems. |
| **Remaining confounders** | Instrument optics, calibration, units, fouling, deployment period. |
| **Acceptable wording** | “Turner and YSI RFU are not comparable on the raw scale and are analysed separately.” |
| **Prohibited wording** | “Interchangeable”; “converted”; “cross-calibrated”; “equivalent.” |

### C18 — Generalisation

| Element | Specification |
|---|---|
| **Candidate claim** | The results generalise to other lakes, years, or cyanobacteria communities. |
| **Evidence that would support** | A multi-lake, multi-year, standardised design with external validation. |
| **Evidence that would not support** | Two lakes, two Buffalo Pound seasons, one Mendota record, different instruments and protocols. |
| **Remaining confounders** | Lake type, community, instrument, period, sampling, depth, QC, endpoint. |
| **Acceptable wording** | “The findings apply to the included dates in these two lakes and do not establish a general sensor–biomass relationship.” |
| **Prohibited wording** | “In lakes generally”; “universal proxy”; “globally applicable.” |

### C19 — Absolute agreement

| Element | Specification |
|---|---|
| **Candidate claim** | The sensor and microscopy agree in absolute terms. |
| **Evidence that would support** | Same quantity, same units, paired measurements, bias and limits of agreement, calibration, replicates. |
| **Evidence that would not support** | RFU vs biovolume/biomass; different units; no conversion; no replicates. |
| **Remaining confounders** | Scale, quantity, calibration, depth, time. |
| **Acceptable wording** | “Absolute agreement is not estimable because the sensor and microscopy measure different quantities on different scales.” |
| **Prohibited wording** | “Good agreement”; “limits of agreement”; “bias correction”; “concordance.” |

### C20 — Causal depth effect

| Element | Specification |
|---|---|
| **Candidate claim** | Depth alignment causes a difference in sensor–microscopy association. |
| **Evidence that would support** | A controlled comparison with depth as the only manipulated difference; paired profiles; randomisation or matching on all other factors. |
| **Evidence that would not support** | Two different lakes, instruments, periods, communities, protocols, and endpoints. |
| **Remaining confounders** | Everything that differs between Mendota and Buffalo Pound. |
| **Acceptable wording** | “The two settings differ in depth alignment, but the comparison is confounded and cannot isolate a depth effect.” |
| **Prohibited wording** | “Depth alignment causes”; “depth explains”; “the two-lake experiment shows.” |

## 4. What positive, negative, and null results would mean

### 4.1 Positive association

A positive ρ means that dates with higher sensor fluorescence tended to have higher microscopy abundance **in the included sample**. It does **not** mean:

- the sensor is accurate;
- the sensor is calibrated;
- the sensor can be used for management;
- the sensor captures all taxa;
- the sensor represents the whole column;
- the relationship holds in other lakes/seasons.

### 4.2 Negative association

A negative ρ may indicate:

- a real inverse relationship at the sampled dates;
- a depth/community mismatch;
- quenching or fouling;
- range restriction;
- a statistical artifact of small n or influential dates.

It does **not** prove the sensor is “wrong” or “useless.” Report it descriptively and investigate the pre-specified sensitivities.

### 4.3 Near-zero association

A near-zero ρ may indicate:

- no monotonic relationship in the sample;
- a nonlinear relationship;
- different taxa dominating at different times;
- depth mismatch;
- date-only matching;
- small n/range restriction.

It does **not** prove “no relationship in nature.” Report the estimate and the limitations.

## 5. Mandatory limitations paragraph

Every report must include a paragraph equivalent to:

> This is a descriptive, date-level comparison of two lakes. The sensor and microscopy measurements differ in quantity, scale, depth, timing, and sampling frequency. Mendota compares a 0.5 m sensor with a 0–8 m composite over 2006–2020; Buffalo Pound compares a 0.82 m sensor with a 0.8 m sample over two seasons (2018–2019). Turner and YSI instruments are not cross-calibrated and are analysed separately. Mendota biovolume and Buffalo Pound biomass are not numerically equivalent and are not pooled. The analysis does not define blooms, estimate toxicity, validate the sensor, predict biomass, or evaluate early warning. Associations are descriptive and may reflect measurement artifacts, depth/community mismatch, or sampling selection. The results apply only to the included dates and do not generalise to other lakes or periods.

## 6. Prohibited phrases

The following phrases are prohibited in any project output based on this study:

- “validated proxy”
- “validated sensor”
- “accurate biomass measurement”
- “sensor accuracy”
- “predicts biomass”
- “forecast skill”
- “early warning”
- “lead time”
- “bloom detection”
- “bloom/non-bloom classification”
- “true positive / false positive”
- “matched false-alarm rate”
- “toxicity risk”
- “toxic bloom”
- “whole-water-column biomass”
- “depth alignment improves agreement”
- “depth causes”
- “Turner and YSI are interchangeable”
- “cross-calibrated”
- “absolute agreement”
- “limits of agreement”
- “concordance”
- “generalises to lakes”
- “proves”
- “demonstrates causality”

If a sentence requires one of these phrases to be interesting, the study cannot support the sentence.

## 7. Governance

- **Gate 2 remains PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- This matrix is a constraint on future reporting, not a report of findings.
- No analysis may begin until the protocol is reviewed and explicitly approved.
