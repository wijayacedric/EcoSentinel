# QC and Missingness Rules

**Sprint:** 4L.14  
**Status:** PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Date:** 2026-11-24

> **No analysis is authorised. The counts and overlap assessments described here are prohibited future steps until D-15 approval.**

## 1. Purpose

This document implements Sprint 4L.13 revision R-05. It replaces ambiguous rules such as “retain H if plausible” with an explicit, reproducible decision tree.

It covers:

- every relevant flag code;
- exact treatment of flagged numeric values;
- undocumented flags;
- negative observations;
- physical plausibility bounds and their evidence;
- missing values;
- exclusions and sensitivity handling;
- the B7 overlap issue;
- what must be reported after approval.

It does **not** calculate new analytical results.

## 2. Principles

1. **Flags are information, not automatic deletion codes.**
2. **No imputation, interpolation, or zero-fill.**
3. **Every exclusion has a reason code.**
4. **Primary and sensitivity populations are both defined.**
5. **If a defensible limit cannot be established, classify the value as `UNRESOLVED` rather than silently retaining or excluding it.**
6. **Do not invent ecological thresholds.** The bounds below are physical/analytical plausibility bounds or documented instrument ranges, not bloom thresholds.
7. **Raw values are preserved.**

## 3. Mendota flag dictionary

| Code | Documented meaning | Primary handling | Sensitivity handling |
|---|---|---|---|
| blank | No flag | `USABLE` if numeric and within bounds | — |
| `C` | Sensor off | `EXCLUDED_C` | Include numeric values if finite (`SENS_C`) |
| `E` | Sensor noisy/malfunctioning | `EXCLUDED_E` | Include numeric values if finite and within bounds (`SENS_E`) |
| `H` | Outside standard range | `USABLE_H` if numeric, finite, and within broad bounds; otherwise `UNRESOLVED_H` | Exclude all `H` (`SENS_STRICT`) |
| `G` | Suspected biofouling | `EXCLUDED_G` | Include numeric values (`SENS_G`) |
| `O` | Undefined | `EXCLUDED_O` | Not used; report count |
| other/undocumented | No documented meaning | `UNRESOLVED_FLAG` | Include numeric values only if finite and within bounds (`SENS_UNDOC`) |

### 3.1 Numeric `C`

`C` is defined as “sensor off,” but many records contain numeric values. These may be stale, last-value, or partial-day values. They are excluded from primary and included in `SENS_C`. The report must state how many pigment dates are lost, particularly in 2014–2015, when Turner chlorophyll has many `C` flags.

### 3.2 `H` retention

`H` means “outside of standard range,” not “invalid.” Retaining `H` avoids truncating high values that may be real blooms. But an `H` value is not automatically valid.

Primary rule:

- numeric, finite, and within the broad bounds in §5 → `USABLE_H`;
- numeric but outside broad bounds → `UNRESOLVED_H` (excluded primary; sensitivity include if finite).

Strict sensitivity `SENS_STRICT` excludes all `H` values and is intended to approximate the 4L.10 “unflagged” counts (128 Turner chlorophyll, 139 Turner phycocyanin). Exact n may differ because the revised protocol also applies station/negative rules; the count audit will report the actual value.

### 3.3 Undocumented flags

Eight Mendota columns contain values outside their documented code lists. Any undocumented code is `UNRESOLVED_FLAG`:

- excluded from primary;
- included in `SENS_UNDOC` only if numeric, finite, and within broad bounds;
- reported by column and count.

Do not reinterpret an undocumented code as if it had a documented meaning.

## 4. Buffalo Pound flag dictionary

| Code | Documented meaning | Primary handling | Sensitivity handling |
|---|---|---|---|
| blank | No flag | `USABLE` if numeric and within bounds | — |
| `M` | Missing/failure | `MISSING` | — |
| `C` | Faulty/unrealistic | `EXCLUDED_C` | Include numeric values if finite (`SENS_C`) |
| `B7` | Fouling spike/decrease after site visit | `EXCLUDED_B7` | Include (`SENS_B7`) |
| `A2` | PAR below range, set to 0 | Not relevant to pigments; if PAR used contextually, retain 0 | — |
| `A3` | Inverted PAR | Not relevant to pigments | — |
| `A4` | 2015 underwater PAR shading | Not relevant to 2018–2019 pigments | — |
| `A5` | Local rainfall | Not relevant | — |
| `A6` | Conductivity correction | Not relevant to pigments; conductivity ancillary | — |
| `B6` | Raw conductivity step changes | Not relevant to pigments | — |
| other/undocumented | No documented meaning | `UNRESOLVED_FLAG` | Include numeric values only if finite and within bounds (`SENS_UNDOC`) |

