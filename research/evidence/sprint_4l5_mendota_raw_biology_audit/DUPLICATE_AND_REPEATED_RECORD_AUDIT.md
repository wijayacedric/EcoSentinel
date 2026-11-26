# Duplicate and Repeated-Record Audit

**Date:** 2026-11-24T07:22:12.805937+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Exact duplicate rows

- **29 groups / 58 rows** are exact duplicates of all 15 fields.
- All are **MO 1999-11-22** and appear to be a duplicated sample/import block (29 species groups, each duplicated).
- No records were removed. If used, one copy of the affected sample should be treated as the analysis unit; this is a documented data-quality defect.

## Same lake/date/station/depth/taxon groups

- **1,009 groups / 2,048 rows** share the same five-field key; that is 11.0% of all rows.
- Multiplicity: {'2': 990, '3': 8, '4': 11}.
- **966 groups** have >1 distinct `cells_per_ml`; **976** have >1 distinct `biovolume_conc`.
- No group contains multiple `genus` or `division` values.
- These are consistent with the EML warning that multiple entries for the same species/date may represent different variants or vegetative states. They should **not** be treated as independent samples, and should not be deleted automatically.
- Top groups include Microcystis aeruginosa (4 rows on several dates), Coelosphaerium/Woronichinia, and Miscellaneous.

## Examples

| lakeid | sampledate | depth_range | taxa_name_clean | n_rows | n_distinct_cells_per_ml | n_distinct_biovolume_conc | cells_min | cells_max | biovolume_min | biovolume_max |
|---|---|---|---|---|---|---|---|---|---|---|
| MO | 1995-01-24 | 0-2m | Miscellaneous | 2 | 2 | 2 | 104.174 | 989.65 | 580.133 | 5511.266 |
| ME | 1995-01-24 | 0-8m | Miscellaneous | 2 | 2 | 2 | 677.129 | 2031.387 | 11312.598 | 30166.929 |
| ME | 1995-03-08 | 0-8m | Miscellaneous | 2 | 2 | 2 | 1041.737 | 1145.911 | 32505.591 | 112600.0 |
| FI | 1995-03-28 | 0-2m | Dinobryon cylindricum | 2 | 2 | 2 | 13.151 | 26.302 | 2709.208 | 5418.416 |
| FI | 1995-03-28 | 0-2m | Miscellaneous | 2 | 2 | 2 | 1770.953 | 2916.863 | 16243.731 | 80747.296 |
| MO | 1995-03-28 | 0-2m | Miscellaneous | 2 | 2 | 2 | 694.491 | 2864.776 | 15953.664 | 24172.219 |
| ME | 1995-03-28 | 0-8m | Miscellaneous | 2 | 2 | 2 | 1041.737 | 4791.989 | 11602.665 | 135900.0 |
| MO | 1995-04-11 | 0-2m | Miscellaneous | 2 | 2 | 2 | 520.868 | 1875.126 | 10442.398 | 11149.436 |
| ME | 1995-04-11 | 0-8m | Miscellaneous | 2 | 2 | 2 | 729.216 | 2916.863 | 32487.462 | 44670.26 |
| ME | 1995-04-24 | 0-8m | Miscellaneous | 2 | 2 | 2 | 1145.911 | 4062.774 | 57433.191 | 89086.712 |

## Effective sample size

The number of records is **not** the number of independent biological observations. The independent unit is the sampling date (or date × station/depth), not the taxon row. ME has 402 unique dates; MO 355; WI 23; FI 1.
