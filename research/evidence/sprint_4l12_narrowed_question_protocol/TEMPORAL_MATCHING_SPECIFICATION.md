# Temporal Matching Specification

**Sprint:** 4L.12  
**Status:** PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Date:** 2026-11-24

> **No analysis may begin until this protocol has been reviewed and explicitly approved.**

## 1. Purpose

This document defines how a microscopy observation is matched to a sensor observation. It is deliberately conservative.

The central rule is:

> **Primary matching is same calendar date only. A same-day match is not a simultaneous measurement. No onset, lead time, or bloom timing is inferred.**

## 2. Why matching is difficult

### 2.1 Date-only biology

- Mendota microscopy has a `sampledate` but no sample time.
- Buffalo Pound microscopy has a `DOY` but no sample time.
- Sensor data are high-frequency (1-minute at Mendota, 10-minute at Buffalo Pound), but the biological sample is a single date-stamped observation.
- A sensor daily average integrates a full day; the biological sample represents an unknown time within that day.

### 2.2 Sparse biology

- Mendota: 402 dates over 26 years; median interval 14 days; maximum 120 days.
- Buffalo Pound: 42 dates over two seasons; median 4 days (2018), 8 days (2019); maximum 12/16 days.
- The biological series cannot resolve onset, termination, or a few-day lead time.

### 2.3 Different locations and depths

- Mendota: buoy at approximately 43.0995, −89.4045; NTL sampling site at approximately 43.09885, −89.40545; ~105.7 m apart. Sensor 0.5 m; biology 0–8 m composite.
- Buffalo Pound: single buoy near the water-treatment intake; biology at 0.8 m; sensor at 0.82 m. Coordinates are not independently re-verified.
- Same-day matching does not establish spatial co-location.

### 2.4 Diel cycles and quenching

- Chlorophyll and phycocyanin fluorescence are affected by light-induced non-photochemical quenching; published reductions reach up to ~79% for chlorophyll and ~59% for phycocyanin under maximum light.
- A full-day average includes daylight quenching and nighttime values. It is not a nighttime biomass estimate.
- Mendota daily values are provider-computed averages of 1-minute observations; the daily file does not allow reconstruction of a nighttime-only value.
- Buffalo Pound 10-minute data do allow a nighttime sensitivity analysis, but the primary analysis uses a full-day mean to match the Mendota structure.

## 3. Primary matching rule

### 3.1 Definition

A biological observation is matched to a sensor observation when:

1. the biological date and the sensor date are the **same calendar date** in the provider’s local date system;
2. the biological observation passes the inclusion rules in `DATASET_INCLUSION_EXCLUSION_RULES.md`;
3. the sensor daily summary passes the QC and coverage rules in `QC_AND_MISSINGNESS_PROTOCOL.md`.

### 3.2 No time-of-day matching

No hour-level matching is attempted. The biological data have no sample time, and the sensor daily file has no within-day distribution. Any claim of “same-time” or “simultaneous” measurement is prohibited.

### 3.3 No interpolation

- If there is no sensor value on the biological date, the date is excluded from the primary analysis.
- Do not interpolate across missing days.
- Do not carry forward the previous or next value.
- Do not fill missing values with zero.

### 3.4 No substitution across depths or instruments

- Mendota: do not substitute the YSI value for a missing Turner value, or vice versa.
- Buffalo Pound: do not substitute the deep sensor for the shallow sensor.
- Do not substitute a different pigment (e.g., chlorophyll for phycocyanin).

## 4. Sensor daily summaries

### 4.1 Lake Mendota

The primary sensor value is the **provider-supplied daily average** in `knb-lter-ntl.129.42`.

- The EML states that daily values are averages of 1-minute observations.
- The daily file does not include the number of valid minutes, so within-day coverage cannot be independently verified.
- The primary analysis accepts the provider daily average if the value is numeric and passes the flag rule.
- A sensitivity analysis excludes `H`-flagged values (the stricter 4L.10 “unflagged only” rule).
- A nighttime-only value cannot be computed from the daily file. This is a structural limitation, not a missing-data problem.

