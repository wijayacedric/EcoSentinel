# Dataset Inclusion and Exclusion Rules

**Sprint:** 4L.12  
**Status:** PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Date:** 2026-11-24

> **No analysis may begin until this protocol has been reviewed and explicitly approved. This document defines future analysis populations; it does not create them.**

## 1. Scope

This document defines which existing observations may enter the proposed descriptive measurement study, which are excluded, and why. It covers:

- Lake Mendota daily sensor data (`knb-lter-ntl.129.42`);
- Lake Mendota phytoplankton microscopy (`knb-lter-ntl.88.31`);
- Buffalo Pound Lake buoy sensor data (FRDR `10.20383/103.01100`);
- Buffalo Pound Lake phytoplankton microscopy (Borealis `10.5683/SP3/MP6NXF`).

No new data are acquired. No raw file is modified. No derived dataset is created in this sprint.

## 2. Common principles

1. **Date is the unit of analysis.** Sensor readings and taxon rows are subsamples/components, not independent observations.
2. **No interpolation, no imputation, no zero-filling.** Missing dates are excluded, not reconstructed.
3. **No pooling across lakes, instruments, or depth classes** unless a rule explicitly says so.
4. **No species-level primary endpoint.** Broad cyanobacteria totals are used because taxonomy is non-stationary.
5. **No bloom/non-bloom labels, event intervals, thresholds, or toxicity endpoints.**
6. **Raw values are preserved.** Exclusions are analysis rules, not edits to source files.
7. **Every exclusion is counted and reported.** The analysis must include a flow table: all biological dates → dates in window → dates with sensor record → dates with valid sensor → dates in primary analysis.
8. **“Unflagged” is not “validated.”** Provider flags, undocumented codes, and unflagged anomalies are handled explicitly in `QC_AND_MISSINGNESS_PROTOCOL.md`.

## 3. Lake Mendota — sensor data

### 3.1 Source and identity

- Package: `knb-lter-ntl.129.42`, North Temperate Lakes LTER daily meteorological and metabolism data, Lake Mendota.
- Local file: `research/evidence/sprint_4l7_mendota_daily_sensor_audit/acquisition/129.42/North_Temperate_Lakes_LTER_Daily_Meteorological_and_Metabolism_Data_-_Lake_Mendota__cba9ed12834b8f315d6b10675bb60c5a.dat`
- Identity: 490,187 bytes; MD5 `eb7b3a3848b27074bac4504236ccefc3`; SHA-256 `104ef1b33769bc0ad1d3e9e6dff28219b743b81ce89ee888460d2df255981343`; 38 columns; 3,996 rows; 2006-07-09 to 2025-11-18; 0 duplicate dates; 0 malformed rows.
- Daily values are provider-derived averages of 1-minute observations. The file does not carry within-day counts, so within-day coverage cannot be reconstructed from this file.

### 3.2 Variable-level inclusion

