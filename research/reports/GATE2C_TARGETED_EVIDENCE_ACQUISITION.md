# Gate 2C — Targeted Independent Evidence Acquisition

**Project:** EcoSentinel — Detecting Early Changes in Freshwater Ecosystems Using Multivariate Time-Series Analysis  
**Research question:** "Can persistent changes in relationships between freshwater environmental variables provide earlier warning of cyanobacterial blooms than conventional monitoring, at comparable false-alarm rates?"  
**Primary dataset:** Buffalo Pound Lake, Saskatchewan, Canada (DOI: 10.20383/103.01100)  
**Status:** Gate 2C investigation complete; human review required. **Gate 2 NOT approved. No labels created. No modeling performed.**  
**Date:** 2026-11-22  
**Authoring agent:** OpenCode (bounded targeted investigation)  
**Authoritative baseline:** `research/reports/GATE2_2017_2019_INTEGRATED_EVIDENCE_ASSESSMENT.md` (Exploratory only; 0 independently reconstructed events from accessible evidence).

## 1. Executive summary

This targeted investigation examined four priority sources for additional independently measured biological evidence: Boyer et al. (2025), Buffalo Pound Water Treatment Plant (BPWTP) records, Saskatchewan Water Security Agency (WSA) records, and Painter et al. (2022) dataset verification.