### 4.1 `B7` is an interval flag

`B7` marks the period between the last maintenance visit and the visit where fouling was identified. It is not a point measurement error flag.

Primary excludes `B7`; `SENS_B7` includes it. The report must quantify:

- number of B7 dates in 2018–2019;
- biomass distribution on B7 vs non-B7 dates;
- whether B7 is concentrated in one season/year;
- ρ with and without B7 (after approval).

If B7 dates are systematically high biomass, the primary result is conditional on excluding high-biomass periods. That must be stated prominently.

### 4.2 Negative and above-range pigment values

- Negative `ChlRFUShallow_RFU` or `BGPCShallowRFU_RFU`: `NEG_RFU`; retained in primary as observed low signal; `SENS_NEG` excludes.
- Values above the documented 0–100 RFU operating range: `ABOVE_RANGE`; retained in primary with flag; `SENS_ABOVE` excludes. Do not interpret the magnitude as quantitative if the sensor may be saturated.
- Negative values for DO, temperature, pH, turbidity, or conductance: physically implausible; `IMPLAUSIBLE`; excluded primary; not included in sensitivity.

## 5. Broad bounds and evidence

These bounds are **physical/analytical plausibility bounds**, not ecological thresholds. They are used to catch impossible values, not to define blooms.

| Variable | Mendota primary bounds | Buffalo Pound primary bounds | Evidence / rationale |
|---|---|---|---|
| Chlorophyll RFU | finite numeric; negative retained as `NEG_RFU`; no upper bound | 0–100 RFU documented; negative retained as `NEG_RFU`; >100 `ABOVE_RANGE` | Mendota daily EML does not document an operating range; BP data paper documents 0–100 RFU |
| Phycocyanin RFU | finite numeric; negative retained as `NEG_RFU`; no upper bound | 0–100 RFU documented; negative retained as `NEG_RFU`; >100 `ABOVE_RANGE` | Same |
| DO mg/L | 0–50 | 0–50 | Broad instrument/analytical range; BP data paper specifies 0–50 mg/L |
| DO % saturation | 0–500 | 0–500 | Broad instrument/analytical range; BP data paper specifies 0–500% |
| Water temperature | −5 to 50 °C | −5 to 50 °C | Liquid freshwater range; BP data paper specifies −5 to 50 °C |
| pH | 0–14 | 0–14 | Definitional pH scale; BP data paper specifies 0–14 |
| Turbidity | not used in primary/secondary | 0–1000 NTU documented | BP data paper; Mendota turbidity is ancillary only |
| Specific conductance | not used in primary/secondary | 0–100,000 µS/cm documented | BP data paper; Mendota conductance is ancillary only |

### 5.1 What is not bounded

- For Mendota DO and water temperature, the daily EML does not state instrument operating ranges. The bounds in §5 are broad physical/analytical screens, not manufacturer specifications. Values outside are `UNRESOLVED_PHYSICAL`, reported, and sensitivity-tested; they are not silently deleted.
- Mendota RFU has no documented upper bound. Do not impose one. High values are retained if finite and non-negative.
- Mendota turbidity, pH, fDOM, and conductance are ancillary; they are not used in primary/secondary estimands. Their coverage is reported, but no biological inference is drawn.
- PAR, pCO2, and weather are outside the measurement question; not used.

### 5.2 If a value is outside a bound

- `UNRESOLVED_PHYSICAL`: excluded from primary; sensitivity includes if finite; reported.
- Do not silently delete.
- Do not replace with zero, LOD/2, or a model value.

## 6. Negative RFU rule

Negative RFU values are **retained in primary as observed sensor output** and flagged `NEG_RFU`.

Rationale:

- RFU is relative, not concentration;
- negative values can arise from baseline/blank subtraction or noise near zero;
- no instrument-specific blank/noise threshold is documented;
- excluding all negatives could truncate the low end and inflate rank correlations;
- R-05 requires not silently excluding unresolved values.

Sensitivity `SENS_NEG` excludes negative RFU. The report must state:

