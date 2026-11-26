# QC and Missingness Review

**Sprint:** 4L.13  
**Status:** INDEPENDENT REVIEW — NOT APPROVAL  
**Protocol reviewed:** Sprint 4L.12, PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

> **This review does not approve the protocol or authorise analysis.**

## 1. What the protocol gets right

The 4L.12 QC protocol is more careful than most:

- it distinguishes missing, flagged, excluded, and usable observations;
- it recognises that “unflagged” is not “validated”;
- it preserves raw values;
- it forbids imputation;
- it requires flag counts and a flow table;
- it proposes sensitivity analyses for `H`, `B7`, negatives, and the 2019-07-17 anomaly;
- it documents the Mendota flag-code inconsistencies and the Buffalo Pound flag dictionary.

These are genuine strengths.

The protocol’s weakness is **operationalization**: several rules depend on unstated judgement (“plausible,” “pending review”), and several choices may systematically change the observed relationship.

## 2. Mendota flags

### 2.1 Documented codes

| Code | Meaning | 4L.12 primary rule | Review assessment |
|---|---|---|---|
| `C` | Sensor off | Exclude | Defensible, but many `C` records contain numeric values; they may be stale/last-value. Exclude primary, sensitivity include. |
| `E` | Noisy/malfunctioning | Exclude | Defensible. |
| `H` | Outside standard range | Retain if numeric and plausible | Directionally correct, but “plausible” is not operational. |
| `G` | Suspected biofouling | Exclude | Defensible; Turner has no `G`, so absence is not evidence. |
| `O` | Undefined | Exclude | Correct. |

### 2.2 Numeric values carrying flags

The 4L.9/4L.10 audits document:

- `avg_do_wtemp`: 1,534 numeric `C` values;
- `avg_par_below`: 668 numeric `C`;
- `avg_do_raw`: 277 numeric `C`;
- `avg_spec_cond`: 118 numeric `C`;
- YSI chlorophyll: 113 numeric `C`.

The protocol excludes these from primary and includes them in sensitivity. That is transparent. But the report must show how many pigment dates are lost, especially for Turner chlorophyll in 2014–2015:

- 2014 Turner chlorophyll: 147 `C` flags out of 162 records;
- 2015: 97 `C` out of 169.

Excluding `C` may leave very few Turner chlorophyll dates in those years. If so, the “14-year” record is not evenly represented, and seasonal/era analyses may be dominated by a few years.

**Recommendation:** Report n by year for each pigment, and state whether any year contributes too few dates to support the year-cluster/leave-one-year-out analysis.

### 2.3 Undocumented codes

Eight columns contain codes outside their documented lists (e.g., `H` in wind speed, `E` in pH, `O` in conductance). The protocol excludes undocumented codes from primary. That is correct, but the report must quantify how many pigment dates are affected. For pigments, the main undocumented issue is `E` in some YSI columns; the counts are small. The larger issue is the absence of a complete flag dictionary.

### 2.4 `H` retention: the “plausible” problem

The protocol says “retain numeric `H` if physically plausible.” This is not reproducible. What is “plausible” for Turner chlorophyll? The observed maximum is 16,211 RFU; the instrument’s documented range is not in the daily EML. For YSI, the observed maximum is 9.46; the operating range may be 0–100 RFU (as in the Buffalo Pound data paper). For phycocyanin, the observed maximum is 12,831 Turner and 5.27 YSI.

A second analyst could choose different bounds. The protocol must provide:

- exact lower/upper bounds per variable;
- a rule for values above the instrument’s documented range;
- a rule for negative `H` values;
- a rule for `H` values that are extreme but physically possible (e.g., a dense surface scum).

**Recommendation:** Use a two-part rule:

1. **Physical bounds** (e.g., RFU ≥ 0; DO 0–50 mg L⁻¹; temp −5–50 °C; pH 0–14; turbidity ≥ 0).
2. **Provider `H` retention** if the value is within the physical bounds and below a pre-specified absurd upper bound (e.g., 10× the 99.9th percentile of the unflagged distribution, computed before analysis). The upper bound must be pre-specified, not chosen after seeing the correlation.

Alternatively, retain all `H` values within physical bounds and run a sensitivity excluding them. This is simpler and more transparent.

### 2.5 Negative pigment values

The protocol excludes negative pigment values from primary and includes them in a stress-test sensitivity.

This is **not clearly justified**. Negative RFU values can occur from:

- baseline/blank subtraction;
- instrument noise around zero;
- low signal below detection;
- calibration drift.

The technical literature is mixed: some sources say negative fluorescence indicates a problem; others show models output negative values at low concentrations; some studies replace negative phycocyanin with zero because it is below detection (Ma et al. 2023). The protocol has no instrument-specific blank/noise data, so it cannot distinguish “invalid” from “near-zero.”

**Consequence:** Excluding all negatives from primary removes low-signal dates. In a rank correlation, this can truncate the low end and inflate ρ. It can also bias seasonal comparisons if negatives cluster in low-biomass seasons.

**Recommendation:** Choose one of two defensible rules:

- **(a) Retain negatives in primary** as observed RFU values; run a sensitivity excluding them. This treats the sensor output as the measurement, including baseline noise.
- **(b) Exclude negatives from primary** only if a documented instrument-specific blank/noise threshold shows they are invalid; otherwise do not exclude solely for sign.

The current rule (exclude primary, include sensitivity) is defensible only if the protocol explicitly states that negative RFU is treated as below detection/invalid and shows the effect on n and ρ. It does not.

