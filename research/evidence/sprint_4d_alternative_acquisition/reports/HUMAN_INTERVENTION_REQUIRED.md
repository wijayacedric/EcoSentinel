# Human Intervention Required (Sprint 4D)

**Date:** 2026-11-22  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. Greifensee 2018-2023 biological (ERIC 000C2G / monthly packages)

**Status:** Partially acquired via official CKAN direct resource URLs.  
**Acquired automatically:** ERIC landing README/LICENSE; monthly package metadata enumerated; monthly READMEs/LICENSEs/notes and 5p0x class_and_feat tarballs downloaded where size <= 150MB (see C2G download manifest).  
**Remaining / human action:**
- **Large 5p0x class_and_feat files (>150MB):** Download manually from official ERIC package pages. Exact files and URLs are listed in `manifests/MASTER_FILE_MANIFEST.csv` / `reports/ACQUISITION_METHODS_AND_RESULTS.md` with status `skipped_size`. Each is a direct CKAN resource URL on opendata.eawag.ch.
- **0p5x class_and_feat, raw_data, images:** Not downloaded (large; raw TIFF/image archives explicitly deprioritized per brief). Record availability; download only if scientifically required.
- **May 2022 package:** DOI `10.25678/x00B8V` resolves to `https://opendata.eawag.ch/dataset/aquascope_may_2022` (note DOI casing/character in C2G listing). Verify and download needed files manually if not captured by automated run.

**How:** Browser download from each ERIC package page or direct `curl -L -O <resource-url>` from a network that can access opendata.eawag.ch. Preserve original filenames; record SHA256.

## 2. Lake Mendota (EDI/PASTA)

**Status:** Not acquired. Official automated routes exhausted in this environment.

| Package | DOI/ID | Official page | Required human action |
|---|---|---|---|
| Phytoplankton | `knb-lter-ntl.88.31` / `10.6073/pasta/bd03330e83fc52a5442bb39e131c95e9` | https://portal.edirepository.org/nis/mapbrowse?packageid=knb-lter-ntl.88.31 | Log in / access via browser or authorized network; download all data entities, metadata, licence. If PASTA 403 persists for public, confirm package access policy with EDI. |
| HF temperature | `10.6073/PASTA/8CEFF296AD68FA8DA6787076E0A5D992` | Resolve DOI on EDI portal | Download complete package/data entities + metadata/licence. |
| Microbial Observatory | `10.6073/PASTA/7E533C197ED8EBD27777A89A2C8D7DFE` | Resolve DOI on EDI portal | Download complete package/data entities + metadata/licence. |

**What was tried:** PASTA `readDataPackage`, `listDataEntities`, `readMetadata`, `readDataPackageDoi` returned 403 for public access; `/package/name/eml/knb-lter-ntl/88` returned 404; DataONE solr no match; portal dataviewer redirected to login. No bypass attempted.

## 3. Buffalo Pound buoy (FRDR 10.20383/103.01100)

**Status:** **Already available locally and reused/verified.** All 8 annual cleaned CSVs (2014-2021) plus CITATION.txt, LICENSE.txt, README.txt, data_flags.csv were found in `data/raw/buffalo_pound/FRDR_dataset_1095_download_621_202611201621/` and copied/hashed into sprint4d evidence.  
**Human action:** None required unless you need to re-verify against FRDR original via Globus or confirm additional files not present locally.

## 4. Buffalo Pound Painter (Borealis 10.5683/SP3/MP6NXF)

**Status:** Partially acquired. 35 scientifically relevant non-image files downloaded via Borealis API and hash-verified. Output figures/tiffs/jpegs and some code images not downloaded.  
**Human action:** Only if specific omitted files are needed; download via official Borealis page/API. Preserve existing sprint4b/sprint4c files.

## 5. Dryad 10.5061/dryad.0zpc86775 (Greifensee companion)

**Status:** Metadata investigated only. Dataset is "Biodiversity forecasting in natural plankton communities..." (Merz/Pomati 2025, v9, ~1.44GB) - **not equivalent** to ERIC 000C2G Aquascope images/classifications. Dryad file listing/download endpoints returned 404/401 in this environment.  
**Human action:** Only if scientifically needed; manual Dryad download with provenance/hash recording.
