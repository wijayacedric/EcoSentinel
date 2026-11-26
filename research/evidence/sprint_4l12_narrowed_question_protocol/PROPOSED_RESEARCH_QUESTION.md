# Proposed Research Question

**Sprint:** 4L.12  
**Status:** PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Date:** 2026-11-24

> **No analysis may begin until this protocol has been reviewed and explicitly approved.**

## 1. Purpose of this document

This document converts the Sprint 4L.11 strategic direction — **CONTINUE — NARROWED RESEARCH QUESTION** — into a precise, testable descriptive question.

It also records where the original 4L.11 wording is scientifically imprecise and recommends a replacement. The replacement does **not** authorise analysis. It is a proposal for human review.

## 2. The 4L.11 wording and its problem

The 4L.11 wording was:

> How comparable are high-frequency surface sensor proxies (chlorophyll/phycocyanin fluorescence, dissolved oxygen and temperature) with independent microscopy-derived cyanobacteria biovolume in Lake Mendota and Buffalo Pound Lake, and how do observed associations and data quality vary by season, sensor era and depth alignment?

The phrase **“how comparable”** is too broad. It can mean at least six different things:

| Term | What it requires | Is it proposed here? |
|---|---|---|
| **Statistical association** | A directional, usually monotonic, relationship between two variables | **Yes — primary descriptive target** |
| **Correlation** | A specific linear (Pearson) or rank (Spearman) statistic | **Spearman primary; Pearson secondary only** |
| **Agreement** | Two measurements of the *same quantity*, on the *same scale*, with quantified bias and limits of agreement | **No — not estimable** |
| **Predictive performance** | A calibrated model evaluated on held-out data with error/accuracy metrics | **No — not proposed** |
| **Biological measurement validity** | Evidence that the sensor is an unbiased, calibrated measure of cyanobacteria biomass across conditions | **No — cannot be established with these data** |
| **Ecological interpretation** | A causal or mechanistic explanation of the pattern | **No — descriptive only** |

The critical distinction is **association versus agreement**. Two variables can be strongly rank-associated while disagreeing substantially in absolute terms. Chlorophyll/phycocyanin fluorescence is reported in relative fluorescence units (RFU), whereas microscopy biovolume is reported in µm³ mL⁻¹ and Buffalo Pound biomass in mg m⁻³. These are different quantities on different scales. Without a validated conversion, absolute agreement, Bland–Altman limits of agreement, concordance correlation, and predictive accuracy are **not estimable**.

A second problem is that the 4L.11 wording mixes **chlorophyll** (a pigment present in all phytoplankton) with **phycocyanin** (a cyanobacterial accessory pigment). They answer different questions. Chlorophyll is expected to track total phytoplankton biomass; phycocyanin is expected to track cyanobacteria specifically. The protocol therefore treats them as separate primary variables, not as interchangeable “sensor proxies.”

A third problem is that **depth alignment** is a lake-level descriptor, not an experimental treatment. Mendota compares a 0.5 m sensor with a 0–8 m composite; Buffalo Pound compares a 0.82 m sensor with a 0.8 m sample. Many other differences between the lakes (community composition, instruments, sampling programme, period, QC, taxonomy) are confounded with depth. The protocol can describe the two settings side by side; it cannot attribute a difference in association to depth alignment.

## 3. Recommended primary question

> **In Lake Mendota (2006–2020) and Buffalo Pound Lake (2018–2019), among same-day paired observations and analysed separately by lake and sensor era, what are the direction, strength and descriptive uncertainty of the rank association between surface chlorophyll and phycocyanin fluorescence and independent microscopy-derived cyanobacteria biovolume (Mendota) or cyanobacteria biomass (Buffalo Pound), and how do these associations vary by season and depth-alignment setting?**

This is a **descriptive measurement/comparability study**. It is **not** an early-warning validation, a bloom-detection study, a sensor calibration, or a test of toxicity.

### 3.1 Operational definition of “comparability”

For this protocol, **comparability** means only:

1. **Rank association** — whether dates with higher sensor fluorescence also tend to have higher microscopy-derived cyanobacteria abundance, measured by Spearman’s ρ.
2. **Relative concordance** — whether the direction of change between consecutive biological sampling dates tends to agree with the direction of change in the sensor series (exploratory secondary analysis only).
3. **Descriptive variation** — whether the observed rank association differs across pre-specified seasons and sensor eras.

