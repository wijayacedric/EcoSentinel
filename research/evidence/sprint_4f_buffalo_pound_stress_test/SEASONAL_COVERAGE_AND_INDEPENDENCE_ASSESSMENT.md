# Seasonal Coverage and Independence Assessment — Buffalo Pound

**Date:** 2026-11-23T23:22:37.724583+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. Seasonal representation

| Year | May | Jun | Jul | Aug | Sep | Oct | Nov-Apr |
|---|---:|---:|---:|---:|---:|---:|---|
| 2018 bio | 1 | 5 | 10 | 7 | 2 | 0 | 0 |
| 2019 bio | 1 | 3 | 4 | 4 | 4 | 1 | 0 |

- Buoy deployment is also ice-free only (May-Oct; 2014-2021).
- No winter, spring (April), or late-autumn (November) biological observations.
- 2018 sampling is concentrated in July (10 of 25 dates); 2019 is more evenly spread but has a 16-day gap.

## 2. Sampling regularity

- 2018 median gap 4 d (max 12 d) — roughly twice weekly.
- 2019 median gap 8 d (max 16 d) — roughly weekly with a mid-season gap.
- No evidence in the files of event-triggered sampling; dates are broadly regular. However, field logs are unavailable, so trigger bias cannot be excluded.
- 2018 duplicate date-species rows and 2019 REP labels indicate counting/sample encoding differences, not additional dates.

## 3. What two seasons can establish

- Descriptive seasonal succession within two ice-free seasons.
- Co-variation between biological biomass and environmental conditions at ~42 dates.
- Method feasibility, data-quality requirements, and exploratory hypotheses.

## 4. What two seasons cannot establish

- Multi-year recurrence or stationarity of relationships.
- Stable false-alarm rates or matched-FAR performance.
- Held-out temporal validation across years.
- Defensible non-bloom exposure: both seasons have high cyanobacteria biomass (~71% of summed biomass), and no winter/spring baseline exists.
- Independence of "events" across years: same lake, same station, same seasonal cycle.

## 5. Pseudoreplication risk

- 40k+ 10-min sensor records → 5,387 records on bio dates → **42 date-level observations**.
- 1,222 taxon rows / 248 cyanophyte rows → **42 dates** (and some duplicate counting rows).
- Treating sensor readings, taxon rows, or within-season dates as independent events would grossly overstate effective sample size.
- Two years are not "many independent bloom events"; they are two seasonal cycles in one lake.

## 6. Conclusion

Buffalo Pound is suitable for **exploratory within-season analysis** with explicit pseudoreplication controls. It is not suitable for confirmatory event/false-alarm evaluation.