**Do not** attempt to reconstruct a daily average from the hourly or high-resolution entities in this sprint. Those entities were deliberately not acquired, and acquiring them would be a new data acquisition.

### 4.2 Buffalo Pound

The primary sensor value is the **mean of all valid 10-minute values on the calendar date**, after applying the QC rule.

- 2018 and 2019 are 10-minute cadence; expected 144 values per full day.
- A date is eligible only if:
  - at least **50% of expected values** are valid (≥72 values); and
  - at least one valid value occurs in each half of the day (00:00–11:59 and 12:00–23:59).
- The 50% rule prevents a “daily mean” from being a half-day mean. It is a completeness rule, not an ecological threshold.
- If a date fails the coverage rule, it is excluded from the primary analysis and included in a sensitivity analysis with a lower coverage requirement (any valid value).
- The daily mean is computed on the raw 10-minute values, not on hourly averages.

### 4.3 Why the summaries differ

Mendota’s provider daily average and Buffalo Pound’s computed daily mean are both full-day means. They are structurally similar but not identical:

- Mendota: provider average, unknown number of valid minutes, 1-minute base.
- Buffalo Pound: analyst-computed mean, known number of valid 10-minute values, 10-minute base.

The protocol accepts this asymmetry and states it in every cross-lake comparison. It does not adjust one lake to look like the other.

## 5. Time zones and calendar dates

### 5.1 Mendota

- Provider: North Temperate Lakes LTER, Wisconsin, USA.
- Local time zone: US Central Time (UTC−6 standard, UTC−5 daylight).
- The daily file does not state a time zone. The protocol treats the `sampledate` and daily summary as **local calendar date** values, as supplied.
- No UTC conversion is applied. A UTC conversion could shift dates by 5–6 hours and is not justified without documentation.

### 5.2 Buffalo Pound

- Provider: University of Saskatchewan / FRDR.
- Location: Saskatchewan, Canada.
- Saskatchewan observes Central Standard Time (UTC−6) year-round, without daylight saving.
- The README and data paper do not state a time zone. The protocol treats `DateTime` as **local clock time** and uses the calendar date as recorded.
- No UTC conversion is applied.

### 5.3 Date parsing

- Mendota: parse `YYYY-MM-DD`.
- Buffalo Pound: convert `DOY` to calendar date within the stated year.
  - 2018 and 2019 are non-leap years; DOY 1 = January 1.
  - If a future leap year is added, use the actual calendar, not a fixed 365-day assumption.
- Reject impossible dates (e.g., DOY 366 in a non-leap year).
- Do not shift a date to the nearest sensor date in the primary analysis.

### 5.4 Date boundaries

- A biological sample and a sensor reading are “same-day” if they share the same calendar date after the above parsing.
- A sample at 23:59 and a sensor reading at 00:01 the next day are **not** same-day.
- No allowance for a several-hour offset is made in the primary analysis.

## 6. Wider temporal windows

### 6.1 Primary

**Same-day only.** This is the only primary matching rule.

### 6.2 Sensitivity: ±1 day

A single sensitivity analysis may use a **±1-day window**:

- If a same-day sensor value exists, use it.
- If not, use the nearest sensor date within one day.
- If both −1 and +1 days have valid values and the same-day value is missing, use the **mean of the two**.
- If only one adjacent day is valid, use that day.
- The window is used only for dates that would otherwise be excluded; it does not replace a valid same-day value.

This sensitivity analysis is **not** a same-time comparison. It asks whether the descriptive pattern is sensitive to a small amount of date mismatch. It must be labelled “±1-day window association,” not “agreement.”

### 6.3 No ±3, ±7, or ±14-day primary or sensitivity windows

Wider windows are **not** proposed because:

