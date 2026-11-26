# Lake Müggelsee Evidence Audit

**Date:** 2026-11-25  
**Status:** Metadata-level evidence audit. No dataset files were downloaded, ingested, or analysed.  
**Purpose:** Determine whether Lake Müggelsee is a credible conditional Stage 2 dataset lead for EcoSentinel.

> **Verdict:** Credible lead, **not a qualified dataset**. The biological and sensor programmes are structurally strong and substantially better matched than EcoSentinel's current datasets, but access is restricted, the biological and sensor stations are not strictly co-located, event definition is unresolved, and variable-specific coverage/QC must be verified before any qualification claim.

---

## 1. Dataset inventory

| ID | FRED package | Title | Period | Cadence | Key content | Access | Relevance |
|---|---|---|---:|---|---|---|---|
| M-PHY | FRED 867 (current DOI; also served as package 3) | Müggelsee phytoplankton | 1979-03-01 to ongoing | Irregular; protocol weekly growing season, biweekly ice cover | Phytoplankton biomass/biovolume; species list; integrated samples | **All rights reserved**; request to Sabine Hilt/Tom Shatwell | Primary biological endpoint |
| M-WEEK | FRED 1 (legacy package; no DOI displayed) | Müggelsee weekly sampling multiparameter probe | 1978-07-26 to 2019-03-18 | 7 days; 14 days in winter | Temperature, conductivity, oxygen, pH, Chl a, phycocyanin, Secchi, turbidity at multiple stations/depths | **All rights reserved**; request to Sabine Hilt | Historical sensor context and depth profiles |
| M-HF | FRED 1145 (DOI 10.18728/igb-fred-1145.0) | Müggelsee Station High Frequency insitu | 2001-10-31 to ongoing | 5-minute averages; hourly gaps before 2013; no under-ice HF | Temperature, conductivity, pH, oxygen, turbidity, Chl a, phycocyanin at 1.5 m | **All rights reserved**; request to Tom Shatwell | Primary environmental predictor series |
| M-PROF | FRED 165 (no DOI displayed) | Müggelsee station Profile Data | 2004-01-01 to ongoing | 30 seconds; 1 hour before 2011 | Temperature, conductivity, oxygen, pH, Chl a, phycocyanin, turbidity profiles 0.5–5 m | **All rights reserved**; request to Tom Shatwell | Depth-resolved context at the HF station |

**Important distinction:** FRED 867 and FRED package 3 are the same phytoplankton dataset under different package/DOI history. FRED 1 is a legacy weekly multiparameter package, not the high-frequency station. FRED 1145 is the high-frequency station. FRED 165 is the high-frequency profile dataset at that station.

---

## 2. Biological records

### 2.1 Sampling frequency and coverage

The IGB phytoplankton metadata document states:

- The lake is sampled **weekly during the growing season** and **biweekly during ice cover**.
- From 1979–1986, phytoplankton was sampled weekly (biweekly in winter) at the deepest section (M7), integrated from 0.5, 4, and 7 m.
- Since 1987, integrated samples have been collected weekly at five lake stations (M3, M5, M7, M8, M10).
- Sampling continues to the present.

Source: IGB, *Sampling protocol for Lake Müggelsee: Metadata description of sampling and phytoplankton analyses* (PDF linked from FRED 867; authors Helgard Täuscher, Katrin Preuss, Jürgen Schreiber, Rita Adrian).

**Assessment:** The cadence is adequate for a weekly-resolution bloom-onset analysis. It is not sub-weekly; a claimed warning horizon shorter than about two weeks cannot be resolved.

### 2.2 Taxonomic resolution

- Phytoplankton are identified and counted by inverted microscopy (Utermöhl technique), following DIN EN 15204 and Tümpling & Friedrich.
- A species list of all taxa contributing to total biovolume is maintained; rare/stray findings are recorded separately.
- Cell dimensions are measured; biovolume is calculated from geometric shapes.
- Taxonomic resolution increased in 1993–1995 (Aulacoseira, centric diatoms, *Peridinium*, *Gymnodinium* assigned to size classes). Before 1995, unidentified taxa were aggregated at genus/family/class level; total biovolume is described as adequately reflecting total algal mass.
- Counters: Sigrid Hoeg (1979–1998), Helgard Täuscher (1998–July 2015), Katrin Preuss (August 2015–ongoing), with one-year overlap training.

