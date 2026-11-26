# QC and Missingness Protocol

**Sprint:** 4L.12  
**Status:** PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Date:** 2026-11-24

> **No analysis may begin until this protocol has been reviewed and explicitly approved.**

## 1. Purpose

This document defines how quality-control flags, missing values, anomalies, detection limits, and calibration uncertainty are handled in the proposed descriptive study.

It has three goals:

1. prevent “unflagged” from being treated as “validated”;
2. prevent silent deletion of inconvenient observations;
3. make every inclusion/exclusion decision reproducible and reportable.

## 2. Core principles

1. **Flags are information, not automatic deletion codes.** A flag may mean missing, faulty, extreme-but-real, fouling-affected, or undocumented. Each is handled explicitly.
2. **No imputation.** No mean, median, regression, interpolation, carry-forward, or zero-fill.
3. **No deletion without a rule.** Every excluded value/date is counted and listed with a reason.
4. **Primary and sensitivity populations are both reported.** A result that depends on a QC choice must be shown under both choices.
5. **Raw values are preserved.** QC rules apply to analysis populations, not to source files.
6. **Sensor RFU is not concentration.** No conversion to chlorophyll-a or phycocyanin concentration is applied.

## 3. Lake Mendota — flag dictionary and decision rules

### 3.1 Documented flags

The daily EML defines, where listed:

| Code | General meaning | Primary handling |
|---|---|---|
| `C` | Sensor off | Exclude numeric and missing `C` values from primary; include numeric `C` in sensitivity |
| `E` | Sensor noisy or malfunctioning | Exclude from primary; include in sensitivity only if numeric and physically plausible |
| `H` | Outside of standard range | **Retain numeric `H` values in primary if physically plausible**; exclude in a stricter sensitivity |
| `G` | Sensor suspected biofouling | Exclude from primary; include in sensitivity |
| `O` | Undefined (observed once in `avg_spec_cond`) | Exclude; undefined meaning |
| blank | No flag | Include if numeric and physically plausible; not proof of validity |

**Why `H` is retained in primary:** `H` means “outside of standard range,” not “invalid.” For pigments, high values may be exactly the bloom conditions of interest. Excluding all `H` values would truncate the upper tail and could bias the association. The stricter “unflagged only” analysis is retained as a sensitivity and matches the 4L.10 counts (128 Turner chlorophyll, 139 Turner phycocyanin).

**Why `C` is not treated as missing:** many `C` records contain numeric values (e.g., 1,534 for `avg_do_wtemp`, 668 for `avg_par_below`, 277 for `avg_do_raw`, 118 for `avg_spec_cond`, 113 for YSI chlorophyll). `C` is a quality judgment, not an empty cell. Numeric `C` values are excluded from primary and retained for sensitivity.

### 3.2 Undocumented flags and metadata inconsistencies

The daily EML’s per-column code lists omit values that occur in the data:

| Column | Documented | Observed extras | Count |
|---|---|---|---:|
| `flag_avg_rel_hum` | C, E | H | 6 |
| `flag_avg_wind_speed` | C | H | 124 |
| `flag_avg_par_below` | C, G | H | 90 |
| `flag_avg_do_wtemp` | C, H | E | 3 |
| `flag_avg_ph` | C | E | 1 |
| `flag_avg_fdom` | C | E | 1 |
| `flag_avg_turbidity` | C | E | 1 |
| `flag_avg_spec_cond` | C, H | E, O | 18 |

Primary rule: treat any undocumented code as an exclusion, because its meaning is not established. Sensitivity: test whether including these values changes the descriptive pattern. Do not reinterpret an undocumented code as if it had a documented meaning.

### 3.3 Unflagged but implausible values

“Unflagged” is not a validation label. Known examples:

- 31 negative turbidity values, all unflagged; 62 negative YSI phycocyanin values; 1 negative YSI chlorophyll; 3 negative PAR below water; 2006 specific conductance ~0.4 µS cm⁻¹.
- Negative pigment values are physically implausible for the proposed endpoint. Exclude from primary; include in a stress-test sensitivity.
- Negative DO or temperature values are implausible; exclude from primary.
- Zero values: retain only if physically plausible for the variable. Pigment zeros are not a documented detection-limit code; treat as observed low signal, not as missing.

### 3.4 Physical plausibility bounds

