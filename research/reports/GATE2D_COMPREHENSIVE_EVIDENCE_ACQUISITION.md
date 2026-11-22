# Gate 2D — Comprehensive Independent Biological Evidence Acquisition and Verification

**Project:** EcoSentinel — Detecting Early Changes in Freshwater Ecosystems Using Multivariate Time-Series Analysis  
**Research question:** "Can persistent changes in relationships between freshwater environmental variables provide earlier warning of cyanobacterial blooms than conventional monitoring, at comparable false-alarm rates?"  
**Primary dataset:** Buffalo Pound Lake, Saskatchewan, Canada (DOI: 10.20383/103.01100)  
**Date:** 2026-11-22  
**Status:** Gate 2D investigation complete (bounded by accessible/public evidence and authorization limits). **Gate 2 NOT approved. No labels created. No modeling performed. No Gate 4 started.**  
**Author:** OpenCode (primary research execution agent; autonomous within authorized scope)

## 1. Executive summary

Gate 2D conducted a targeted-but-broad investigation to locate, obtain, verify, and assess independent biological evidence for Buffalo Pound Lake (2014–2021). The investigation inspected existing repository evidence, downloaded and verified public Painter 2022 Borealis files, accessed the Boyer 2021 USask thesis as publication-level context, inspected WSA/Saskatchewan water-quality portals, and downloaded/extracted BPWTP annual reports (2014–2021).

**Genuinely new/strengthened evidence obtained:**
- **Painter et al. 2022 dataset (Borealis DOI 10.5683/SP3/MP6NXF, CC BY-NC-SA 4.0):** Publicly downloaded to `research/evidence/gate2d/painter_2022_borealis/` on 2026-11-22. Checksums verified against Borealis metadata. Confirmed 2018 (25 DOYs) and 2019 (17 DOYs) sampling dates, schemas, and 2019-07-17 anomaly (DOY 198: 9 rows, total biomass 45.81 mg/m3, cyanophyte 41.02 mg/m3; neighbors DOY 191 12587.1/11919.8, DOY 210 9497.89/6755.17). Toxin files present but format/units/sample-identity/interpretation not fully verified for confirmed-evidence use.
- **BPWTP annual reports (2014–2021, public PDFs):** Downloaded to `research/evidence/gate2d/bpwtp_reports/` and text-extracted with `pypdf` in a temporary venv. Monthly raw/treated-water microcystin tables were extracted for 2017–2021 (May–Oct); 2016 includes narrative microcystin values (July/September, peak 7 µg/L raw; 0.1 µg/L or less after conventional treatment; non-detectable after GAC); 2014–2015 report annual organics/microcystin screening entries (limited timing detail). These are independent lab toxin measurements at intake/treated water, but sparse, intake-located, and not phytoplankton taxonomy/biovolume.
- **Boyer 2021 USask MES thesis (handle 10388/13318):** Publicly accessible PDF downloaded and text-extracted in temp; confirms 2017 Buffalo Pound sampling context (July 10–Sep 21 / DOY 191–264 described; biweekly plus additional discrete samples). Publication-level corroboration only; no accessible record-level raw dataset obtained.
- **WSA/Saskatchewan water-quality portal:** Primary Station portal identifies "QU'APPELLE R. HWY 2 ABOVE BUFFALO POUND LK. MDSTRM" with chemical/field parameters (including chlorophyll a, nutrients, pH, DO, etc.) but no phytoplankton taxonomy/cell counts/microcystin parameters visible in station parameter list. Suitability for independent biological bloom reconstruction remains unverified/low.

**Bottom line:** Evidence position improved modestly (public Painter files verified in-repo evidence dir; BPWTP microcystin records extracted). However, the core bottleneck remains: **0 independently reconstructed biological bloom events** from accessible evidence under pre-approved biological-only criteria; **no defensible independent non-bloom exposure denominator**; **matched-FAR confirmatory evaluation remains not defensible**. Final classification: **C — Exploratory only** (bordering on B for limited toxin-context evidence, but insufficient for confirmatory matched-FAR).

## 2. Exact investigation scope

