# Unresolved Evidence and Recommendations — Lake Mendota (Sprint 4E.1)

**Date:** 2026-11-22  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Key blockers

1. **EDI/PASTA access blocked in this environment.** PASTA `readDataPackage`/`listDataEntities`/`searchDataPackages` returned 403 "Public Access not authorized" for knb-lter-ntl.88.31 and related endpoints. DOI/mapbrowse resolved to EDI login HTML. No bypass attempted.
2. **No file-level verification possible.** Cannot confirm taxa, cyanobacteria fields, biovolume/cell density, sampling design, depths, timestamps, QC, or licence at package level.
3. **No alignment audit possible.** Biological-environmental pairing remains unverified.

## Evidence still missing

- 88.31 data entities, schema, units, methods, QC, licence.
- Cyanobacteria-specific taxonomic resolution and biovolume/cell density availability.
- Sampling frequency, seasonality, station/depth metadata.
- HF buoy and Microbial Observatory file-level metadata and overlap with biological sampling.
- Defensible non-bloom exposure and event-evaluation feasibility evidence.

## Recommendations (non-decisional)

- **Human/manual access:** Download knb-lter-ntl.88.31 and the two environmental packages via authorized EDI portal/browser session. Preserve originals, record SHA256, package version, entity IDs, and licence text.
- **After acquisition:** Run file-level audit (schema, units, missingness, cyanobacteria fields, depth/station/time overlap) before any feasibility conclusion.
- **Do not proceed to Gate 2 review** based on current evidence. Mendota remains **unverified**, not supported or rejected.
- **No change to research question, protocol, or Gate 2 status.**
