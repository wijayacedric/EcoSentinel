# Sprint 4D Executive Report — Alternative Official Data Acquisition

**Project:** EcoSentinel  
**Date:** 2026-11-22  
**Phase:** Sprint 4D — Alternative Official Acquisition, Provenance, and Technical Verification  
**Gate 2 status:** **PAUSED / NOT APPROVED — Option C (Exploratory Only)** (unchanged)

## 1. Objective and boundaries

Sprint 4D pursued alternative official automated acquisition routes for outstanding Sprint 4C targets. No biological labels, modelling, confirmatory analysis, protocol/gate changes, external contacts, uploads, commits, or pushes were performed. No Anubis/CAPTCHA/auth/access controls were bypassed.

## 2. Outcomes by target

| Target | Status | What was acquired/reused | What remains |
|---|---|---|---|
| **B. ERIC 000C8P environmental** | **Successfully acquired and verified** | 6/6 files via CKAN direct resource URLs; size+SHA256 verified; CSV headers/rows/timestamps audited | Licence discrepancy (CKAN CC-BY vs prior DataCite CC0 note) needs human clarification; deep QC/unit semantic audit pending |
| **B. ERIC 000C2G biological monthly** | **Partially acquired** | Landing README/LICENSE; 60 monthly sub-packages enumerated; 40 5p0x class_and_feat tarballs downloaded (<=150MB), 20 skipped (>150MB); READMEs/LICENSEs/notes downloaded | 20 large 5p0x class_and_feat files (>150MB); 0p5x/raw/images not downloaded; tarball contents not inspected for class/taxon/ROI validation |
| **B. Dryad 10.5061/dryad.0zpc86775** | **Not acquired (not equivalent)** | Metadata only | Different dataset; files 404/download 401; only acquire if scientifically needed |
| **C. NTL 88.31 phytoplankton** | **Official automated routes exhausted; human intervention required** | None | Manual/authorized EDI download |
| **C. Mendota HF temp 8CEFF296...** | **Human intervention required** | None | Manual/authorized EDI download |
| **C. Mendota Microbial Obs 7E533C...** | **Human intervention required** | None | Manual/authorized EDI download |
| **D. BP buoy FRDR 10.20383/103.01100** | **Existing files reused and verified** | 8 annual CSVs 2014–2021 + CITATION/LICENSE/README/data_flags copied from local FRDR download; SHA256 verified | Optional FRDR/Globus re-verification against remote manifest |
| **D. Painter Borealis MP6NXF** | **Partially acquired** | 35 relevant non-image files downloaded via Borealis API; SHA256 recorded; 7 pre-existing sprint4c files preserved | Remaining figures/tiffs/jpeg/code not downloaded; NC-SA review needed |

## 3. Key technical findings

- **ERIC CKAN direct resource URLs work** despite Anubis on HTML landing pages. This resolved Sprint 4C blocker for 000C8P completely.
- **C2G 5p0x class_and_feat total volume ~9.30 GB** (59 files). 40 files <=150MB acquired; 20 skipped with URLs recorded for manual download.
- **EDI/PASTA public access returned 403** for knb-lter-ntl.88.31 read endpoints in this environment; portal dataviewer redirected to login. Treated as access barrier, not proof of unavailability.
- **BP buoy files were already local** (8 annual CSVs 2014–2021, 68 cols). No re-download needed.
- **Painter Borealis API** allowed targeted file download. 35/56 files acquired by relevance; Borealis MD5 checksums available.

## 4. Integrity and provenance

- C8P: 6/6 size-matched CKAN; SHA256 recorded.
- C2G monthly: per-file SHA256 recorded in `manifests/c2g_download_manifest.csv`; 0 errors.
- BP buoy: 8/8 SHA256 recorded; copied from `data/raw/buffalo_pound/FRDR_dataset_1095_download_621_202611201621/`.
- Painter: 35 downloaded files SHA256 recorded; Borealis MD5 recorded.
- Dryad r4454: existing Sprint 4B zip referenced, not duplicated.

## 5. Licence/reuse flags (human review)

- **ERIC 000C8P:** CKAN CC-BY 4.0 vs earlier DataCite CC0 note — verify authoritative licence.
- **ERIC 000C2G/monthly:** CC-BY 4.0 indicated; confirm per package before reuse.
- **Mendota EDI:** unverified.
- **Painter MP6NXF:** CC BY-NC-SA 4.0 — NC-SA compatibility review required.
- **BP buoy FRDR:** LICENSE.txt copied; verify current FRDR terms.

## 6. Deliverables

- `research/evidence/sprint_4d_alternative_acquisition/reports/SPRINT_4D_EXECUTIVE_REPORT.md`
- `research/evidence/sprint_4d_alternative_acquisition/reports/ACQUISITION_METHODS_AND_RESULTS.md`
- `research/evidence/sprint_4d_alternative_acquisition/manifests/MASTER_FILE_MANIFEST.csv`
- `research/evidence/sprint_4d_alternative_acquisition/logs/DOWNLOAD_AND_ACCESS_LOG.csv`
- `research/evidence/sprint_4d_alternative_acquisition/reports/PACKAGE_PROVENANCE_REGISTER.csv`
- `research/evidence/sprint_4d_alternative_acquisition/reports/LICENCE_AND_REUSE_REGISTER.csv`
- `research/evidence/sprint_4d_alternative_acquisition/reports/FILE_STRUCTURE_AND_METADATA_AUDIT.md`
- `research/evidence/sprint_4d_alternative_acquisition/reports/HUMAN_INTERVENTION_REQUIRED.md`
- `research/evidence/sprint_4d_alternative_acquisition/reports/UPDATED_CANDIDATE_ACQUISITION_STATUS_MATRIX.csv`
- `research/evidence/sprint_4d_alternative_acquisition/manifests/c2g_download_manifest.csv`

## 7. Recommended next acquisition steps (no primary-lake recommendation)

1. Human/manual download of 20 large C2G 5p0x class_and_feat files (>150MB) from official ERIC resource URLs listed in `c2g_download_manifest.csv`.
2. Human/authorized EDI download for NTL 88.31, Mendota HF temp, and Microbial Observatory; record entity IDs, checksums, licences.
3. Clarify 000C8P licence (CC-BY vs CC0 discrepancy) from authoritative ERIC record before reuse.
4. After acquisition, run file-level biological/environmental audit: taxon classes, cyanobacteria class validity, ROI units, depth/station/time alignment, QC/missingness, Dec 2018–May 2019 gap impact.

**Gate 2 remains PAUSED / NOT APPROVED — Option C (Exploratory Only).** No multi-lake research strategy change made.
