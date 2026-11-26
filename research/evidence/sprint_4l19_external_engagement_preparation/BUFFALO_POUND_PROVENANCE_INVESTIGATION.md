# Buffalo Pound Data Provenance Investigation

**Sprint:** 4L.19  
**Date:** 2026-11-25  
**Scope:** The two Buffalo Pound Lake datasets used by the proposed P3/P4 estimands.  
**Status:** Investigation complete for the sources accessible in this sprint. **D-05, D-02 and D-08 remain OUTSTANDING — NOT APPROVED.** No analysis, count audit, biological endpoint calculation or derived dataset was produced.

> **Bottom line.** P3/P4 depend on **two separately published datasets**, not one integrated dataset: a 2014–2021 high-frequency buoy dataset (FRDR, CC BY 4.0) and a 2018–2019 microscopy dataset (Borealis, CC BY-NC-SA 4.0). The sensor variables come from the buoy dataset; the cyanobacteria endpoint comes from the microscopy dataset. The datasets share a site and some authors, but have different licences, documentation, QC systems and version histories. The biomass field is arithmetically consistent with a volume-derived formula, but the provider’s derivation is not stated in the dataset documentation. Duplicate rows and `REP1`/`REP2` semantics remain undocumented. B7 is a **caution interval**, not a removal flag. Negative RFU and values above 100 RFU remain unresolved. Date-specific coverage, time zone and phytoplankton sample times remain undocumented.

---

## 1. Evidence standard

Material claims are graded:

- **A — direct primary evidence:** dataset files, repository metadata, official data dictionary, original paper or official instrument manual.
- **B — official institutional or manufacturer evidence:** institutional profiles, repository records, official documentation.
- **C — published secondary evidence:** peer-reviewed papers describing methods or prior findings.
- **D — reasonable inference:** a conclusion that follows from the evidence but is not explicitly stated by the provider.
- **E — unverified or unresolved:** no adequate source; must not be treated as fact.

The investigation distinguishes:

1. what the provider documents;
2. what the files show arithmetically or structurally;
3. what can reasonably be inferred;
4. what only the custodian can confirm.

---

## 2. Two datasets, not one

| Feature | Buoy dataset | Biological dataset |
|---|---|---|
| Title | A long-term water quality and meteorological data set (2014–2021) of a eutrophic prairie lake: Buffalo Pound Lake, Saskatchewan, Canada | Data for: Early and late cyanobacterial bloomers in a shallow, eutrophic lake |
| Repository | Federated Research Data Repository (FRDR) | Borealis (Wilfrid Laurier University) |
| DOI | `10.20383/103.01100` | `10.5683/SP3/MP6NXF` |
| Version | FRDR record published 2025-09-12; record states it is a previous version of a newer FRDR record (link returned 404 on 2026-11-25) | Version 1.0; deposited 2022-07-11; last updated 2025-01-20 |
| Licence | CC BY 4.0 | CC BY-NC-SA 4.0 |
| Period | 2014-06-11 to 2021-10-07 | 2018-05-29 to 2019-10-03 |
| Core content | 10-minute buoy and weather data; YSI 6600, 6025 chlorophyll, 6131 phycocyanin; 0.82 m and 2.83 m sensors | Microscopy taxonomy, cell density, cell volume, biomass; 0.8 m samples; YSI profile casts; toxins |
| Data paper | Baulch et al. 2025, *Data in Brief* 63:112290, `10.1016/j.dib.2025.112290` | Painter et al. 2022, *Environmental Science: Processes & Impacts* 24:1212–1227, `10.1039/D2EM00078D` |
| Primary contact in metadata | Helen Baulch (PI); Katy Nugent, Jay Bauer, Kristin Painter, Lisa Boyer, Lana Vuleta, Colin Whitfield, Jason Venkiteswaran (co-investigators) | Kristin Painter (corresponding author and dataset contact); Jason Venkiteswaran (dataset contact) |

**Verified:** the two datasets are separate deposits with different DOIs, licences and metadata. The buoy dataset’s README cites the 2025 *Data in Brief* paper; the biological dataset’s README cites the 2022 Painter paper and the ESS Open Archive preprint.

