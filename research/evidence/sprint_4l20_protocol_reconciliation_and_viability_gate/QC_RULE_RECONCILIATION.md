# QC Rule Reconciliation

**Sprint:** 4L.20  
**Date:** 2026-11-26  
**Purpose:** Reconcile the 4L.14 QC rules with the 4L.18/4L.19 evidence and the 4L.14 review addendum, and propose a defensible QC position for the reduced Stage 1 design.  
**Status:** Proposed reconciliation. **NOT APPROVED. No analysis authorised.**

---

## 1. Principles

1. **A flag is information, not automatically an invalidity code.**
2. **No imputation, interpolation, zero-fill or LOD/2 substitution.**
3. **No invented flag meanings or numeric thresholds.**
4. **Conservatism is not validation.** Excluding a value because its meaning is unknown is a defensible analysis-population choice, not proof that the value is wrong.
5. **Every exclusion gets a reason code and a reported count.**
6. **Primary and sensitivity populations are both reported.**
7. **The QC system defines an analysis population, not “clean” or “true” measurements.**
8. **If a rule cannot be resolved from evidence, an independent reviewer must decide or the issue must remain explicitly unresolved.**

---

## 2. What the evidence actually establishes

### 2.1 Mendota flags

From the NTL-LTER daily sensor EML (`knb-lter-ntl.129.42`):

| Flag | Documented meaning | Limitations |
|---|---|---|
| `C` | Sensor off | Numeric values can remain; not equivalent to missing |
| `E` | Sensor noisy or malfunctioning | Not defined in every column; Turner pigment columns list only C/H |
| `H` | Outside of standard range | **No numeric range is defined** |
| `G` | Sensor — suspected biofouling | “Suspected,” not confirmed invalid; Turner pigment columns have no G |
| `O` | Undefined | One value in specific conductance; meaning unknown |

From the 4L.9 audit:

- `C` with numeric values exists (e.g., 316 Turner chlorophyll C flags; many DO C-with-value records).
- `H` is common; Turner chlorophyll 54, Turner phycocyanin 41; some H values are plausible extremes, others are not.
- `G` is era-specific; Turner pigment columns have no G flags. Absence of G does not prove absence of fouling.
- Undocumented codes exist in eight columns.
- Negative Turner phycocyanin: 4 unflagged values (2012-06-10 to 2012-06-16); no negative Turner chlorophyll listed.
- Turner RFU has no documented upper bound; extreme high values exist (chlorophyll max 16,211.54; phycocyanin max 12,831.18).

### 2.2 Buffalo Pound flags (if retained for future work)

- `M`: missing/failure — removal.
- `C`: faulty/unrealistic — removal.
- `B7`: caution interval covering the entire period between maintenance visits; not a removal flag.
- `A2–A6`, `B6`: not pigment-primary.
- Negative pigment RFU: no documentation; unresolved.
- >100 RFU: outside the documented 0–100 RFU full scale; cannot be assumed quantitative.
- Coverage: no date-specific expected cadence; fixed 72/144 rule withdrawn.

### 2.3 What is not established

- A numeric H range for Mendota.
- A biological meaning for negative RFU.
- A saturation/clipping/processing explanation for >100 RFU.
- A date-specific Buffalo Pound coverage rule or time zone.
- Duplicate/`REP` semantics or biomass derivation for Buffalo Pound.
- A validated sensor–biomass calibration for either lake.

---

## 3. Rule-by-rule disposition

