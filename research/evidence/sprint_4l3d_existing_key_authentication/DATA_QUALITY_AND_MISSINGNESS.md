# Data Quality and Missingness

**Date:** 2026-11-24T07:10:03.729185+00:00  
**Status: NOT PERFORMED — raw CSV not acquired.**

## Metadata-level findings

- No QC-flag columns and no detection limits in the schema.
- Multiple same-species/date rows may be variants or vegetative states (EML).
- Species may not have been determined for all slides (EML).
- February 2013 taxonomy updates affect names and genus/species resolution.
- Sampling is biweekly ice-free, 4-weekly late season, usually one winter sample.
- Mendota samples are 0–8 m composites; point-sensor comparison needs an explicit depth comparator.

## Pending raw checks

1. Missingness by column, lake, year, season.
2. Zero-vs-missing semantics.
3. Duplicate rows/keys and same-species/date variants.
4. Negative/anomalous/implausible values.
5. Taxon richness/identification changes across 2013.
6. Arithmetic consistency: cells/NU × NU/mL vs cells/mL; biovolume × density vs biomass.
7. Effective sample size: sampling dates, not rows.

## Claim status

No missingness or quality claim is made about the raw data. The file has not been inspected.
