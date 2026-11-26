# Sprint 4L.9 Executive Report — Mendota Daily Sensor Raw Audit and Biological Feasibility

**Date:** 2026-11-24  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Acquisition status: ACQUIRED AND AUDITED — exploratory feasibility improved with major limitations.**  
**Final feasibility decision: EXPLORATORY FEASIBILITY SUPPORTED WITH MAJOR LIMITATIONS.**

## 1. Scope and integrity

The previously acquired `knb-lter-ntl.129.42` daily entity was audited read-only. The actual bytes match the Sprint 4L.8A baseline:

- **490,187 bytes**; MD5 `eb7b3a3848b27074bac4504236ccefc3`; SHA-1 `bb1d8a281a3d580cad45549551abdbaed1ae03fe`; SHA-256 `104ef1b33769bc0ad1d3e9e6dff28219b743b81ce89ee888460d2df255981343`.
- **38 columns**, **3,996 data rows**, **0** malformed rows, **0** duplicate dates, **0** exact duplicate rows, **0** date-parse errors.
- Date range **2006-07-09 to 2025-11-18**; 3,996 unique dates over a 7,073-day calendar span (~56.5% of days). The difference is the open-water deployment pattern, not missing rows in a year-round series.
- The raw file was not renamed, rewritten or normalised. No additional entity was acquired.

## 2. Variable coverage

All 18 variables and 18 flag columns are present. Coverage is strongly variable-specific:

- Long records: air temperature, RH, wind, DO (2006+); Turner chlorophyll/phycocyanin (2006–2019); pCO2 (2016+); PAR (sustained 2016+).
- 2019+ only: YSI chlorophyll/phycocyanin, pH, fDOM, turbidity, specific conductance.
- Unflagged coverage ranges from **31.4%** (YSI chlorophyll) to **91.5%** (wind direction).
- Severe within-era gaps: Turner chlorophyll 2014 (**14** unflagged) and 2015 (**70**); Turner phycocyanin 2007 (**6**); DO 2008 (**18**), 2010 (**59**), 2014 (**50**), 2017 (**62**).
- Winter coverage is minimal (15 records; no January/February). Seasonal analysis is open-water-season analysis.

## 3. QC and metadata

- Flags `C`, `E`, `H`, `G` are used; `O` appears once and is undefined.
- Eight flag columns contain values outside their own daily-EML code lists: `rel_hum` H, `wind_speed` H, `par_below` H, `do_wtemp` E, `ph` E, `fdom` E, `turbidity` E, `spec_cond` E/O.
- `C` is not equivalent to missing: many `C` records retain numeric values (e.g., 1,534 numeric `C` values for `avg_do_wtemp`).
- `G` (biofouling) is used only for YSI chlorophyll/phycocyanin and PAR below; the Turner era has no `G` flags, which does not prove the absence of fouling.
- Missing values are often unflagged (“empty unflagged”), especially for variables before their sensor era. No missing value was treated as zero.
- Unflagged does not mean accurate: negative turbidity (31), negative YSI phycocyanin (62), negative YSI chlorophyll (1), negative PAR below (3) and 2006 conductance values ~0.4 µS/cm are present. They are reported, not deleted.
- No calibration coefficients, serial numbers, detection limits or maintenance logs are present. The EML documents 2017–2024 fouling/outage events and 2019–2020 cleaning/calibration, but not per-record calibration.
- Validation: **17/18** internal checks pass; the single non-conformance is the documented flag-code metadata inconsistency. An independent parser reproduced all key counts with **zero** coverage, overlap or percentage mismatches (`VALIDATION_REPORT.md`, `INDEPENDENT_VERIFICATION.md`).

## 4. Sensor-era comparability

- **Turner vs YSI chlorophyll/phycocyanin:** both deployed in 2019; 156/160 paired dates. Turner median chlorophyll 1,354.7 RFU vs YSI 0.39 RFU (median ratio 0.000332); phycocyanin 802.0 vs 0.5895 (ratio 0.000835). The EML itself says “significant magnitude differences.” No crosswalk exists; do not concatenate.
- **DO:** values exist from 2006, but the inventory's DO records start 2016; pre-2016 instrument identity is unresolved. DO flags vary by year; no documented cross-calibration.
- **Water temperature:** `avg_do_wtemp` is labelled YSI water temp but exists from 2006; 2019+ is heavily `C`-flagged (1,087 `C`; 371 unflagged of 1,612). It is not a clean continuous series. Ancillary dataset 130 is documented but not acquired.
- **pH/fDOM/turbidity/conductance:** 2019+ only; short overlap with biology.
- **pCO2/PAR:** pCO2 begins 2016 (inventory says 2017); PAR has 2007 near-zero values (ten 0.0, one 0.002) and a sustained 2016+ record. Both are contextual.

## 5. Biology–sensor overlap

The biology reference is 402 Mendota dates, 1995–2020, median 14 days, predominantly 0–8 m composite; 371/402 dates have no station value and there are no sampling times.

Same-day unflagged overlap:

| Proxy | Same-day dates | % of all 402 | % of within-span |
|---|---:|---:|---:|
| Turner chlorophyll | 128 | 31.8% | 62.1% |
| Turner phycocyanin | 139 | 34.6% | 67.5% |
| YSI chlorophyll | 21 | 5.2% | 75.0% |
| YSI phycocyanin | 22 | 5.5% | 78.6% |
| DO raw | 99 | 24.6% | 44.8% |
| pH / fDOM / turbidity / conductance | 22 | 5.5% | 78.6% |