**Consequence:** P3/P4 are a **cross-dataset linkage**, not a single curated sensor–biology table. Any audit must document both source datasets, both licences, both QC systems and the linkage rule. A defect in either dataset affects P3/P4.

---

## 3. Buoy dataset — what is documented

### 3.1 Identity and version

- FRDR record: title as above; publication date 2025-09-12; publisher Federated Research Data Repository / Dépôt fédéré de données de recherche.
- Authors: Baulch, Nugent, Bauer, Painter, Boyer, Vuleta, Whitfield, Venkiteswaran.
- Licence: CC BY 4.0.
- Related identifier: the record is a supplement to `10.1016/j.dib.2025.112290` and a **previous version** of a newer FRDR record (`cbf4ec95-1673-4fca-a9a1-4c569b446221`). That newer record returned HTTP 404 when checked on 2026-11-25.
- The local download is `FRDR_dataset_1095_download_621_202611201621`. Its `README.txt` states it was modified on 2025-10-17 by Lisa Boyer; the CSV files carry September 2025 timestamps.

**Unresolved:** whether the local download is the current FRDR version, the newer version, or an intermediate version. The repository’s “previous version” note and the README modification date do not align cleanly. The custodian should confirm the current version and whether any values changed.

### 3.2 Sampling design

From the *Data in Brief* paper (A):

- Sensors were mounted on a stationary floating buoy with a weather station.
- Data were collected every **15 minutes in 2014** and every **10 minutes from 2015 to 2021** during the open-water deployment season.
- The buoy carried YSI 6600, 6025 chlorophyll, 6131 phycocyanin, 6136 turbidity, 6560 temperature, 6565/6561 pH and 6150+ ROX dissolved oxygen sensors.
- Shallow sensors were at **0.82 m**; deep sensors at **2.83 m**.
- The paper describes automated screening plus manual review of field notes, values outside operating ranges, values outside expected environmental ranges, repeated values and erratic rate changes.
- Data gaps are associated with sensor failure, maintenance, fouling and ice cover.

From the README (A):

- The dataset contains one CSV per study year, 2014–2021.
- `DateTime` is `YYYY-MM-DD HH:MM:SS`; **no time zone is stated**.
- Missing data are `NA`; flag columns end in `_Flag`; flags appear only when notation is required.
- The README summarises methods by reference to the *Data in Brief* paper; it does not provide a full data dictionary beyond the variable list.

### 3.3 Sensor ranges and calibration

From the *Data in Brief* paper, Table 7 (A):

- Chlorophyll (`ChlRFUShallow_RFU`, YSI 6025, wiped optical fluorescence): **0–100 RFU**; accuracy not specified.
- Phycocyanin (`BGPCShallowRFU_RFU`, YSI 6131, wiped optical fluorescence): **0–100 RFU**; accuracy not specified.
- Turbidity (YSI 6136): 0–1,000 NTU.
- Temperature (YSI 6560): −5 to 50 °C.
- pH (YSI 6565/6561): 0–14.
- DO (YSI 6150+ ROX): 0–50 mg/L; 0–500% saturation.

From the *Data in Brief* methods (A):

- pH was calibrated with pH 4, 7 and 10 buffers; oxygen with air-saturated water; conductivity with a 1,413 µS standard.
- Chlorophyll, phycocyanin and turbidity were found to show minimal drift and were typically calibrated **only at the start and end of the field seasons**.
- Turbidity and pigment sensors used a **two-point calibration**: high-purity water (Milli-Q) and commercial standards; turbidity used YSI 6073 G; **pigment sensors used rhodamine solutions**, in accordance with manufacturer instructions.
- During maintenance visits, pre- and post-maintenance values were used to assess biofouling and drift.
- The paper reports drift as consistently minimal, “typically within the range of expected sensor error”.

**Interpretation (D):** RFU are relative fluorescence units calibrated against a rhodamine standard, not chlorophyll or phycocyanin concentrations. A 0–100 RFU range is an instrument operating range, not a biological scale. The absence of per-record calibration coefficients means the audit cannot reconstruct absolute pigment concentrations; it can only compare relative fluorescence ranks.

### 3.4 QC flags

From `data_flags.csv` and the *Data in Brief* Table 2 (A):