- **In scope:** Public/web-accessible sources; existing repo evidence; Painter 2022 Borealis; Boyer 2025/2021 publications; BPWTP annual reports; WSA/Saskatchewan portals; targeted web searches; public repository checks; PDF extraction/OCR alternatives where feasible; evidence documentation.
- **Out of scope / not performed:** Contacting researchers/agencies; submitting data requests; bypassing access controls/paywalls/auth; accepting licenses on user's behalf; modifying raw primary dataset in `data/raw/`; creating model labels; training/tuning models; Gate 4; changing research question/primary dataset; commits/pushes.
- **Time:** Investigation executed 2026-11-22.

## 3. Search methodology

1. Read mandatory Gate 2/2C documents and inspect repository.
2. Prioritize highest-value sources: Painter 2022 public dataset, Boyer 2025/2021, BPWTP annual reports, WSA portals.
3. Use targeted web searches, direct URL fetches, public APIs (Borealis, Semantic Scholar), and file downloads.
4. For PDFs, install `pypdf` in temporary venv under `/private/var/folders/.../T/opencode` (reversible) and extract text; record extraction limitations.
5. Verify downloaded files with checksums where available; preserve originals in `research/evidence/gate2d/`.
6. Assess evidence against independence, accessibility, temporal coverage, event-reconstruction, non-bloom exposure, and matched-FAR criteria.
7. Record failed/inaccessible sources and human-authorization needs.

## 4. Search log

| Date | Query / action | Platform/source | Result | Relevant leads/files | Status | Reason for stopping |
|---|---|---|---|---|---|---|
| 2026-11-22 | Read mandatory Gate 2 reports/register | Local repo | Loaded 4 docs | Existing Gate 2 baseline | Complete | Baseline established |
| 2026-11-22 | "Boyer Higgins Baulch 2025 Freshwater Biology 10.1111/fwb.70131 supplementary data Dryad Zenodo Figshare" | websearch | Generic/no useful results | None | Stopped | Poor results; used direct DOI/Semantic Scholar |
| 2026-11-22 | "Buffalo Pound Lake phytoplankton counts microcystin laboratory data 2014-2021 Saskatchewan Water Security Agency open data" | websearch | No useful results | None | Stopped | Refined to direct portal URLs |
| 2026-11-22 | "Buffalo Pound Water Treatment Plant annual report phytoplankton cyanobacteria monitoring data Saskatchewan" | websearch | No useful results | BPWTP site known | Stopped | Used direct BPWTP site |
| 2026-11-22 | Fetch Boyer DOI page | webfetch Wiley | 403 | — | Failed | Access control; previously browser-accessed |
| 2026-11-22 | Fetch Semantic Scholar record for 10.1111/fwb.70131 | API | Success | OA metadata; pdfdirect URL (403 on fetch) | Complete | Metadata captured |
| 2026-11-22 | Fetch Borealis dataset 10.5683/SP3/MP6NXF | Borealis API | Success | File inventory, license, checksums | Complete | Dataset verified |
| 2026-11-22 | Download Painter phyto/biomass/toxin/nutrient/README files | Borealis datafile API | Success | `research/evidence/gate2d/painter_2022_borealis/*` | Complete | Checksums matched |
| 2026-11-22 | Fetch USask HARVEST Boyer thesis handle 10388/13318 | webfetch | Success | Thesis metadata + PDF link | Complete | Publicly accessible |
| 2026-11-22 | Download Boyer 2021 thesis PDF | USask HARVEST | Success | Temp PDF; text extracted | Complete | Publication-level context only |
| 2026-11-22 | Fetch https://waterquality.saskatchewan.ca/PrimaryStation | webfetch | Success | Station list incl. Qu'Appelle R HWY 2 above Buffalo Pound; chemical params only | Complete | No phytoplankton/toxin params visible |
| 2026-11-22 | Fetch BPWTP annual report page | webfetch | Success | 2014–2021 PDF links | Complete | Downloaded reports |
| 2026-11-22 | Download BPWTP annual reports 2014–2021 | curl | Success | `research/evidence/gate2d/bpwtp_reports/*.pdf` | Complete | 8 PDFs downloaded |
| 2026-11-22 | Extract BPWTP PDFs with pypdf (temp venv) | local script | Partial success | Microcystin tables/mentions extracted; font warnings | Complete | Text extraction sufficient for microcystin sections |
| 2026-11-22 | "Buffalo Pound Lake phytoplankton monitoring dataset..." / open.canada.ca / CanWIN | websearch | No useful results | None | Stopped | No credible Buffalo Pound phytoplankton dataset found |
| 2026-11-22 | "Buffalo Pound Lake cyanobacteria microcystin monitoring data University of Saskatchewan Helen Baulch dataset repository" | websearch | No useful results | — | Stopped | No public record-level dataset found |
| 2026-11-22 | "Qu'Appelle Long-Term Ecological Research Program Buffalo Pound phytoplankton data QU-LTER" | websearch | No useful results | — | Stopped | No accessible dataset identified |

