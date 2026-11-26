# Gate 2F — Comprehensive Multi-Institutional Biological Evidence Discovery and Acquisition

**Project:** EcoSentinel — Detecting Early Changes in Freshwater Ecosystems Using Multivariate Time-Series Analysis  
**Research question:** "Can persistent changes in relationships between freshwater environmental variables provide earlier warning of cyanobacterial blooms than conventional monitoring, at comparable false-alarm rates?"  
**Primary dataset:** Buffalo Pound Lake, Saskatchewan, Canada (DOI: 10.20383/103.01100)  
**Date:** 2026-11-22  
**Status:** Gate 2F investigation complete within authorised/public scope. **Gate 2 NOT approved. No labels created. No modeling performed. No Gate 4 started.**  
**Author:** OpenCode (primary research execution agent)

## 1. Executive summary

Gate 2F conducted a broader multi-institutional/repository search for independent biological monitoring records for Buffalo Pound Lake (2014–2021, with context beyond). The investigation covered Borealis, FRDR, ECCC National Long-term Water Quality Monitoring (NLET), DataStream, Saskatchewan WSA/GeoHub portals, open.canada, USask HARVEST, Semantic Scholar, BPWTP publications, and targeted web searches for relevant researchers/programs (Baulch, Painter, Boyer, Abirhire, Spence, Davies, QU-LTER).

**Key finding:** No genuinely new, publicly downloadable, record-level independent biological dataset suitable for bloom-event reconstruction was discovered beyond evidence already obtained/verified in Gate 2D/2E (Painter 2022, BPWTP annual-report microcystin, Boyer 2021 thesis context). Several leads were identified as request-only or not verified as containing biological event records.

**Net effect on Gate 2:** No material improvement sufficient to move from **Option C — Exploratory only** toward A/B. Gate 2 remains blocked.

## 2. Search methodology

1. Reviewed Gate 2D/2E reports, evidence register, and protocol; inspected current repo/working tree.
2. Queried public repositories/APIs where accessible: Borealis API search, FRDR search/HTML parsing, ECCC NLET sites CSV, DataStream API/web endpoints.
3. Inspected Saskatchewan WSA Primary Station portal and attempted GeoHub search.
4. Ran targeted web searches for Buffalo Pound phytoplankton/cyanobacteria/toxin datasets, researcher names, QU-LTER, and institutional records.
5. Attempted to locate Boyer 2025 SI/raw data through alternate public routes (Semantic Scholar, publisher, HARVEST); no bypass of access controls.
6. Classified sources by evidence tier, independence, accessibility, and usefulness (A–E).
7. Recorded searches in `research/evidence/gate2f/search_logs/gate2f_search_log.md`.

**Limits:** No external contact, no authentication bypass, no form submission, no paywall circumvention. Some portals are JS-rendered or returned limited API responses; these were recorded as limited/failed where applicable.

## 3. Institutions, repositories, and programs investigated

| Category | Investigated | Method | Outcome |
|---|---|---|---|
| University repositories/archives | USask HARVEST, USask research group pages (limited), Borealis (USask/other) | webfetch, API, web search | Boyer 2021 thesis already known/public; no new Buffalo Pound phyto dataset |
| Federal data portals | ECCC NLET/open.canada, DataStream | webfetch, curl CSV/API | NLET has no Buffalo Pound/Qu'Appelle sites; no phyto/cell counts/toxins in NLET; DataStream API/web limited |
| Provincial portals | Saskatchewan WSA Primary Station, GeoHub | webfetch/curl | Primary Station chemical/field params only; no verified historical biological records |
| Treatment plant/lab | BPWTP annual reports/publications | existing downloaded PDFs; web search | Microcystin evidence already extracted; no new public phytoplankton/cell count dataset found |
| Research repositories | Borealis, FRDR, Dryad/Zenodo/Figshare (targeted search) | API/search/web | No new Buffalo Pound biological record-level dataset found |
| Research programs/researchers | QU-LTER, Baulch, Painter, Boyer, Abirhire, Spence, Davies, Higgins | web search/literature leads | Publications/context leads; no public downloadable biological datasets beyond Painter 2022 |

## 4. Source-by-source inventory

