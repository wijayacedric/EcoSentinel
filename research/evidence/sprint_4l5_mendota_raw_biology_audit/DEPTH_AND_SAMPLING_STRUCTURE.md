# Depth and Sampling Structure

**Date:** 2026-11-24T07:22:12.805937+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Depth categories by lake

| lakeid | depth_range | sta | records |
|---|---|---|---|
| FI | 0-2m |  | 25 |
| ME | 0-2m |  | 40 |
| ME | 0-8m |  | 8581 |
| ME | 0-8m | 1 | 780 |
| MO | 0-2m |  | 8030 |
| MO | 0-2m | 1 | 356 |
| MO | 0-8m |  | 310 |
| WI | 0-2m |  | 532 |

## Key findings

- **Mendota is predominantly 0–8 m** (9,361 records), consistent with the metadata composite design.
- **40 Mendota records are labelled 0–2 m** on 2002-09-23 and 2002-10-21. This contradicts the metadata; no correction was applied.
- **Monona is predominantly 0–2 m** (8,386 records) but has **310 records labelled 0–8 m** on 11 dates in 1995 and 2002–2004. This also contradicts the metadata.
- WI and FI are 0–2 m only; FI has one date (1995-03-28).
- `sta` is blank for 17,518 records; `1` appears for 1,136 records in ME 2011–2012 and MO 2011. Station identity is not consistently recorded.
- The actual data do not prove that every Mendota sample is a 0–8 m composite; the majority label supports it, but the 40 exceptions are unresolved.

## Consequences for sensor comparison

A 0–8 m integrated phytoplankton sample is not equivalent to a point sensor at 0.5 m (chlorophyll/phycocyanin/DO) or to a thermistor at a fixed depth. Any future comparison must define a depth comparator (e.g., surface layer, euphotic-zone integration, or total water-column biomass) and must not claim point measurements represent the whole composite.

## Sampling cadence

See `MENDOTA_RECORD_COVERAGE.csv`, `ANNUAL_SAMPLING_COVERAGE.csv`, and `SAMPLING_INTERVALS_AND_GAPS.csv`. Mendota has 13–19 dates per year and a median gap of 14 days; the longest gaps are winter/ice periods. This supports seasonal/multi-week analysis, not daily warning.
