# Two-Case-Study Design

**Sprint:** 4L.14  
**Status:** PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Date:** 2026-11-24

> **This document does not approve the design or authorise analysis.**

## 1. Design statement

The study is **two independent lake-specific case studies**:

- **Case 1 — Lake Mendota:** 0.5 m sensor vs 0–8 m microscopy composite; Turner 2006–2019 primary; YSI 2019–2020 secondary.
- **Case 2 — Buffalo Pound Lake:** 0.82 m sensor vs 0.8 m microscopy sample; YSI 6600 2018–2019.

Each case asks the same general question: how does surface pigment fluorescence rank with microscopy-derived cyanobacteria abundance? The cases are reported side by side.

They are **not**:

- a pooled analysis;
- a controlled comparison;
- a natural experiment;
- a validation of one lake by the other;
- a depth-alignment experiment.

## 2. Why two case studies

The two cases provide:

- a **depth-mismatched** example (Mendota 0.5 m vs 0–8 m composite);
- a **depth-aligned** example (Buffalo Pound 0.82 m vs 0.8 m sample);
- different sensor eras and instruments;
- different biological communities and bloom phenology;
- different sampling frequencies and QC systems;
- different biological endpoints (biovolume vs biomass).

This is useful for a descriptive measurement audit: it shows whether the expected mixed/variable relationship appears in both settings, and it documents how data quality differs.

It is **not** a test of depth alignment. Depth is one difference among many.

## 3. Confounders

| Dimension | Mendota | Buffalo Pound | Consequence |
|---|---|---|---|
| Lake type | Large, deep, dimictic eutrophic lake | Shallow, polymictic eutrophic reservoir | Different stratification, mixing, nutrient dynamics, bloom phenology |
| Morphometry | Deep; 0–8 m composite | Average depth ~3 m; 0.8 m sample | Different vertical structure and sample integration |
| Period | 2006–2020 | 2018–2019 | Different climate, management, trophic state |
| Biological cadence | Median 14 days | Median 4/8 days | Different temporal resolution and censoring |
| Biological depth | 0–8 m tube composite | 0.8 m discrete sample | Different sample integration, not just depth |
| Sensor depth | 0.5 m | 0.82 m | Different surface layer |
| Sensor instrument | Turner Cyclops 7; YSI EXO2 | YSI 6600 | Different optics, calibration, RFU scale |
| Sensor output | RFU; Turner/YSI non-comparable | RFU; single instrument family | No cross-lake RFU comparison |
| Community | Mixed phytoplankton; cyanobacteria median 67.2% of biovolume | Bloom-season cyanobacteria ~71% of biomass; *Dolichospermum*/*Planktothrix* phases | Different pigment content, morphology, toxicity |
| Taxonomy | 468 names; non-stationary; 2013 update | 73/56 taxa; 39 shared; 2018/2019 schema change | Different taxonomic resolution and stability |
| QC | C/E/H/G/O flags; undocumented codes; no per-record calibration | M/C/A2–A6/B6/B7; documented; interval fouling flags | Different exclusion patterns and bias |
| Endpoint | Biovolume (µm³ mL⁻¹) | Biomass (mg m⁻³) | Different quantity and derivation |
| Spatial setting | Buoy ~106 m from NTL site; station mostly blank | Single buoy near intake; biology site not independently co-located | Different spatial mismatch |
| Sampling programme | Long-term LTER | Research/data-buoy programme | Different field logistics and selection |

**Conclusion:** The cases differ in depth alignment, but also in lake type, morphometry, community, instrument, period, sampling, QC, and endpoint. The design cannot attribute a difference to depth.

## 4. Cross-case synthesis rules

Permitted:

- side-by-side descriptive tables of ρ, n, and sensitivity ranges;
- side-by-side scatterplots (separate panels);
- narrative comparison of direction/magnitude and data quality;
- explicit statement of confounders.

Not permitted:

- pooled correlation/regression;
- converting biomass to biovolume or vice versa;
- concatenating Turner and YSI;
- claiming Buffalo Pound validates Mendota;
- claiming depth alignment causes a difference;
- claiming a generalisable multi-lake relationship;
- treating the two cases as independent replicates of a common parameter.

## 5. What the cases can establish

At most:

- whether the expected mixed/variable relationship appears in each case;
- whether the descriptive association differs across seasons/eras within each case;
- how QC/missingness affect the estimate in each case;
- how the two settings differ in data quality and interpretability.

## 6. What the cases cannot establish

- a universal sensor–biovolume relationship;
- a conversion factor;
- a depth effect;
- a lake effect;
- a bloom/toxicity/early-warning conclusion;
- a generalisable multi-lake model.

## 7. Implications for the question

The revised question uses “two separate lake-specific case studies” and does not use “depth-alignment setting” as an explanatory variable. This document is the design rationale for that wording.

## 8. Governance

- **Protocol: PROPOSED — NOT APPROVED.**
- **Gate 2: PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- No analysis is authorised until the required human decisions and explicit D-15 approval are recorded.
