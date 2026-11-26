# D-05 QC Evidence Resolution Report

**Sprint:** 4L.18  
**Decision:** D-05 — Primary QC rule  
**Current status:** **OUTSTANDING — NOT APPROVED**  
**Purpose:** Determine which proposed QC rules are genuinely supported by primary evidence, which are conditional, and which require custodian clarification.

> **Verdict: D-05 cannot be finalised on current evidence.** Some rules are supported by instrument documentation or provider flags; several are assumptions, and the core Buffalo Pound flags/coverage issues remain unresolved. A conservative interim analysis population can be described, but it is not a validated QC system.

---

## 1. Evidence base

| Source | What it establishes | Limits |
|---|---|---|
| NTL-LTER daily EML, `knb-lter-ntl.129.42` | Per-column flag definitions for Mendota: C, E, H, G; no numeric H range; O undefined | No per-record calibration, coefficients, or numeric H definition |
| 4L.9 Mendota raw sensor audit | Actual flag distributions, C-with-value, undocumented codes, unflagged implausibles | Audit, not provider confirmation of every code |
| Buffalo Pound `README.txt` and `data_flags.csv` | M, C, A2–A6, B6, B7 definitions; variable depths; sensor models | No time-zone statement; no per-record calibration coefficients |
| Baulch et al. 2025, *Data in Brief* 63:112290, PMC12720111 | YSI 6600/6025/6131 sensor models; 0–100 RFU ranges; B7 interval definition; calibration/maintenance practice; data screening | Does not resolve every local data-field flag or negative-RFU semantics |
| YSI 6-Series manual Rev J | 6025 chlorophyll range ~0–400 µg/L / 0–100 RFU; 6131 phycocyanin 0–100 RFU; accuracy not specified; 6131 detection limit ~220 cells/mL | Manufacturer performance in controlled conditions; not lake-specific validation |
| YSI 6025 specification sheet | Chlorophyll range ~0–400 µg/L, 0–100 RFU | Manufacturer specification; no local calibration |
| USGS TM 1-D10 (2022) | RFU is a percentage of the sensor operating range (0–100%); fluorescence is a proxy; quenching/interferences; validation needed | Generic guidance, not a Mendota/Buffalo Pound QC record |
| 4L.14 QC rules and addendum | Proposed rules and identified unresolved issues | Proposal, not evidence |

---

## 2. Exact flag meanings

### 2.1 Mendota daily EML

| Flag | Documented meaning | Where documented | Key limitation |
|---|---|---|---|
| **C** | Sensor off | Most flag columns | Numeric values can remain with C; not equivalent to missing |
| **E** | Sensor noisy or malfunctioning | Air temp, RH, YSI chlorophyll/phycocyanin, DO sat/raw, pCO2 (not every column) | Some E values appear in columns whose local code list omits E |
| **H** | Outside of standard range | Air temp, wind direction, Turner/YSI chlorophyll/phycocyanin, PAR, DO, specific conductance (not every column) | **No numeric range is defined**; H is not automatically invalid |
| **G** | Sensor — suspected biofouling | YSI chlorophyll/phycocyanin, PAR below | “Suspected,” not confirmed invalid; Turner columns have no G |
| **O** | **Undefined** | Not defined in the EML | One value in `flag_avg_spec_cond`; meaning unknown |

**Verified:** the code definitions are present in the EML. **Not verified:** the numeric boundaries for H, the validity of C-with-value records, the meaning of O, and whether G means “discard” or “caution.”

### 2.2 Buffalo Pound flags

