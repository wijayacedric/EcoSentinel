# Independent reproduction results

## Procedure and integrity

A fresh standard-library Python script reads the original version 88.31 data export as bytes and CSV records, parses numeric values independently, groups rows directly, and parses the EML for field meaning. It writes only to this Sprint 4L.6 folder. It does not import Sprint 4L.5 code or tables. Script: `scripts/independent_reproduction.py`.

| Check | Independent result |
|---|---:|
| Bytes / SHA-256 / MD5 | 2,448,830 / `a63d7cfa0502e3cdab6d8939f21820f305295e030d4d08bf10bfc69b22829db2` / `a0363cc7fdfd6c12889750fea27bd542` |
| Header fields | 15; exact expected header |
| Rows / row arity | 18,654 / all 18,654 have 15 fields |
| Date parses / year mismatch | all valid / 0 |
| All-lake dates | 640, 1995-01-24 to 2020-12-10 |
| Lake records | ME 9,401; MO 8,696; WI 532; FI 25 |
| Lake unique dates | ME 402; MO 355; WI 23; FI 1 |
| ME date span | 1995-01-24–2020-12-10 |

## Mendota date cadence

402 distinct dates, 401 gaps; min 2d, median 14d, mean 23.57d, max 120d. There are 72 gaps ≥30d, 35 ≥60d, six ≥90d. Annual dates range from 13 (2014) to 19 (1995), with 13–19 dates/year in each year 1995–2020. Annual month coverage and gaps are in `reproduction/ANNUAL_ME_SAMPLE_DATES.csv`. These calendar gaps include winter and within-season omissions; a 14-day median is not a guarantee of regular two-week sampling.

## Numeric fields

All seven numeric fields parse as finite, nonnegative values with zero missing/negative values. Independent descriptive quantiles are below; output precision shown compactly. These are exported field values, not a validation of laboratory method or uncertainty.

| field | n | zeros | min | median | p95 | max | mean |
|---|---:|---:|---:|---:|---:|---:|---:|
| gald | 18,654 | 3 | 0 | 12 | 133.380095 | 3,200 | 34.071945 |
| cells_per_nu | 18,654 | 1 | 0 | 1 | 52.5 | 48,000 | 15.577160 |
| nu_per_ml | 18,654 | 0 | 0.1704 | 75.7308 | 11,772.43025 | 357,259.5436 | 2,613.500244 |
| cells_per_ml | 18,654 | 1 | 0 | 227.1924 | 37,519.23905 | 10,074,657.1215 | 10,587.725757 |
| biovolume_conc | 18,654 | 3 | 0 | 6,578.0223 | 435,845.369135 | 84,070,000 | 133,607.298860 |
| biomass_conc | 18,654 | 64 | 0 | 0.006589195 | 0.437 | 84.6924 | 0.138147517 |
| relative_total_biovolume | 18,654 | 18 | 0 | 0.406 | 23.5249 | 283,806.87 | 19.459943 |

Further quantiles and by-lake distributions are independently in `reproduction/INDEPENDENT_REPRODUCTION_SUMMARY.json`. `cells_per_ml` vs `cells_per_nu × nu_per_ml` was checked for 18,653 nonzero denominators: max relative error 0.000228, no discrepancy above 1%. Biomass compared to biovolume×10⁻⁶ has 61 zero/positive mismatches, plus small-value differences. Arithmetic agreement does not prove the conversion assumption for each taxon.

## Taxonomy, whitespace, missing codes

- 11 division values; Cyanophyta 8,581 rows.
- 12 blank `taxa_name` rows, 1,632 blank genus rows.
- 468 distinct **nonblank** cleaned taxon strings; 176 distinct **nonblank** genera. Counts including a blank string are 469/177.
- 8,514 raw taxon values have trailing whitespace; 927 have double spaces.
- 889 records have nonblank genus whose value differs from the first token of cleaned taxon name. This mechanical mismatch count includes candidate nomenclatural updates and formatting/identification issues; it is not an error count.
- The pre/post-February-2013 inventory gives 204 names only before and 72 only after using the script's date partition; those are literal-name inventory differences, not confirmed extinctions/arrivals or taxonomy changes.
- The regex flag count is 20 distinct names/1,038 records under the script's `sp|spp|var|cf` pattern. It is a screening rule, not an authoritative taxonomic-resolution measure.

## Repeated and relative records

On key `(lakeid, sampledate, sta, depth_range, stripped taxa_name)`: 1,009 groups / 2,048 rows / 1,039 rows beyond one per group. 966 groups vary in `cells_per_ml`; 976 vary in `biovolume_conc`. On unstripped names: 996 groups / 2,021 rows, showing whitespace affects grouping. Exact full-row duplicate check: 29 duplicate groups, 58 rows/29 excess rows, all at MO 1999-11-22.

On sample grouping `(lakeid, sampledate, sta, depth_range)`: 781 groups; 762 sums 99–101%; 14 sum 199–201%; three sum zero; two are otherwise anomalous (98.864 and 283,906.853). Alternate groupings without `sta` or without `depth_range` happened to produce the same group counts/statistics in this file because observed combinations are nested; this does not establish the true denominator.

## Depth and station

Depth counts reproduce: ME 9,361 rows 0–8m and 40 rows 0–2m; MO 8,386 rows 0–2m and 310 rows 0–8m; WI 532 and FI 25 all 0–2m. `sta` is blank on 17,518 records; station `1` on ME 780 and MO 356. No sample-time field or per-row quality flags are present.

## Reproduction limits

Verified is the exported file and package EML, not the truth of entered counts, slide-level identifications, sample volume, denominator, original calculations, sample replicates, or missing/failed sampling visits. No bloom/event status has been inferred.