## 5. Source-by-source findings

### A1. Painter et al. 2022 / Borealis 10.5683/SP3/MP6NXF
- **Access:** Public, CC BY-NC-SA 4.0. Downloaded and checksums verified.
- **Files verified:** `BP_PhytoTax_2018_KP.csv`, `BP_PhytoTax_2019_KP.csv`, `BP_GroupsBiomass_2018_KP.csv`, `BP_GroupsBiomass_2019_KP.csv`, `BP_2018_toxins_0.8m.csv`, `BP_2019_toxins_0.8.csv`, `Nutrients_Biomass_BP_clean.csv`, `README.md`.
- **Sampling dates:** 2018 25 DOYs; 2019 17 DOYs (confirmed). No continuous daily observations.
- **2019-07-17 anomaly:** Confirmed unresolved (DOY 198 low biomass between high-biomass neighbors). No explanatory field note found in inspected files.
- **Toxins:** Files present; wide/encoded format; LOD/LOQ rows; 2019-07-17 row present. Not verified for confirmed-evidence use.
- **Independence:** Microscopy/taxonomy/biomass independent of buoy RFU by method.
- **Reconstruction:** Candidate interval-censored observations only; no approved event definition; cannot establish continuous event boundaries or non-bloom exposure.

### A2. Boyer et al. 2025 / Boyer 2021 thesis
- **Boyer 2025:** OA metadata confirmed via Semantic Scholar; DOI/pdfdirect webfetch 403 in-session; SI previously failed; underlying record-level data request-only. No new accessible raw data.
- **Boyer 2021 thesis (USask HARVEST 10388/13318):** Publicly accessible. Provides 2017 Buffalo Pound context (July 10–Sep 21, DOY 191–264 described; biweekly plus additional discrete samples; phytoplankton/biovolume/N2 fixation). Publication-level corroboration; not accessible raw record-level dataset for independent event reconstruction.
- **Human authorization required** for any data request to authors.

### A3. Buffalo Pound Water Treatment Plant annual reports
- **Access:** Public PDFs 2014–2021 downloaded.
- **Extracted evidence:** Monthly microcystin (May–Oct) raw/treated tables for 2017–2021; 2016 narrative July/September values with peak 7 µg/L raw; 2014–2015 annual organics screening including microcystin (limited). Treated-water microcystin generally <0.1 µg/L or below MAC.
- **2017:** May 2 <0.1/<0.1; Jun 6 <0.1/<0.1; Jul 4 <0.1/<0.1; Aug 8 0.3/<0.1; Sep 11 0.7/<0.1; Oct 16 0.1/<0.1 µg/L (raw/treated).
- **2018:** May 8 <0.1/<0.1; Jun 18 0.4/<0.1; Jul 16 0.3/<0.1; Aug 20 <0.1/<0.1; Sep 17 <0.1/<0.1; Oct 16 0.1/<0.1.
- **2019:** May 6 <0.1/<0.1; Jun 17 0.3/<0.1; Jul 15 0.6/<0.1; Aug 12 4.5/<0.1; Sep 16 0.3/<0.1; Oct 28 0.3/<0.1.
- **2020:** May 5 <0.1/<0.1; Jun 15 1.1/<0.1; Jul 13 0.9/<0.1; Aug 10 0.3/<0.1; Sep 14 <0.1/<0.1; Oct 26 <0.1/<0.1.
- **2021:** May 3 <0.1/<0.1; Jun 14 0.38/0.04; Jul 12 0.2/<0.1; Aug 9 0.4/<0.1; Sep 13 <0.1/<0.1; Oct 25 <0.1/<0.1.
- **Independence:** Lab toxin assay is independent of buoy RFU measurement method. However, intake location/treatment-plant context differs from buoy; monthly sampling sparse; not phytoplankton community/biovolume.
- **Limitations:** No phytoplankton cell counts/taxonomy/biovolume tables extracted; microcystin is toxin evidence, not a complete biological bloom definition; monthly May–Oct only; <LOD handling; method details not fully extracted.

