# Sprint 4L.3 Handover

**Date:** 2026-11-23T23:58:36.852965+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Status: PARTIALLY COMPLETE.**

## Completed

- Created project-level `AGENTS.md` with permanent research/execution standards.
- Verified target package/entity/size/MD5 and output location.
- Discovered and retrieved metadata for newer revision **88.32**; confirmed the data entity is identical by objectName/size/MD5.
- Documented acquisition failure: no `EDI_API_KEY`; no network request/data bytes.
- Produced metadata-level schema, coverage, methods, quality/QC assessment, search log, literature review, feasibility analysis and deliverables.
- Inspected primary EDI/DataONE metadata, NTL protocols, NSF PAR, Carey 2016, Carpenter 2020, Beal 2022, O'Brien 2023, taxonomic-consistency and temporal-resolution literature, and PhycoTech materials.

## Not completed (blocked)

- Raw CSV acquisition (`f2de15b2...`).
- Actual size/SHA256/MD5 verification of the CSV.
- Mendota-specific row counts, dates, gaps, missingness, duplicates, taxa counts, units/outliers.
- Empirical confirmation of depth/station/taxonomy consistency.
- Any event/non-bloom labelling or confirmatory evaluation (prohibited).

## First action for continuation

With a user-authorised EDI key present only as `EDI_API_KEY`:

```bash
python3 research/evidence/sprint_4k_mendota_authorised_access/scripts/edi_mendota_acquire.py \
  --package 88.31 --include-data \
  --entity f2de15b2fff6ae962a04c150c0a1c510 \
  --max-bytes 3000000 \
  --outdir research/evidence/sprint_4l_mendota_biology_audit/acquisition
```

Then independently verify size 2,448,830 B and MD5 `a0363cc7fdfd6c12889750fea27bd542`, compute SHA256, and perform the raw audit in `BIOLOGICAL_DATA_QUALITY.md`/`SAMPLING_TIMELINE.md`.

## Key scientific conclusions

- Genuine independent microscopy endpoint (metadata).
- Biweekly–monthly sampling → seasonal/multi-week scale only.
- 0–8 m composite vs buoy 0.5 m point sensors → major depth mismatch.
- No QC flags/detection limits; 2013 taxonomic updates; single-analyst consistency self-reported.
- Prior Mendota HF/forecasting literature is substantial; no novelty claim.

## Files

`SPRINT_4L3_EXECUTIVE_REPORT.md`, `DATASET_SCHEMA.csv`, `MENDOTA_RECORD_COVERAGE.csv`, `SAMPLING_TIMELINE.md`, `BIOLOGICAL_VARIABLES_AND_METHODS.md`, `DATA_QUALITY_AND_MISSINGNESS.md`, `EXTERNAL_SEARCH_LOG.md`, `LITERATURE_AND_METADATA_REVIEW.md`, `FEASIBILITY_AND_GATE2_IMPLICATIONS.md`, `SPRINT_4L3_HANDOVER.md`.