It does **not** mean absolute agreement, bias correction, calibration, validation, or prediction.

### 3.2 Why “agreement” is not claimed

- RFU and biovolume/biomass are not the same measurand.
- There is no cross-calibration between Turner and YSI, and no conversion from RFU to biovolume.
- A high rank correlation can coexist with large proportional bias.
- Absolute agreement would require paired measurements of the same quantity, replicated across the full range, with documented calibration and error models. Those data do not exist in this project.
- Therefore the protocol reports **rank association and relative concordance**, and explicitly refuses **absolute agreement** language.

## 4. Primary biological endpoint

### 4.1 Mendota

**Total cyanobacteria biovolume concentration** per sampling date:

- Source: NTL-LTER phytoplankton microscopy, package `knb-lter-ntl.88.31`, Mendota (`lakeid = ME`).
- Rows: `division = Cyanophyta` after whitespace trimming.
- Value: sum of `biovolume_conc` across all cyanobacteria rows for the date.
- Unit: µm³ mL⁻¹ (equivalent to 10⁻³ mm³ m⁻³; the source EML defines 10⁶ µm³ mL⁻¹ = 1 mm³ mL⁻¹).
- Depth: `depth_range = 0-8m` only.
- Taxonomic scope: broad division-level total; no species-level crosswalk in the primary analysis.

This endpoint measures cyanobacterial volume, **not** bloom status, toxicity, surface scum, or whole-lake exposure.

### 4.2 Buffalo Pound

**Total cyanobacteria biomass** per sampling date:

- Source: Painter et al. 2022 microscopy, Borealis `10.5683/SP3/MP6NXF`.
- Rows: `Group = Cyanophyte` after whitespace trimming (cross-checked against `Phylum = Cyanophyta`).
- Value: sum of `Biomass_mg_m3` across cyanobacteria rows for the date.
- Unit: mg m⁻³.
- Depth: `Depth = 0.8` only.
- Taxonomic scope: broad group-level total; no species-level primary analysis.

**Important:** Buffalo Pound supplies **biomass**, not biovolume. The source has `Cell_Volume_um3` and `Cell_Density_L`, from which biovolume could be derived, but deriving a new endpoint is **not authorised** in this sprint. The two lakes therefore do not share a common numeric endpoint. They are analysed separately, and the cross-lake comparison is a structured descriptive contrast, not a pooled correlation.

### 4.3 Why biovolume is principal, and biomass is the Buffalo Pound substitute

Biovolume is closer to the geometric microscopy measurement and is less dependent on an assumed density conversion. Mendota supplies it directly. Buffalo Pound supplies biomass, which is the provided, documented endpoint. Using the supplied biomass avoids creating an unauthorised derived dataset and avoids inventing a cross-lake conversion.

The protocol must state in every result that **Mendota biovolume and Buffalo Pound biomass are not numerically equivalent**.

## 5. Secondary biological endpoints

These are pre-specified as secondary/exploratory. They do not replace the primary endpoint.

| ID | Endpoint | Mendota source | Buffalo Pound source | Role |
|---|---|---|---|---|
| B1 | Cyanobacteria cell density | sum `cells_per_ml` for Cyanophyta | sum `Cell_Density_L` for Cyanophyte | Secondary; tests whether results depend on count versus volume |
| B2 | Total phytoplankton biovolume | sum `biovolume_conc` all divisions | sum `Biomass_mg_m3` all groups | Secondary; tests whether chlorophyll tracks total biomass rather than cyanobacteria specifically |
| B3 | Non-cyanobacteria biovolume/biomass | sum all non-Cyanophyta divisions | sum all non-Cyanophyte groups | Secondary; discriminant contrast |
| B4 | Bloom-forming genus subsets | `Microcystis`, `Dolichospermum`/`Anabaena`, `Aphanizomenon`, `Planktothrix`, `Woronichinia` | same, where present | Exploratory only; requires an approved taxonomic mapping; not a primary endpoint |
| B5 | Heterocyte counts | not applicable | supplied heterocyte files | Exploratory context only; not a biomass endpoint |
| B6 | Toxins | not available in this dataset | supplied toxin files, format unverified | **Excluded**; not verified for quantitative use |