| Source column | Unit | Depth | Era | Primary role | Inclusion rule |
|---|---|---|---|---|---|
| `avg_chlor_rfu_turner` | RFU | 0.5 m | 2006-07-09 to 2019-11-03 | **P1 primary sensor** | Include numeric values; exclude `C`, `E`, `G`, `O` flags; retain `H` if numeric and ≥0; exclude negative values from primary |
| `avg_phyco_rfu_turner` | RFU | 0.5 m | 2006-07-09 to 2019-11-03 | **P2 primary sensor** | Same rule |
| `avg_chlor_rfu_ysi` | RFU | 0.5 m | 2019-04-16 to 2025-11-18 (analysis to 2020-12-10) | Secondary Q1 | Same rule; separate era; never concatenate with Turner |
| `avg_phyco_rfu_ysi` | RFU | 0.5 m | 2019-04-16 to 2025-11-18 (analysis to 2020-12-10) | Secondary Q1 | Same rule; separate era; never concatenate with Turner |
| `avg_do_raw` | mg L⁻¹ | 0.5 m | 2006-07-11 to 2025-11-18 | Secondary contextual | Exclude `C`, `E`, `G`, `O`; retain `H` if 0–50 mg L⁻¹; negative excluded |
| `avg_do_sat` | % saturation | 0.5 m | 2006-08-05 to 2025-11-18 | Secondary contextual | Exclude `C`, `E`, `G`, `O`; retain `H` if 0–500%; negative excluded |
| `avg_do_wtemp` | °C | 0.5 m | 2006-07-09 to 2025-11-18 | Secondary contextual | Exclude `C`, `E`; retain `H` if −5 to 50 °C; provenance caveat; not a clean continuous series |
| `avg_turbidity` | FNU | 0.5 m | 2019-04-16 to 2025-11-18 | Ancillary interference | Exclude `C`, `E`; retain `H` if ≥0; negative excluded; ~22 same-day biology dates only |
| `avg_ph` | pH units | 0.5 m | 2019-04-16 to 2025-11-18 | Ancillary | Exclude `C`, `E`; retain `H` if 0–14; not a primary/secondary estimand |
| `avg_fdom` | RFU/QSU | 0.5 m | 2019-04-16 to 2025-11-18 | Ancillary | Exclude `C`, `E`; not a primary/secondary estimand |
| `avg_spec_cond` | µS cm⁻¹ | 0.5 m | 2019-04-16 to 2025-11-18 (2006 unusable) | Ancillary | Exclude all 2006 values; exclude `C`, `E`, `H`, `O`; not a primary/secondary estimand |
| `avg_par` | µmol m⁻² s⁻¹ | 2 m above water | 2007–2025 | **Excluded** | Atmospheric light context; not a biomass proxy; coverage/role insufficient |
| `avg_par_below` | µmol m⁻² s⁻¹ | 1 m | 2016–2025 | **Excluded** | Light context; not a biomass proxy; coverage/role insufficient |
| `avg_pco2_ppm` | ppm | 1 m | 2016–2025 | **Excluded** | Carbon context; not relevant to the measurement question |
| `avg_air_temp`, `avg_rel_hum`, `avg_wind_speed`, `avg_wind_dir` | various | above water | 2006–2025 | **Excluded** | Meteorological context; not relevant |

### 3.3 Era rules

- **Turner era:** use `avg_chlor_rfu_turner` and `avg_phyco_rfu_turner` for 2006–2019.
- **YSI era:** use `avg_chlor_rfu_ysi` and `avg_phyco_rfu_ysi` for 2019–2020.
- **2019 transition year:** both instruments were deployed. Analyse each separately. Do not average, convert, or choose the “better” instrument after seeing results.
- The 2026 data revision separated Turner and YSI columns. The older single combined column must **not** be used.
- No Turner–YSI cross-calibration is applied. The paired 2019 data are used only for a descriptive non-comparability check (Q7).

### 3.4 Depth rules

- All primary Mendota sensor variables are at **0.5 m**.
- The biological endpoint is a **0–8 m composite**.
- Do not interpret the 0.5 m value as a whole-column value.
- Do not apply a depth correction, because none is documented or validated.
- The 1 m PAR/pCO2 and 2 m above-water PAR variables are not depth-comparable to the 0–8 m composite and are excluded from biological comparison.

### 3.5 Analysis window

- Primary window: **2006-07-09 to 2020-12-10** (first sensor date to last biology date).
- Sensor data after 2020-12-10 are outside the biology record and are not used in the measurement study.
- Sensor data before 2006 are not available.
- Although several source columns extend to 2025, every measurement-study table and analysis is restricted to the 2006–2020 window. The longer sensor record is not used for sensor-only trend claims.

## 4. Lake Mendota — biological data

### 4.1 Source and identity

- Package: `knb-lter-ntl.88.31`, North Temperate Lakes LTER phytoplankton, Madison lakes.
- Local file: `research/evidence/sprint_4l_mendota_biology_audit/acquisition/88.31/North_Temperate_Lakes_LTER_-_Phytoplankton_-_Madison_Lakes_Area__f2de15b2fff6ae962a04c150c0a1c510.dat`
- Identity: 2,448,830 bytes; MD5 `a0363cc7fdfd6c12889750fea27bd542`; SHA-256 `a63d7cfa0502e3cdab6d8939f21820f305295e030d4d08bf10bfc69b22829db2`; 15 columns; 18,654 data rows; ASCII CSV/CRLF.
- Mendota subset: `lakeid = ME`; **9,401 records / 402 dates**; 1995-01-24 to 2020-12-10; median interval 14 days; maximum gap 120 days.