These are broad plausibility screens, not ecological thresholds:

| Variable | Plausible range for primary | Action outside range |
|---|---|---|
| Turner/YSI chlorophyll RFU | ≥0 | Exclude negative; retain high values if numeric |
| Turner/YSI phycocyanin RFU | ≥0 | Exclude negative; retain high values if numeric |
| DO mg L⁻¹ | 0–50 | Exclude outside |
| DO % saturation | 0–500 | Exclude outside |
| Water temperature | −5 to 50 °C | Exclude outside |
| pH | 0–14 | Exclude outside |
| Turbidity | ≥0 | Exclude negative |
| Specific conductance | >0 | Exclude 2006 values; exclude ≤0 |
| PAR | ≥0 | Exclude negative |

The bounds are deliberately wide. They are not used to define blooms, thresholds, or “normal” conditions.

### 3.5 Mendota calibration and detection-limit status

- No per-record calibration coefficients, serial numbers, detection limits, or maintenance logs are present in the daily file.
- The EML documents sensor changes, fouling events, and maintenance in narrative form, not as per-record QC.
- The 2017 DO biofouling event and the 2023 YSI wiper failure are documented events, not complete per-record flags.
- Turner and YSI have “significant magnitude differences” and no cross-calibration.
- Therefore the sensor values are treated as **relative, instrument-specific signals**, not calibrated concentrations.

## 4. Buffalo Pound — flag dictionary and decision rules

### 4.1 Documented flags

| Code | Meaning | Primary handling |
|---|---|---|
| `M` | Missing / sensor removed / failure / logging error | Exclude |
| `C` | Faulty or unrealistic | Exclude |
| `A2` | PAR below factory range, set to 0 | Not relevant to pigments; if PAR used contextually, retain as 0 |
| `A3` | Inverted PAR, possible bloom/plume/obstruction | Not relevant to pigments |
| `A4` | 2015 underwater PAR shading | Not relevant to 2018–2019 pigments |
| `A5` | Localized rainfall event | Not relevant |
| `A6` | Specific conductivity correction (2017 shallow/deep; 2018 deep) | Not relevant to pigments; conductivity ancillary |
| `B6` | Raw specific conductivity step changes | Not relevant to pigments |
| `B7` | Chlorophyll/phycocyanin/turbidity spike then decrease after site visit (fouling) | **Exclude from primary**; include in sensitivity |
| blank | No flag | Include if numeric, positive, and coverage passes; not proof of validity |

The Buffalo Pound flags are better documented than Mendota’s, but `B7` is an interval flag: it marks the period between the last maintenance visit and the visit where fouling was identified. It can cover many days and may overlap genuine high-biomass periods. Excluding B7 from primary could bias against high values; the sensitivity analysis including B7 is therefore mandatory.

### 4.2 Pigment-specific rules

- Chlorophyll and phycocyanin are reported in RFU, 0–100 RFU operating range, accuracy not specified.
- Negative values are physically implausible; exclude from primary; include in stress-test sensitivity.
- Values above 100 RFU are outside the documented operating range. Retain only if flagged as acceptable? The dataset's operating range is 0–100 RFU; values above may be saturation/extrapolation. The protocol should exclude values above the documented range from primary and include in sensitivity, or retain and flag. Which is better?
  - If the sensor saturates at 100 RFU, values above are not quantitative. Excluding them truncates high blooms. Retaining them as “above-range” is more transparent. The protocol can retain numeric values above 100 RFU in primary but flag them as above-range, and run a sensitivity excluding them. That avoids deleting high values. The data paper says operating range 0–100 RFU, but actual values may exceed; the flag system may catch them. We don't know. To be safe: **retain numeric values, flag above-range, sensitivity excludes above-range**. This parallels H retention.
- Do not convert RFU to chlorophyll-a or phycocyanin concentration.

### 4.3 Coverage rule

A Buffalo Pound date enters the primary analysis only if:

- ≥50% of expected 10-minute values are valid (≥72 of 144); and
- at least one valid value occurs in each half of the day (00:00–11:59 and 12:00–23:59).

If a date fails, it is excluded from primary and included in a sensitivity with any valid value. Report the number of excluded dates and the reason.

### 4.4 B7 and fouling