- Mendota’s median biology interval is 14 days; a ±7-day window can span an entire bloom phase.
- Buffalo Pound’s median interval is 4–8 days; a ±7-day window can span multiple samples and different ecological states.
- Wider windows increase the chance of matching a sensor peak to a biological sample from a different state.
- A wider-window association cannot be interpreted as same-time comparability.
- The prior 4L.9/4L.10 ±1/±3/±7/±14 tables were descriptive overlap counts, not matching rules. They are not adopted here.

### 6.4 No lag analysis

Do not compute cross-correlation, lagged regression, lead time, or “sensor leads biology” statistics. The data cannot support them.

## 7. Multiple sensor values per date

### 7.1 Mendota

- The daily file has one row per date.
- If a future revision contains duplicate dates, stop and resolve before analysis; do not average duplicates silently.

### 7.2 Buffalo Pound

- Multiple 10-minute values per date are expected.
- Primary: mean of valid values, subject to the coverage rule.
- Sensitivity: nighttime median (00:00–05:00) and daytime median (10:00–16:00), to show the direction of diel quenching.
- Do not treat individual 10-minute values as independent observations.

## 8. Multiple biological values per date

### 8.1 Mendota

- One `0-8m` composite per date is expected.
- If multiple `0-8m` rows occur for a date, sum biovolume across rows after applying the taxonomy rule. This is a component aggregation, not a replicate average.
- If multiple `sta` values occur, use station `1` if present; otherwise use the blank-station rows. Do not pool stations.
- Do not average across depth classes.

### 8.2 Buffalo Pound

- One `0.8m` sample per date is expected.
- If duplicate date × species rows occur (2018), collapse by mean before summing, per `DATASET_INCLUSION_EXCLUSION_RULES.md`.
- If both `REP1` and `REP2` occur on one date (they do not), average them.
- Do not treat replicate rows as independent dates.

## 9. Flag and missingness interaction with matching

A date can fail matching for several distinct reasons. The analysis must report them separately:

| Reason | Mendota | Buffalo Pound |
|---|---|---|
| No biological sample | Date absent from 88.31 | Date absent from 2018/2019 files |
| Biology outside depth rule | `0-2m` | `Depth != 0.8` |
| Biology outside window | Before 2006-07-09 or after 2020-12-10 | Outside 2018/2019 seasons |
| No sensor record on date | No row in daily file | No buoy record |
| Sensor value missing | Empty cell | `NA` / `M` |
| Sensor value flagged | `C`, `E`, `G`, `O`; `H` handled separately | `C`, `B7`; `M` |
| Sensor value physically implausible | Negative pigment; DO/temp out of range | Negative pigment; out of range |
| Insufficient within-day coverage | Not assessable from daily file | <50% expected values or one half-day missing |
| Biological endpoint invalid | No cyanobacteria rows; depth/station ambiguity | No cyanobacteria rows; group/phylum mismatch |

The flow table must show these categories, not just a final n.

## 10. What same-day matching does and does not mean

### 10.1 It means

- A biological sample and a sensor daily summary exist on the same calendar date.
- The comparison is date-level.
- The sensor summary represents the whole day, not the instant of sampling.

### 10.2 It does not mean

- The sensor and the microscope measured the same water parcel.
- The sensor and the sample were collected at the same time.
- The sensor value represents the 0–8 m composite.
- A difference in values is measurement error alone.
- A temporal lead or lag can be inferred.
- A bloom onset or termination can be dated.

## 11. Matching audit

Before estimation, the analysis must produce a matching audit with:

- total biological dates in the source;
- dates inside the analysis window;
- dates meeting the depth rule;
- dates with any sensor row;
- dates with a numeric sensor value;
- dates passing the flag rule;
- dates passing the coverage rule (Buffalo Pound);
- final primary n for each estimand;
- a list of excluded dates with reasons;
- a comparison of included vs excluded dates by year and month (descriptive only).

The audit is a table of counts and dates. It is not a correlation analysis and does not test hypotheses.

## 12. Governance

- **Gate 2 remains PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- No matching, interpolation, correlation, plot, or derived dataset is created in this sprint.
- No analysis may begin until the protocol is reviewed and explicitly approved.
