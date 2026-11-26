# Biology–Sensor Temporal Compatibility

**Date:** 2026-11-24T08:45:50.090661+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Verified biology reference

- 402 Mendota microscopy dates, 1995-01-24 to 2020-12-10; median interval 14 days.

## Metadata-level overlap

- 129.42 package coverage: 2006–2025.
- **230/402 biology dates (57.2%) fall within 2006–2020**, the period where both the biological record and package metadata overlap.
- 172 biology dates (42.8%) predate 2006; no biology dates post-2020.
- **Actual daily sensor records verified on biology dates: 0.** The daily entity was not acquired.
- Per-year potential overlap is in `BIOLOGY_SENSOR_DATE_OVERLAP.csv`; `daily_sensor_records_verified=0` for every year.

## Temporal limitations

- Biology has **date only**, no sample time. A microscopy date cannot be assumed to be the exact sensor time.
- Sensor data are daily averages; day-level matching is the only defensible resolution unless sample times are recovered.
- Missingness by season/year, variable-specific same-day availability, and preceding/following coverage cannot be assessed without the daily file.
- No interpolation, event labels or model predictors were created.

## Required after acquisition

1. Same-day valid record counts per variable/year.
2. Preceding/following daily coverage using explicitly descriptive windows (availability only).
3. Seasonal/year-specific missingness.
4. Whether daily aggregation is adequate or hourly data are required for a specific variable.
5. Whether sample times exist in field logs.

**No same-day sensor–biology match is claimed.**