| Flag | Documented meaning | Consequence |
|---|---|---|
| `M` | Missing; sensor removed/damaged; values not recorded/logged | Exclude from primary |
| `C` | Data deemed faulty or unrealistic | Exclude from primary |
| `A2` | PAR below factory range; adjusted to 0 | PAR not primary |
| `A3` | Inverted PAR; environmental or error | PAR not primary |
| `A4` | 2015 PAR shading | PAR not primary |
| `A5` | Localised rainfall event | Not pigment QC |
| `A6` | Corrected specific conductivity | Not pigment primary |
| `B6` | Raw conductivity step changes | Not pigment primary |
| `B7` | Chlorophyll/phycocyanin/turbidity spike followed by decrease after site visit | **Caution interval**, not removal |

### 3.5 B7 — exact semantics

The *Data in Brief* paper states (A):

> “A flag of B7 was used to identify likely periods where fouling could impact data quality. Because the onset of fouling is difficult to diagnose, the impacted period was defined as the entire duration between the last site maintenance visit and the subsequent visit where the issue was identified.”

This is decisive for D-05:

- B7 is a **period-level caution flag** covering the interval between maintenance visits.
- It does **not** establish that every observation in the interval is invalid.
- Automatic exclusion of all B7 values is **not supported** by the provider’s definition.
- Retaining B7 values in the primary population with a flag, and running a B7-exclusion sensitivity, is the defensible provisional treatment.
- The custodian should confirm whether the deposited data retain B7-flagged values or whether any were removed.

### 3.6 Negative RFU and values above 100 RFU

- The *Data in Brief* paper discusses negative **PAR** values and their replacement with zero (A2), but does **not** document negative chlorophyll or phycocyanin RFU.
- The paper documents the 0–100 RFU operating range but does **not** state whether values above 100 occur, whether they are saturation/clipping, or how they were processed.
- The 4L.18 audit found negative RFU values and noted that their meaning is undocumented.
- YSI documentation supports 0–100 RFU as the full-scale range for the 6025/6131 sensors; it does not establish that negative values are valid low concentrations.

**Classification:** both negative RFU and >100 RFU **require custodian clarification**. They must not be interpreted as biological signals or silently deleted.

### 3.7 Coverage and time zone

- The intended cadence is documented: 15 minutes in 2014, 10 minutes from 2015.
- Daily record counts vary: 121–144 in 2018 and 42–131 in 2019 (project audit, 4L.17).
- The fixed 72/144 rule was withdrawn in 4L.14 because 144 is not a documented date-specific expectation.
- No time-zone statement appears in the README or the *Data in Brief* paper.
- Saskatchewan observes Central Standard Time year-round, so a local CST interpretation is plausible, but the dataset does not state whether timestamps are local, UTC, or logger time. **Do not assume.**
- Partial-day deployment, maintenance outages, and date-boundary conventions are not documented.
- A day with many records concentrated in a short interval is not equivalent to a day with evenly distributed records; record count alone is not representativeness.

**Classification:** date-specific expected cadence, time zone, date boundary and partial-day handling **require custodian clarification**.

---

## 4. Biological dataset — what is documented

### 4.1 Identity and version

- Borealis DOI `10.5683/SP3/MP6NXF`; version 1.0; deposited 2022-07-11; last updated 2025-01-20.
- Title: “Data for: Early and late cyanobacterial bloomers in a shallow, eutrophic lake”.
- Authors: Painter, Venkiteswaran, Simon, Duy, Sauvé, Baulch.
- Licence: CC BY-NC-SA 4.0.
- Dataset contact: Laurier Library Research Data Services; Kristin Painter; Jason Venkiteswaran.
- The README states the dataset mirrors the 2022-07-12 commit of the `biogeochem/buffalopound_blooms` GitHub repository.
- The dataset contains `BP_PhytoTax_2018_KP.tab`, `BP_PhytoTax_2019_KP.tab`, group biomass tables, YSI profile casts, toxins, heterocytes, nutrients, and R scripts.

### 4.2 Biological methods

From the dataset README and the 2022 paper abstract (A/C):