| Flag | Documented meaning | Source | Relevance |
|---|---|---|---|
| **M** | Missing; sensor removed/damaged; values not recorded/logged | `data_flags.csv`; Data in Brief Table 2 | Exclude from primary |
| **C** | Data deemed faulty or unrealistic | `data_flags.csv`; Data in Brief Table 2 | Exclude from primary |
| **A2** | PAR below factory range; adjusted to 0 | `data_flags.csv` | PAR not in primary |
| **A3** | Inverted PAR; environmental or error | `data_flags.csv` | PAR not in primary |
| **A4** | 2015 PAR shading | `data_flags.csv` | PAR not in primary |
| **A5** | Localised rainfall event | `data_flags.csv` | Not pigment QC |
| **A6** | Corrected specific conductivity | `data_flags.csv` | Not pigment primary |
| **B6** | Raw conductivity step changes | `data_flags.csv` | Not pigment primary |
| **B7** | Chlorophyll/phycocyanin/turbidity spike followed by decrease after site visit | `data_flags.csv`; Data in Brief Table 2 | **Caution flag**, not a removal flag |

**Critical finding:** the Data in Brief paper states B7 was used to identify likely periods where fouling *could* impact data quality, and the affected period was defined as the **entire duration between the last maintenance visit and the subsequent visit where the issue was identified**. This is a broad caution interval, not proof that every value in the interval is invalid.

### 2.3 Instrument ranges

- YSI 6025 chlorophyll: **~0–400 µg/L; 0–100 RFU**.
- YSI 6131 phycocyanin: **0–100 RFU**; accuracy not specified; detection limit ~220 cells/mL.
- The Buffalo Pound Data in Brief Table 7 lists both shallow sensors as **0–100 RFU**.
- USGS TM 1-D10 states RFU is a percentage of the sensor’s operating range (**0–100%**).

**Conclusion:** 0–100 RFU is a **manufacturer full-scale/operating range**, not merely a display convention. Values above 100 are outside the documented full scale and cannot be assumed quantitative. Whether the dataset contains such values and whether they are saturation/clipping or extrapolation requires the custodian/data audit.

---

## 3. Rule-by-rule classification