| QC issue | Existing rule | Current evidence | Defensible status | Recommended handling | Approval required |
|---|---|---|---|---|---|
| **Missing values** | Exclude; no imputation | EML/NA; provider missingness; no zero-fill | **Verified and defensible** | Exclude; report counts; no imputation | No (technical) |
| **Mendota `C`** | Exclude primary; SENS_C includes numeric | C = sensor off; numeric C exists; may be stale/partial | **Defensible only conditionally** | Exclude primary; report numeric C separately; SENS_C as diagnostic only; do not treat numeric C as valid | Statistical reviewer |
| **Mendota `E`** | Exclude primary; SENS_E includes | E = noisy/malfunctioning; not in Turner pigment code list | **Defensible only conditionally** | Exclude where present; report; no SENS_E equivalence claim | Statistical reviewer |
| **Mendota `G`** | Exclude primary; SENS_G includes | G = suspected biofouling; Turner pigment columns have no G | **Not applicable to Turner** | No G action for Turner; if YSI were used, caution + sensitivity; do not call G invalid by definition | Scientific reviewer |
| **Mendota `O`** | Exclude primary; report | O undefined | **Verified as unresolved** | Exclude primary; report; no interpretation | No (technical), reviewer informed |
| **Undocumented flags** | Exclude primary; SENS_UNDOC numeric only | Eight columns have undocumented codes | **Defensible as conservative** | Exclude primary; report by column; SENS_UNDOC diagnostic only | Statistical reviewer |
| **Mendota `H`** | Retain primary if numeric; SENS_STRICT excludes | H = outside standard range; **no numeric range**; H includes plausible and implausible values | **Unsupported as written; requires independent reviewer decision** | Option A: exclude H primary as `UNRESOLVED_RANGE`, SENS_H includes numeric. Option B: include H primary with flag, SENS_H excludes. Report both. Do not call H valid or invalid without a documented range. | **Statistical reviewer**; NTL provider input desirable |
| **Negative RFU** | Retain primary as observed sensor output; SENS_NEG excludes; not interpreted as zero/low concentration | No provider documentation supports treating negative pigment RFU as a valid low concentration; retaining them in a rank analysis still assumes their ordering is meaningful; 4 Turner P2 negatives | **Requires custodian clarification / reviewer decision** | Exclude primary; SENS_NEG includes; report n and rank positions; no below-baseline/zero interpretation | Statistical reviewer; instrument provider input desirable |
| **Upper RFU bound (Mendota)** | No upper bound; retain finite non-negative | EML documents no range; extreme values exist | **Not resolvable; do not invent a bound** | Retain finite non-negative values; report extremes; no upper truncation; no bloom interpretation of high RFU | Scientific/statistical reviewer |
| **Upper RFU bound (Buffalo Pound)** | >100 retained primary with flag; SENS_ABOVE excludes | 0–100 RFU documented full scale; >100 may be saturation/clipping | **Contradicted / requires custodian** | Exclude >100 primary; SENS_ABOVE includes; report; if Buffalo Pound removed, defer | Custodian + reviewer |
| **Buffalo Pound B7** | Exclude primary; SENS_B7 includes | B7 = entire interval between maintenance visits; caution, not removal | **Contradicted as automatic exclusion; requires custodian** | Retain with flag; SENS_B7 excludes; report interval overlap; if Buffalo Pound removed, defer | Custodian + reviewer |
| **Buffalo Pound coverage** | ≥50% of 144 and both halves | Daily counts 42–144; no date-specific cadence; fixed rule withdrawn | **Unsupported** | No fixed threshold; require custodian date-specific rule; until then descriptive only; if removed, defer | Custodian |
| **Buffalo Pound duplicate/REP** | Mean-before-sum primary; sum/first-row sensitivity | 2018 19 duplicate groups; 2019 2; REP1/REP2 disjoint; semantics undocumented | **Unsupported as a primary rule** | No primary BP endpoint until custodian defines aggregation; mean/sum/first are different endpoint definitions, not robustness checks; if removed, defer | Custodian |
| **Buffalo Pound biomass derivation** | Arithmetic consistency; 1 g/cm³; P3/P4 downgrade | Broad microscopy/cell-volume method verified; exact multiplier/density/rounding/provider field unconfirmed | **Arithmetically consistent but unverified** | Keep P3/P4 exploratory or remove; no primary BP endpoint; request provider statement; if removed, defer | Custodian + scientific reviewer |
| **Mendota station rule** | Station 1 if present, otherwise blank; multiple non-1 stations exclude | Station blank for 371/402 dates; 31 dates station 1; methods say deep-hole sampling | **Defensible only conditionally; reviewer decision** | Primary includes all eligible 0–8 m dates; report station status; SENS_STATION1/SENS_BLANK; no station covariate | Scientific/statistical reviewer |
| **Mendota daily mean** | Provider daily mean of 1-minute data | Daily mean; no within-day counts; biology date-only; sample time unknown | **Defensible only as the only available summary; not a sample-time measurement** | Retain provider mean; state not equivalent to sample moment; no BP cross-lake equivalence claim | Scientific/statistical reviewer |
| **Detection-conditioned population** | Require at least one cyanobacteria row; no zero | Empty row not documented as zero; conditioning changes target population | **Defensible if explicit** | Define primary population as sampled dates with reported cyanobacteria row; report no-row dates separately; no zero-inclusive claim | Scientific reviewer |
| **Broad physical bounds** | DO 0–50, DO sat 0–500, temp −5–50, pH 0–14 | BP data paper; physical/analytical screens; Mendota EML does not document most ranges | **Defensible only conditionally** | Use only for contextual variables; label as screens, not validation; report values outside; no silent deletion | Statistical reviewer |
| **YSI era** | Mendota YSI 2019–2020 secondary | n≈21/22; instrument transition; no crosswalk | **Unsupported as a parallel estimate** | Remove from Stage 1; Turner only | Scientific/statistical reviewer |
| **±1-day window** | Exploratory sensitivity | Date-only biology; ±1 day changes sample composition | **Unsupported as a robustness claim** | Remove; same-date only; if reviewer requires, label exploratory co-occurrence, not robustness | Statistical reviewer |