| Source | Institution | Evidence type | Years | Sampling frequency | Location | Independence | Accessibility | Extraction | Usefulness | Next action |
|---|---|---|---|---|---|---|---|---|---|---|
| Painter et al. 2022 dataset (DOI 10.5683/SP3/MP6NXF) | USask/Borealis | Phytoplankton taxonomy, biomass, toxins files | 2018–2019 | 25/17 discrete dates | Buffalo Pound, 0.8 m | Independent (microscopy) | Public, downloaded | Downloaded, checksums verified, derived summary created | **A (candidate, limited)** | Use only as interval-censored candidate evidence under pre-approved criteria; resolve 2019-07-17 anomaly; verify toxins |
| Painter et al. 2023 Blooms/flows dataset (DOI 10.5683/SP3/IP8JSZ) | USask/Borealis | Buoy sensor data, GAM/code, climate/hydrometric | 2014–2020 | High-frequency/sensor-derived | Buffalo Pound buoy | **Not independent** (buoy-derived bloom periods) | Public | Metadata inspected; no phyto taxonomy files | **D** for independent ground truth / **C** contextual | Do not use as biological ground truth |
| Baulch 2014–2021 buoy/meteorological dataset (FRDR 49311077...) | USask/FRDR | Buoy/meteorological water quality | 2014–2021 | Sub-hourly | Buffalo Pound buoy | Not independent ground truth | Public | Known primary dataset | **D** as ground truth; primary predictor dataset | Keep as predictor dataset only |
| FRDR DOM/water quality dataset (4131a773...) | USask/FRDR | DOM/water quality (no bio keywords found) | 2016–2019 | Spatiotemporal (per metadata) | Buffalo Pound | N/A for bloom ground truth | Public | Metadata/description inspected | **C/D** | No phytoplankton/cell count extraction possible from description |
| BPWTP annual reports 2014–2021 | Buffalo Pound Water Treatment Plant | Raw/treated microcystin; limited 2014–2016 narrative/screening | 2014–2021 | Monthly May–Oct (2017–2021); limited earlier | Intake/treated water | Independent lab toxin method | Public, downloaded | PDFs downloaded; microcystin extracted | **B** (supporting toxin evidence) | Human-authorized request for underlying lab/phyto records |
| Boyer et al. 2025 (DOI 10.1111/fwb.70131) | Freshwater Biology/USask | Phytoplankton, chl-a, nutrients, N2 fixation (reported) | 2017 | 15 samples, ~5 days, DOY 190–264 (reported) | Buffalo Pound | Mixed (methods independent; phase boundaries buoy-informed) | Full text previously accessed; SI/raw inaccessible | Publication-level only | **E** (potentially useful, inaccessible raw) | Human-authorized data request |
| Boyer 2021 thesis (USask HARVEST 10388/13318) | USask | Thesis context, 2017 sampling description | 2017 | Described biweekly/additional samples | Buffalo Pound | Publication-level | Public | Accessed/text-searched | **C** | Corroboration only; no raw record-level dataset |
| ECCC NLET | Environment and Climate Change Canada | Physical-chemical water quality (no phyto/cell counts/toxins) | varies | varies | No Buffalo Pound/Qu'Appelle sites found in site CSV | N/A | Public | Sites CSV checked | **D** for biological events | None for Buffalo Pound bio |
| WSA Primary Station portal | Saskatchewan WSA/Govt SK | Chemical/field/chlorophyll-a listed; no phytoplankton/taxonomy/microcystin visible | unknown/portal | unknown | Qu'Appelle R HWY 2 above Buffalo Pound (river station) | Unknown; likely not bio event ground truth | Public portal | Inspected | **C/E** | Human-authorized inquiry for historical biological records |
| Spence 2025 BPWTP 39-year chlorophyll-a record | BPWTP/USask (reported) | Lab chlorophyll-a (reported) | 39 years (per paper) | typically weekly (reported) | BPWTP intake/Buffalo Pound | Lab method potentially independent; not public | Request-only (reported) | Not accessible | **E** | Human-authorized request to BPWTP/WSA; verify method/location/units |
| DataStream | Gordon Foundation/hubs | Water quality data platform | varies | varies | No confirmed Buffalo Pound biological records obtained | Unknown | Limited/API unclear in-session | Search attempted; inconclusive | **E** | Manual/authorized follow-up if needed |
| QU-LTER / other USask projects | USask/GIWS | Various limnology publications | varies | varies | Qu'Appelle/Buffalo Pound context | varies | Mixed/publication-level | Web search only | **C/E** | Only pursue specific record-level leads with clear biological fields |

## 5. Datasets actually downloaded/verified in Gate 2F

| Item | Status | Location | Verification |
|---|---|---|---|
| Painter 2022 files | Already downloaded in Gate 2D | `research/evidence/gate2d/painter_2022_borealis/` | Checksums previously verified; re-used in Gate 2E |
| BPWTP annual reports 2014–2021 | Already downloaded in Gate 2D | `research/evidence/gate2d/bpwtp_reports/` | Public PDFs; text extraction derived file present |
| ECCC NLET sites CSV | Queried via curl, not stored as evidence (public, large) | Not saved | grep for Buffalo/Qu'Appelle returned no matches |
| Borealis IP8JSZ metadata | Inspected via API | Not downloaded (no new bio data) | File inventory confirms buoy/GAM/climate/hydrometric only |

**No new biological record-level dataset was downloaded in Gate 2F.**

## 6. Biological measurements extracted/available

