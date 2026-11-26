# File Structure and Metadata Audit (Sprint 4C)

**Date:** 2026-11-22  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## A. Greifensee 2014-2015 (Dryad r4454) — reused existing

- **Local zip:** `research/evidence/sprint4b_candidate_audit/downloads/A_greifensee_dryad_r4454/doi_10_5061_dryad_r4454__v20190126.zip`
- **SHA256:** `9b66b59eccde06fef560d24ffd02321ffb892dc411d9091ec2d375260908888b`
- **Archive contents (4 files, 2,568,607 bytes uncompressed):**
  - `Dataset_ELE_Greifensee_2014plus2015_TS_cytobuoy_env_logabund.csv` — 2,468,336 bytes; 9366 rows x 44 cols; datetime range 2014-07-17 12:00 to 2015-11-28 04:00; depths 1.0-10.0m (7); mostly 4h intervals.
  - `README_for_Dataset_ELE_Greifensee_2014plus2015_TS_cytobuoy_env_logabund.csv` — 3,954 bytes.
  - `Dataset_ELE_Greifensee_long_term_TS_microscopy_env.csv` — 93,397 bytes; 388 rows x 36 cols; 1984-03-01 to 2016-06-01; monthly.
  - `README_for_Dataset_ELE_Greifensee_long_term_TS_microscopy_env.csv` — 2,920 bytes.
- **Timestamp/units:** datetime dd/mm/yyyy HH:MM; dens_* log(cells/mL); cyano_percent % by cell number; depths meters. Units documented in READMEs.
- **Missingness:** cytobuoy biological 7235 non-null/2131 null; inflow/nutrient/zooplankton high missingness. Long-term biological 346/42 null.
- **Transformations:** None performed by Sprint 4C.

## B. Greifensee 2018-2023 (ERIC 000C2G, 000C8P) — not downloaded

- **Status:** Blocked by Anubis bot protection on opendata.eawag.ch. No files downloaded; no headers/rows inspected.
- **Expected per brief:** 000C2G monthly phytoplankton feature/classification files + README/licence/docs; 000C8P 6 resources (README, CTD CSV, Metadata XLSX, Meteo CSV, Nutrients CSV, licence).
- **Audit:** Not possible.

## C. Lake Mendota (knb-lter-ntl.88.31, HF temp, Microbial Observatory) — not downloaded

- **Status:** PASTA/EDI access returned 401/404 in this environment; no package metadata or data entities retrieved.
- **Audit:** Not possible.

## D. Buffalo Pound Painter (MP6NXF) — partial existing reconciled

- **Local sprint4c copies:** `research/evidence/sprint_4c_multi_lake_acquisition/downloads/buffalo_pound/painter_biological/` (7 files copied from sprint4_global_bio; no overwrites).
- **Integrity:** SHA256 verified for 7 files; matches Sprint 4 manifest.
- **Files present:**
  - `data__clean_data__BP_PhytoTax_2018_KP.csv` — 133,635 bytes; 818 rows x 18 cols; 25 unique DOY.
  - `data__clean_data__BP_PhytoTax_2019_KP.csv` — 65,439 bytes; 17 unique DOY.
  - `data__clean_data__BP_2018_toxins_0.8m.csv` — 16,302 bytes; complex multi-row header; latin-1 encoding.
  - `data__clean_data__BP_2019_toxins_0.8.csv` — 15,845 bytes; complex header.
  - `data__clean_data__Nutrients_Biomass_BP_clean.csv` — 2,352 bytes; 44 rows.
  - `README.md`, `data__clean_data__clean_data.md`, `manifest.json`.
- **Missing from full package:** 49 of 56 Borealis files not present locally (code, figures, additional raw/processed files). Not downloaded in Sprint 4C.
- **Provenance discrepancy:** local dir name in sprint4_global_bio uses `MPNXF`; intended DOI is `MP6NXF`. Documented; no rename/overwrite.

## D. Buffalo Pound buoy (FRDR 10.20383/103.01100) — not downloaded

- **Status:** FRDR landing page reachable; file transfer is Globus-gated. Not accessible in this environment.
- **Expected per brief:** 8 annual high-frequency buoy CSVs (2014-2021) + metadata/QC flags.
- **Audit:** Not possible.