### 4.2 Row inclusion

| Field | Rule |
|---|---|
| `lakeid` | `ME` only |
| `sampledate` | Parse as calendar date; must lie in the analysis window 2006-07-09 to 2020-12-10 for primary |
| `depth_range` | `0-8m` only for primary. Exclude `0-2m` (two dates: 2002-09-23 and 2002-10-21; both outside the sensor window) |
| `division` | Trim whitespace. Primary cyanobacteria: `Cyanophyta`. Total phytoplankton: all non-blank divisions. Non-cyanobacteria: all non-blank divisions except `Cyanophyta` |
| `taxa_name` | Trim whitespace; do not use for primary aggregation; retain for audit |
| `genus` | Do not use for primary aggregation; it has 889 mismatches with the first token of `taxa_name` |
| `biovolume_conc` | Primary endpoint; sum across included rows per date; unit µm³ mL⁻¹ |
| `cells_per_ml` | Secondary endpoint; sum across included rows per date |
| `biomass_conc` | Secondary only; derived from biovolume; not independent |
| `relative_total_biovolume` | **Excluded**; denominator inconsistent, with groups summing to ~200%, 0%, and one catastrophic value |
| `sta` | Include blank or `1`. If multiple station values occur on a date, retain station `1` if present; otherwise retain the blank-station rows. Do not pool multiple stations |
| `nu_per_ml`, `cells_per_nu`, `gald` | Retain for audit; not primary endpoints |

### 4.3 Depth and station rules

- 400 dates are `0-8m`; 2 dates are `0-2m`. Only the 400 `0-8m` dates are eligible.
- The two `0-2m` dates are 2002-09-23 and 2002-10-21; they predate the sensor record, so they would be excluded by the analysis window anyway.
- `sta` is blank for 371/402 Mendota dates and `1` for 31 dates. Station metadata are too sparse to support spatial matching. The protocol treats the sample as the deep-hole station described in the EML but does not claim per-sample coordinates.
- The EML describes a tube sampler composited over 0–8 m at the deep-hole region. The sensor is at a buoy approximately 105.7 m from the NTL sampling site (4L.10). This is site-level proximity, not per-sample co-location.

### 4.4 Taxonomy rules

- **Primary:** broad `Cyanophyta` total only.
- **Secondary B4:** genus/species subsets only if a dated, documented crosswalk is approved before analysis. No crosswalk is approved in this sprint.
- Do not compare raw species names longitudinally. The EML documents taxonomic updates in February 2013 and other transitions; 204 names occur only pre-2013 and 72 only post-2013.
- Do not infer toxicity from a genus name.
- Do not treat `Cyanophyta` as equivalent to “harmful cyanobacteria” or “bloom-forming cyanobacteria.”

### 4.5 Repeated records and anomalies

- **Repeated same-key rows:** 1,009 lake/date/station/depth/taxon groups (2,048 rows) share keys but differ in values; the EML says multiple entries may represent variants or vegetative states. For the broad cyanobacteria total, **sum biovolume across rows**. Do not treat rows as independent dates.
- **Exact duplicates:** 29 exact duplicate row-groups / 58 rows, all Monona (`MO`) 1999-11-22, not Mendota. No Mendota action required beyond the general sum rule.
- **Coelastrum 2011-07-25 anomaly:** one Mendota row has cells = 0, biovolume = 7.688e-05, biomass = 84.6924, relative = 283,806.87. This is a non-cyanobacteria row. It does not affect the primary cyanobacteria endpoint. For the secondary total-biomass endpoint, exclude this row and flag it; for total biovolume, retain it but note it.
- **Biomass zeros:** 61 rows have biomass = 0 with small positive biovolume. This is low-value truncation. Biomass is secondary only; biovolume is primary.
- **Relative total biovolume:** do not use. It is not uniformly a percentage and has unresolved denominator anomalies.
- **12 blank taxa / 1,632 blank genus:** retain for audit; exclude blank-taxon rows from taxonomic subsets; they do not affect the broad division total if division is populated.