- Primary excludes B7-flagged pigment values.
- Sensitivity includes B7 and reports whether the association changes.
- If the primary and B7-inclusive results differ materially, the protocol cannot adjudicate which is “true”; both are reported, and the uncertainty is stated.
- Do not treat “no B7 flag” as proof of no fouling.

### 4.5 Buffalo Pound calibration and detection-limit status

- Pigment sensors were calibrated at the start and end of each field season with rhodamine standards; they were not calibrated weekly.
- Maintenance was approximately weekly in peak season and every two weeks otherwise.
- Accuracy for chlorophyll and phycocyanin is “not specified” in the data paper.
- No detection limit is provided for the field pigment sensors.
- Therefore the Buffalo Pound RFU values are relative signals with documented maintenance but no concentration calibration.

## 5. Missingness taxonomy

Every missing observation must be assigned to one of these categories:

| Category | Definition | Example | Primary handling |
|---|---|---|---|
| Structural | Sensor or sample not deployed by design | Mendota pH before 2019; Buffalo Pound winter | Exclude; report |
| Temporal | Outside the lake’s open-water/biology window | Mendota December–March; Buffalo Pound November–April | Exclude; report |
| Equipment | Sensor failure, power loss, damage | Mendota 2021 buoy outage; Buffalo Pound 2015 DO collapse | Exclude; report |
| QC | Value present but flagged faulty/noisy/fouling | `C`, `E`, `G`, `B7` | Exclude primary; sensitivity |
| Biological | No microscopy sample or no cyanobacteria rows | Sparse Mendota winter sampling | Exclude; report |
| Analytical | Value below detection or not reported | Mendota biomass zeros | Retain biovolume; biomass secondary with caveat |
| Unknown | Empty cell with no flag and no explanation | Mendota empty-unflagged values | Exclude; report as unknown |

The distinction matters: structural missingness is expected and not a data-quality failure; equipment/QC missingness may be informative and can bias the sample.

## 6. Missing-not-at-random (MNAR) risks

The protocol must explicitly discuss these risks:

1. **Bloom-targeted sampling.** Field campaigns may target visible blooms, so biological sampling dates are not a random sample of days. This can inflate or deflate associations depending on the sensor’s response.
2. **Fouling-related failures.** Sensor fouling may be more likely during high-biomass periods; excluding B7/G values could remove high-biomass dates.
3. **Seasonal deployment.** Sensors operate in open water; winter/under-ice conditions are absent. The study cannot describe winter.
4. **Depth mismatch.** Mendota’s 0–8 m composite may decouple from surface fluorescence under stratification; the sampling dates may over-represent mixed or bloom conditions.
5. **Taxonomic selection.** Broad cyanobacteria totals include taxa with different pigment content and morphology; the community composition may vary with sampling date.
6. **Instrument transitions.** Turner/YSI changes and maintenance events may coincide with ecological transitions.
7. **Date-only sampling.** The biological sample time is unknown; diel cycles and quenching are averaged in the sensor daily value.

The analysis cannot correct MNAR. It can:

- report included vs excluded dates by year, month, and biological endpoint (descriptive);
- run the pre-specified QC sensitivity analyses;
- state that the observed associations apply to the included dates, not to all days.

## 7. Anomaly register

| Anomaly | Dataset | Evidence | Primary handling | Sensitivity |
|---|---|---|---|---|
| Coelastrum 2011-07-25 | Mendota biology | cells=0, biovolume=7.688e-05, biomass=84.6924, relative=283,806.87 | Does not affect cyanobacteria biovolume; exclude row from total-biomass secondary | Include and report |
| Relative total biovolume groups | Mendota biology | 14 groups ~200%, 3 groups 0%, 1 catastrophic | Do not use the field at all | Not applicable |
| 0–2 m Mendota labels | Mendota biology | 40 records on 2 dates in 2002 | Exclude by depth rule | Not applicable |
| Blank station | Mendota biology | 371/402 dates blank | Include; do not claim per-sample coordinates | Station-aware subset if n permits |
| Repeated same-key rows | Mendota biology | 1,009 groups / 2,048 rows | Sum biovolume across rows | Not applicable |
| 2006 specific conductance | Mendota sensor | ~0.4 µS cm⁻¹; all flagged | Exclude | Not applicable |
| 2017 DO biofouling | Mendota sensor | EML narrative | Exclude `E`/`G`; retain `H` if plausible | Include flagged numeric |
| 2023 YSI wiper failure | Mendota sensor | EML narrative; outside biology window | Not used | Not applicable |
| Negative pigment values | Both | Unflagged negatives | Exclude from primary | Include as stress test |
| Buffalo Pound duplicates | BP biology | 19 date–species groups with 2 rows in 2018; no replicate ID | Mean before summing | Sum; first row |
| Buffalo Pound `REP` labels | BP biology | REP1/REP2 on disjoint dates | Treat date as one sample | Not applicable |
| 2019-07-17 | BP biology | 45.81 mg m⁻³ total vs 12,587/9,498 neighbours; all REP2 | Retain and flag | Exclude |
| B7 fouling intervals | BP sensor | 604 flags in 2014, 803 in 2020; interval-based | Exclude from primary | Include |
| Conductivity corrections 2017/2018 | BP sensor | A6/B6 | Conductivity ancillary; exclude flagged | Not applicable |
| 2015 DO collapse | BP sensor | 38.5% valid | Outside 2018–2019 window | Not applicable |

