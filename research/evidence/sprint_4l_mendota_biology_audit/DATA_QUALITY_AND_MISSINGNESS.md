# Data Quality and Missingness — 88.31 (Metadata-Level)

**Date:** 2026-11-23T23:58:36.852965+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Status

**Raw data not acquired.** The checks below are the required audit plan and the metadata-level findings. Row-level missingness, duplicates and outliers are **not yet verified**.

## Metadata-level findings

| Item | Finding | Implication |
|---|---|---|
| QC flag columns | **None in schema** | Cannot distinguish suspect counts from valid counts without external protocol/QA records. |
| Detection limits | **Not provided** | Low-abundance taxa and zeros cannot be interpreted against a documented limit. |
| Replicate identifier | **None** | Same species/date rows may be variants or counting replicates; effective N cannot be established. |
| Species resolution | Species-level expected; EML says species may not be determined for all slides | Unidentified taxa and changing resolution affect richness/composition metrics. |
| Taxonomic update | February 2013, multiple name/genus changes | Pre/post-2013 names must be harmonised; some changes are retrospective. |
| Taxonomist consistency | Same analyst (A.L.S.) reported for 1995–2010; PhycoTech says sole enumerator | Long-term consistency likely, but self-reported; independent intercalibration not documented. |
| Sampling design | Biweekly ice-free, 4-weekly late season, ~1 winter | Uneven intervals; under-ice observations sparse. |
| Depth | Mendota 0–8 m composite | Not a point sample; buoy comparison requires depth-integrated or surface comparator. |
| Multiple entries | EML warns same species/date may be variants/vegetative states | Do not treat every row as an independent observation. |

## Required raw-data checks (not yet performed)

1. Row count and exact date range; duplicate header/blank rows.
2. `lakeid` values; Mendota-specific row/date counts.
3. Dates per year/month; interval distribution; gaps; winter sampling.
4. Duplicate keys `(lakeid, sampledate, sta, depth_range, taxa_name)` and same-species/date variants.
5. Missingness/zeros for `gald`, `cells_per_nu`, `nu_per_ml`, `cells_per_ml`, `biovolume_conc`, `biomass_conc`, `relative_total_biovolume`.
6. Arithmetic consistency (cells/NU × NU/mL vs cells/mL; biovolume × density vs biomass).
7. Taxa list by year; cyanobacteria; unidentified taxa; pre/post-2013 name changes.
8. Outliers/implausible values; taxa with zero dimensions; detection-limit artefacts.
9. Station/depth consistency; whether `depth_range` is always 0–8 for Mendota.
10. Independence: rows are taxa within a sample, not independent time points; effective N is sampling dates.

## Why this matters

The dataset could be large (2.45 MB) yet contain far fewer independent biological occasions. Without raw data, effective sample size, missingness, and taxonomic consistency cannot be quantified. No labels were created.