The windows (±1/±3/±7/±14 days) are reported in `BIOLOGICAL_OVERLAP_WINDOWS.csv`. They increase coverage modestly but do not create intraday alignment. Same-day overlap is concentrated in summer/autumn and in 2016–2019 for Turner chlorophyll; YSI overlap is 2019–2020 only.

## 6. Depth and spatial compatibility

- Sensors: 0.5 m for chlorophyll/phycocyanin/DO/pH/conductance/turbidity/fDOM; 1 m for pCO2; 2 m above/1 m below for PAR.
- Biology: 400 dates 0–8 m composite; 2 dates 0–2 m.
- Buoy and NTL sampling coordinates are ~106 m apart; station is blank for 371/402 dates.
- A 0.5 m point measurement is not a 0–8 m composite. Depth compatibility is **weak/conditional**; atmospheric variables are not comparable.

## 7. The four scientific uses

| Use | Verdict | Core reason |
|---|---|---|
| A. Exploratory seasonal ecological analysis | **Supported with major limitations** | Multi-year daily environmental series exist, but open-water only, variable-specific gaps/flags, era changes |
| B. Descriptive comparison with microscopy cyanobacteria | **Partially supported — exploratory only** | 128–139 same-day Turner proxy dates; sparse 14-day biology; 0.5 m vs 0–8 m; RFU proxies |
| C. Multivariate environmental relationships | **Limited / not robustly supported** | Collinearity, missingness, era breaks, short 2019+ overlap, sparse biology |
| D. Early-warning evaluation | **Not supported** | No labels/events; 14-day date-only biology; depth mismatch; proxies not independent; no precursor design |

## 8. What this establishes / what remains unknown

**Establishes:** the daily entity is authentic and structurally clean; all 18 variables exist; coverage is variable- and era-specific; Turner/YSI proxies are not directly comparable; same-day biology overlap is partial; depth compatibility is weak; flags are incomplete/inconsistent; the dataset can support descriptive exploratory work.

**Unknown:** per-record calibration/accuracy; exact sensor change dates; pre-2016 DO and pre-2019 water-temperature provenance; whether flagged extremes are real or erroneous; whether 0.5 m represents the 0–8 m composite; whether a validated Turner–YSI crosswalk exists; whether taxonomy can be harmonised; any protocol-approved bloom/non-bloom definition.

## 9. Gate 2

**Gate 2 remains PAUSED / NOT APPROVED — Option C (Exploratory Only).** No bloom/non-bloom labels, event intervals, confirmatory models, hypothesis tests, protocol changes, external contacts, uploads, commits or pushes were made. Downloading and auditing the daily file does not authorise confirmatory work.

## 10. Deliverables

See `DELIVERABLES_INDEX.md` for the full map. Core outputs:

- `RAW_FILE_INTEGRITY_VERIFICATION.md`, `RAW_FILE_INTEGRITY.csv`
- `SCHEMA_AUDIT.md`, `SCHEMA_AUDIT.csv`
- `VARIABLE_COVERAGE_AUDIT.md`, `VARIABLE_COVERAGE_SUMMARY.csv`
- `ANNUAL_VARIABLE_COVERAGE.csv`, `SEASONAL_VARIABLE_COVERAGE.csv`
- `SAMPLING_INTERVALS_AND_GAPS.md`, `SAMPLING_INTERVALS_AND_GAPS.csv`, `INTERVAL_DISTRIBUTION.csv`
- `QC_FLAG_AUDIT.md`, `QC_FLAG_DISTRIBUTIONS.csv`, `QC_FLAG_TOP_YEARS.csv`, `FLAGGED_VALUE_DISTRIBUTIONS.csv`, `UNDOCUMENTED_FLAGS.csv`
- `SENSOR_ERA_COMPARABILITY.md`, `SENSOR_ERA_SUMMARY.csv`, `TURNER_YSI_OVERLAP.csv`, `SENSOR_TRANSITIONS.csv`
- `TEMPORAL_COMPATIBILITY.md`, `BIOLOGICAL_OVERLAP.csv`, `BIOLOGICAL_OVERLAP_WINDOWS.csv`, `BIOLOGICAL_OVERLAP_BY_YEAR.csv`, `BIOLOGICAL_OVERLAP_BY_SEASON.csv`
- `DEPTH_AND_SPATIAL_COMPATIBILITY.md`, `DEPTH_COMPATIBILITY.csv`
- `SCIENTIFIC_FEASIBILITY_ASSESSMENT.md`, `FEASIBILITY_MATRIX.csv`
- `EXTERNAL_SEARCH_LOG.md`, `SOURCE_REGISTER.md`, `SOURCE_REGISTER.csv`
- `VALIDATION_REPORT.md`, `VALIDATION.json`, `INDEPENDENT_VERIFICATION.md`, `INDEPENDENT_VERIFICATION.json`
- `scripts/audit_sensor_raw.py`, `scripts/verify_audit.py`, `scripts/write_reports.py`
- `summary.json`, `TABLES_INDEX.csv`, `EVIDENCE_SHA256_REGISTER.csv`, sidecar
- `SPRINT_4L9_HANDOVER.md`
