# Acquisition Methods and Results (Sprint 4D)

**Date:** 2026-11-22  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## B. Greifensee 2018-2023

### B1. ERIC 000C8P environmental (DOI 10.25678/000C8P)
- **Official route that succeeded:** Eawag ERIC CKAN API `package_show` returned direct resource download URLs on `opendata.eawag.ch/dataset/.../resource/.../download/...`. These direct URLs returned HTTP 200 with expected sizes, bypassing the Anubis HTML landing-page challenge encountered in Sprint 4C.
- **Files acquired (6/6):** `readme.txt` (2913 B), `metadata.xlsx` (13065 B), `license.txt` (18828 B), `ctd_2018-2023.csv` (118766931 B), `nutrients_2019-2023.csv` (45838 B), `meteo_2018-2023.csv` (107685200 B). All size-matched CKAN; SHA256 recorded.
- **Verification:** CSV headers/rows inspected. CTD: 1,638,229 rows x 12 cols, 2018-04-19 00:07:04 to 2023-06-30 21:15:07. Meteo: 1,403,802 rows x 14 cols, 2018-04-18 20:00:03 to 2023-06-30 21:50:00. Nutrients: 474 rows x 10 cols, 2019-04-02 to 2023-06-29.
- **Licence discrepancy:** CKAN package license `cc-by` / CC-BY 4.0; earlier DataCite lookup in Sprint 4B indicated CC0 for 000C8P. Flagged for human review; do not assume CC0.

### B2. ERIC 000C2G biological landing (DOI 10.25678/000C2G)
- **Official route:** CKAN `package_show` succeeded. Landing package contains README, LICENSE, and 60 monthly sub-DOIs. Monthly packages enumerated via CKAN `package_search?q=doi:...`.
- **Acquired:** landing README/LICENSE. Monthly READMEs/LICENSEs/notes and 5p0x `class_and_feat_5p0xMAG_*.tar.gz` files where size <=150MB downloaded via direct CKAN resource URLs (see `manifests/c2g_download_manifest.csv` when finalized).
- **Not downloaded:** 5p0x class_and_feat files >150MB (recorded with URLs/sizes; 9.30 GB total for 59 5p0x files). 0p5x feature/class, raw_data, and image tarballs not downloaded (deprioritized; raw TIFF/images excluded per brief).
- **May 2022 anomaly:** C2G listing DOI `10.25678/x00B8V` resolved to `https://opendata.eawag.ch/dataset/aquascope_may_2022` (DOI 10.25678/X00B8V). Package enumerated and included.

### B3. Dryad companion 10.5061/dryad.0zpc86775
- **Investigated:** DataCite/Dryad API metadata retrieved. Title "Biodiversity forecasting in natural plankton communities..." v9, 2025-06-11, 1.44GB. **Not equivalent** to ERIC 000C2G Aquascope monthly image/classification package.
- **Result:** File listing endpoint 404, download 401. Not acquired. Recorded as related/provenance note only.

## C. Lake Mendota

| Target | Methods tried | Result |
|---|---|---|
| knb-lter-ntl.88.31 phytoplankton | PASTA readDataPackage/listDataEntities/readMetadata/readDataPackageDoi; DataONE solr; portal dataviewer/metadataviewer | 403/404/login redirect; no files acquired |
| HF temp 10.6073/PASTA/8CEFF296... | Not attempted after EDI barrier confirmed | Not acquired |
| Microbial Observatory 10.6073/PASTA/7E533C... | Not attempted after EDI barrier confirmed | Not acquired |

**Conclusion:** Official automated routes exhausted in this environment. Genuine human-only/authorized access barrier likely.

## D. Buffalo Pound

### D1. Buoy FRDR 10.20383/103.01100
- **Result:** All 8 annual cleaned CSVs (2014-2021) plus CITATION/LICENSE/README/data_flags already present locally at `data/raw/buffalo_pound/FRDR_dataset_1095_download_621_202611201621/`. Copied to sprint4d and SHA256-verified. No Globus transfer attempted.

### D2. Painter Borealis 10.5683/SP3/MP6NXF
- **Result:** Borealis API inventoried 56 files. Downloaded 35 scientifically relevant non-image files (all `data/*`, `docs/*`, README/readme.txt, md files, Rproj). Skipped output figures/tiffs/jpeg and R figure scripts as non-priority for biological observation acquisition. SHA256 recorded; Borealis MD5 available in manifest.
- **Existing 7 files in sprint4c:** preserved; not overwritten.