B4 is deliberately exploratory. Mendota taxonomy is non-stationary (468 unique names, 176 genera, 204 names only pre-2013 and 72 only post-2013; 889 genus-field mismatches). Buffalo Pound has 73 taxa in 2018 and 56 in 2019, with only 39 shared. Species-level longitudinal claims are not defensible without a dated crosswalk.

## 6. Primary sensor variables

| ID | Variable | Lake / era | Unit | Depth | Role |
|---|---|---|---|---|---|
| S1 | Turner chlorophyll fluorescence | Mendota, 2006–2019 | RFU | 0.5 m | Primary P1 |
| S2 | Turner phycocyanin fluorescence | Mendota, 2006–2019 | RFU | 0.5 m | Primary P2 |
| S3 | YSI 6600 chlorophyll fluorescence | Buffalo Pound, 2018–2019 | RFU | 0.82 m | Primary P3 |
| S4 | YSI 6600 phycocyanin fluorescence | Buffalo Pound, 2018–2019 | RFU | 0.82 m | Primary P4 |

Turner and YSI are **never concatenated**. They are different instruments with different optical systems, calibration histories, and RFU scales. The 2019 Mendota paired data show median ratios of approximately 0.00033 (chlorophyll) and 0.00084 (phycocyanin) for YSI relative to Turner — orders of magnitude apart. No crosswalk exists.

## 7. Secondary sensor variables

| Variable | Role | Inclusion rule |
|---|---|---|
| Dissolved oxygen (mg L⁻¹ and % saturation) | Contextual/physiological | Secondary; not a biomass proxy; report separately |
| Water temperature | Contextual | Secondary; Mendota provenance ambiguous before 2019; do not treat as a clean continuous series |
| Turbidity | Optical interference/confounder | Ancillary only; Mendota coverage is ~22 same-day dates, all 2019–2020; not enough for era/season analysis |
| pH, specific conductance, fDOM | Ancillary | Mendota coverage ~22 same-day dates, all 2019–2020; exclude from primary/secondary estimands; report coverage only |
| PAR (above/below water) | Light context | **Exclude** from biological comparison; coverage and role do not justify inclusion |
| pCO2 | Carbon context | **Exclude**; not relevant to the measurement question |
| Air temperature, RH, wind | Meteorological context | **Exclude**; not relevant |

The protocol does not treat DO or temperature as “sensor proxies for biomass.” They are contextual variables that may help interpret the optical signal, but they are not alternative measurements of cyanobacteria.

## 8. Observational unit and target population

### 8.1 Observational unit

**One lake–date observation.** Each observation consists of:

- one biological endpoint value for that date and depth class;
- one sensor daily summary for the same date and instrument era.

Sensor readings within a day (1-minute at Mendota, 10-minute at Buffalo Pound) are **subsamples**, not independent observations. Taxon rows within a biological sample are **components**, not independent observations. The effective sample size is the number of dates, not the number of sensor records or taxon rows.

### 8.2 Target population

The target population is the set of dates on which:

- a valid biological endpoint exists under the rules in `DATASET_INCLUSION_EXCLUSION_RULES.md`;
- a valid same-day sensor summary exists under the rules in `TEMPORAL_MATCHING_SPECIFICATION.md`; and
- the date lies within the lake-specific analysis window.

Mendota window: **2006-07-09 to 2020-12-10** (sensor record start to last biology date).  
Buffalo Pound window: **2018-05-29 to 2019-10-03** (the two biological seasons).

### 8.3 Scope of inference

The scope is **two specific lakes, specific periods, specific instruments, and specific sampling programmes**. The study does not estimate:

- a universal sensor–biovolume relationship;
- a global conversion factor;
- bloom/non-bloom status;
- toxicity risk;
- early-warning lead time;
- whole-water-column biomass from a surface sensor;
- causal effects of depth alignment.

## 9. Primary estimands

There are four primary estimands. They are fixed before analysis.