### 4.6 Mendota analysis population

The primary Mendota population is:

> All Mendota dates in 2006-07-09 to 2020-12-10 with a `0-8m` cyanobacteria biovolume total and a same-day, valid Turner chlorophyll or phycocyanin daily value under the QC rules.

The maximum size under the strict 4L.10 “unflagged only” rule is **128 for chlorophyll** and **139 for phycocyanin**. The protocol’s primary QC rule may retain `H`-flagged numeric values, so the final n may be larger. The final n must be enumerated and reported, not assumed.

## 5. Buffalo Pound — sensor data

### 5.1 Source and identity

- FRDR dataset: `10.20383/103.01100`, “A long-term water quality and meteorological data set (2014–2021) of a eutrophic prairie lake: Buffalo Pound Lake, Saskatchewan, Canada.”
- Local directory: `data/raw/buffalo_pound/FRDR_dataset_1095_download_621_202611201621/`
- Eight annual CSVs; 68 columns; **142,760 records**; 2014 15-minute, 2015–2021 10-minute; ice-free 2014-06-11 to 2021-10-07.
- Single buoy near the water-treatment intake; shallow sonde at **0.82 m**; deep sonde at **2.83 m**.
- Shallow sensors: YSI Sonde 6600; chlorophyll model 6025; phycocyanin model 6131; both optical, wiped, 0–100 RFU, accuracy not specified; temperature model 6560 (±0.15 °C); DO 6150+ROX (±1% or ±0.1 mg L⁻¹); pH ±0.2; turbidity ±0.3 NTU or ±2%; specific conductance ±0.5%.
- Pigment sensors calibrated at the start and end of each field season with rhodamine standards; maintenance approximately weekly during peak season and every two weeks otherwise; B7 flags mark likely fouling intervals between visits.
- The data paper states that chlorophyll and phycocyanin are reported in **RFU**, not concentration.

### 5.2 Variable-level inclusion

| Source column | Unit | Depth | Primary role | Inclusion rule |
|---|---|---|---|---|
| `ChlRFUShallow_RFU` | RFU | 0.82 m | **P3 primary sensor** | Include only blank-flag numeric values; exclude `M`, `C`, `B7`; negative excluded; B7 sensitivity only |
| `BGPCShallowRFU_RFU` | RFU | 0.82 m | **P4 primary sensor** | Same rule |
| `TempShallow_C` | °C | 0.82 m | Secondary contextual | Blank-flag numeric; exclude `M`, `C`; plausible −5 to 50 °C |
| `ODOShallow_mg/L` | mg L⁻¹ | 0.82 m | Secondary contextual | Blank-flag numeric; exclude `M`, `C`; plausible 0–50 mg L⁻¹ |
| `ODOSatShallow_%` | % saturation | 0.82 m | Secondary contextual | Blank-flag numeric; exclude `M`, `C`; plausible 0–500% |
| `pHShallow` | pH units | 0.82 m | Ancillary | Blank-flag numeric; exclude `M`, `C`; 0–14 |
| `TurbShallow_NTU+` | NTU/FNU | 0.82 m | Ancillary interference | Blank-flag numeric; exclude `M`, `C`, `B7`; negative excluded |
| `SpCondShallow_uS/cm` | µS cm⁻¹ | 0.8 m | Ancillary | Blank-flag numeric; exclude `M`, `C`, `A6`, `B6`; 2018 shallow correction documented; not a primary/secondary estimand |
| `TempDeep_C`, `pHDeep`, `ODODeep_mg/L`, `ODOSatDeep_%`, `SpCondDeep_uS/cm`, `ChlorophyllRFUDeep_RFU`, `BGPCDeepRFU_RFU` | various | 2.83 m | **Excluded** | Deep sensors are not depth-aligned with the 0.8 m biology; deep suite ends in 2019; do not pool with shallow |
| `Temp00`–`Temp04` thermistors | °C | 0.54–3.56 m | **Excluded** from primary | Contextual only; not a pigment proxy |
| `PARAir`, `PARW1`, `PARW2` | µmol m⁻² s⁻¹ | above/0.62/0.78 m | **Excluded** | Light context; not a biomass proxy; 2015 shading flag |
| Weather variables | various | above water | **Excluded** | Not relevant to the measurement question |