### A4. Saskatchewan WSA / Saskatchewan.ca
- **Primary Station portal:** `https://waterquality.saskatchewan.ca/PrimaryStation` accessible; station "QU'APPELLE R. HWY 2 ABOVE BUFFALO POUND LK. MDSTRM" present. Parameters listed include chlorophyll a, nutrients, ions, pH, temp, DO, TDS, TSS, turbidity, etc.; **no phytoplankton taxonomy/cell counts/cyanobacteria biovolume/microcystin visible**. River station, not lake buoy biological monitoring.
- **WSA Surface Water Quality Data page:** 1970–2011 historical; 2012-current "next phase". Not verified for 2014–2021 Buffalo Pound biological records.
- **Conclusion:** No verified independent biological bloom-reconstruction data obtained.

### A5. Other institutions/repositories
- USask HARVEST: Boyer thesis found (public). No public record-level Boyer 2017 biological dataset found.
- open.canada.ca, CanWIN, FRDR, Zenodo/Figshare targeted searches: no relevant Buffalo Pound 2014–2021 phytoplankton/cyanobacteria record-level dataset identified in targeted queries.
- ECCC long-term monitoring: not confirmed as Buffalo Pound phytoplankton bloom-event dataset; no accessible record-level evidence obtained.

## 6. All successfully located datasets and documents

| Item | Location | Type | Access date | Notes |
|---|---|---|---|---|
| Painter 2022 dataset | `research/evidence/gate2d/painter_2022_borealis/` (from Borealis DOI 10.5683/SP3/MP6NXF) | Public biological dataset | 2026-11-22 | Checksums verified |
| BPWTP annual reports 2014–2021 | `research/evidence/gate2d/bpwtp_reports/` | Public PDFs | 2026-11-22 | Text extracted for microcystin |
| BPWTP microcystin extraction | `research/evidence/gate2d/bpwtp_reports/bpwtp_microcystin_extract.txt` | Derived text extraction | 2026-11-22 | Derived from public PDFs |
| Boyer 2021 thesis metadata/page | https://harvest.usask.ca/items/9dde7e9b-474c-4b91-b509-6f836a3ede3d | Public thesis record | 2026-11-22 | PDF downloaded to temp only |
| WSA Primary Station portal | https://waterquality.saskatchewan.ca/PrimaryStation | Public portal | 2026-11-22 | No phytoplankton/toxin params visible |

## 7. Links and citations to primary sources

- Baulch, H.M. et al. (2025). *Data in Brief* 63:112290. DOI: 10.1016/j.dib.2025.112290.
- Boyer, L.M. (2021). *The dynamics of biological nitrogen fixation in prairie lakes*. MES thesis, University of Saskatchewan. https://hdl.handle.net/10388/13318.
- Boyer, L.M., Higgins, S.N., Baulch, H.M. (2025). *Freshwater Biology* 70:e70131. DOI: 10.1111/fwb.70131.
- Painter, K. et al. (2022). *Environ. Sci.: Processes Impacts* 24:1212–1227. DOI: 10.1039/D2EM00078D.
- Painter, K. et al. (2022). Borealis dataset. DOI: 10.5683/SP3/MP6NXF.
- Painter, K. et al. (2023). *Ecosphere* 14:e4472. DOI: 10.1002/ecs2.4472.
- BPWTP annual reports: https://www.buffalopoundwtp.ca/publications/annual-report (2014–2021 PDFs).
- WSA Surface Water Quality Data: https://wsask.ca/recreation-environment/lakes-and-rivers-overview/surface-water-quality-data/.
- Saskatchewan Primary Station Water Quality: https://waterquality.saskatchewan.ca/PrimaryStation.

## 8. Downloaded file inventory

