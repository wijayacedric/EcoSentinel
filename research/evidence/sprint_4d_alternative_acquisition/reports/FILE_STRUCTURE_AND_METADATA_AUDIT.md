# File Structure and Metadata Audit (Sprint 4D)

**Date:** 2026-11-22  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## B1. ERIC 000C8P environmental — acquired

| File | Rows | Cols | Time range / key fields | Units/notes | Missing/flags |
|---|---:|---:|---|---|---|
| ctd_2018-2023.csv | 1,638,229 | 12 | 2018-04-19 00:07:04 to 2023-06-30 21:15:07; `timestamp` | Press, Temp, CondF, O2, O2ppm, pH, PAR, Turb, Chla, PhycoEr, PHY (see metadata.xlsx/readme) | Not fully profiled; metadata.xlsx present |
| meteo_2018-2023.csv | 1,403,802 | 14 | 2018-04-18 20:00:03 to 2023-06-30 21:50:00; `timestamp` | windspeed/dir, air temp/humidity/pressure, precipitation etc. | `NA` observed in first row |
| nutrients_2019-2023.csv | 474 | 10 | 2019-04-02 to 2023-06-29; `date`, `sample` | nitrate, nitrite, ammonium, oP, TP, TN, TOC, silica | `NA` observed |
| metadata.xlsx | - | - | 2+ sheets expected | Variable definitions/units | Not fully extracted here |
| readme.txt | - | - | - | Package documentation | - |
| license.txt | - | - | - | CC-BY 4.0 text | - |

**Not audited deeply:** full unit/QC semantic validation, depth/station mapping, alignment with biological 000C2G, Dec 2018–May 2019 gap assessment (needs targeted check).

## B2. ERIC 000C2G monthly biological — partial

- **Enumerated:** 60 monthly sub-DOIs from landing package (May 2018–Jun 2023); May 2022 resolved via `x00B8V` -> `aquascope_may_2022`.
- **Resource pattern observed:** `class_and_feat_5p0xMAG_*.tar.gz`, `class_and_feat_0p5xMAG_*.tar.gz`, `images_*`, `raw_data_*`, `README.txt`, `LICENSE/LICENSE.txt`, occasional missing-data notes.
- **Downloaded:** small/medium files per manifest (pending final background completion). Large 5p0x class_and_feat (>150MB) and raw/images not downloaded.
- **Biological verification:** Not completed. Tarballs not extracted/inspected for column definitions, taxon classes, ROI counts, units, or cyanobacteria class validation in this sprint.

## C. Mendota — not acquired

No files to audit.

## D1. BP buoy FRDR — reused existing

| File | Rows | Cols | Date range (first-last DateTime) | SHA256 |
|---|---:|---:|---|---|
| BPBuoyData_2014_Cleaned.csv | 8015 | 68 | 2014-06-11 22:15 to 2014-09-05 1:15 | ee6a008b839888e1d6e9544cd39ff5d3b91a290d7d3273740cdcf66fb81a6931 |
| BPBuoyData_2015_Cleaned.csv | 20438 | 68 | 2015-05-14 21:10 to 2015-10-06 11:50 | 2283d58439c296040c7da41336ff413cdbc561cc1fe2d07efb85e13651cf534d |
| BPBuoyData_2016_Cleaned.csv | 18975 | 68 | 2016-05-18 16:50 to 2016-09-28 15:50 | b044f812debc84e8d4df0ecb44ea1772c5499f1c0a4e049d559de4e3531ceb9e |
| BPBuoyData_2017_Cleaned.csv | 22023 | 68 | 2017-05-09 17:20 to 2017-10-11 12:40 | 05d7e3beb988675a5f4e94f3315493ca555d983ee0792883f919d6cec809d1cd |
| BPBuoyData_2018_Cleaned.csv | 20162 | 68 | 2018-05-15 16:00 to 2018-10-04 11:30 | 3fd8c6ce2694adf0734e4c950f6ea11dbd8897c2663773d5d1eec438a30ac797 |
| BPBuoyData_2019_Cleaned.csv | 18026 | 68 | 2019-05-29 17:00 to 2019-10-03 13:20 | b5cc48dba1a645b7b4eee19ea7c24289dacb43b76e2fca7d1d06c1f758a2571b |
| BPBuoyData_2020_Cleaned.csv | 16836 | 68 | 2020-06-05 16:30 to 2020-10-01 13:20 | 7396d2689930c88dc95c2ea455d0e67eda78030d73aa0b729a9463b314b1c502 |
| BPBuoyData_2021_Cleaned.csv | 18285 | 68 | 2021-05-31 20:20 to 2021-10-07 14:30 | fcf8e57d1f2260e6312a5e177dcdac382e3a2893e49b19af51e7f13d76a942d3 |

Also copied: CITATION.txt, LICENSE.txt, README.txt, data_flags.csv. Full QC-flag semantic audit not completed.

## D2. Painter Borealis — partial

35 relevant non-image files downloaded via Borealis API; SHA256 recorded. Includes raw_data (YSI 2018/2019), clean_data (phyto/toxins/nutrients), processed_data (heterocytes, groups biomass, major cyanos, phyto matrices, toxin LOD/LOQ variants), docs/readmes/md. Figures/tiffs/jpeg and most R scripts omitted by prioritization.