| ID | Proposed rule | Classification | Exact evidence | Recommendation |
|---|---|---|---|---|
| R-01 | Exclude `C` from primary | **Supported only conditionally** | EML: C = sensor off; 4L.9: C can carry numeric values (e.g., 1,534 water-temp values) | Exclude C primary; do **not** treat numeric C as equivalent valid data. Report C-with-value counts; custodian should confirm whether numeric C is stale/valid. |
| R-02 | Exclude `E` from primary | **Supported only conditionally** | EML: E = noisy/malfunctioning; not documented in every column; 4L.9 finds E in columns whose local list omits it | Exclude E primary; treat undocumented E as unresolved; no “include numeric” equivalence. |
| R-03 | Exclude `G` from primary | **Unsupported as automatic invalidation; supported as caution** | EML: G = suspected biofouling; “suspected,” not confirmed invalid; Turner has no G | Do not call G invalid by definition. Either retain primary with G flag and run SENS_G exclusion, or obtain custodian confirmation. |
| R-04 | Exclude `O` from primary | **Supported as unresolved; meaning unverified** | EML defines no O; one value in spec cond | Exclude O primary; report it; no sensitivity interpretation until defined. |
| R-05 | Retain `H` if numeric/within documented range | **Unsupported as written for Mendota** | EML: H = “outside of standard range”; no numeric range; 4L.9 shows H is common and some values plausible, some not | Do not retain H as valid without a documented range. Exclude H primary; SENS_H includes numeric values. For Buffalo Pound, H is not the applicable flag. |
| R-06 | Exclude undocumented flags from primary | **Supported as a conservative rule** | 4L.9: eight columns have values outside local code lists; O undefined | Exclude primary; report as `UNRESOLVED_FLAG`; no sensitivity treated as equivalent. |
| R-07 | Negative RFU: retain primary / call below-baseline | **Requires custodian clarification** | USGS: RFU is 0–100% of operating range; no source says negative is a valid low concentration; YSI 1-point calibration zeros the sensor; negative values can occur near zero | Do not call negative RFU “below-baseline” without documentation. Exclude primary; report numeric values; SENS_NEG only as diagnostic. |
| R-08 | Buffalo Pound `B7`: exclude primary | **Unsupported as automatic invalidation** | Data in Brief: B7 marks the interval between maintenance visits where fouling was identified; it is a caution flag, not a removal flag | Do not exclude all B7 by default. Retain primary with B7 flag and run SENS_B7 exclusion; custodian should confirm whether B7 means “discard” or “caution.” |
| R-09 | Buffalo Pound >100 RFU: exclude primary, sensitivity includes | **Supported conditionally** | YSI 6025/6131 0–100 RFU; Data in Brief Table 7; USGS RFU 0–100% full scale | Exclude >100 primary; report as above-range; sensitivity includes only as diagnostic. Whether values are saturation/clipping requires custodian/data audit. |
| R-10 | Buffalo Pound coverage ≥72/144 and both halves | **Unsupported** | 4L.9/4F: daily counts 121–144 (2018), 42–131 (2019); no date-specific expected cadence; addendum F-01 withdrew the rule | Do not use 72/144. Require date-specific expected cadence, deployment/time zone and exposure duration from custodian. |
| R-11 | Broad physical bounds (DO 0–50 mg/L, DO sat 0–500%, temp −5–50 °C, pH 0–14, turbidity ranges) | **Supported only conditionally** | Buffalo Pound Data in Brief Table 7 documents these ranges; Mendota EML does not document instrument ranges for most variables | Use as broad screens, not validation. For Mendota, label as assumptions; report values outside; no silent deletion. pH 0–14 is definitional. |
| R-12 | Missing values excluded; no imputation | **Supported** | EML missingness; Buffalo Pound M/NA; 4L.14 rule | Exclude; report; no zero-fill, interpolation, or LOD/2. |
| R-13 | Buffalo Pound `M` and `C` excluded | **Supported** | Data flags: M missing; C faulty/unrealistic; Data in Brief says C marks removed/erroneous data | Exclude primary. |
| R-14 | 0–100 RFU is an actual operating/full-scale range | **Verified** | YSI 6025/6131 manuals and Data in Brief Table 7; USGS RFU 0–100% of operating range | Use as above-range boundary; do not interpret 100 as a concentration or bloom threshold. |
| R-15 | Buffalo Pound time zone/timestamp convention | **Requires custodian clarification** | README: `DateTime` is `YYYY-MM-DD HH:MM:SS`; no timezone suffix; no timezone statement | Essential for date/window alignment and day/night sensitivity. |
| R-16 | B7 overlap with high biomass | **Requires custodian/count audit** | 4L.14 review: overlap not quantified; B7 interval definition is broad | Do not assume exclusion is unbiased. Report overlap after authorised audit or custodian statement. |
| R-17 | Calibration/maintenance records | **Partially supported** | Data in Brief: sensors calibrated at start/end; DO/pH/conductivity during maintenance; B7 from site visits | No per-record coefficients/serial numbers. Custodian should confirm available logs and drift. |

---

## 4. What is actually supported

1. **Mendota C/E definitions** are documented, but C-with-value and undocumented E values prevent treating “C/E excluded” as fully resolved.
2. **Mendota H cannot be retained by a documented range** because no numeric H range exists. H should be excluded from primary and included only in a numeric sensitivity.
3. **Mendota G is a suspicion flag, not proof of invalidity.** Automatic primary exclusion is a conservative choice, not a documented requirement.
4. **Mendota O is undefined.** It cannot be interpreted.
5. **Buffalo Pound M/C are removal flags**; excluding them is supported.
6. **Buffalo Pound B7 is a caution interval**, not a removal flag. Excluding all B7 from primary is not supported by the data paper.
7. **0–100 RFU is a real manufacturer full-scale range** for YSI 6025/6131. Values above 100 are outside the documented range and cannot be assumed quantitative.
8. **Negative RFU has no documented biological meaning.** It may be baseline/zero-offset behaviour, but this is an inference; custodian clarification is required.
9. **Coverage cannot be fixed at 72/144.** Date-specific cadence, deployment and time zone are missing.
10. **No per-record calibration/QA record** exists in the accessible documentation; the data paper describes maintenance/calibration practice but not record-level coefficients.