The anomaly register is not a licence to delete data. It is a list of decisions that must be reported and tested.

## 8. Detection limits and analytical censoring

- Mendota: no detection limits are provided. Biomass zeros with positive biovolume (61 rows) indicate low-value truncation. Biovolume is the primary endpoint; biomass is secondary.
- Buffalo Pound: no detection limits are provided for the field pigment sensors. Toxin files have LOD/LOQ rows but are excluded.
- Do not treat zero as “below detection” unless the source documents it.
- Do not substitute LOD/2, LOD/√2, or any censored-value convention. No such convention is documented.
- If a value is below the sensor’s operating range, flag it as below-range; do not convert it to zero unless the provider did so (e.g., Buffalo Pound A2 PAR).

## 9. Calibration and comparability

### 9.1 Turner vs YSI (Mendota)

- Both output RFU but differ by orders of magnitude.
- 2019 paired medians: Turner chlorophyll 1,354.74 vs YSI 0.39; Turner phycocyanin 802.01 vs YSI 0.59.
- Median ratios: ~0.00033 (chlorophyll), ~0.00084 (phycocyanin).
- No cross-calibration equation, correction factor, or conversion is present.
- Primary rule: never concatenate. Analyse separately.
- Secondary Q7: describe the paired ratios/ranks on the ~11 biology dates where both instruments and biology overlap; do not fit a calibration.

### 9.2 Turner/YSI vs microscopy

- No conversion from RFU to biovolume/biomass is applied.
- A rank association is not a calibration.
- A regression slope, if reported descriptively, is not a validated conversion and must not be used to predict biomass.

### 9.3 Buffalo Pound pigment sensors

- Same instrument family across 2018–2019, but calibration only at season start/end.
- No concentration calibration.
- Do not compare RFU magnitudes across lakes or instruments.

## 10. Reporting requirements

Every QC report must include:

1. **Flag counts** by variable, year, and season: blank, C, E, H, G, O, M, B7, other.
2. **Missingness counts** by category (structural, temporal, equipment, QC, biological, analytical, unknown).
3. **Flow table** from all biological dates to final primary n, with reasons.
4. **Included vs excluded comparison**: year, month, and available biological endpoint (descriptive; no tests).
5. **Sensitivity table**: primary vs strict-unflagged vs flagged-inclusive vs anomaly-excluded vs window ±1 day.
6. **Anomaly list**: every date/value excluded or flagged, with source and reason.
7. **Calibration/detection-limit statement**: what is documented, what is not, and what is assumed.
8. **“Unflagged ≠ validated” statement** in the methods and limitations.

## 11. What would invalidate the analysis

The analysis should stop and return to human review if:

- the primary n is too small to describe (report n; no formal threshold);
- the raw files do not match the recorded hashes;
- a date/time or depth ambiguity cannot be resolved by the pre-specified rules;
- a flag code is found to have a different meaning than documented;
- a licence restriction prevents the proposed use;
- the analysis requires a conversion or calibration that does not exist.

It should **not** stop merely because the association is weak, negative, or absent. A null/negative descriptive result is a legitimate outcome.

## 12. Governance

- **Gate 2 remains PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- No cleaning, transformation, imputation, flag recoding, or derived dataset is performed in this sprint.
- No analysis may begin until the protocol is reviewed and explicitly approved.