| Path | Source | Retrieval date | Type | Integrity/provenance |
|---|---|---|---|---|
| `research/evidence/gate2d/painter_2022_borealis/BP_PhytoTax_2018_KP.csv` | Borealis 354701 | 2026-11-22 | Original CSV | MD5 `f57e21b23e561e3d15f4a11865449341` |
| `research/evidence/gate2d/painter_2022_borealis/BP_PhytoTax_2019_KP.csv` | Borealis 354711 | 2026-11-22 | Original CSV | MD5 `2fc0856bd5efa15f5cf96ca6cdfde45f` |
| `research/evidence/gate2d/painter_2022_borealis/BP_GroupsBiomass_2018_KP.csv` | Borealis 354725 | 2026-11-22 | Original CSV | MD5 `02da4e9aee5dc565afd1f229196143ef` |
| `research/evidence/gate2d/painter_2022_borealis/BP_GroupsBiomass_2019_KP.csv` | Borealis 354712 | 2026-11-22 | Original CSV | MD5 `3ca8940ed76ba4bc048cb7121c9745c8` |
| `research/evidence/gate2d/painter_2022_borealis/BP_2018_toxins_0.8m.csv` | Borealis 354733 | 2026-11-22 | Original CSV | MD5 `5ae39943552c3381a841592a71c0a968` |
| `research/evidence/gate2d/painter_2022_borealis/BP_2019_toxins_0.8.csv` | Borealis 354681 | 2026-11-22 | Original CSV | MD5 `5add75f7c981dc38b8e58160a9c8fcb4` |
| `research/evidence/gate2d/painter_2022_borealis/Nutrients_Biomass_BP_clean.csv` | Borealis 354719 | 2026-11-22 | Original CSV | MD5 `2fc2e7908a22e7bd6f2709b0d6bc453b` |
| `research/evidence/gate2d/painter_2022_borealis/README.md` | Borealis 354920 | 2026-11-22 | Original MD | MD5 `dedf2acd37ace824d426c1550e2bca0a` |
| `research/evidence/gate2d/bpwtp_reports/annual-report-2014.pdf`–`2021.pdf` | BPWTP website | 2026-11-22 | Original PDFs | Public reports; sizes recorded in shell log |
| `research/evidence/gate2d/bpwtp_reports/bpwtp_microcystin_extract.txt` | Derived from BPWTP PDFs | 2026-11-22 | Derived text | Extraction via pypdf; verify against original PDFs |

## 9. Provenance and licence information

| Source | Licence / terms | Attribution | Notes |
|---|---|---|---|
| Painter 2022 Borealis dataset | CC BY-NC-SA 4.0 | Painter, K. et al.; Borealis | Use with attribution; non-commercial/share-alike |
| BPWTP annual reports | Public website reports; no explicit open-data license observed on page | Buffalo Pound Water Treatment Plant / BPWTC | Publicly accessible; use for evidence assessment with citation |
| Boyer 2021 thesis | USask HARVEST public thesis record | Lisa M. Boyer, USask | Publicly accessible thesis |
| WSA/Saskatchewan portals | Public government web portals | WSA / Government of Saskatchewan | Accessed for verification; no bulk download performed |

## 10. Biological independence assessment

| Evidence | Measurement method | Independent of buoy RFU predictors? | Suitability as biological ground truth |
|---|---|---|---|
| Painter microscopy/taxonomy/biovolume | Microscopy, lab enumeration/biomass | **Yes (method)** | Candidate independent biological observations; sparse interval-censored |
| Painter toxin files | Lab toxin/cyanopeptide assays (reported) | **Potentially yes**, but format/units/sample identity unverified | Not confirmed until verified |
| Boyer 2025 biological assays | Microscopy, chl-a, nutrients, N2 fixation, NH4 uptake (reported) | **Methods yes; phase boundaries mixed** | No accessible raw data; not reconstructed |
| BPWTP microcystin | Lab microcystin assay (raw/treated intake) | **Yes (method)** | Independent toxin evidence; sparse monthly; intake location; not bloom taxonomy/biovolume |
| WSA Primary Station chlorophyll a | Lab/field chemical parameter (portal listing) | Method may be independent but not buoy RFU; station is river above lake | Not bloom event ground truth; limited relevance |
| Painter 2023 / buoy RFU | Sensor-derived | **No** | Not ground truth |

## 11. Sampling frequency and temporal coverage