### 5.3 Era rules

- Buffalo Pound biology exists only in **2018 and 2019**. Sensor data from 2014–2017 and 2020–2021 are outside the biological analysis window and are not used in the measurement study.
- The shallow sonde is the same instrument family (YSI 6600) across 2018–2019. It is still treated as one era, not merged with Mendota Turner or Mendota YSI.
- Do not use the deep YSI 6920 series as a second era; it is a different depth and a different instrument.

### 5.4 Depth and location rules

- Biological depth: **0.8 m**.
- Shallow sensor depth: **0.82 m** (documented).
- This is the closest depth alignment in the project. It is described as “depth-aligned,” not “co-located” or “simultaneous.”
- The buoy is a single station near the water-treatment intake; the biological sampling location is described as Buffalo Pound Lake, 0.8 m. Coordinates are not independently re-verified in this sprint. Do not claim exact spatial co-location.
- Deep sensors (2.83 m) and thermistors are not used for the primary comparison.

### 5.5 Analysis window

- **2018-05-29 to 2018-09-17** (25 biological dates).
- **2019-05-29 to 2019-10-03** (17 biological dates).
- Total documented biological dates: **42**.

## 6. Buffalo Pound — biological data

### 6.1 Source and identity

- Borealis dataset: `10.5683/SP3/MP6NXF`, “Data for: Early and late cyanobacterial bloomers in a shallow, eutrophic lake.”
- Licence: **CC BY-NC-SA 4.0**.
- Local files: `research/evidence/sprint_4c_multi_lake_acquisition/downloads/buffalo_pound/painter_biological/data__clean_data__BP_PhytoTax_2018_KP.csv` and `..._2019_KP.csv`.
- 2018: 25 dates, 817 taxon rows, 73 taxa, 170 cyanophyte rows; 2018-05-29 to 2018-09-17; median gap 4 days; maximum 12 days.
- 2019: 17 dates, 405 taxon rows, 56 taxa, 78 cyanophyte rows; 2019-05-29 to 2019-10-03; median gap 8 days; maximum 16 days.
- 2018 schema: `Sample_ID`, `Location`, `Depth`, `DOY`, `Species_Code`, `Species_Name`, `Cell_Density_L`, `Biomass_mg_m3`, `Length_um`, `Width_um`, `Cell_Volume_um3`, `Group`, `Description_Code`, `Phylum`, `Family`, `Genus`, `Species`, `name_code`.
- 2019 schema: same but `REP` replaces `Sample_ID`.
- No `Biovolume` column; only `Cell_Volume_um3` and `Cell_Density_L`. The primary Buffalo Pound endpoint is therefore **biomass**, not biovolume.

### 6.2 Row inclusion

| Field | Rule |
|---|---|
| `Depth` | `0.8` only |
| `Group` | Trim whitespace. Primary cyanobacteria: `Cyanophyte`. Cross-check `Phylum = Cyanophyta` |
| `Phylum` | Use as a consistency check; if `Group` and `Phylum` disagree, flag the row and exclude from primary pending review |
| `Biomass_mg_m3` | Primary endpoint; sum across included cyanobacteria rows per date; unit mg m⁻³ |
| `Cell_Density_L` | Secondary endpoint; sum across included cyanobacteria rows per date |
| `Cell_Volume_um3` | Retain for audit; do not derive a new biovolume endpoint without separate approval |
| `Species_Name`, `Genus`, `Species` | Retain for audit; do not use for primary aggregation |
| `Group` totals | Use `BP_GroupsBiomass_2018_KP.tab` / `2019` as a cross-check, not as an independent dataset |
| Toxins | **Excluded**; format, units, compound mapping and sample identity are not verified |
| Heterocytes | **Excluded** from primary/secondary estimands; exploratory context only |
| YSI profiles | **Excluded** from primary; discrete profiles (0.2–4.0 m; 20 dates in 2018, 16 in 2019) are not high-frequency and are not the same instrument era |
| Nutrients | **Excluded**; not relevant to the measurement question |

