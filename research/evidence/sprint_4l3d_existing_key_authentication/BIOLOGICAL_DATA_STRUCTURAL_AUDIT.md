# Biological Data Structural Audit

**Date:** 2026-11-24T07:10:03.729185+00:00  
**Status: METADATA-LEVEL ONLY — raw CSV not acquired.**

## Known schema (from EML)

15 columns: `lakeid, year4, sampledate, sta, depth_range, division, taxa_name, gald, cells_per_nu, nu_per_ml, cells_per_ml, biovolume_conc, biomass_conc, relative_total_biovolume, genus`.

## Known design

- Four Madison lakes; Mendota 0–8 m composite; others 0–2 m.
- 1995-01-24 to 2020-12-31; biweekly ice-free, 4-weekly late season, occasional winter.
- Utermöhl microscopy; PhycoTech; 3 slides/sample; species-level; geometric biovolume; biomass conversion.
- February 2013 taxonomic updates.
- No QC flag or detection-limit columns.

## Raw audit required (not yet performed)

- Encoding/CSV dialect; header exactness; row count; column count.
- Date parsing, range, per-year/month counts, gaps.
- Lake identifiers; Mendota-only rows/dates; station/depth values.
- Duplicate rows and duplicate `(lakeid, sampledate, sta, depth_range, taxa_name)` keys.
- Same-date/species variants/vegetative states.
- Missingness/zeros for all numeric fields.
- Taxonomic list by year; cyanobacteria; unidentified taxa; pre/post-2013 harmonisation.
- Cell density/biovolume/biomass consistency; outliers; negative/implausible values.
- Sampling cadence by lake; winter/under-ice representation.
- Metadata-vs-file discrepancies.

## Constraint

No labels, event intervals, modelling or hypothesis tests. Raw file acquisition is blocked pending user key input.