| Source | Years | Frequency / dates | Coverage quality | Gap/uncertainty |
|---|---|---|---|---|
| Painter 2022 | 2018–2019 | 25 and 17 discrete dates | Two seasons, point observations | 1–16 day gaps; 2019-07-17 anomaly; no continuous coverage |
| Boyer 2025 (reported) | 2017 | 15 samples, ~every 5 days, DOY 190–264 | One season, publication-level | Raw data inaccessible; ~5-day gaps; phase boundaries buoy-informed |
| BPWTP microcystin | 2014–2021 | 2014–2015 annual/limited; 2016 narrative (Jul/Sep); 2017–2021 monthly May–Oct | 6 monthly samples/year for 2017–2021 | Monthly only; May–Oct; intake location; toxin only |
| WSA Primary Station | unknown for relevant bio | not verified | unverified | No phytoplankton/toxin params visible |

## 12. Candidate biological event reconstruction

**No independently reconstructed biological bloom events are approved.** Candidate observations below are **not labels**, **not continuous confirmed periods**, and **not for model training**.

### Painter 2018 (candidate, interval-censored)
- **Evidence:** 25 microscopy dates with biomass by taxa. High cyanophyte biomass observed on multiple sampled dates (e.g., DOY 171/06-19 2718 mg/m3 cyano; DOY 190/07-09 8020; DOY 197/07-16 10899; DOY 240/08-28 5279; DOY 248/09-05 10744 per prior verified extraction; 09-17 4349).
- **Candidate interval:** Cyanobacteria-dominant observations between 2018-06-13 and 2018-09-17, but only at sampled dates. Gaps 1–12 days; no onset before 06-13; right-censored after 09-17.
- **Status:** **Candidate only**; cannot be converted to continuous event without pre-approved criteria and uncertainty bounds.

### Painter 2019 (candidate, interval-censored)
- **Evidence:** 17 dates; high cyanophyte biomass on 07-10 (11919.8), 07-29 (6755.2), 08-07 (15957.1), 09-13 (10499.3), 09-17 (7006.2), 09-26 (13460.7), 10-03 (19260.3); 07-17 anomaly (41.02).
- **Candidate interval:** Discrete cyanobacteria-dominant samples across summer/autumn; 2019-07-17 anomaly breaks continuity.
- **Status:** **Candidate only**; unresolved anomaly; 4–16 day gaps.

### Boyer 2017 (publication-level only)
- **Evidence:** Reported 15 samples and published phases; raw data inaccessible.
- **Status:** **Not reconstructable from accessible raw evidence.** Published phases not independent ground truth.

### BPWTP microcystin (toxin evidence, candidate support only)
- **Evidence:** Monthly raw-water microcystin values (2017–2021). Notable raw values: 2016 peak 7 µg/L (narrative); 2017 Sep 11 0.7 µg/L; 2018 Jun 18 0.4 µg/L; 2019 Aug 12 4.5 µg/L; 2020 Jun 15 1.1 µg/L; 2021 Aug 9 0.4 µg/L.
- **Status:** **Candidate toxin-context evidence only**. Cannot define bloom onset/termination/taxonomy; monthly sparse; no non-detects-as-non-bloom rule approved.

## 13. Explicit event-boundary uncertainty

- All Painter events are interval-censored between discrete samples; gaps up to 16 days.
- 2019-07-17 anomaly creates an unresolved discontinuity.
- Boyer 2017 pre-bloom starts DOY 187 before first biological sample DOY 190; phase boundaries buoy-informed.
- BPWTP microcystin is monthly; cannot bound onset/termination within month-scale gaps; <0.1 µg/L does not equal confirmed non-bloom.
- No candidate event has defensible onset, termination, or duration.

## 14. Non-bloom exposure assessment

**Cannot be established.** No pre-approved biological non-bloom definition exists. Unsampled intervals, missing years, low-toxin monthly samples, and sensor-only periods cannot be treated as confirmed non-bloom exposure. Therefore no defensible FAR denominator exists.

## 15. Matched-FAR feasibility assessment

**Not defensible.** Required elements missing: independently reconstructed events (0 confirmed), confirmed non-bloom exposure (none), approved event/exposure definitions, defensible operating-point/FAR protocol, and sufficient temporal precision for lead-time claims. BPWTP monthly microcystin data does not provide the required event/non-event resolution.

## 16. Contradictory evidence and unresolved anomalies