### 6.3 Replicate and duplicate rules

- **2018:** no `REP` field; 25 unique `Sample_ID` values. Nineteen date–species groups have two rows with different densities/biomass, consistent with counting replicates but without a replicate identifier.
  - Primary rule: collapse duplicate date × species rows by **mean** before summing to the date total.
  - Sensitivity rule: collapse by **sum** and by **first row** to show the effect of the unresolved replicate structure.
- **2019:** `REP1` occurs on 12 dates and `REP2` on 5 dates, on disjoint dates. The labels are not paired replicates.
  - Primary rule: treat each date as one sample; do not treat `REP` as a replicate estimate.
  - If both `REP1` and `REP2` had occurred on the same date (they do not), average them; this is a contingency rule only.
- Do not treat 1,222 taxon rows or 248 cyanophyte rows as independent observations.

### 6.4 The 2019-07-17 anomaly

- Date: 2019-07-17 (DOY 198).
- Record: 9 taxon rows, all `REP2`; total biomass **45.81 mg m⁻³**; cyanophyte biomass **41.02 mg m⁻³** (89.5%).
- Neighbours: 2019-07-10 (DOY 191) total 12,587.1 mg m⁻³, cyanophyte 11,919.8; 2019-07-29 (DOY 210) total 9,497.9 mg m⁻³, cyanophyte 6,755.2.
- Taxonomy and group-biomass files agree; a same-date toxin sample exists but is not verified for quantitative use.
- **Primary rule: retain the date and flag it.** Do not delete, correct, or interpret it as a bloom termination or non-bloom.
- **Sensitivity rule: exclude 2019-07-17** and report the change. If the primary result depends materially on this single date, that dependence is a finding, not a reason to prefer the sensitivity result.

### 6.5 Buffalo Pound analysis population

The primary Buffalo Pound population is:

> All 42 documented biological dates in 2018–2019 with a `0.8 m` cyanobacteria biomass total and a same-day, valid shallow chlorophyll or phycocyanin daily summary under the QC and coverage rules.

The maximum is **42 dates**. After QC and coverage, the final n may be lower. The final n must be enumerated and reported.

## 7. Cross-lake rules

### 7.1 No pooled analysis

- Do not pool Mendota and Buffalo Pound into a single correlation, regression, or meta-analysis.
- Do not convert Buffalo Pound biomass to biovolume, or Mendota biovolume to biomass, without a documented conversion approved separately.
- Do not convert RFU to biomass or biovolume.
- Do not concatenate Turner and YSI.

### 7.2 Permitted cross-lake synthesis

Only a **side-by-side descriptive comparison** is permitted:

- sign of the association (positive/negative/near-zero);
- rank association and its descriptive interval;
- seasonal pattern;
- sensitivity to QC and anomaly handling;
- data-quality and missingness summary.

No claim that a difference is caused by depth alignment. The lakes differ in:

| Confounder | Mendota | Buffalo Pound |
|---|---|---|
| Lake type | Large, deep, dimictic eutrophic lake | Shallow, polymictic eutrophic reservoir |
| Biological period | 2006–2020 (14 years of overlap) | 2018–2019 (2 seasons) |
| Biological cadence | Median 14 days; date-only | Median 4/8 days; date-only |
| Biological depth | 0–8 m composite (400 dates) | 0.8 m point sample (42 dates) |
| Sensor depth | 0.5 m | 0.82 m |
| Sensor instrument | Turner Cyclops 7 (2006–2019); YSI EXO2 (2019–2020) | YSI 6600 (2018–2019) |
| Sensor output | RFU; Turner/YSI non-comparable | RFU; single instrument family |
| Community | Mixed phytoplankton; cyanobacteria median 67.2% of biovolume | Bloom-season cyanobacteria ~71% of biomass; Dolichospermum/Planktothrix phases |
| Taxonomy | 468 names; non-stationary; Feb 2013 update | 73/56 taxa; 39 shared; 2018/2019 schema change |
| QC | C/E/H/G/O flags; undocumented codes; no per-record calibration | M/C/A2–A6/B6/B7; documented; B7 interval flags |
| Depth alignment | Mismatched | Aligned |
| Endpoint | Biovolume (µm³ mL⁻¹) | Biomass (mg m⁻³) |