- Samples were collected in 2018 and 2019, May–October, at Buffalo Pound Lake.
- The study used microscopy to identify and describe cyanobacterial species.
- The paper reports a mid-summer diazotrophic *Dolichospermum* bloom and an autumn *Planktothrix agardhii* bloom.
- The paper’s key finding is that the autumn *Planktothrix* bloom formed >60% of phytoplankton biomass but was **not detected by sensor or laboratory-derived chlorophyll-a**.

**Interpretation (C/D):** this is direct prior evidence that the sensor chlorophyll–biomass relationship at Buffalo Pound is not uniformly strong. It does not by itself invalidate P3/P4, but it makes a strong positive association unlikely to be universal and should be stated as prior context.

The full 2022 paper methods were not accessible in this sprint (RSC returned HTTP 403; ESSOAr/Authorea PDF endpoints returned HTML challenge pages). The dataset README gives the citation but not the full microscopy protocol. The *Data in Brief* paper describes the buoy, not the biological sampling. Therefore:

- the general methods are **supported by the paper abstract and dataset structure**;
- the exact counting protocol, detection limits, sample times, replicate collection and taxonomic resolution are **not fully verified** from accessible primary text.

### 4.3 `Biomass_mg_m3`

The 2018 and 2019 taxonomy tables contain:

`Sample_ID` (2018 only), `Location`, `Depth`, `DOY`, `Species_Code`, `Species_Name`, `Cell_Density_L`, `Biomass_mg_m3`, `Length_um`, `Width_um`, `Cell_Volume_um3`, `Group`, `Description_Code`, `Phylum`, `Family`, `Genus`, `Species`, `name_code`.

A deterministic arithmetic check of example rows (not an analysis) shows:

| Row | Cell volume (µm³) | Cell density (L⁻¹) | Product × 10⁻⁶ | Reported biomass (mg m⁻³) |
|---|---:|---:|---:|---:|
| *Merismopedia glauca* | 18 | 143,680 | 2.58624 | 2.59 |
| *Planktolyngbya limnetica* | 271.4 | 16,600 | 4.50524 | 4.51 |
| *Woronichinia compacta* | 500 | 400 | 0.20000 | 0.20 |

The 4L.14 review previously checked all positive rows and found median ratios of 1.000 × 10⁻⁶ in both years, with ranges consistent with rounding. That is strong evidence that the field is **arithmetically derived** as:

\[
\text{Biomass}_{mg\,m^{-3}} \approx \text{Cell\_Volume}_{\mu m^3} \times \text{Cell\_Density}_{L^{-1}} \times 10^{-6}
\]

which implies a density assumption of **1 g cm⁻³** and a wet-weight-equivalent biomass proxy.

**However:** arithmetic consistency does not prove the provider’s processing method. The dataset README does not state the formula, density, rounding order, whether biomass is computed at taxon level before summing, or whether any corrections were applied. The 2022 paper methods would be expected to state this, but the full text was not accessible. Classification: **arithmetically consistent but not provider-confirmed**.

### 4.4 Duplicate rows and `REP1`/`REP2`

A structural inspection of the supplied taxonomy files (not a biological count audit) found:

- **2018:** 817 rows, 25 sampling dates, 25 `Sample_ID` values, 18 columns. There are **19 duplicate date–species groups**, comprising 19 extra rows. The duplicates occur within the same `Sample_ID`; examples include *Merismopedia* and *Woronichinia* rows with different cell densities and biomasses.
- **2019:** 405 rows, 17 sampling dates, 18 columns (no `Sample_ID`; includes `REP`). There are **2 duplicate date–species groups**, both within `REP1`.
- **2019 `REP`:** `REP1` occurs on 12 dates (294 rows); `REP2` occurs on 5 dates (111 rows). The sets of dates are **disjoint**; no date has both `REP1` and `REP2`.
- The 2019 anomaly date 2019-07-17 (DOY 198) is entirely `REP2`.

**What this means:** `REP1` and `REP2` are **not paired technical replicates** in the supplied data. They may be replicate designations, replacement samples, counting batches, or sample IDs; the documentation does not say. The duplicate date–species rows within the same sample are also unexplained; they could be split counts, duplicate entries, or separate counting chambers.