**Assessment:** Species-level cyanobacteria records are plausible, but the metadata does not explicitly guarantee a consistent cyanobacteria-specific taxon list across the whole series. Taxonomic resolution and name changes require a crosswalk.

### 2.3 Biomass/biovolume

The metadata document gives the conversion:

> 10⁹ µm³ = 1 mm³ = 1 mg (specific weight = 1 g/cm³) = 10⁶ µm³ = 1 µg

and states biomass is reported in µg/L, equivalent to mg/m³.

**Assessment:** This directly supports a microscopy-derived wet-weight biomass endpoint with a documented 1 g/cm³ density assumption. This is stronger documentation than the Buffalo Pound biomass derivation and resolves one of the 4L.14 endpoint concerns for Müggelsee, not for Buffalo Pound.

### 2.4 Bloom events and non-bloom periods

- The record is year-round (weekly growing season, biweekly ice cover), so non-bloom periods are likely represented.
- The metadata does not provide an approved bloom-event definition.
- Whether at least ten independent bloom events can be defined from the cyanobacteria biomass series is **not verified**.
- Event definition must be pre-specified and independent of the sensor predictors; it cannot be borrowed from a phycocyanin threshold.

**Assessment:** Event/non-event coverage is promising but unproven. This is the single most important biological question for Stage 2.

---

## 3. Environmental and sensor records

### 3.1 High-frequency station (FRED 1145)

- Station: “Georg Mothes” measuring station, 52.4462°N, 13.6500°E (WGS84), about 300 m off the north shore; water depth about 5.5 m.
- Since October 2001; 5-minute averages from second-level sampling.
- Fixed measurement at **1.5 m** depth.
- Variables listed by FRED: turbidity, water temperature, conductivity, oxygen concentration and saturation, pH, chlorophyll a, phycocyanin.
- Phycocyanin measurement began with the YSI 6600V2-4 in **July 2007**; it is not a 2001–present series.
- Instrument history:
  - YSI 6600 from 2001.
  - YSI 6600V2-4 from July 2007 (optical oxygen sensor; phycocyanin added).
  - Two sensors from October 2014: one fixed at 1.5 m, one profiling every 30 minutes.
  - YSI EXO2 from August 2019 (new station).
- Under-ice periods: the station is removed; an hourly sensor at 1.5 m is deployed at a dolphin. High-frequency data are not year-round.
- Before 2013, there were gaps every hour because the probe was used for profile measurements.

Source: FRED 1145 page and IGB measuring-station metadata PDF.

### 3.2 Profile data (FRED 165)

- 2004–ongoing; 30-second interval (1 hour before 2011).
- Profiles at 0.5–5.0 m.
- Variables: temperature, conductivity, oxygen, pH, chlorophyll a, phycocyanin, turbidity.
- Same station as FRED 1145.

**Assessment:** The profile data could support depth-resolved comparisons and help address the surface-vs-integrated mismatch. It does not make the biological samples point-co-located, because the phytoplankton samples are integrated across stations and depths.

### 3.3 Weekly multiparameter data (FRED 1)

- 1978-07-26 to 2019-03-18; 7-day interval, 14 days in winter.
- Multiple stations (M3, M5, M7, M8, M10, MS1) and depths.
- Variables include temperature, conductivity, oxygen, pH, chlorophyll a (HPLC and YSI), phycocyanin, Secchi, turbidity.
- Legacy package; no DOI displayed.

**Assessment:** Potentially useful for historical context and cross-checking, but variable-specific coverage, depth matching, and instrument continuity are not established from the metadata. It should not be treated as a continuous 40-year sensor series without a file-level audit.

---

## 4. Spatial relationship

| Station | Coordinates | Relationship to HF station |
|---|---|---|
| HF station (M210) | 52.4462°N, 13.6500°E | Reference point; 1.5 m fixed sensor; 5.5 m water depth |
| M5 | 52.4435°N, 13.6524°E | Closest biological station, roughly 0.3–0.4 km away |
| M7 | 52.4350°N, 13.6590°E | Roughly 1.3–1.5 km away |
| M3 | 52.4385°N, 13.6703°E | Roughly 1.6–1.8 km away |
| M8 | 52.4424°N, 13.6355°E | Roughly 1.0–1.2 km away |
| M10 | 52.4318°N, 13.6328°E | Roughly 1.9–2.1 km away |