### 2.6 Unflagged but implausible values

The protocol acknowledges negative turbidity, negative YSI phycocyanin, negative PAR, and 2006 conductance. It excludes negative pigments but not all implausible values. The report must list every exclusion and its count.

## 3. Buffalo Pound flags

### 3.1 Documented codes

| Code | Meaning | 4L.12 primary rule | Review assessment |
|---|---|---|---|
| `M` | Missing/failure | Exclude | Correct. |
| `C` | Faulty/unrealistic | Exclude | Correct. |
| `A2` | PAR below range → 0 | Not relevant to pigments | Correct. |
| `A3` | Inverted PAR | Not relevant | Correct. |
| `A4` | 2015 PAR shading | Not relevant (2018–2019) | Correct. |
| `A5` | Local rainfall | Not relevant | Correct. |
| `A6` | Conductivity correction | Not relevant to pigments | Correct. |
| `B6` | Conductivity step changes | Not relevant | Correct. |
| `B7` | Fouling spike/decrease | Exclude primary; sensitivity include | Potentially problematic; see below. |

### 3.2 `B7` exclusion

`B7` marks a period between the last maintenance visit and the visit where fouling was identified. It is an **interval flag**, not a point flag. The protocol excludes B7-flagged pigment values from primary.

**Problem:** B7 periods may overlap high-biomass conditions. If fouling is more likely during blooms, excluding B7 removes high-biomass dates and can attenuate or inflate ρ. The protocol’s sensitivity including B7 helps, but it does not quantify the overlap.

**Recommendation:** Before primary analysis, report:

- number of B7 dates;
- biomass distribution on B7 vs non-B7 dates;
- ρ with and without B7;
- whether B7 dates are concentrated in one season/year.

If B7 dates are systematically high biomass, the primary result is conditional on excluding high-biomass periods; that must be stated prominently.

### 3.3 Coverage rule

The protocol requires ≥50% of expected 10-minute values and both halves of the day. This is a reasonable completeness rule, but:

- coverage may correlate with fouling/maintenance;
- a date with 72 values all in one half-day would fail the both-halves rule; a date with 72 values spread across the day would pass;
- the rule has not been applied, so actual n is unknown.

**Recommendation:** Report coverage for every biological date, and compare included vs excluded dates by biomass and season.

### 3.4 Negative values

The same issue applies: Buffalo Pound negative pigment values are excluded from primary. The protocol should state whether negatives are below detection or invalid, and report their effect.

## 4. Missingness taxonomy

The protocol’s taxonomy (structural, temporal, equipment, QC, biological, analytical, unknown) is good. But the flow table has not been completed. The report must show:

- all biological dates;
- dates in window;
- dates meeting depth rules;
- dates with any sensor record;
- dates with numeric values;
- dates passing each flag rule;
- dates passing coverage;
- final n per estimand;
- excluded dates and reasons.

This is essential for reproducibility and for assessing MNAR.

## 5. Systematic exclusion bias

The protocol acknowledges MNAR but does not quantify it. The main risks are:

1. **Bloom-targeted sampling** — dates may over-represent blooms.
2. **Fouling-related failures** — B7/G exclusion may remove high-biomass dates.
3. **Sensor era** — C flags in 2014–2015 may remove chlorophyll dates.
4. **Depth mismatch** — 0–8 m composite may decouple from surface sensor under stratification.
5. **Taxonomic selection** — broad totals include taxa with different pigment content.
6. **Date-only sampling** — daily mean includes diel quenching.
7. **Coverage** — Buffalo Pound dates with incomplete days may differ from complete days.

**Recommendation:** For each exclusion, report the biological endpoint distribution of included vs excluded dates (median, IQR, n). Do not test significance; describe.

## 6. Reproducibility of the QC rule

A reproducible QC rule must be a decision tree, not a paragraph. For each variable, specify:

1. missing/empty → exclude;
2. flag code → primary/sensitivity status;
3. numeric value → physical bounds;
4. negative → retain/exclude rule;
5. above-range → retain/exclude rule;
6. coverage → pass/fail;
7. final status → usable/excluded with reason code.

The protocol should include a table with every flag combination and outcome. Without it, two analysts can apply different rules.

## 7. Findings

| ID | Finding | Severity |
|---|---|---|
| F1 | QC taxonomy is thoughtful and preserves raw data | Pass |
| F2 | “Retain H if plausible” is not operational | **Major** |
| F3 | Negative-value exclusion is not justified and may truncate low signal | **Major** |
| F4 | B7 exclusion may remove high-biomass dates; overlap not quantified | **Major** |
| F5 | C flags in 2014–2015 may make the Turner record uneven | Major |
| F6 | Coverage rule not applied; actual n unknown | Major |
| F7 | Missingness taxonomy is good but flow table incomplete | Moderate |
| F8 | No exact decision tree; reproducibility is incomplete | Major |

## 8. Required changes

1. Provide exact numeric bounds and a decision tree for every flag combination.
2. Justify or reverse the negative-value exclusion; report its effect on n and ρ.
3. Quantify B7 overlap with biomass and report ρ with/without.
4. Report n by year/season for each pigment; flag sparse years.
5. Complete the flow table from source dates to final n.
6. Compare included vs excluded dates descriptively.
7. Keep “unflagged ≠ validated” and no-imputation rules.

## 9. Governance

- **Protocol: PROPOSED — NOT APPROVED.**
- **Gate 2: PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- No decision is approved by this review.
- No analysis is authorised until the required revisions and D-15 approval are recorded.