**Classification:** **requires custodian clarification**. Do not average, sum or drop these rows by assumption.

### 4.5 Sampling times

The biological dataset includes `BP_YSI_2018.tab` and `BP_YSI_2019.tab`. These are **profile casts**, not high-frequency pigment series: they contain Date, Time, Depth, Temperature, Conductivity, DO saturation, DO concentration and pH, but no chlorophyll or phycocyanin.

A structural inspection found:

- 2018: profile dates overlap **19 of 25** biological dates; times are approximately **10:20–13:33**.
- 2019: profile dates overlap **16 of 17** biological dates; times are approximately **11:15–13:30**.

**Interpretation (D):** these are likely the visit times at which the phytoplankton samples were collected, because the dates align closely and the profiles are part of the same sampling programme. But the dataset documentation does not explicitly state that the phytoplankton sample was collected at the same time as the YSI profile. The exact phytoplankton sample time remains **unconfirmed**.

**Consequence for D-06:** the claim “biology has dates, not sampling times” is too strong for Buffalo Pound. The more accurate statement is: “the phytoplankton sample time is not documented; co-dated YSI profiles suggest late-morning to early-afternoon visits on most dates.” This strengthens the case for a Buffalo Pound daytime sensitivity, but it does not establish exact temporal alignment or make a full-day mean equivalent to the sample moment.

---

## 5. Linkage risks

The proposed P3/P4 linkage is:

- **Sensor:** `ChlRFUShallow_RFU` or `BGPCShallowRFU_RFU` from the buoy dataset, 0.82 m, 10-minute records, daily summary.
- **Biology:** sum of `Biomass_mg_m3` for `Group = Cyanophyte` from the 2018/2019 taxonomy tables, 0.8 m, one sample per date.
- **Match:** same calendar date.

Risks:

1. **Different repositories and licences.** CC BY 4.0 (buoy) and CC BY-NC-SA 4.0 (biology). A combined derived product may trigger ShareAlike; this is a D-14 issue.
2. **Different QC systems.** Buoy flags (`M`, `C`, `B7`, etc.) and biology duplicate/REP issues are independent.
3. **Different version histories.** Buoy record has a possible newer version; biology is version 1.0 with a 2025 update.
4. **Different documentation.** The buoy paper is a data descriptor; the biology paper is an ecological study. Neither documents the cross-dataset linkage.
5. **Different sampling logic.** The buoy is continuous; the biology is a discrete sample. Same date is not same time or same water parcel.
6. **Possible shared authors.** Several authors appear on both datasets; this is useful for custodian contact but does not make the datasets internally consistent.
7. **Sensor detection limitation.** The Painter paper reports that the autumn *Planktothrix* bloom was not detected by sensor chlorophyll; this is a direct caution for P3.

---

## 6. What is confirmed, supported, inferred and unresolved

### Confirmed (A/B)

- The two datasets are separate deposits with the stated DOIs, licences and periods.
- The buoy sensors are YSI 6600, 6025 and 6131; shallow pigments are at 0.82 m; the documented range is 0–100 RFU.
- The buoy sampling interval is 15 minutes in 2014 and 10 minutes from 2015.
- B7 is a caution interval covering the period between maintenance visits.
- Pigment sensors were calibrated at the start and end of seasons with a two-point rhodamine standard; per-record coefficients are not supplied.
- The biological dataset is microscopy-derived, at 0.8 m, with `Biomass_mg_m3` and cell volume/density fields.
- 2018 has 25 sampling dates; 2019 has 17.
- 2019 `REP1` and `REP2` occur on disjoint dates.

### Supported but not provider-confirmed (C/D)

- `Biomass_mg_m3` is arithmetically consistent with cell volume × cell density × 10⁻⁶ and a density of 1 g cm⁻³.
- The duplicate rows are likely data-processing or counting artifacts rather than independent samples, because they occur within the same `Sample_ID`/`REP`.
- The YSI profile times likely approximate the biological visit times.
- The autumn *Planktothrix* bloom was poorly detected by sensor chlorophyll (Painter 2022).

### Unresolved (E)