- number of negative RFU dates per pigment/lake;
- their rank positions;
- whether excluding them changes ρ materially.

Negative RFU is **not** interpreted as zero biomass or as a valid low concentration.

## 7. Missingness taxonomy

| Category | Definition | Primary handling |
|---|---|---|
| Structural | Sensor/sample not deployed by design | `MISSING_STRUCTURAL`; excluded; reported |
| Temporal | Outside open-water/biology window | `MISSING_TEMPORAL`; excluded; reported |
| Equipment | Failure, power loss, damage | `MISSING_EQUIPMENT`; excluded; reported |
| QC | Value present but flagged faulty/noisy/fouling | `EXCLUDED_*`; sensitivity where defined |
| Biological | No microscopy sample or no cyanobacteria rows | `MISSING_BIOLOGY`; excluded; reported |
| Analytical | Below detection/zero truncation | `ANALYTICAL`; retained if numeric; biomass secondary caveat |
| Unknown | Empty with no flag/explanation | `MISSING_UNKNOWN`; excluded; reported |

No imputation. No interpolation. No zero-fill.

## 8. Buffalo Pound coverage rule

A date is eligible only if:

- ≥50% of expected 10-minute values are valid (≥72 of 144); and
- at least one valid value occurs in each half of the day (00:00–11:59 and 12:00–23:59).

If not:

- `EXCLUDED_COVERAGE` primary;
- `SENS_COVERAGE` includes dates with any valid value.

The 50% rule is a completeness rule, not an ecological threshold. Its purpose is to prevent a “daily mean” from being a half-day mean.

## 9. Exclusion reason codes

Every excluded date/value receives one primary reason code:

| Code | Meaning |
|---|---|
| `MISSING_STRUCTURAL` | Not deployed |
| `MISSING_TEMPORAL` | Outside window |
| `MISSING_EQUIPMENT` | Failure/power/damage |
| `MISSING_BIOLOGY` | No sample/endpoint |
| `MISSING_UNKNOWN` | Empty, no explanation |
| `EXCLUDED_C` | `C` flag |
| `EXCLUDED_E` | `E` flag |
| `EXCLUDED_G` | `G` flag |
| `EXCLUDED_O` | `O` flag |
| `EXCLUDED_B7` | B7 fouling |
| `UNRESOLVED_FLAG` | Undocumented flag |
| `UNRESOLVED_PHYSICAL` | Outside broad bounds |
| `UNRESOLVED_STATION` | Multiple non-1 stations without station 1 |
| `UNRESOLVED_GROUP` | Group/Phylum mismatch |
| `EXCLUDED_COVERAGE` | BP coverage fail |
| `NEG_RFU` | Negative RFU (primary retained; sensitivity excludes) |
| `ABOVE_RANGE` | BP RFU >100 (primary retained; sensitivity excludes) |

A date may have multiple secondary reasons; the primary reason is the first in the hierarchy: missing > biology > QC > coverage > station/group > negative/above-range.

## 10. What must be reported after approval

The count-only audit must report:

1. Flag counts by variable/year/season.
2. Missingness counts by category.
3. Reasons for every excluded date.
4. Final n per estimand.
5. n by year and season.
6. Included vs excluded biological endpoint distributions (median, IQR, n) — descriptive only.
7. B7 overlap: n, biomass distribution, season/year concentration.
8. Negative RFU counts and ranks.
9. `H` counts and strict-unflagged sensitivity.
10. `C` counts and their effect on 2014–2015 Turner coverage.
11. Coverage failures for Buffalo Pound.
12. Any `UNRESOLVED` values and how they were handled.

This audit is not a correlation analysis and does not create a cleaned dataset.

## 11. What remains unresolved

- The exact number of B7-flagged 2018–2019 pigment values is not known until the audit.
- The effect of B7 exclusion on biomass distribution is not known until the audit.
- The number of negative RFU values in Buffalo Pound is not known until the audit.
- The number of `H` values retained/excluded is known from 4L.9 for Mendota but not fully for Buffalo Pound.
- The source method for Buffalo Pound replicates is not documented; the mean rule remains an assumption.

These are explicitly unresolved, not silently resolved.

## 12. Governance

- **Protocol: PROPOSED — NOT APPROVED.**
- **Gate 2: PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- No analysis is authorised until the required human decisions and explicit D-15 approval are recorded.
