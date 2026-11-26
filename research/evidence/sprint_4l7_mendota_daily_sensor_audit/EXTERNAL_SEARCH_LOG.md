# External Search Log — Sprint 4L.7

**Date:** 2026-11-24T08:45:50.090661+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Source categories defined before searching

1. EDI package metadata, revisions, entity inventory and DataONE sysmeta.
2. NTL-LTER high-frequency/buoy documentation and sensor inventory.
3. Official manufacturer documentation for YSI EXO2, Turner Cyclops-7F and related sensors.
4. Scientific literature on buoy fluorometry, biofouling, calibration and sensor limitations.
5. Prior project evidence (4L.1, 4L.2, 4L.3, 4L.3C, 4L.5, 4L.6).
6. Authentication/access evidence from 4L.3C/4L.3D.

## Queries and sources

| # | Query/route | Sources inspected | Finding | Status |
|---:|---|---|---|---|
| 1 | EDI 129.42 EML/entity inventory | `metadata_129.42.xml` (146,471 B); `entity_inventory_129.42.csv` | 4 entities; daily 490,187 B; hourly 11,380,329; HR 682,487,953; sensor list 1,039 | Full metadata |
| 2 | DataONE CN sysmeta daily entity | `cn/v2/meta/...cba9ed...` | size 490,187; SHA-1 `bb1d...`; replica LTER only | Full sysmeta |
| 3 | DataONE CN object daily entity | `cn/v2/object/...cba9ed...` | 404 (no CN replica) | Tested |
| 4 | NTL high-frequency data page | https://lter.limnology.wisc.edu/high-frequency-data/ | Links 129/130; live viewer; buoy deployment | Full page |
| 5 | EDI package summary 129.42 | https://portal.edirepository.org/nis/mapbrowse?...129...42 | metadata summary; data login | Identified; login |
| 6 | YSI EXO2 product page | https://www.ysi.com/exo2 | 7 ports, central antifouling wiper; Total Algae Chl/PC ranges; SmartQC | Full page |
| 7 | Turner Cyclops-7F product page | https://www.turnerdesigns.com/cyclops-7f-submersible-fluorometer | discontinued 2025; calibration with dye standards; biofouling/operational limitations | Full page |
| 8 | "in situ fluorometer biofouling chlorophyll phycocyanin lake buoy validation limitations" | Open Research Europe; ASLO; Frontiers; NIWA guidance | fluorescence needs validation; biofouling/community composition affect readings | Excerpts |
| 9 | "Lake Mendota buoy sensor calibration biofouling..." | NTL page; SSEC buoy; PAR dataset | biofouling from algae/zebra mussels noted in related buoy data; sensor maintenance relevant | Excerpts |
| 10 | Existing project evidence | 4L.1 sensor inventory; 4L.5 raw biology; 4L.6 independent audit; 4L.3C access | sensor eras; biological constraints; access block | Full reports |

## Inaccessible/incomplete

- **Daily 129.42 entity:** not acquired; no key; CN object 404; LTER GMN path 403 documented in 4L.3C.
- **Hourly/HR entities:** deliberately not downloaded.
- **Manufacturer manuals:** product pages inspected; PDF manuals not parsed.
- **Calibration/maintenance logs:** not available in EML/sensor list.
- **AlgaeBase:** not relevant here; no new biological taxonomy work.
- **Full scientific PDFs:** some literature inspected as abstracts/excerpts; noted.

## Conflicting evidence

- Manufacturer specs indicate good performance/anti-fouling, while independent literature documents biofouling, community-composition and calibration limitations. Both are recorded; actual daily QC is needed.
- Package metadata says 2006–2025, but the sensor inventory shows era-specific channels and not all variables span the package. Package-level coverage is not variable-level coverage.

## Why searching stopped

The package/entity structure, sensor era documentation and manufacturer limitations are sufficiently established for a feasibility audit. The decisive missing item is the raw daily entity, not more literature. No exhaustive claim beyond the listed sources.