| ID | Lake | Sensor era | Sensor variable | Biological endpoint | Maximum n (strict unflagged) | Primary statistic |
|---|---|---|---|---|---:|---|
| P1 | Mendota | Turner 2006–2019 | Chlorophyll RFU | Cyanobacteria biovolume (0–8 m) | 128 | Spearman ρ |
| P2 | Mendota | Turner 2006–2019 | Phycocyanin RFU | Cyanobacteria biovolume (0–8 m) | 139 | Spearman ρ |
| P3 | Buffalo Pound | YSI 6600 2018–2019 | Chlorophyll RFU | Cyanobacteria biomass (0.8 m) | 42 | Spearman ρ |
| P4 | Buffalo Pound | YSI 6600 2018–2019 | Phycocyanin RFU | Cyanobacteria biomass (0.8 m) | 42 | Spearman ρ |

The n values are **upper bounds under the strict “unflagged only” rule** used in Sprint 4L.10. The primary QC rule in this protocol retains some `H`-flagged numeric values (see `QC_AND_MISSINGNESS_PROTOCOL.md`), so the final n may be larger. The final n must be enumerated and reported before estimation. No n is guaranteed.

## 10. Secondary questions

These are pre-specified but subordinate. They must not be promoted to primary claims after seeing results.

| ID | Question | Analysis | Status |
|---|---|---|---|
| Q1 | Does the Mendota YSI era (2019–2020) show a similar descriptive pattern to the Turner era? | Separate Spearman ρ for YSI chlorophyll/phycocyanin; n ≈ 21/22 | Secondary; small n; descriptive only |
| Q2 | Do cyanobacteria cell-density endpoints show the same pattern as biovolume/biomass? | Spearman ρ for B1 vs S1–S4 | Secondary |
| Q3 | Does chlorophyll track total phytoplankton biomass better than cyanobacteria specifically? | Spearman ρ for B2 vs S1/S3; compare descriptively with P1/P3 | Secondary |
| Q4 | Does phycocyanin track cyanobacteria better than chlorophyll does? | Compare P1 vs P2 and P3 vs P4 descriptively; no formal test | Secondary |
| Q5 | Does the association vary by season? | Spearman ρ within spring/summer/autumn; report n; no interaction test | Secondary/exploratory |
| Q6 | Does the association vary between the depth-mismatched Mendota setting and the depth-aligned Buffalo Pound setting? | Side-by-side descriptive comparison; no causal attribution | Secondary/exploratory |
| Q7 | Are Turner and YSI interchangeable in 2019? | Descriptive same-day ratios/ranks on ~11 biology dates; no calibration | Secondary; documentation of non-comparability |
| Q8 | How sensitive are results to QC, temporal window, and the Buffalo Pound 2019-07-17 anomaly? | Pre-specified sensitivity analyses | Secondary |

## 11. What the question does not ask

The protocol explicitly does **not** ask:

- whether sensors can detect blooms;
- whether sensors can provide early warning;
- whether sensor alarms have acceptable false-alarm rates;
- whether sensor fluorescence is a validated measure of toxicity;
- whether surface sensors represent whole-water-column biomass;
- whether depth alignment causes better agreement;
- whether Turner and YSI can be converted;
- whether the results generalise to other lakes.

Those questions would require different data and different designs.

## 12. Precision verdict

**The 4L.11 wording is not sufficiently precise.** It conflates association, agreement, correlation, prediction, and validation.

**The recommended wording in Section 3 is precise only if the following are accepted:**

1. “Comparability” is operationally defined as rank association plus relative concordance, not absolute agreement.
2. Mendota biovolume and Buffalo Pound biomass are separate endpoints and are never pooled.
3. Turner and YSI are separate instrument eras and are never concatenated.
4. The cross-lake depth contrast is descriptive, not causal.
5. No predictive, validation, bloom, toxicity, or early-warning claim is permitted.

If those five conditions are not accepted, the question should return to human review or the project should move to **PAUSE — INSUFFICIENT SCIENTIFIC FEASIBILITY** rather than proceed with an ambiguous measurement study.

## 13. Governance

- **Gate 2 remains PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- No labels, event intervals, confirmatory models, hypothesis tests, threshold optimisation, protocol changes, external contacts, uploads, commits or pushes were made in preparing this document.
- No analysis may begin until the full 4L.12 protocol is reviewed and explicitly approved.