The phytoplankton sample is not a single point: it is an integration of stations and depths (0–4 m, 5–7 m, or 0–7 m depending on stratification). The HF station is a fixed 1.5 m point near the north shore.

**Assessment:** “Co-located” is **not strictly satisfied**. The dataset is a same-lake, same-season, depth-partially-overlapping design, not a point-to-point validation. A Stage 2 design would need to justify that lake-wide integrated microscopy represents the HF station's 1.5 m optical signal, or use the profile data to model the depth relationship. This is a material limitation.

---

## 5. Access and licensing

- FRED 867: “All rights reserved. Please send a request to Sabine Hilt if you like to use this data.”
- FRED 1: “All rights reserved. Please send a request to Sabine Hilt.”
- FRED 1145: “All rights reserved. Please send a request to Tom Shatwell.”
- FRED 165: “All rights reserved. Please send a request to Tom Shatwell.”
- Metadata files are published under CC BY 4.0; the data files are not open.
- No data files were downloaded. No access was bypassed.

**Assessment:** Access is possible only through a request. The authorised enquiry was sent to both researchers on 2026-11-25. Until a reply grants access, Müggelsee is a **lead**, not an available dataset.

---

## 6. What is verified vs inferred

| Claim | Status |
|---|---|
| Phytoplankton exists from 1979–ongoing | **Verified** from FRED metadata and IGB protocol |
| Weekly growing-season / biweekly ice sampling | **Verified** from IGB protocol |
| Species-level microscopy and biovolume/biomass | **Verified** from IGB protocol |
| Biomass uses 1 g/cm³ density | **Verified** from IGB protocol |
| HF station at 1.5 m from 2001 | **Verified** from FRED metadata |
| Phycocyanin from July 2007 | **Verified** from IGB station metadata |
| Chl/temp/DO/pH/turbidity/conductivity at 1.5 m | **Verified** from FRED metadata |
| 5-minute cadence | **Verified** from FRED metadata |
| Biological and HF stations are co-located | **Not verified; likely partial only** |
| ≥10 independent bloom events can be defined | **Not verified** |
| Non-bloom periods are adequately sampled | **Likely but not verified at file level** |
| Sensor calibration/maintenance records available | **Partial**: instrument list and maintenance description exist; full calibration/QC records not verified |
| Data can be obtained for educational research | **Unknown; request required** |

---

## 7. Stage 2 relevance

Müggelsee is the strongest external candidate identified because it combines:

- a 47-year weekly/biweekly species-level phytoplankton series (1979–present);
- a 19-year phycocyanin series (2007–present);
- a 25-year high-frequency chlorophyll/temperature/oxygen/pH/turbidity/conductivity series (2001–present);
- depth-profile data from 2004–present;
- documented methods, biomass conversion, and station history.

It is not yet qualified because:

- access is restricted;
- the biological and sensor stations are spatially separated and integrate different depths;
- bloom events and non-bloom periods have not been independently defined;
- variable-specific coverage, QC flags, and calibration records are unverified;
- taxonomic consistency across 1993–1995 and 2015 changes is unverified.

---

## 8. Questions for the data custodians

The research enquiry asks:

1. Is the weekly/biweekly sampling frequency and station/depth integration correctly described for the full series?
2. Are cyanobacteria-specific taxa, biovolume/biomass, and cell density available at sample level?
3. Are sample dates and times available, and can bloom/non-bloom periods be independently identified?
4. Are the HF station and phytoplankton stations comparable enough for a same-lake analysis, given the spatial offset and depth integration?
5. Which variables are available in each period, with what QC flags, calibration records, and instrument changes?
6. Can the data be accessed for independent educational research, under what terms, and through whom?

---

## 9. Verdict

**Credible Stage 2 lead — not a qualified dataset.**

The metadata evidence is strong enough to justify a targeted enquiry, but not strong enough to claim availability, compatibility, or event adequacy. The authorised email has been sent; if access is granted, the next step is a metadata/data-dictionary review before any download or analysis.