- Exact duplicate-row and `REP1`/`REP2` semantics.
- Provider’s exact biomass derivation, density, rounding and correction history.
- Whether B7-flagged values were retained or removed in the deposited files.
- Negative RFU meaning and treatment.
- Values >100 RFU: occurrence, cause, processing.
- Date-specific expected cadence, outages, partial-day handling.
- Time zone and date-boundary convention.
- Phytoplankton sample times.
- Current FRDR version and whether the local download is superseded.
- Calibration/maintenance records at record level.
- Any corrections or errata.

---

## 7. Custodian roles

The evidence distinguishes:

| Role | Person | Evidence | Limitation |
|---|---|---|---|
| Principal investigator / accountable dataset contact | **Helen Baulch**, Professor, University of Saskatchewan | FRDR record and README list her as PI contact; *Data in Brief* first author | Has not confirmed current custody in this sprint |
| Operational data/instrument manager | **Katy Nugent**, GIWS, University of Saskatchewan | README co-investigator; lab manager/field technician profile; data paper co-author | Role in current data requests not formally stated |
| Biological dataset corresponding author/contact | **Kristin Painter**, University of Saskatchewan / Environment and Climate Change Canada | Borealis dataset contact; 2022 paper corresponding author; USask adjunct profile | May have moved; current ECCC email verified on USask profile |
| Co-author / repository contact | **Jason Venkiteswaran**, Wilfrid Laurier University | Borealis dataset contact; co-author on both datasets | Not the PI; may not hold buoy QC records |
| Co-author / data curator | **Lisa Boyer**, University of Saskatchewan | README modified by Lisa Boyer; co-author | Role in current custody not stated |

**Recommended route:** address the enquiry to **Helen Baulch** as the accountable PI, with **Katy Nugent** (operational data) and **Kristin Painter** (biological data) copied. This covers the two datasets without guessing a single “custodian”. The email is prepared in `BUFFALO_POUND_FINAL_CUSTODIAN_EMAIL.md`; it has **not been sent**.

---

## 8. Decision implications

### D-05 — primary QC

Cannot be finalised. The evidence supports:

- exclude `M` and `C` from primary;
- retain B7 with a flag and run a B7-exclusion sensitivity;
- exclude negative RFU from primary pending clarification;
- exclude >100 RFU from primary pending clarification;
- do not use the fixed 72/144 coverage rule;
- treat G as a caution, not automatic invalidity (Mendota);
- do not retain H as valid without a numeric range (Mendota).

This is a **conservative interim population**, not a validated QC system.

### D-02 — Buffalo Pound endpoint

The endpoint is a derived wet-weight-equivalent biomass proxy. It is not biovolume, dry weight, carbon biomass or a direct gravimetric measurement. The exact derivation and duplicate handling remain unconfirmed. P3/P4 remain **exploratory only**.

### D-08 — replicate handling

`REP1`/`REP2` are not paired replicates in the supplied data. No aggregation rule can be justified without custodian clarification. Do not average, sum or drop by assumption.

### D-06 — daily summary

Option A remains the provisional project-owner preference because Mendota has no sample times and a common daily statistic is needed. The new Buffalo Pound profile-time evidence strengthens a **daytime sensitivity** for Buffalo Pound; it does not justify changing the primary to daytime for both lakes. D-06 remains **OUTSTANDING — NOT APPROVED**.

### D-09 — 2019-07-17

The anomaly is real in the supplied data (9 rows, all `REP2`, total 45.81 mg m⁻³, cyanophyte 41.02 mg m⁻³). It must be retained and flagged; exclusion is a sensitivity only if analysis is later authorised. No bloom interpretation. Still blocked by D-05.

---

## 9. Verdict

**The provenance investigation has resolved the dataset identity, authorship, licences, sensor models, B7 semantics and the arithmetic form of `Biomass_mg_m3`. It has not resolved the custodian-only questions.**

The most important unresolved item is not a statistical one: it is whether the deposited duplicate rows, `REP` labels, biomass derivation, B7 handling, negative/above-range RFU, coverage and time zone mean what the analysis would need them to mean. Until the custodian answers, P3/P4 cannot move from exploratory to primary, D-05 cannot be finalised, and D-15 cannot be approved.

**No contact was made. No data were acquired. No analysis was performed.**
