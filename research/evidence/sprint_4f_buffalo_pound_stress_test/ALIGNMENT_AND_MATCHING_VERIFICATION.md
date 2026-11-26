# Alignment and Matching Verification — Buffalo Pound

**Date:** 2026-11-23T23:22:37.724583+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. Matching logic used

- Biological `DOY` converted to calendar date for the stated year (non-leap; DOY 149 = 29 May).
- Buoy `DateTime` parsed as `YYYY-MM-DD HH:MM` and grouped by calendar date.
- A biological date is "matched" if ≥1 buoy record exists that day.
- No interpolation; no sub-daily matching; no labels.

## 2. Results

| Year | Bio dates | Matched buoy days | Records/day min/median/max | Valid key vars on bio days |
|---|---:|---:|---|---|
| 2018 | 25 | **25/25** | 121 / 134 / 144 | Temp 93.1%, pH 93.1%, DO 93.1%, SpCond 93.1%, Turb 93.1%, Chl 93.1%, BGPC 93.1% |
| 2019 | 17 | **17/17** | 42 / 130 / 131 | Temp 98.9%, pH 98.9%, DO 98.9%, SpCond 98.9%, Turb 98.8%, Chl 98.9%, BGPC 98.8% |

- Total buoy records on biological dates: 3,345 (2018) + 2,042 (2019) = 5,387.
- These collapse to **42 date-level environmental observations** when paired with biology. They are repeated measurements, not independent events.

## 3. Depth and location

- Biological depth: 0.8 m (all rows).
- Buoy shallow sensor depth: 0.82 m (documented), effectively 0.8 m. **Depth-compatible.**
- Deep buoy sensors (2.8 m) are not used for the main match.
- YSI profiles provide 0.2-4.0 m context on 20/25 (2018) and 16/17 (2019) bio dates, including 0.8 m.
- Single lake station; buoy coordinates not independently re-verified against biological site coordinates in this sprint.

## 4. Time-zone and date precision

- Buoy timestamps have no timezone suffix; README does not state timezone. Saskatchewan observes CST year-round, but this is **not verified from the data documentation**.
- Biological data provide date (DOY) only, no sample time. Matching is therefore **day-level**, not hour-level.
- Consequence: a "same-day" match does not prove the buoy and biological sample were simultaneous; diel cycles (DO, pH) cannot be resolved.

## 5. Independence of matches

- Multiple buoy readings per biological date are **not** independent biological replicates.
- 2018 duplicate date-species rows are counting replicates without IDs; 2019 REP labels are disjoint-date labels, not paired replicates.
- Effective independent biological sample size ≈ **42 sampling dates**, not 40k+ sensor records or 1,222 taxon rows.

## 6. Conclusion

The previously reported same-date, same-depth matching is **confirmed at day level**. It is genuine alignment, but it does not create additional independent events; the effective sample size is small.