---

## 4. Proposed Mendota-only QC position

This is a **proposed analysis population**, not a validated QC system.

### 4.1 Primary population

A Mendota date enters the primary P2/P1 population if:

1. `lakeid = ME`;
2. `depth_range = 0-8m`;
3. `sampledate` is in the Turner era (2006-07-09 to 2019-11-03);
4. the date has at least one cyanobacteria row (`division = Cyanophyta` after whitespace trimming);
5. cyanobacteria biovolume total is finite and ≥ 0;
6. the date has a same-day Turner phycocyanin (P2) or chlorophyll (P1) value;
7. the Turner value is numeric and finite;
8. the value is not flagged `C`, `O`, or an undocumented code;
9. `H` is handled according to the reviewer-approved rule (include-with-flag or exclude-primary);
10. negative RFU is excluded primary, with `SENS_NEG` including it;
11. missing values are excluded; no imputation;
12. station is reported but does not exclude the date; `SENS_STATION1` and `SENS_BLANK` are reported.

### 4.2 What is not in the primary population

- YSI-era values.
- 0–2 m biology dates.
- Dates with no cyanobacteria row (reported separately).
- Dates with no same-day Turner value.
- Values flagged `C`, `O`, or undocumented.
- Negative RFU (primary); included only in `SENS_NEG`.
- Buffalo Pound data of any kind.

### 4.3 Sensitivities (proposed, reduced)

| ID | Sensitivity | Purpose |
|---|---|---|
| `SENS_H` | Opposite H treatment from primary | Show whether H handling changes the association |
| `SENS_NEG` | Include negative RFU | Show whether the 4 negatives matter |
| `SENS_STATION1` | Restrict to station 1 dates | Station metadata check |
| `SENS_BLANK` | Restrict to blank-station dates | Station metadata check |
| `SENS_SEASON` | Seasonal descriptive strata (n≥10 only) | Seasonal confounding check |
| `SENS_LOYO` | Leave-one-year-out range | Influence diagnostic, not a CI |

No BP-specific sensitivities. No ±1-day. No bootstrap. No p-values.

### 4.4 Reporting requirements

- n before and after each exclusion.
- Counts of C/E/G/O/H/undocumented/negative values by pigment/year.
- H-treated vs H-excluded results.
- Negative-included vs negative-excluded results.
- Station-1 vs blank-station results.
- Seasonal stratum n; no stratum rho if n<10.
- Leave-one-year-out full set, not only min/max.
- Explicit statement: this is an analysis population, not “clean” or “validated” data.

---

## 5. What remains unresolved

| Issue | Status | Who can resolve |
|---|---|---|
| Numeric H range | Unresolved | NTL-LTER provider; otherwise reviewer decides treatment |
| Negative RFU meaning | Unresolved | Instrument provider; otherwise reviewer decides treatment |
| Actual n | Unknown | Count-only audit after separate authorisation |
| Within-day sensor coverage | Unknown | NTL-LTER provider |
| Biology sample times | Unknown | NTL-LTER/PhyCoTech |
| Station semantics | Incomplete | NTL-LTER provider |
| Depth mismatch | Not correctable | No depth-resolved biology; reviewer must accept reframing |
| Competition licence review | Not completed | Licence/competition reviewer |
| Buffalo Pound QC | Deferred | Custodian, if Buffalo Pound is ever revisited |

---

## 6. Verdict

**The 4L.14 QC section cannot be approved as written.** It retains H without a documented range, retains negative RFU in the primary population as observed output (implicitly treating their rank ordering as meaningful), retains >100 RFU as quantitative, excludes B7 automatically, and uses a withdrawn coverage rule.

For the reduced Mendota-only design:

- C/E/O/undocumented exclusion is defensible.
- H requires an explicit reviewer decision; both options are assumptions.
- Negative RFU should be excluded primary with a sensitivity; four P2 values are low materiality but must be reported.
- No upper RFU bound should be invented.
- Missingness exclusion is verified.
- Station rule should include all eligible dates with station sensitivity.
- Detection-conditioned population must be explicit.
- Daily mean is the only available summary, not a sample-time measurement.

**No rule is approved by this document. No analysis is authorised.**