- **2019-07-17 Painter anomaly:** remains unresolved; contradicts simple continuous-bloom interpretation.
- **Boyer 2017 pre-bloom boundary:** starts 3 days before first biological sample; mixed independence.
- **BPWTP 2019 Aug 12 raw microcystin 4.5 µg/L** indicates strong toxin signal, but monthly sampling prevents onset/termination reconstruction.
- **2014–2015 BPWTP reports:** microcystin appears as annual organics screening rather than monthly May–Oct table - weaker temporal evidence.

## 17. Failed and inaccessible sources

| Source | Failure/limit | Impact |
|---|---|---|
| Boyer 2025 SI Appendix S1 | Previously failed download; not retried | No accessible raw 2017 sample table |
| Boyer 2025 underlying raw data | Request-only; no public repo found | No reconstructable 2017 raw dataset |
| Wiley direct webfetch/pdfdirect | 403 | Used existing browser-access record; no new download |
| BPWTP PDF extraction completeness | pypdf text extraction imperfect; no OCR for scanned/vector issues | Possible missed tables; microcystin sections extracted |
| WSA 2012-current biological records | Not verified in portal; no phytoplankton/toxin params visible in Primary Station | No verified 2014–2021 biological records |
| Open Canada/CanWIN/FRDR targeted searches | No useful dataset found | No additional public dataset identified |

## 18. Outstanding human-authorisation requirements

1. **Boyer 2025 corresponding-author data request** (human-authorized): request SI Appendix S1 and record-level 2017 biological data.
2. **BPWTP/WSA records request** (human-authorized): request phytoplankton/cyanobacteria/taxonomy/biovolume/cell counts, cyanotoxins, lab chl-a, sample dates/locations/depths/methods/units/QA for 2014–2021.
3. **Any formal portal/data-use agreements** requiring acceptance on behalf of user - do not accept without authorization.

## 19. Comparison with previous Gate 2 findings

| Item | Gate 2C status | Gate 2D status | Material change? |
|---|---|---|---|
| Painter 2022 accessibility | Public, not in repo | Downloaded into evidence dir with checksums; schemas/anomaly re-verified | **Yes, minor** (provenance/accessibility strengthened) |
| BPWTP microcystin records | Reports public, content unverified | 2014–2021 PDFs downloaded; 2017–2021 monthly microcystin tables extracted; 2016 narrative extracted | **Yes, moderate** (new independent toxin evidence) |
| Boyer 2021 thesis | Metadata noted earlier | Public thesis accessed and text-searched for 2017 Buffalo Pound context | Minor corroboration |
| WSA portal | Access route identified | Primary Station inspected; no phytoplankton/toxin params visible | Clarified limitation |
| Independently reconstructed events | 0 | 0 confirmed (candidates only) | **No** |
| Non-bloom exposure | Not establishable | Not establishable | **No** |
| Matched-FAR feasibility | Not defensible | Not defensible | **No** |
| Overall classification | C — Exploratory only | C — Exploratory only | **No material change to confirmatory feasibility** |

## 20. Final A–D feasibility classification

**C — Exploratory only.**

Promising independent toxin evidence (BPWTP microcystin 2016–2021) and verified public Painter 2022 biological data improve descriptive/exploratory context. However, they do not provide independently reconstructed bloom events, defensible non-bloom exposure, or the temporal/biological resolution needed for the original confirmatory matched-FAR comparison.

## 21. Exact remaining requirements for Gate 2 approval

- Accessible record-level independent biological data (phytoplankton/cyanobacteria counts/biovolume/taxonomy and/or validated toxin records with methods/QA) covering relevant seasons.
- Pre-approved biological-only event definition and interval-censoring rules.
- Independent event reconstruction with audited provenance.
- Defensible non-bloom exposure/unknown handling.
- Sufficient temporal resolution for lead-time claims.
- Pre-approved matched-FAR evaluation design with defensible exposure denominator.
- Human Gate 2/3 review and approval.

## 22. Recommended next actions

1. **Human decision:** authorize/decline Boyer 2025 data request and BPWTP/WSA record-level data requests.
2. **If authorized:** obtain record-level data, verify provenance/independence/units/sample IDs, then draft Gate 2/3 criteria for human approval.
3. **If not authorized/available:** maintain exploratory-only scope; do not proceed to Gate 4 or confirmatory claims.
4. **Preserve all evidence:** keep `research/evidence/gate2d/` and register/report updates under version control when user authorizes commits.