### 7.3 What the cross-lake comparison can say

- “The Mendota Turner chlorophyll association was [direction/size] in this sample; the Buffalo Pound chlorophyll association was [direction/size].”
- “The two settings differ in depth alignment, but they also differ in lake type, period, instrument, community, sampling frequency, and endpoint; the comparison cannot isolate depth.”
- “The descriptive patterns are consistent/inconsistent with the hypothesis that depth alignment matters, but they do not test it.”

### 7.4 What it cannot say

- “Depth alignment causes better agreement.”
- “Buffalo Pound validates the Mendota sensor.”
- “The two lakes show a generalisable sensor–biomass relationship.”
- “Surface sensors represent whole-water-column biomass.”

## 8. Exclusion summary

| Exclusion | Scope | Reason | Count / status |
|---|---|---|---|
| Mendota `0-2m` biology | 2 dates (2002-09-23, 2002-10-21) | Different depth class; outside sensor window | Excluded |
| Mendota non-`ME` lakes | Monona, Wingra, Fish | Different lakes | Excluded |
| Mendota `relative_total_biovolume` | All rows | Denominator inconsistent | Excluded |
| Mendota Coelastrum 2011-07-25 row | Total-biomass secondary only | Catastrophic biomass/relative anomaly | Excluded from total biomass; retained for total biovolume with flag |
| Mendota 2006 specific conductance | 83 numeric values | Scale/era problem; all flagged | Excluded |
| Mendota pH/fDOM/turbidity/conductance outside 2019–2020 | All | No biology overlap / short overlap | Not used in primary/secondary estimands |
| Mendota PAR/pCO2/weather | All | Not biomass proxies / coverage / role | Excluded |
| Mendota Turner/YSI concatenation | All | No cross-calibration; orders-of-magnitude difference | Prohibited |
| Buffalo Pound deep sensors | All | Different depth; deep suite ends 2019 | Excluded |
| Buffalo Pound thermistors | All | Not pigment proxies | Excluded |
| Buffalo Pound YSI profiles | All | Discrete, not high-frequency | Excluded |
| Buffalo Pound toxins | All | Format/units/sample identity unverified | Excluded |
| Buffalo Pound nutrients/heterocytes | All | Not primary/secondary endpoints | Excluded |
| Buffalo Pound 2019-07-17 | Primary retained; sensitivity excludes | Unresolved anomaly | Flagged, not deleted |
| Buffalo Pound B7-flagged pigment values | Primary excluded; sensitivity includes | Fouling interval | Flagged |
| Buffalo Pound negative pigment values | Primary excluded; sensitivity includes | Physically implausible | Flagged |
| Cross-lake pooling | All | Different endpoints/instruments/periods | Prohibited |

## 9. Provenance and licence

| Dataset | Licence | Attribution requirement | Notes |
|---|---|---|---|
| NTL-LTER 129.42 | CC BY 4.0 | Cite NTL-LTER and dataset DOI/package | Daily sensor data |
| NTL-LTER 88.31 | CC BY 4.0 | Cite NTL-LTER and dataset DOI/package | Phytoplankton microscopy |
| FRDR Buffalo Pound buoy | CC BY 4.0 | Cite Baulch et al. 2025 and FRDR DOI | Sensor data |
| Painter et al. 2022 Borealis | CC BY-NC-SA 4.0 | Cite Painter et al. 2022 and Borealis DOI; non-commercial; share-alike | Microscopy data |

The Painter licence is **non-commercial and share-alike**. Any competition entry, poster, or public output that uses these data must be checked against those terms before release. This is a human/legal decision, not an analysis decision.

## 10. Governance

- **Gate 2 remains PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- This document defines future rules only. It does not create labels, events, models, derived datasets, or analysis outputs.
- No raw file is modified.
- No analysis may begin until the protocol is reviewed and explicitly approved.