| Source | Measurements available | Extracted in repo? | Usable for event reconstruction? |
|---|---|---|---|
| Painter 2022 | Taxonomy, cell density, biomass mg/m3, biovolume dims, group/phylum/genus/species, sample ID, DOY, location, depth, REP (2019) | Yes (original CSVs + derived summary) | Candidate only, interval-censored |
| Painter 2022 toxins | Toxin CSVs present | Original files downloaded; interpretation unverified | Not confirmed |
| BPWTP reports | Raw/treated microcystin (µg/L), monthly 2017–2021; 2016 narrative; 2014–2015 limited screening | Derived text extraction | Supporting toxin evidence only |
| Boyer 2025 | Reported phyto/chl-a/nutrients/N2 fixation/NH4 uptake | No raw accessible | No |
| WSA Primary Station | Chlorophyll a/nutrients/ions/field params (portal list) | No record-level extraction | No |

## 7. Coverage and sampling assessment

| Source | Years | Frequency | Biological event suitability | Major gaps |
|---|---|---|---|---|
| Painter 2022 | 2018–2019 | 25 and 17 discrete dates | Candidate point observations only | 1–16 day gaps; 2019-07-17 anomaly; no 2014–2017,2020–2021 |
| BPWTP microcystin | 2014–2021 (variable) | Monthly May–Oct 2017–2021; limited earlier | Toxin context only | No taxonomy/biovolume; monthly; intake-located |
| Boyer 2025 | 2017 | ~15 samples (reported) | Inaccessible raw; mixed boundaries | No accessible record-level data |
| ECCC NLET | N/A | N/A | None for Buffalo Pound | No relevant station |

## 8. Independence assessment

- **Independent by method (candidate/supporting):** Painter microscopy/biomass; BPWTP lab microcystin; Boyer biological assays (methods).
- **Not independent / circular for ground truth:** Buoy phycocyanin/RFU, buoy-derived Painter 2023 bloom periods, any threshold derived from same buoy predictors.
- **Mixed:** Boyer published phase boundaries partly buoy/sensor-informed.

## 9. Accessibility and licence status

| Source | Licence/terms | Access |
|---|---|---|
| Painter 2022 Borealis | CC BY-NC-SA 4.0 | Public |
| Painter 2023 IP8JSZ | CC BY-NC-SA 4.0 | Public |
| BPWTP annual reports | Public website reports; no explicit open-data licence observed | Public |
| ECCC NLET | Open Government Licence - Canada | Public |
| FRDR/Borealis metadata | Public | Public |
| Boyer 2025 SI/raw | Publisher/author controlled | Request-only / inaccessible |
| BPWTP/WSA historical lab records | Unknown | Request required |

## 10. Unsuccessful/limited searches and unresolved leads

| Lead | Result | Why unresolved | Next action (human-authorized) |
|---|---|---|---|
| DataStream API/web | API returned `{"message":null}`; explore URL 404 in-session | Platform/API behavior uncertain | Manual portal check or authorized inquiry |
| WSA GeoHub/interactive station query | JS/limited fetch; no biological params visible in Primary Station | Historical biological records not verified | Request WSA historical biological monitoring records |
| Boyer 2025 SI Appendix S1 | 403/inaccessible in-session | Access control/no public repo | Authorized author request |
| BPWTP phytoplankton/cell counts 2014–2021 | Not found in public annual reports | May exist internally only | Authorized BPWTP/WSA records request |
| Spence 2025 39-year BPWTP chl-a | Reported in paper; not public | Data held by BPWTP/WSA | Authorized request; verify independence/method |
| Abirhire Buffalo Pound phyto dataset | No public dataset found | May not exist publicly or different lake focus | No external contact without authorization |
| CanWIN | Not conclusively searched via robust API | Time/portal behavior | Low-priority manual check |

## 11. Final scientific assessment

Gate 2F did **not** discover a new publicly downloadable, record-level independent biological dataset capable of changing Gate 2 feasibility. The evidence base remains: Painter 2022 (2018–2019 sparse point observations, candidate only), BPWTP microcystin (sparse toxin support), Boyer 2025/2021 (context, inaccessible raw). This supports **Option C — Exploratory only**. Option A/B are not justified by currently accessible evidence.

## 12. References

- Baulch et al. 2025, Data in Brief, DOI 10.1016/j.dib.2025.112290; FRDR dataset 49311077-df4b-4071-81b6-ac328a77d430.
- Boyer 2021, USask HARVEST 10388/13318.
- Boyer, Higgins, Baulch 2025, Freshwater Biology, DOI 10.1111/fwb.70131.
- Painter et al. 2022, Environ. Sci.: Processes Impacts, DOI 10.1039/D2EM00078D; Borealis DOI 10.5683/SP3/MP6NXF.
- Painter et al. 2023, Ecosphere, DOI 10.1002/ecs2.4472; Borealis DOI 10.5683/SP3/IP8JSZ.
- BPWTP annual reports 2014–2021: https://www.buffalopoundwtp.ca/publications/annual-report.
- ECCC NLET: https://open.canada.ca/data/en/dataset/67b44816-9764-4609-ace1-68dc1764e9ea.
- WSA Primary Station: https://waterquality.saskatchewan.ca/PrimaryStation.
- Gate 2F search log: `research/evidence/gate2f/search_logs/gate2f_search_log.md`.