**Key findings:**
- **Boyer et al. 2025 (DOI 10.1111/fwb.70131):** Publication is open access per Semantic Scholar (isOpenAccess true; CC BY-NC-ND; PDF URL reported), but direct PDF/webfetch access returned 403 during this session. Full text was previously accessed via browser (2026-11-22) per existing record. Supplementary information (`fwb70131-sup-0001-AppendixS1.docx`) was previously attempted and download failed (0 bytes). No public data repository/archive containing record-level underlying biological observations was identified in targeted search. Paper states data available from corresponding author upon reasonable request — **request required; no accessible raw data obtained**. No change to independently reconstructed event count.
- **BPWTP records:** Annual reports for 2014–2021 are publicly accessible as PDFs on buffalopoundwtp.ca. PDF content could not be reliably text-extracted in-session (no PDF parser available; `strings` extraction yielded no biological keyword matches for 2019 report). Presence of phytoplankton/cyanobacteria/microcystin lab records with dates/methods/units/identifiers is **unverified** from accessible content. Public accessibility of reports ≠ verified accessible biological event evidence.
- **WSA records:** WSA publishes a Surface Water Quality Data portal (https://waterquality.saskatchewan.ca/) linked from Saskatchewan.ca/WSA pages, with Primary Station and River Basin searches. WSA page states historical 1970–2011 data publicly available and 2012-current publication planned as next phase. Whether Buffalo Pound 2014–2021 phytoplankton/cyanobacteria/toxin records with sufficient sampling frequency, methods, units, and independence are present is **unverified**. Access/verification requires human-directed query.
- **Painter et al. 2022 dataset:** Borealis dataset (DOI 10.5683/SP3/MP6NXF, CC BY-NC-SA 4.0) is publicly accessible. I verified by downloading `BP_PhytoTax_2018_KP.csv` and `BP_PhytoTax_2019_KP.csv` to a temporary directory on 2026-11-22, inspecting headers/DOYs, confirming the 2019-07-17 anomaly, then deleting temp files. Sampling DOYs match prior record (2018: 25 dates; 2019: 17 dates). Anomaly confirmed (DOY 198: 9 rows, total biomass 45.81 mg/m3, cyanophyte 41.02 mg/m3; neighbors DOY 191/210 high biomass). Toxin CSVs exist and were inspected for headers/format; interpretation/units/sample identity remain unverified for confirmed-evidence use. Dataset provides independent biological measurements but remains sparse, interval-censored, and not independently reconstructed into approved event periods.

**Net effect:** No newly accessible record-level biological evidence was obtained that enables independent event reconstruction. The number of independently reconstructable biological bloom events remains **0 confirmed**. Independent non-bloom exposure cannot be established. Matched FAR confirmatory evaluation remains not defensible.

**Final classification: C — Exploratory only.**

## 2. Investigation scope

- **In scope:** Targeted inspection of Boyer 2025, BPWTP records, WSA records, Painter 2022 dataset; verification of publicly accessible sources; documentation of access routes/barriers.
- **Out of scope / not performed:** Broad literature search; repeated failed downloads (same SI download not retried; Wiley PDF 403 recorded once); external contact; raw data modification; label creation; modeling; Gate 4; dataset/research-question changes.
- **Repository inspection:** Confirmed existing Gate 2 docs and absence of Painter raw CSVs in repo before external checks. Temp downloads used only for verification and deleted.

## 3. Findings by priority

### Priority 1 — Boyer et al. (2025), Freshwater Biology, DOI 10.1111/fwb.70131

| Field | Finding | Evidence/status |
|---|---|---|
| Citation | Boyer, L.M., Higgins, S.N., Baulch, H.M. (2025). Cyanobacterial Bloom Development, Nitrogen Fixation and Community Change: Insights on Rapid Change From a Shallow Lake. *Freshwater Biology* 70:e70131. | Verified |
| Access (publication) | Semantic Scholar API (2026-11-22) reports `isOpenAccess:true`, `openAccessPdf.status:HYBRID`, license CC BY-NC-ND, URL `https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/fwb.70131`. Direct webfetch to DOI page and pdfdirect returned 403 in-session. | Partially accessible; programmatic fetch blocked |
| Full text | Previously accessed via in-app browser 2026-11-22 (recorded in existing Gate 2 docs). Not re-downloaded. | Publication-level accessible previously |
| Supplementary info / Appendix S1 | Known SI file: `fwb70131-sup-0001-AppendixS1.docx` (Wiley supplement URL recorded in prior docs). Prior download attempt failed (0 bytes). Not retried. | Inaccessible in-session; access route unresolved |
| Underlying biological observations | Paper states data available from corresponding author upon reasonable request (per prior verified text extraction). No public repository/archive with record-level biological observations identified in targeted search. | **Request required; not publicly accessible/obtained** |
| Data-access route | Corresponding author request (human-authorized only). No institutional/public repo identified. | Human authorization required before contact |
| Suitability for independent event reconstruction | Publication reports 15 discrete biological sampling dates (DOY 190–264, 2017) and measurements, but accessible raw record-level data not obtained; phase boundaries buoy-informed. | **Not sufficient as accessible reconstructed-event evidence now** |

**Conclusion:** No new accessible raw biological data obtained. Boyer remains publication-level evidence with mixed independence; cannot support independently reconstructed event periods without accessible raw data and biological-only criteria.

### Priority 2 — Buffalo Pound Water Treatment Plant (BPWTP) records

| Field | Finding | Evidence/status |
|---|---|---|
| Public source located | BPWTP Annual Reports page: https://www.buffalopoundwtp.ca/publications/annual-report (accessed 2026-11-22). Annual report PDFs publicly listed for 2010–2025, including 2014–2021. | Publicly accessible listings |
| Targeted content check | Attempted to download 2019 annual report PDF; file downloaded (8,474,075 bytes) but PDF text extraction unavailable in environment (no pdftotext/mutool/gs/pypdf/pdfplumber). `strings` search for microcystin/cyanobacter/phytoplankton/algal bloom returned no readable matches. | **Content unverified** |
| Biological variables | Unknown from verified accessible content. Reports may contain operational/lab summaries, but phytoplankton ID/enumeration, cyanobacterial biomass, lab chl-a, microcystin/cyanotoxin dates/methods/units/sample IDs not verified. | Unverified |
| Independence | Unknown until records inspected. Treatment-plant operational measurements may not be independent biological ground truth without method/location/provenance review. | Unverified |
| Temporal coverage/frequency | 2014–2021 annual reports exist as documents; internal sampling frequency/dates unknown. | Unverified |
| Access route | Public PDF download for reports; deeper lab records may require human-authorized request to BPWTP/City of Regina/City of Moose Jaw partners as appropriate. | Partial public access; further access may require authorization |

**Conclusion:** BPWTP annual reports are publicly accessible documents but not verified as accessible biological event evidence. No confirmed phytoplankton/microcystin record-level dataset extracted.

### Priority 3 — Saskatchewan Water Security Agency (WSA)

| Field | Finding | Evidence/status |
|---|---|---|
| Public sources located | WSA Surface Water Quality Data page: https://wsask.ca/recreation-environment/lakes-and-rivers-overview/surface-water-quality-data/ (accessed 2026-11-22). Links to Saskatchewan.ca water quality info: https://www.saskatchewan.ca/residents/environment-public-health-and-safety/environmental-health/water-and-wastewater-management/water-quality-information. Portal links: https://waterquality.saskatchewan.ca/PrimaryStation and https://waterquality.saskatchewan.ca/RiverBasin. | Publicly accessible pages/portals identified |
| Coverage stated | WSA page: "Historical surface water quality data... publicly available for 1970-2011... next phase... publishing remainder of primary data from 2012-current..." Saskatchewan.ca page describes Primary Station and River Basin search by variables/date ranges. | Publication-level portal description |
| Buffalo Pound 2014–2021 biological data | Not verified. Portal was not interactively queried in this session; variables for Buffalo Pound (phytoplankton, cyanobacteria, microcystin, lab chl-a, sample IDs, methods, units, frequency) are unknown. | **Unverified** |
| Independence | Unknown until specific variables/methods verified. Sensor-derived or in-situ buoy-adjacent measures would require independence assessment. | Unverified |
| Access route | Public portal query; if needed data not available, human-authorized request to WSA/WSA Client Services may be required. | Public route exists; suitability unverified |

**Conclusion:** WSA portal is a plausible access route, but no verified Buffalo Pound 2014–2021 independent biological record-level evidence was obtained. Cannot be counted as confirmatory evidence.

### Priority 4 — Painter et al. (2022) dataset verification

| Field | Finding | Evidence/status |
|---|---|---|
| Citation / provenance | Painter, K. et al. (2022). *Data for: Early and late cyanobacterial bloomers in a shallow, eutrophic lake*. Borealis. DOI 10.5683/SP3/MP6NXF. CC BY-NC-SA 4.0. | Verified via Borealis API 2026-11-22 |
| File inventory | Borealis API confirms phyto tax, group biomass, heterocytes, toxins, nutrients, YSI, R code, README, outputs. Key files: `BP_PhytoTax_2018_KP.csv`, `BP_PhytoTax_2019_KP.csv`, `BP_2018_toxins_0.8m.csv`, `BP_2019_toxins_0.8.csv`. | Verified |
| Public accessibility | Publicly downloadable via Borealis API/datafile endpoints. I downloaded phyto tax CSVs to temp on 2026-11-22 for verification; deleted after inspection. | **Accessible (public)** |
| Sampling dates (verified) | 2018 DOYs: 149,158,164,170,172,176,184,187,190,193,197,199,205,206,211,212,220,221,226,229,233,235,240,248,260 (25 dates; 2018-05-29–2018-09-17). 2019 DOYs: 149,154,163,170,186,191,198,210,219,227,233,242,246,256,260,269,276 (17 dates; 2019-05-29–2019-10-03). | Verified from public files |
| Schema/units (observed) | 2018 header includes `Sample_ID,Location,Depth,DOY,Species_Code,Species_Name,Cell_Density_L,Biomass_mg_m3,...,Phylum,Family`. 2019 includes `Location,Depth,DOY,REP,Species_Code,...,Biomass_mg_m3,...`. Units as column names suggest cells/L and mg/m3, but full metadata/protocol verification still needed for event-definition use. | Partially verified |
| 2019-07-17 anomaly | Confirmed in public file: DOY 198 has 9 rows, total biomass 45.81 mg/m3, cyanophyte 41.02 mg/m3. Neighbors DOY 191: total 12587.1, cyano 11919.8; DOY 210: total 9497.89, cyano 6755.17. | Confirmed; cause unresolved |
| Toxin files | `BP_2018_toxins_0.8m.csv` and `BP_2019_toxins_0.8.csv` present; headers show LOD/LOQ rows and wide format with encoding artifacts. A 2019-07-17 row exists (Enki ID 25993 observed), but clean parsing/units/sample identity/interpretation not verified. | Present but **not verified for confirmed evidence use** |
| Independence | Microscopy/taxonomy/biomass are independent of buoy RFU predictors as measurement methods. | **Independent biological measurements** |
| Event reconstruction suitability | Supports candidate interval-censored biological observations only, subject to pre-approved criteria and handling of gaps/anomaly. Does not support continuous event boundaries or confirmed non-bloom exposure. | **Exploratory/candidate only; not confirmatory ground truth** |

**Conclusion:** Painter 2022 is publicly accessible and independently measured, but sparse/interval-censored. Verification improved confidence in file accessibility and anomaly, but did not create independently reconstructed event periods.

## 4. Source-by-source evidence table

| Source | Data type | Accessibility | Raw data actually available? | Independence from buoy predictors | Temporal coverage (verified) | Sampling frequency | Spatial relevance | Variables | Units | Limitations | Suitability |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Boyer et al. 2025 (FWB 70:e70131) | Biological/chemical publication; underlying data request-only | Publication OA per Semantic Scholar; pdfdirect/DOI webfetch 403 in-session; SI download failed previously; underlying data on request | **No record-level raw data obtained** | Mixed: assays independent methods; phase boundaries buoy-informed | 2017 DOY 190–264 reported (15 samples) | ~every 5 days (reported) | Buffalo Pound Lake buoy/near-buoy & U Regina site (reported) | Phytoplankton ID/enumeration/biovolume/heterocytes, chl-a, nutrients, N2 fixation, NH4+ uptake (reported) | Reported in paper; not independently verified from raw files | No accessible raw data; SI inaccessible; phase boundaries not independent ground truth | **Contextual/publication-level only** |
| BPWTP Annual Reports (2014–2021) | Operational/reports; possible lab summaries | Public PDFs listed on BPWTP website | PDFs accessible; biological record-level content unverified | Unknown | 2014–2021 annual report documents exist; sampling dates unknown | Unknown | Buffalo Pound intake/treatment plant context (likely) | Unknown/unverified | Unknown/unverified | PDF text not extractable in-session; content and independence unverified | **Unsuitable until verified** |
| WSA Surface Water Quality Data portal | Surface water quality database (variables unknown for Buffalo Pound 2014–2021) | Public portal/pages identified | Portal accessible; Buffalo Pound 2014–2021 biological records unverified | Unknown | 1970–2011 stated; 2012-current "next phase" per WSA page | Unknown | Province-wide stations; Buffalo Pound relevance unverified | Unknown; portal query needed | Unknown | Coverage/variables/frequency for Buffalo Pound 2014–2021 unverified | **Unsuitable until verified** |
| Painter et al. 2022 Borealis dataset | Biological microscopy, toxins, nutrients, YSI | Public (CC BY-NC-SA 4.0) | **Yes, public raw files accessible**; verified by temp download 2026-11-22 | Microscopy/taxonomy/biomass independent methods; toxin interpretation unverified | 2018: 25 dates; 2019: 17 dates (verified DOYs) | Discrete; 1–16 day gaps | Buffalo Pound Lake (50.5858N, -105.3834W) | Taxonomy, cell density, biomass, biovolume, group biomass, heterocytes, toxins, nutrients, YSI | cells/L, mg/m3 in phyto files (column names); toxin units/format unverified | Sparse, interval-censored; 2019-07-17 anomaly; toxin format unverified; no pre-approved event definition | **Exploratory/candidate only** |

## 5. Verified accessible datasets and exact locations

| Dataset/source | Exact location | Verification date | Notes |
|---|---|---|---|
| Painter 2022 dataset metadata | https://borealisdata.ca/api/datasets/:persistentId/?persistentId=doi:10.5683/SP3/MP6NXF | 2026-11-22 | Public API accessible; CC BY-NC-SA 4.0. |
| Painter 2022 phyto taxonomy 2018 | https://borealisdata.ca/api/access/datafile/354701?format=original | 2026-11-22 | Downloaded to temp for verification; 818 lines; 25 DOYs confirmed. |
| Painter 2022 phyto taxonomy 2019 | https://borealisdata.ca/api/access/datafile/354711?format=original | 2026-11-22 | Downloaded to temp for verification; 406 lines; 17 DOYs confirmed; DOY 198 anomaly confirmed. |
| Painter 2022 toxin files | https://borealisdata.ca/api/access/datafile/354733?format=original ; https://borealisdata.ca/api/access/datafile/354681?format=original | 2026-11-22 | Files accessible; headers inspected; interpretation unverified. |
| BPWTP annual reports index | https://www.buffalopoundwtp.ca/publications/annual-report | 2026-11-22 | Public PDF links for 2014–2021 present. |
| WSA Surface Water Quality Data page | https://wsask.ca/recreation-environment/lakes-and-rivers-overview/surface-water-quality-data/ | 2026-11-22 | Public page; portal links identified. |
| Saskatchewan water quality portal | https://waterquality.saskatchewan.ca/PrimaryStation ; https://waterquality.saskatchewan.ca/RiverBasin | 2026-11-22 | Links identified; contents not queried/verified. |

## 6. Sources requiring human authorization

| Source | Authorization needed | Why | What to request |
|---|---|---|---|
| Boyer et al. 2025 corresponding author/data custodian | Human-authorized contact/request | Underlying biological data stated as available upon reasonable request; no public raw data obtained | Record-level sampling dates, sample IDs, location/depth, phytoplankton counts/biovolume/biomass, heterocyte biovolume, chl-a, nutrients, N2 fixation, ammonium uptake, QA/method metadata; SI Appendix S1. |
| BPWTP / partner utilities | Human-authorized records request if public reports insufficient | Annual report PDFs public but biological record-level data unverified; deeper lab records may not be public | 2014–2021 phytoplankton enumeration/biovolume, cyanobacterial taxa, microcystin/cyanotoxins, lab chl-a, sampling dates/times, locations, methods, units, detection limits, QA/sample IDs. |
| WSA / Saskatchewan data custodians | Human-authorized inquiry if portal lacks needed data | Portal coverage for 2014–2021 Buffalo Pound biological variables unverified | Buffalo Pound station biological monitoring records 2014–2021: phytoplankton/cyanobacteria, toxins, lab chl-a, methods, units, frequency, sample IDs, independence from buoy. |

## 7. Failed or inaccessible sources and reasons

| Source | Attempt | Result | Reason / obstacle | Next documented route |
|---|---|---|---|---|
| Boyer 2025 DOI landing page via webfetch | https://onlinelibrary.wiley.com/doi/10.1111/fwb.70131 | 403 | Publisher access control/bot protection | Use browser/manual access; previously accessed via browser 2026-11-22. |
| Boyer 2025 pdfdirect via webfetch | https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/fwb.70131 | 403 | Publisher access control | Manual/browser download; not retried repeatedly. |
| Boyer 2025 SI Appendix S1 | Prior session download attempt | Failed (0 bytes) | Download failure / access handling | Manual browser download or author request (human-authorized). |
| BPWTP 2019 annual report text extraction | Downloaded PDF, `strings`/no parser | Content unverified | No PDF text extraction tooling in environment; PDF encoding | Human/manual PDF inspection or install approved parser in controlled environment. |
| WSA water quality portal data query | Not interactively queried | Unverified | Requires interactive portal search/UI; not completed in bounded session | Human-directed portal query for Buffalo Pound 2014–2021 biological variables. |

## 8. Scientific independence assessment

- **Painter 2022 microscopy/taxonomy/biomass:** Independent biological measurements by method relative to buoy RFU predictors. Suitable as candidate independent biological observations only after accessible verification and pre-approved event criteria.
- **Painter 2022 toxins:** Potentially independent lab measurements, but format/units/sample identity/interpretation unverified; not confirmed evidence.
- **Boyer 2025 biological assays:** Independent measurement methods as reported, but raw data inaccessible and published phase boundaries partly buoy-informed. Not independently reconstructed event evidence.
- **BPWTP/WSA records:** Independence unknown until verified by method/provenance. Operational sensor/chlorophyll proxies would not be independent ground truth for buoy-predictor evaluation.
- **Buoy RFU/phycocyanin/chlorophyll, Painter 2023:** Not independent.

## 9. Temporal coverage assessment

| Source | Coverage | Gaps / limits | Effect |
|---|---|---|---|
| Boyer 2025 | 2017 DOY 190–264 reported (15 samples) | ~5-day gaps; pre-bloom starts DOY 187 before first biological sample; raw data inaccessible | Cannot reconstruct precise or confirmed event boundaries. |
| Painter 2022 | 2018: 25 dates; 2019: 17 dates | 1–16 day gaps; 2019-07-17 anomaly; right-censoring at season ends | Interval-censored only; no continuous confirmation. |
| BPWTP annual reports | 2014–2021 documents exist | Content unverified | No verified temporal biological record. |
| WSA portal | 1970–2011 stated; 2012-current uncertain | Buffalo Pound 2014–2021 biological variables/frequency unverified | No verified coverage for target period. |
| Overall 2014–2021 | 2017–2019 have publication/priorly examined evidence; 2014–2016,2020–2021 remain unverified | Major coverage gap | Insufficient for confirmatory 2014–2021 evaluation. |

## 10. Effect on event reconstruction feasibility

- **Independently reconstructed biological bloom events (accessible evidence):** **0 confirmed** (unchanged).
- Painter 2022 verification improved confidence in public accessibility and sampling/anomaly details, but did not create pre-approved, biologically reconstructed event periods. Sparse interval censoring remains.
- Boyer 2025 remains inaccessible at raw-data level; no reconstruction possible from accessible record-level observations.
- BPWTP/WSA remain unverified potential routes.

**Conclusion:** Event reconstruction feasibility is **not materially improved**.

## 11. Effect on matched false-alarm-rate feasibility

- No confirmed independent non-bloom exposure.
- No approved event/exposure definitions.
- No defensible event denominator/numerator for matched FAR comparison.
- Sampling gaps and boundary uncertainty prevent precise lead-time/FAR evaluation.

**Conclusion:** Matched FAR confirmatory evaluation remains **not defensible**. Classification remains exploratory only.

## 12. Final A–D recommendation

**C — Exploratory only.**

**Reasoning:** Targeted investigation identified publicly accessible Painter 2022 files and public BPWTP/WSA access routes, but did not obtain accessible record-level biological evidence sufficient to reconstruct independent bloom events or establish non-bloom exposure. Boyer 2025 raw data remains request-only. BPWTP/WSA biological suitability for Buffalo Pound 2014–2021 is unverified. The original confirmatory comparison (earlier warning than conventional monitoring at comparable FAR) remains unsupported by accessible evidence.

## 13. Specific next steps requiring human decisions

1. **Authorize/decline Boyer 2025 data request:** If authorized, request SI Appendix S1 and record-level biological data from corresponding author; verify independence, units, sample IDs, and coverage before use.
2. **Authorize/decline BPWTP/WSA records inquiry:** Request 2014–2021 phytoplankton/cyanobacteria/toxin/lab chl-a records with methods, units, detection limits, QA, and sample IDs; confirm independence from buoy predictors.
3. **Direct portal/PDF review:** Human may inspect BPWTP annual report PDFs and query WSA waterquality.saskatchewan.ca for Buffalo Pound 2014–2021 biological variables.
4. **If no new verified evidence:** keep project in exploratory/descriptive scope; do not approve Gate 2; do not proceed to Gate 4.
5. **If new evidence obtained:** update register and integrated assessment; draft Gate 2/3 biological-only event/exposure criteria for human approval before any reconstruction.

## 14. References and access dates

| Reference | Location/DOI/URL | Access date | Notes |
|---|---|---|---|
| Boyer, L.M., Higgins, S.N., Baulch, H.M. (2025). *Freshwater Biology* 70:e70131 | DOI 10.1111/fwb.70131; https://onlinelibrary.wiley.com/doi/full/10.1111/fwb.70131 | 2026-11-22 (prior browser access; webfetch 403 in this session) | OA per Semantic Scholar; SI/data request required. |
| Semantic Scholar API record for Boyer 2025 | https://api.semanticscholar.org/graph/v1/paper/DOI:10.1111/fwb.70131?fields=title,year,authors,externalIds,isOpenAccess,openAccessPdf,publicationVenue,fieldsOfStudy,url | 2026-11-22 | isOpenAccess true; CC BY-NC-ND pdfdirect URL reported. |
| Painter et al. 2022 paper | DOI 10.1039/D2EM00078D | 2026-11-22 (prior record) | 2018–2019 microscopy study. |
| Painter et al. 2022 dataset | DOI 10.5683/SP3/MP6NXF; https://borealisdata.ca/api/datasets/:persistentId/?persistentId=doi:10.5683/SP3/MP6NXF | 2026-11-22 | Public; verified metadata/files; temp-downloaded phyto CSVs for verification. |
| Painter et al. 2023 | DOI 10.1002/ecs2.4472 | 2026-11-22 (prior record) | Non-independent sensor-derived classification. |
| Baulch et al. 2025 | DOI 10.1016/j.dib.2025.112290 | 2026-11-22 (prior record) | Primary dataset context. |
| BPWTP Annual Reports | https://www.buffalopoundwtp.ca/publications/annual-report | 2026-11-22 | Public PDFs listed 2010–2025. |
| WSA Surface Water Quality Data | https://wsask.ca/recreation-environment/lakes-and-rivers-overview/surface-water-quality-data/ | 2026-11-22 | Public page; portal links. |
| Saskatchewan water quality information | https://www.saskatchewan.ca/residents/environment-public-health-and-safety/environmental-health/water-and-wastewater-management/water-quality-information | 2026-11-22 | Portal links to waterquality.saskatchewan.ca. |
| Gate 2 Integrated Assessment | `research/reports/GATE2_2017_2019_INTEGRATED_EVIDENCE_ASSESSMENT.md` | 2026-11-22 | Authoritative baseline. |