# External Search Log

**Sprint:** 4L.9  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. Source categories defined before searching

1. Project governance and prior sprint evidence (4L.5, 4L.6, 4L.7, 4L.8, 4L.8A).
2. Primary dataset metadata: 129.42 EML, entity inventory, DataONE sysmeta, sensor inventory.
3. NTL-LTER deployment and sampling documentation (high-frequency page, protocols, site coordinates).
4. Manufacturer documentation for the YSI EXO2 and Turner Cyclops-7F.
5. Authoritative methodological guidance on algal fluorometry, calibration, biofouling, reporting units and QA (USGS).
6. Peer-reviewed literature on phycocyanin/chlorophyll fluorescence as a proxy and its limitations.
7. Access/integrity records for the acquired entity.

## 2. Searches and sources inspected

| # | Query / route | Sources inspected | What it establishes | Status |
|---:|---|---|---|---|
| 1 | Local governance and prior evidence | `AGENTS.md`; 4L.5, 4L.6, 4L.7, 4L.8, 4L.8A reports | Project rules; prior biology audit; acquisition/auth history; metadata-level sensor audit | Full |
| 2 | 129.42 EML | `metadata_129.42.xml` (146,471 B) | 38-field daily schema; flags; depths; 2017–2024 event notes; Turner/YSI statement; entity size/MD5; temporal coverage 2006-06-26 to 2025-12-31 | Full |
| 3 | Entity inventory | `entity_inventory_129.42.csv` | Daily/hourly/high-resolution/sensor-list entity IDs and sizes | Full |
| 4 | Sensor inventory | `List_of_sensors_used_on_the_Lake_Mendota_buoy_since_2006...dat` | 20 sensor records; years only; DO/CO2/PAR inventory mismatches | Full |
| 5 | DataONE CN sysmeta | `cn.dataone.org/cn/v2/meta/...cba9ed...` | Daily size 490,187 B; SHA-1 `bb1d...`; LTER replica only | Full |
| 6 | Acquired daily file | Local `.dat` | 490,187 B; 3,996 rows; 38 columns; hashes; date range | Full |
| 7 | NTL high-frequency data page | https://lter.limnology.wisc.edu/high-frequency-data/ | Mendota buoy 129/130 links; deployment typically Apr–Nov; live viewer | Full |
| 8 | NTL research protocols | https://lter.limnology.wisc.edu/protocols/ | Bi-weekly summer / monthly non-summer sampling; integrated southern-lake chlorophyll; phytoplankton biovolume ME/MO; Mendota site coordinate | Full |
| 9 | YSI EXO2 product page/specifications | https://www.ysi.com/exo2 | 7 ports; central antifouling wiper; Total Algae Chl/PC RFU ranges 0–100; sensor specs; calibration/wiper context | Full page/spec table |
| 10 | Turner Cyclops-7F product page | https://www.turnerdesigns.com/cyclops-7f-submersible-fluorometer | Discontinued 2025; dye-standard calibration; RFU output; technical documentation links | Full page |
| 11 | USGS TM1-D10 | https://pubs.usgs.gov/publication/tm1D10/full | Fluorescence is a proxy, not direct abundance; RFU is sensor-specific; diurnal quenching; biofouling; calibration/QA; different sensors not equivalent | Full HTML; relevant sections inspected |
| 12 | Manufacturer manual PDFs | YSI EXO manual; Turner Cyclops manual URLs | Manuals identified; PDF text could not be extracted by the fetch tool (`application/pdf` unsupported) | Identified, not text-inspected |
| 13 | Peer-reviewed phycocyanin literature | Search results: Thomson-Laing et al. 2020 (PubMed); Ma et al. 2022 (MDPI); NIWA guidance | Phycocyanin fluorescence is used as a cyanobacteria proxy but requires site-specific validation; MDPI page returned 403; PubMed page returned only an HHS notice | Identified; not used as primary evidence |
| 14 | EDI portal / package page | EDI mapbrowse 129 | Package summary/login context; data access already resolved by acquisition | Identified |

## 3. Key source conclusions

- **EML:** the daily entity is 490,187 B, MD5 `eb7b3a...`; daily values are averages of 1-minute observations; Turner and YSI chlorophyll/phycocyanin output RFU with “significant magnitude differences”; pH/DO/specific conductance were cleaned/recalibrated every two weeks in 2019, nearly weekly in 2020; multiple outage/fouling events are documented.
- **USGS TM1-D10:** algal fluorometers measure a fluorescence response, not algal abundance/biomass; RFU is sensor-specific; relations vary with species, physiology, temperature and light; nonphotochemical quenching can cause diurnal variability; biofouling and calibration drift require site-specific QA; different makes/models are not equivalent even in the same units.
- **YSI EXO2:** Total Algae chlorophyll and phycocyanin channels report 0–100 RFU (with µg/L ranges) and use a central wiper; performance specifications are controlled-condition values, not a guarantee in lake water.
- **Turner Cyclops-7F:** RFU output; calibration with dye standards; discontinued in 2025; technical documentation exists but the manual PDF was not text-extracted.
- **NTL protocols/page:** open-water deployment, bi-weekly summer/monthly non-summer sampling, integrated southern-lake chlorophyll, phytoplankton biovolume for Mendota/Monona.

## 4. Inaccessible / not used

- Manufacturer PDF manuals: fetch tool rejected `application/pdf`; product pages/spec tables were used instead. Do not claim full manual inspection.
- MDPI article: HTTP 403.
- PubMed page: returned an HHS vulnerability notice rather than the abstract; not used.
- Ancillary NTL dataset 130 (water temperature): deliberately **not acquired**; outside this sprint's single-entity scope.
- Hourly and 1-minute 129.42 entities: deliberately not acquired.
- EDI package data behind login: not re-requested; acquisition already complete.

## 5. Why searching stopped

The primary metadata, sensor inventory, full daily file, NTL deployment/sampling documentation, manufacturer specifications and authoritative USGS fluorometry guidance were inspected. Remaining uncertainty is about per-record calibration, maintenance and sensor identity, which are **not available** in the public metadata and cannot be resolved by more web searching. No external contact was made. No source supports a bloom/non-bloom label, event interval or confirmatory claim.
