# Sprint 4E.1D Executive Report — Mendota Data-Byte Access & File-Level Scientific Audit

**Date:** 2026-11-23T07:09:51.635546+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Verdict: **CONDITIONAL** (file-level feasibility not established)

## Key finding

**Data-byte access is blocked in this environment.** For tested data objects across 88.31/130.29/415.2: CN object/resolve returned 404 or 403 (gmn.lternet.edu), and direct PASTA `readDataEntity` returned **403 Public Access not authorized**. Metadata/ORE were publicly readable from CN, but **sysmeta availability did not imply public data-byte readability**.

## What was verified

- CN metadata/ORE readability for all three packages.
- 130.29 2015 HR entity missing on CN (bounded gap).
- EML-level biological fields in 88.31 suggest potential value (taxa/genus/division/cells_per_ml/biovolume_conc/biomass_conc).
- EML-level environmental fields: 130.29 temp only; 415.2 temp/DO/pH/conductivity.

## What remains unverified (blocked)

- Actual file contents, units, detection limits, QC flags, missingness, cadence.
- Mendota-only subset isolation.
- Temporal-spatial alignment and predictor sufficiency at file level.
- Any Gate 2 event/non-bloom exposure feasibility.

## Final verdict

**CONDITIONAL** — metadata suggests possible relevance, but file-level feasibility cannot be established without authorised data access. This is not a PASS. It is not a scientific FAIL based on inspected data because data were inaccessible; it is an access-blocked conditional.

A PASS would only permit formal Gate 2 readiness review; it would not authorize Gate 2 or confirmatory analysis.