---

## 5. What remains assumption

- That `C` numeric values are invalid rather than stale/valid.
- That `G` values are unsafe rather than merely suspect.
- That `H` values are not valid extremes; the range is unknown.
- That negative RFU is baseline noise rather than a real low signal.
- That `B7` intervals should be excluded rather than flagged.
- That a daily mean is representative of the biological sample day.
- That 2018 and 2019 duplicate rows follow the same semantics.
- That the Buffalo Pound `Biomass_mg_m3` field exactly follows the published conversion.

These assumptions must not be presented as verified QC.

---

## 6. Can D-05 be resolved sufficiently for D-06?

**Not fully.**

- D-06 Option A can remain a **provisional project-owner preference**.
- The daily summaries can be described with explicit non-equivalence and coverage caveats.
- But D-06 cannot be finalised while D-05 is unresolved, because the primary population and the treatment of H/G/B7/negative RFU are undecided.
- D-06 Option A is still the most defensible provisional summary: it is the only common daily statistic available for Mendota, and it avoids inventing a nighttime/daytime window unsupported by sample times. It is not validated.

**If the custodian cannot resolve B7/negative/coverage/H:** the defensible fallback is a conservative, explicitly labelled analysis population (unflagged numeric values; C/E/O excluded; H excluded from primary; G/B7 retained only with sensitivity; negative/above-range excluded primary) and **no claim of clean or validated data**. If reviewers reject that as too assumption-heavy, Stage 1 cannot proceed as a quantitative measurement study.

---

## 7. Does Stage 1 remain scientifically viable?

**Conditionally yes — as a modest exploratory measurement/comparability audit, not as validation.**

It remains viable if:

- the analysis population is explicitly defined and conservative;
- P3/P4 remain exploratory;
- H/G/B7/negative rules are reported with sensitivities, not treated as validated;
- D-06 remains provisional;
- no calibration/validation/EWS claims are made.

It is **not** viable as a confirmatory or early-warning study, and it may become non-viable if independent reviewers require a validated QC system that the custodian cannot provide.

---

## 8. Custodian questions generated by this audit

Essential:

1. What do duplicate date–species rows and `REP1`/`REP2` mean?
2. What is the exact derivation of `Biomass_mg_m3`, including density and conversion factor?
3. What do `M`, `C`, `B7` and any undocumented flags mean in the local files?
4. Does `B7` mean “discard” or “caution”? What is its exact interval?
5. What is the actual YSI 6025/6131 operating range, and how should values >100 RFU be treated?
6. Are negative RFU values valid baseline/zero-offset values, or invalid?
7. What is the date-specific expected sensor cadence and daily coverage?
8. What time zone/timestamp convention applies?
9. Are calibration/maintenance records available per deployment/date?
10. Are 2018 and 2019 replicate/sample structures documented?

Supplementary:

- detection limits/accuracy;
- data dictionary/schema;
- correction/version history;
- any field notes for 2019-07-17.

---

## 9. Verdict

**D-05 is NOT resolved and remains OUTSTANDING — NOT APPROVED.**

The evidence supports a conservative analysis population, but not the current QC rule as a validated system. The most consequential corrections are:

- do not automatically exclude B7 as invalid;
- do not retain Mendota H as valid without a documented range;
- do not call negative RFU “below-baseline” without documentation;
- do not use the 72/144 coverage rule;
- treat G as a caution flag, not automatic invalidity;
- treat 0–100 RFU as a real full-scale range, with >100 unresolved.

D-06 remains provisional; D-15 remains not approved.
