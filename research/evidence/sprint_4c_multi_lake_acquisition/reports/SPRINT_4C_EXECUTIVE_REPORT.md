# Sprint 4C Executive Report — Multi-Lake Dataset Acquisition

**Project:** EcoSentinel  
**Date:** 2026-11-22  
**Phase:** Sprint 4C — Acquisition, Provenance, and File Verification  
**Gate 2 status:** **PAUSED / NOT APPROVED — Option C (Exploratory Only)** (unchanged)

## 1. Objective and boundaries

Sprint 4C attempted acquisition/preservation of outstanding public datasets for Greifensee 2018-2023, Lake Mendota, and Buffalo Pound reconciliation. No biological labels, modelling, confirmatory analysis, protocol/gate changes, external contacts, uploads, commits, or pushes were performed. No authentication/CAPTCHA/access controls were bypassed.

## 2. What was successfully downloaded/reused

| Candidate | Package | Status | Evidence |
|---|---|---|---|
| A | Greifensee 2014-2015 Dryad r4454 | **Reused existing, verified** | Zip in sprint4b evidence; SHA256 `9b66b59eccde06fef560d24ffd02321ffb892dc411d9091ec2d375260908888b`; 4 files extracted/inspected previously. Not duplicated. |
| D | Painter biological MP6NXF (partial) | **Reconciled/copied existing 7 files** | 7 files copied into `research/evidence/sprint_4c_multi_lake_acquisition/downloads/buffalo_pound/painter_biological/`; SHA256 verified against Sprint 4 manifest. No sprint4b overwrite. |

## 3. What was not downloaded (blocked)

| Candidate | Package | Blocker type | Detail |
|---|---|---|---|
| B | ERIC 000C2G biological | Access/bot protection | opendata.eawag.ch Anubis v1.28.2 challenge page; no file links extractable. |
| B | ERIC 000C8P environmental | Access/bot protection | Same Anubis challenge. |
| C | NTL 88.31 phytoplankton | Access/PASTA 401 | PASTA metadata endpoint returned 401 in environment; portal generic shell. |
| C | Mendota HF temp 10.6073/PASTA/8CEFF2... | Access/EDI blocker | Not downloaded after PASTA/EDI blocker. |
| C | Mendota Microbial Observatory 10.6073/PASTA/7E533C... | Access/EDI blocker | Not downloaded after PASTA/EDI blocker. |
| D | BP buoy FRDR 10.20383/103.01100 | Globus-gated | FRDR landing page reachable; file transfer requires Globus. |

## 4. Checksum/provenance status

- **A Dryad:** zip SHA256 verified (existing).
- **D Painter 7 files:** SHA256 verified; match Sprint 4 manifest.
- **B/C/D buoy:** no files downloaded, so no file checksums.
- **Painter discrepancy:** local sprint4_global_bio dir name uses `MPNXF`; intended DOI `MP6NXF`. Documented; no rename/overwrite.

## 5. Licence issues / human review

- **Painter MP6NXF:** CC BY-NC-SA 4.0 — human review for intended use compatibility.
- **ERIC 000C8P:** CC0 per DataCite — likely clear, confirm on package.
- **ERIC 000C2G:** licence not separately verified — human review required.
- **NTL/Mendota EDI packages:** licence unverified — human review required.
- **FRDR buoy:** licence not re-verified this sprint — human review required.

## 6. Required distinction (deliverable status)

| Package | Repo verified | File downloaded | Integrity verified | Biological measurement verified | Environmental measurement verified | Temporal/spatial pairing verified | Licence reviewed | Human action required |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A Dryad r4454 | Yes | Existing | Yes | Group-level only | Partial | Partial | Yes (CC0) | No |
| B ERIC 000C2G | Yes | No | No | No | N/A | No | Partial | Yes |
| B ERIC 000C8P | Yes | No | No | N/A | No | No | Partial | Yes |
| C NTL 88.31 | Partial | No | No | No | N/A | No | No | Yes |
| C Mendota HF temp | No | No | No | N/A | No | No | No | Yes |
| C Microbial Obs | No | No | No | N/A | No | No | No | Yes |
| D Painter MP6NXF | Yes | Partial (7/56) | Yes (7) | Partial | N/A | Partial | Yes | Yes |
| D BP buoy FRDR | Yes (landing) | No | No | N/A | No | No | Not re-verified | Yes |

## 7. Exact deliverable paths

- `research/evidence/sprint_4c_multi_lake_acquisition/reports/SPRINT_4C_EXECUTIVE_REPORT.md`
- `research/evidence/sprint_4c_multi_lake_acquisition/manifests/MASTER_FILE_MANIFEST.csv`
- `research/evidence/sprint_4c_multi_lake_acquisition/reports/DATASET_PACKAGE_REGISTER.csv`
- `research/evidence/sprint_4c_multi_lake_acquisition/logs/DOWNLOAD_AND_ACCESS_LOG.csv`
- `research/evidence/sprint_4c_multi_lake_acquisition/reports/LICENCE_AND_REUSE_REGISTER.csv`
- `research/evidence/sprint_4c_multi_lake_acquisition/reports/FILE_STRUCTURE_AND_METADATA_AUDIT.md`
- `research/evidence/sprint_4c_multi_lake_acquisition/reports/CANDIDATE_ACQUISITION_STATUS_MATRIX.csv`
- `research/evidence/sprint_4c_multi_lake_acquisition/reports/UNRESOLVED_ACCESS_AND_PROVENANCE_ISSUES.md`

## 8. Recommended next acquisition steps

1. **Human/manual download B ERIC packages** from official Eawag ERIC pages (browser session), preserving filenames/hashes; place under `downloads/greifensee_2018_2023/`.
2. **Human/manual download C EDI packages** from official EDI portal pages (NTL 88.31, HF temp, Microbial Observatory); verify package versions/entity IDs; place under `downloads/mendota/`.
3. **Human/manual Globus/FRDR download D buoy** (8 annual CSVs + metadata) into `downloads/buffalo_pound/buoy_environmental/`.
4. **Decide whether to fetch remaining 49 Painter files** from Borealis; if yes, download via official Borealis ZIP/API and verify checksums.
5. After files are present, run a file-level audit pass (headers, rows, timestamps, units, missingness, checksums) before any scientific feasibility assessment.

**Gate 2 remains PAUSED / NOT APPROVED — Option C (Exploratory Only).**
