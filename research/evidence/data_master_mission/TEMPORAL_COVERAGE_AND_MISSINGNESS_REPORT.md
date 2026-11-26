# Temporal Coverage and Missingness Report

**Date:** 2026-11-23T23:18:29.122618+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Buffalo Pound — VERIFIED

| Year | Rows | Interval | First | Last |
|---|---:|---|---|---|
| 2014 | 8,015 | 15 min | 2014-06-11 22:15 | 2014-09-05 01:15 |
| 2015 | 20,438 | 10 min | 2015-05-14 21:10 | 2015-10-06 11:50 |
| 2016 | 18,975 | 10 min | 2016-05-18 16:50 | 2016-09-28 15:50 |
| 2017 | 22,023 | 10 min | 2017-05-09 17:20 | 2017-10-11 12:40 |
| 2018 | 20,162 | 10 min | 2018-05-15 16:00 | 2018-10-04 11:30 |
| 2019 | 18,026 | 10 min | 2019-05-29 17:00 | 2019-10-03 13:20 |
| 2020 | 16,836 | 10 min | 2020-06-05 16:30 | 2020-10-01 13:20 |
| 2021 | 18,285 | 10 min | 2021-05-31 20:20 | 2021-10-07 14:30 |

- **Missingness (key 0.8 m variables):** 2018 ≈87.9% present (≈12.1% missing); 2021 ≈97.5-100% present. Deep pH absent in 2021; deep chlorophyll RFU absent in 2018 (0% present). Missingness is seasonal/sensor-dependent, not random.
- **Flags:** present for all variables; codes in `data_flags.csv`.
- **Biological coverage:** 2018-05-29 to 2018-09-17 (25 dates); 2019-05-29 to 2019-10-03 (17 dates). 2019 has a 16-day mid-season gap (DOY 170→186).

## Lake Mendota — UNRESOLVED

- 88.31: 1995-2020 (EML). 129/130: 2006-current metadata. 415: 2006-2019.
- Actual cadence/gaps cannot be computed: data bytes auth-blocked.

## Western Lake Erie — UNRESOLVED

- Literature: 2012-2021, weekly/biweekly May-Sep, COVID disruption 2020, opportunistic scum samples. No file-level missingness.

## Greifensee — VERIFIED PRIOR

- May 2018-Jun 2023, 60/60 monthly packages; gaps/schema changes documented in Sprint 4D.4.

## Implication

Buffalo Pound has a **verified 8-season environmental record** but only **2 biological seasons**. Mendota is the only candidate with long-term biological metadata plus HF predictors, but is inaccessible. No candidate currently offers multi-year independent biological and environmental coverage simultaneously in verified local data.
