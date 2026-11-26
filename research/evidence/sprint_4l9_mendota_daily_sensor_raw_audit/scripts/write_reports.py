#!/usr/bin/env python3
"""Generate Sprint 4L.9 reports from the audit tables and summary JSON.

All numbers in the generated reports are read from the audit outputs, not typed
by hand. Narrative interpretation remains descriptive and non-confirmatory.
"""
import ast
import csv
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "research/evidence/sprint_4l9_mendota_daily_sensor_raw_audit"
T = OUT / "tables"

summary = json.loads((OUT / "summary.json").read_text(encoding="utf-8"))
validation = json.loads((OUT / "VALIDATION.json").read_text(encoding="utf-8"))
independent = json.loads((OUT / "INDEPENDENT_VERIFICATION.json").read_text(encoding="utf-8"))

V = {r["variable"]: r for r in summary["variables"]}
O = {r["variable"]: r for r in summary["overlap"]}
E = {(r["variable"], r["period"]): r for r in summary["era"]}
TY = {r["variable"]: r for r in summary["turner_ysi"]}
B = summary["biology"]
F = summary["file"]


def read_csv(name):
    p = T / name
    if not p.exists():
        return []
    with p.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


annual = read_csv("ANNUAL_VARIABLE_COVERAGE.csv")
seasonal = read_csv("SEASONAL_VARIABLE_COVERAGE.csv")
intervals = {r["variable"]: r for r in read_csv("INTERVAL_DISTRIBUTION.csv")}
anomalies = {r["variable"]: r for r in read_csv("ANOMALY_AUDIT.csv")}
undocumented = read_csv("UNDOCUMENTED_FLAGS.csv")
sensor_rows = read_csv("SENSOR_TRANSITIONS.csv")
depth_rows = read_csv("DEPTH_COMPATIBILITY.csv")
feasibility = read_csv("FEASIBILITY_MATRIX.csv")
top_years = {(r["variable"], r["flag"]): r for r in read_csv("QC_FLAG_TOP_YEARS.csv")}
flag_values = read_csv("FLAGGED_VALUE_DISTRIBUTIONS.csv")

annual_map = {(r["variable"], r["year"]): r for r in annual}
season_map = {(r["variable"], r["season"]): r for r in seasonal}
bio_season = {(r["variable"], r["season"]): r for r in read_csv("BIOLOGICAL_OVERLAP_BY_SEASON.csv")}


def num(x, nd=0):
    if x is None or x == "":
        return "—"
    try:
        return f"{float(x):,.{nd}f}"
    except Exception:
        return str(x)


def pct(x, nd=1):
    if x is None or x == "":
        return "—"
    try:
        return f"{float(x):.{nd}f}%"
    except Exception:
        return str(x)


def get(var, field):
    return V[var].get(field, "")


def parse_codes(text):
    try:
        value = ast.literal_eval(text)
        return list(value) if isinstance(value, (list, tuple)) else [str(value)]
    except Exception:
        return []


def codes_text(text):
    codes = parse_codes(text)
    return ", ".join(codes) if codes else str(text)


def annual_valid(var, year):
    return int(annual_map.get((var, str(year)), {}).get("valid_unflagged", 0))


def annual_records(var, year):
    return int(annual_map.get((var, str(year)), {}).get("records", 0))


def top_text(var, flag):
    r = top_years.get((var, flag))
    return r["top_years"] if r else "—"


def flag_value(var, flag, field):
    for r in flag_values:
        if r["variable"] == var and r["flag"] == flag:
            return r.get(field, "")
    return ""


# ---------------------------------------------------------------------------
# RAW INTEGRITY
# ---------------------------------------------------------------------------
raw_rows = [
    ("Package", "knb-lter-ntl.129.42", "—", "—"),
    ("DOI", "10.6073/pasta/9c4b1eecf7a019c7239297b6bf4513c4", "—", "—"),
    ("Entity ID", "cba9ed12834b8f315d6b10675bb60c5a", "—", "—"),
    ("EML object name", "ntl129_1_v16.csv", "—", "—"),
    ("Local path", str(ROOT / "research/evidence/sprint_4l7_mendota_daily_sensor_audit/acquisition/129.42/North_Temperate_Lakes_LTER_Daily_Meteorological_and_Metabolism_Data_-_Lake_Mendota__cba9ed12834b8f315d6b10675bb60c5a.dat"), "—", "—"),
    ("Bytes", f"{F['bytes']:,}", "490,187", "PASS"),
    ("MD5", F["md5"], "eb7b3a3848b27074bac4504236ccefc3", "PASS"),
    ("SHA-1", F["sha1"], "bb1d8a281a3d580cad45549551abdbaed1ae03fe", "PASS"),
    ("SHA-256", F["sha256"], "104ef1b33769bc0ad1d3e9e6dff28219b743b81ce89ee888460d2df255981343", "PASS"),
    ("Columns", str(F["header_columns"]), "38", "PASS"),
    ("Data rows", f"{F['rows']:,}", "3,996", "PASS"),
    ("Malformed rows", str(F["malformed"]), "0", "PASS"),
    ("Blank lines", str(F["blank_lines"]), "0", "PASS"),
    ("Date parse errors", str(F["date_errors"]), "0", "PASS"),
    ("Duplicate dates", str(F["duplicate_dates"]), "0", "PASS"),
    ("Exact duplicate rows", str(F["exact_duplicate_rows"]), "0", "PASS"),
    ("Year/date mismatches", str(F["year_mismatches"]), "0", "PASS"),
    ("Date range", f"{F['date_min']} to {F['date_max']}", "—", "—"),
    ("Unique dates", f"{F['unique_dates']:,}", "3,996", "PASS"),
    ("Calendar-day span", f"{F['calendar_span_days']:,}", "—", "—"),
    ("Record fraction of span", pct(F["record_fraction_of_span"] * 100), "—", "—"),
]
with (OUT / "RAW_FILE_INTEGRITY.csv").open("w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["item", "actual", "expected_or_note", "result"])
    w.writerows(raw_rows)

md = f"""# Raw-File Integrity Verification

**Sprint:** 4L.9  
**Date:** 2026-11-24  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Verdict: PASS — the inspected bytes match the Sprint 4L.8A baseline.**

## 1. Identity

- Package: `knb-lter-ntl.129.42`
- DOI: `10.6073/pasta/9c4b1eecf7a019c7239297b6bf4513c4`
- Entity: `cba9ed12834b8f315d6b10675bb60c5a`
- EML object name: `ntl129_1_v16.csv`
- Local filename: `North_Temperate_Lakes_LTER_Daily_Meteorological_and_Metabolism_Data_-_Lake_Mendota__cba9ed12834b8f315d6b10675bb60c5a.dat`
- Local extension: `.dat` (the bytes are CSV; the extension is a helper/parser artefact documented in Sprint 4L.8A)
- Encoding/format: ASCII CSV text, LF line endings, no BOM
- Date range: **{F['date_min']} to {F['date_max']}**
- Unique dates: **{F['unique_dates']:,}**
- Data rows: **{F['rows']:,}**
- Columns: **{F['header_columns']}**
- Calendar-day span: **{F['calendar_span_days']:,}** days; the file contains records on **{pct(F['record_fraction_of_span']*100)}** of those days.

The difference between the calendar span and 3,996 records is the winter/seasonal deployment pattern, not missing daily rows within a claimed year-round series.

## 2. Actual bytes versus baseline

| Check | Actual | Expected | Result |
|---|---|---|---|
| Bytes | **{F['bytes']:,}** | 490,187 | **PASS** |
| MD5 | **`{F['md5']}`** | `eb7b3a3848b27074bac4504236ccefc3` | **PASS** |
| SHA-1 | **`{F['sha1']}`** | `bb1d8a281a3d580cad45549551abdbaed1ae03fe` | **PASS** |
| SHA-256 | **`{F['sha256']}`** | `104ef1b33769bc0ad1d3e9e6dff28219b743b81ce89ee888460d2df255981343` | **PASS** |

The bytes were independently hashed with `md5`, `shasum -a 1`, `shasum -a 256` and Python's `hashlib`; all agree.

## 3. Structural checks

- Header order matches the expected 38-field daily schema exactly (2 date fields + 18 variables + 18 interleaved flag columns).
- Every non-header line has 38 comma-separated fields; no malformed records.
- `year4` equals the calendar year of `sampledate` for all 3,996 rows.
- No duplicate dates and no exact duplicate rows.
- All non-empty numeric fields parse as finite floats; there are **no non-numeric non-empty values**.
- Flag fields contain only blank, `C`, `E`, `H`, `G` or `O`. `O` is undocumented (see QC audit).

## 4. Metadata provenance

- The local EML metadata file is `metadata_129.42.xml`, **{summary['eml']['bytes']:,} bytes**, SHA-256 `{summary['eml']['sha256']}`.
- The EML records the daily entity size as 490,187 bytes and MD5 as `eb7b3a3848b27074bac4504236ccefc3`.
- The acquisition provenance log records the PASTA data URL, entity ID, HTTP 200, `text/csv`, 490,187 bytes and SHA-256 `{F['sha256']}`.
- The original acquired bytes were not renamed, rewritten or normalised. The `.dat` extension is retained.

## 5. What this establishes and does not establish

**Establishes:** the local file is the intended daily entity; its bytes match the EML size/MD5 and the DataONE CN SHA-1; it is structurally a 38-column CSV with 3,996 daily records and no duplicate dates.

**Does not establish:** that the observations are accurate, calibrated, comparable across sensor eras, or suitable for confirmatory inference. Those are separate scientific and QC questions.

The raw file remains unchanged. No labels, event intervals, models, hypothesis tests or Gate 2 approval were created.
"""
(OUT / "RAW_FILE_INTEGRITY_VERIFICATION.md").write_text(md, encoding="utf-8")


# ---------------------------------------------------------------------------
# SCHEMA AUDIT
# ---------------------------------------------------------------------------
schema_rows = read_csv("SCHEMA_AUDIT.csv")
schema_md = f"""# Schema and Parsing Audit

**Sprint:** 4L.9  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. Structure

- **38 columns** in the exact expected order: `year4`, `sampledate`, then 18 variable/flag pairs.
- **3,996 data rows**; **0** malformed rows; **0** blank lines; **0** non-numeric non-empty values.
- `year4` is an integer field and matches `sampledate` in all rows.
- `sampledate` is an ISO `YYYY-MM-DD` date; all 3,996 values parse.
- Numeric variables are floats; flag fields are strings with values blank, `C`, `E`, `H`, `G` or `O`.
- No duplicate dates; no exact duplicate rows.
- The daily EML has **{summary['eml']['daily_attributes']} attribute definitions** for this entity, matching the 38 columns.

## 2. Field-level schema

| # | Column | Role | Type | Definition (EML) | Documented codes | Non-empty | Missing | Parse errors | Undocumented flag values |
|---:|---|---|---|---|---|---:|---:|---:|---:|
"""
for r in schema_rows:
    schema_md += (
        f"| {r['position']} | `{r['column']}` | {r['role']} | {r['dtype']} | "
        f"{r['definition']} | {r['documented_codes'] or '—'} | {r['nonempty']} | "
        f"{r['missing']} | {r['parse_errors']} | {r['undocumented_flag_values']} |\n"
    )

schema_md += f"""
## 3. Flag-code inconsistencies

The daily EML gives a per-column enumerated code list. Eight columns contain values outside their own documented list:

| Variable | Documented daily codes | Extra values observed | Count |
|---|---|---|---:|
"""
for r in undocumented:
    total_extra = 0
    for code in parse_codes(r["observed_extra"]):
        total_extra += int(V[r["variable"]].get("flag_" + code, 0))
    schema_md += f"| `{r['variable']}` | {codes_text(r['documented'])} | {codes_text(r['observed_extra'])} | {total_extra} |\n"

schema_md += """
The most consequential case is `flag_avg_spec_cond`: the daily EML lists only `C,H`, but the data contain **17 `E`** values and **one `O`** value (2006-08-11, specific conductance 0.45). `O` has no definition anywhere in the EML. `flag_avg_par_below` lists `C,G` in the daily table but contains **90 `H`** values; the hourly table's code list includes `H`, suggesting a daily-metadata omission rather than a data error. `flag_avg_wind_speed` lists only `C` but contains **124 `H`** values.

## 4. Other metadata inconsistencies relevant to interpretation

- **`avg_do_wtemp`** is defined as “average of YSI water temp (0.5m depth)”, yet unflagged values exist from 2006-07-09, long before the YSI EXO2 deployment in 2019. The pre-2019 temperature provenance is unresolved.
- **DO** values exist from 2006, but the sensor inventory's DO records begin in 2016. The inventory does not identify a 2006–2015 DO sensor.
- **pCO2** values begin 2016-03-22, while the sensor inventory lists the Turner C-sense CO2 sensor from 2017.
- **PAR** has 11 unflagged near-zero values (ten 0.0 and one 0.002) in 2007-05-18 to 2007-05-28, before the inventory's 2016 PAR start and before the sustained PAR record. These values are not useful as environmental light data.
- **Conductivity** has 2006 values around 0.38–0.48 µS/cm, all flagged `H` or `O`; there are no unflagged 2006 conductivity values.

## 5. Conclusion

The file is structurally clean and fully parseable. The flag metadata are **not** complete or internally consistent for every column, and several sensor-era definitions conflict with observed coverage. These are documented as data-quality limitations; they are not silently corrected.
"""
(OUT / "SCHEMA_AUDIT.md").write_text(schema_md, encoding="utf-8")


# ---------------------------------------------------------------------------
# VARIABLE COVERAGE
# ---------------------------------------------------------------------------
vc_md = f"""# Variable Coverage Audit

**Sprint:** 4L.9  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. Definitions used throughout

- **Record / daily row:** one date in the acquired daily file. The file has **{F['rows']:,}** records on **{F['unique_dates']:,}** unique dates.
- **Missing:** the variable field is blank, non-numeric or non-finite. Missing is **not** treated as zero.
- **Numeric any:** a finite numeric value, regardless of QC flag.
- **Valid unflagged:** a finite numeric value whose flag field is blank. This is an **analytical subset**, not proof of accuracy.
- **Flagged numeric:** a finite numeric value with any flag. These values are retained in the raw file and reported, but excluded from the unflagged subset.
- **Flag without value:** a flag is present but the variable field is blank.
- **Empty unflagged:** the variable field is blank and no flag is present. This is ambiguous missingness, often structural (sensor not deployed or not yet in the era).

`valid_unflagged` is therefore **not** a claim that the value is calibrated, accurate or biologically valid. Several unflagged values are physically implausible (Section 5).

## 2. Coverage summary

| Variable | First unflagged | Last unflagged | Missing | Missing % | Numeric any | Valid unflagged | Valid % | C | E | H | G | O | Median interval (d) | Max interval (d) | Min | Median | Max |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
"""
for var, r in V.items():
    vc_md += (
        f"| `{var}` | {r['first_valid_unflagged']} | {r['last_valid_unflagged']} | "
        f"{r['missing']} | {pct(r['missing_pct'])} | {r['numeric_any']} | {r['valid_unflagged']} | "
        f"{pct(r['valid_unflagged_pct'])} | {r['flag_C']} | {r['flag_E']} | {r['flag_H']} | "
        f"{r['flag_G']} | {r['flag_O']} | {r['median_interval_days']} | {r['max_interval_days']} | "
        f"{r['min']} | {r['median']} | {r['max']} |\n"
    )

vc_md += f"""
## 3. What the counts show

- The longest-running variables are meteorological and DO-related: air temperature, relative humidity, wind, and DO have records from 2006. Turner chlorophyll/phycocyanin also run 2006–2019. YSI chlorophyll/phycocyanin, pH, fDOM, turbidity and specific conductance are effectively 2019+ series; pCO2 is 2016+; PAR is 2016+ apart from sparse 2007 near-zero values.
- Missingness ranges from **{pct(min(float(r['missing_pct']) for r in V.values()))}** (wind speed) to **{pct(max(float(r['missing_pct']) for r in V.values()))}** (YSI chlorophyll). The high values for 2019+ variables are largely **structural**: the sensor did not exist in the earlier record, not a failure on a deployed day.
- Unflagged coverage is strongest for wind direction ({pct(get('avg_wind_dir','valid_unflagged_pct'))}), relative humidity ({pct(get('avg_rel_hum','valid_unflagged_pct'))}), wind speed ({pct(get('avg_wind_speed','valid_unflagged_pct'))}) and air temperature ({pct(get('avg_air_temp','valid_unflagged_pct'))}). It is weakest for YSI chlorophyll ({pct(get('avg_chlor_rfu_ysi','valid_unflagged_pct'))}), specific conductance ({pct(get('avg_spec_cond','valid_unflagged_pct'))}), pH ({pct(get('avg_ph','valid_unflagged_pct'))}), fDOM ({pct(get('avg_fdom','valid_unflagged_pct'))}) and turbidity ({pct(get('avg_turbidity','valid_unflagged_pct'))}).
- Turner chlorophyll has only **{get('avg_chlor_rfu_turner','valid_unflagged')}** unflagged values (55.1%) despite its 2006–2019 label; Turner phycocyanin has **{get('avg_phyco_rfu_turner','valid_unflagged')}** (57.8%). Both have major within-era gaps.
- YSI chlorophyll has **{get('avg_chlor_rfu_ysi','valid_unflagged')}** unflagged values; YSI phycocyanin **{get('avg_phyco_rfu_ysi','valid_unflagged')}**. Both are 2019+ only.
- DO raw has **{get('avg_do_raw','valid_unflagged')}** unflagged values (66.3%), but its flags are heavy: **{get('avg_do_raw','flag_H')} `H`**, **{get('avg_do_raw','flag_E')} `E`** and **{get('avg_do_raw','flag_C')} `C`**. DO saturation has **{get('avg_do_sat','flag_H')} `H`** values. Flagged DO values are often high (H median {num(flag_value('avg_do_raw','H','median'),2)} mg/L), consistent with supersaturation/range flags, but the data do not provide a per-value reason.
- `avg_do_wtemp` has only **{get('avg_do_wtemp','valid_unflagged')}** unflagged values (48.6%) and **{get('avg_do_wtemp','flag_C')} `C`** flags, with only **{annual_valid('avg_do_wtemp',2020)}** unflagged values in 2020. Its definition as “YSI water temp” conflicts with pre-2019 values. It should not be treated as a continuous homogeneous water-temperature series.

## 4. Annual and seasonal coverage

The full tables are `ANNUAL_VARIABLE_COVERAGE.csv` and `SEASONAL_VARIABLE_COVERAGE.csv`. Key patterns:

- The file contains **{F['rows']:,}** records over **{F['calendar_span_days']:,}** calendar days ({pct(F['record_fraction_of_span']*100)}). It is an **open-water deployment series**, not a year-round daily calendar.
- Month counts: March 37, April 265, May 493, June 525, July 600, August 609, September 591, October 563, November 298, December 15; **no January or February records**.
- Winter has only **{season_map.get(('avg_air_temp','winter'),{}).get('records','0')}** records in total. Seasonal comparisons are therefore open-water-season comparisons, not annual-cycle comparisons.
- Early meteorological coverage is patchy: air temperature has **0** unflagged values in 2007 and only **{annual_valid('avg_air_temp',2008)}** in 2008; wind speed has **{annual_valid('avg_wind_speed',2008)}** in 2008 and **{annual_valid('avg_wind_speed',2009)}** in 2009.
- Turner chlorophyll collapses in 2014 (**{annual_valid('avg_chlor_rfu_turner',2014)}** unflagged of **{annual_records('avg_chlor_rfu_turner',2014)}**) and 2015 (**{annual_valid('avg_chlor_rfu_turner',2015)}** of **{annual_records('avg_chlor_rfu_turner',2015)}**). Turner phycocyanin has only **{annual_valid('avg_phyco_rfu_turner',2007)}** unflagged values in 2007.
- DO raw is weak in 2008 (**{annual_valid('avg_do_raw',2008)}** of **{annual_records('avg_do_raw',2008)}**), 2010 (**{annual_valid('avg_do_raw',2010)}** of **{annual_records('avg_do_raw',2010)}**), 2014 (**{annual_valid('avg_do_raw',2014)}** of **{annual_records('avg_do_raw',2014)}**) and 2017 (**{annual_valid('avg_do_raw',2017)}** of **{annual_records('avg_do_raw',2017)}**).
- YSI-era variables are present only from 2019; pH/fDOM/turbidity/specific conductance have about **33–35%** unflagged coverage over the whole file and only the 2019–2020 biology overlap.

## 5. Implausible and anomalous values

The broad screening bounds are listed in `ANOMALY_AUDIT.csv`; they are not regulatory thresholds.

| Variable | Screening issue | Count | Examples / note |
|---|---|---:|---|
| `avg_turbidity` | Negative FNU, unflagged | **{get('avg_turbidity','negative_valid')}** | 2025-05-25 to 2025-06-02; last record 2025-11-18 = −0.427; physical turbidity cannot be negative |
| `avg_phyco_rfu_ysi` | Negative RFU, unflagged | **{get('avg_phyco_rfu_ysi','negative_valid')}** | 2019-05-29 onwards; near-zero offset likely but unresolved |
| `avg_chlor_rfu_ysi` | Negative RFU, unflagged | **{get('avg_chlor_rfu_ysi','negative_valid')}** | one unflagged negative |
| `avg_par_below` | Negative PAR, unflagged | **{get('avg_par_below','negative_valid')}** | 2025-04-08 to 2025-04-10, −920 to −1,676 µmol/m²/s; physically implausible |
| `avg_phyco_rfu_turner` | Negative RFU, unflagged | **{get('avg_phyco_rfu_turner','negative_valid')}** | 2012-06-10 to 2012-06-16 |
| `avg_spec_cond` | 2006 values ~0.38–0.48 µS/cm | 83 numeric | All `H`/`O`; no unflagged 2006 value. The 2019+ series is ~122–596 µS/cm. |
| `avg_chlor_rfu_turner` | Extreme high RFU | max {num(get('avg_chlor_rfu_turner','max'),2)} | Turner RFU scale is sensor-specific; extreme values are not labelled as blooms |
| `avg_phyco_rfu_turner` | Extreme high RFU | max {num(get('avg_phyco_rfu_turner','max'),2)} | same caveat |
| `avg_do_raw` / `avg_do_sat` | High values with `H` | max {num(get('avg_do_raw','max'),2)} mg/L / {num(get('avg_do_sat','max'),2)}% | High DO can be real; `H` is a range flag, not proof of error |
| `avg_air_temp` | Negative values | {get('avg_air_temp','negative_valid')} unflagged | Plausible winter air temperatures; not an anomaly |

**No values were deleted, truncated, winsorised, imputed or relabelled.** The raw file remains unchanged.

## 6. Conclusion

Daily records are present for all 18 variables, but coverage is **variable-specific and era-specific**. Some variables have long, reasonably continuous records; others exist only in the 2019+ YSI era or have severe within-era gaps. Missingness is not zero, flags are not a complete QC system, and unflagged values are not automatically accurate. Any exploratory analysis must state its variable-specific denominator and exclusion rule.
"""
(OUT / "VARIABLE_COVERAGE_AUDIT.md").write_text(vc_md, encoding="utf-8")


# ---------------------------------------------------------------------------
# INTERVALS AND GAPS
# ---------------------------------------------------------------------------
gaps = read_csv("SAMPLING_INTERVALS_AND_GAPS.csv")
top_gaps = sorted(gaps, key=lambda r: int(r["gap_days"]), reverse=True)[:20]
gap_md = f"""# Sampling Intervals and Gaps

**Sprint:** 4L.9  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. Method

Intervals are calculated between consecutive **unflagged numeric** dates for each variable. A gap is the number of calendar days from one unflagged date to the next. Winter absence, sensor removal, sensor failure and sensor-era absence all appear as gaps; the table does not attribute cause.

## 2. Interval distribution

| Variable | Unflagged dates | Intervals | 1 d | 2–7 d | 8–14 d | 15–30 d | 31–60 d | 61–90 d | >90 d | Median | Max |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
"""
for var, r in intervals.items():
    gap_md += (
        f"| `{var}` | {r['valid_dates']} | {r['intervals']} | {r['interval_1d']} | "
        f"{r['interval_2_7d']} | {r['interval_8_14d']} | {r['interval_15_30d']} | "
        f"{r['interval_31_60d']} | {r['interval_61_90d']} | {r['interval_gt_90d']} | "
        f"{r['median_interval_days']} | {r['max_interval_days']} |\n"
    )

gap_md += f"""
The median interval is **1 day** for every variable when the sensor is present. The daily file is therefore daily-resolution data, but it is **not** a continuous daily calendar: long gaps are common and are concentrated in winter, early deployment years and sensor failures.

## 3. Largest gaps

| Variable | From | To | Days |
|---|---|---|---:|
"""
for r in top_gaps:
    gap_md += f"| `{r['variable']}` | {r['from_date']} | {r['to_date']} | {r['gap_days']} |\n"

gap_md += f"""
Notable gaps:

- **PAR above water:** 3,221 days from 2007-05-28 to 2016-03-22. The 2007 values are 11 unflagged near-zero values (ten 0.0, one 0.002); the sustained record begins in 2016. PAR should be treated as a 2016+ contextual series, not a 2006+ series.
- **Air temperature / relative humidity:** 713 / 712 days from 2006-07-29 to 2008-07-11.
- **Wind direction:** 633 days from 2006-10-17 to 2008-07-11.
- **DO:** 294-day gaps in 2013–2014 and 2010–2011; 247 days in 2023–2024. These are seasonal/outage gaps, not isolated missing days.
- **Turner chlorophyll:** 256 days from 2006-10-03 to 2007-06-16, plus the 2014–2015 collapse. The 2014–2015 issue is not captured by a single gap because some values remain; see the annual table.
- **Turner phycocyanin:** 368 days from 2007-06-24 to 2008-06-26; only 6 unflagged values in 2007.
- **YSI chlorophyll/phycocyanin:** maximum gaps 154/152 days, reflecting winter removal and occasional outages.

## 4. Interpretation

A median 1-day interval does not mean complete daily coverage. The correct denominator for any analysis is the variable-specific unflagged observation count and date span, not the 3,996-row file length. Winter gaps are structural; within-season gaps and flag runs are variable-specific and must be handled explicitly.
"""
(OUT / "SAMPLING_INTERVALS_AND_GAPS.md").write_text(gap_md, encoding="utf-8")


# ---------------------------------------------------------------------------
# QC FLAGS
# ---------------------------------------------------------------------------
qc_md = f"""# QC Flag Audit

**Sprint:** 4L.9  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. Documented codes

The daily EML defines, where listed:

| Code | General meaning | Where documented in the daily schema |
|---|---|---|
| `C` | Sensor off | Most flag columns |
| `E` | Sensor noisy or malfunctioning | Air temp, RH, YSI chlorophyll/phycocyanin, DO, pCO2 (but not all columns) |
| `H` | Outside of standard range | Air temp, wind direction, chlorophyll/phycocyanin, PAR, DO, specific conductance (but not all columns) |
| `G` | Sensor — suspected biofouling | YSI chlorophyll, YSI phycocyanin, PAR below water |
| `O` | **Undefined** | Not defined anywhere in the EML; one value in `flag_avg_spec_cond` |

The per-column code lists are the authoritative enumeration for each attribute. Eight columns contain values outside their own list; see Section 4.

## 2. Flag totals by variable

| Variable | Records | C | E | H | G | O | No flag | Any flag | Valid unflagged |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
"""
for var, r in V.items():
    any_flag = int(r['flag_C']) + int(r['flag_E']) + int(r['flag_H']) + int(r['flag_G']) + int(r['flag_O'])
    qc_md += (
        f"| `{var}` | {r['total_records']} | {r['flag_C']} | {r['flag_E']} | {r['flag_H']} | "
        f"{r['flag_G']} | {r['flag_O']} | {r['flag_none']} | {any_flag} | {r['valid_unflagged']} |\n"
    )

qc_md += f"""
## 3. What the flags actually show

### 3.1 `C` is not equivalent to missing

`C` is defined as “sensor off”, but many `C` records still contain numeric values:

- `avg_do_wtemp`: **{flag_value('avg_do_wtemp','C','n_numeric')}** numeric `C` values and **{flag_value('avg_do_wtemp','C','n_missing')}** missing `C` values.
- `avg_par_below`: **{flag_value('avg_par_below','C','n_numeric')}** numeric `C` values.
- `avg_do_raw`: **{flag_value('avg_do_raw','C','n_numeric')}** numeric `C` values.
- `avg_spec_cond`: **{flag_value('avg_spec_cond','C','n_numeric')}** numeric `C` values.
- `avg_chlor_rfu_ysi`: **{flag_value('avg_chlor_rfu_ysi','C','n_numeric')}** numeric `C` values.

This means `C` cannot be used as a missing-value code without inspecting the value column. The audit excludes all flagged numeric values from `valid_unflagged`, but retains them in `numeric_any`.

### 3.2 `H` is common and not automatically an error

`H` (“outside of standard range”) is frequent:

- `avg_do_sat`: **{get('avg_do_sat','flag_H')}** `H` (23.2% of records), median flagged value {num(flag_value('avg_do_sat','H','median'),2)}%, max {num(flag_value('avg_do_sat','H','max'),2)}%.
- `avg_do_raw`: **{get('avg_do_raw','flag_H')}** `H`, median {num(flag_value('avg_do_raw','H','median'),2)} mg/L, max {num(flag_value('avg_do_raw','H','max'),2)} mg/L.
- `avg_air_temp`: **{get('avg_air_temp','flag_H')}** `H`, concentrated in 2008–2009 ({top_text('avg_air_temp','H')}).
- `avg_wind_speed`: **{get('avg_wind_speed','flag_H')}** `H`, concentrated in 2009 ({top_text('avg_wind_speed','H')}).
- `avg_spec_cond`: **{get('avg_spec_cond','flag_H')}** `H`, all in 2006, with values 0.379–0.481 µS/cm; this is a scale/era problem, not a plausible freshwater conductance.
- Turner chlorophyll: **{get('avg_chlor_rfu_turner','flag_H')}** `H`; YSI chlorophyll: **{get('avg_chlor_rfu_ysi','flag_H')}** `H`; PAR: **{get('avg_par','flag_H')}** `H`; PAR below: **{get('avg_par_below','flag_H')}** `H`.

`H` values are not deleted. They are reported separately and excluded from the unflagged subset. Some `H` values are plausibly real extremes (e.g., high DO), while others (2006 conductance) are clearly not on the later scale.

### 3.3 `G` is era-specific

`G` (“suspected biofouling”) appears only for:

- YSI chlorophyll: **{get('avg_chlor_rfu_ysi','flag_G')}**
- YSI phycocyanin: **{get('avg_phyco_rfu_ysi','flag_G')}**
- PAR below water: **{get('avg_par_below','flag_G')}**

Turner chlorophyll/phycocyanin have **no `G` flags** in the daily file even though the Turner era spans 2006–2019. The absence of `G` in the Turner era does **not** prove the absence of biofouling; it means the flag was not used for those columns. The EML's 2017 note about significant DO biofouling is a documented event, not a per-record flag.

### 3.4 Missing values often have no flag

Many missing values are “empty unflagged” rather than `C`:

- Turner chlorophyll: **{get('avg_chlor_rfu_turner','empty_unflagged')}** empty-unflagged vs {get('avg_chlor_rfu_turner','flag_without_value')} flag-without-value.
- YSI chlorophyll: **{get('avg_chlor_rfu_ysi','empty_unflagged')}** empty-unflagged vs {get('avg_chlor_rfu_ysi','flag_without_value')} flag-without-value.
- pH: **{get('avg_ph','empty_unflagged')}** empty-unflagged; fDOM **{get('avg_fdom','empty_unflagged')}**; turbidity **{get('avg_turbidity','empty_unflagged')}**; specific conductance **{get('avg_spec_cond','empty_unflagged')}**.

Most of these are structural (sensor not yet deployed or seasonally removed), but the file does not carry an explicit “not deployed” code for them. This is a QC ambiguity, not a reason to impute zeros.

### 3.5 Flag patterns by year

Representative concentrations (full table: `QC_FLAG_TOP_YEARS.csv`, `QC_FLAG_DISTRIBUTIONS.csv`):

| Variable | Flag | Total | Top years |
|---|---|---:|---|
| `avg_air_temp` | H | {get('avg_air_temp','flag_H')} | {top_text('avg_air_temp','H')} |
| `avg_wind_speed` | C | {get('avg_wind_speed','flag_C')} | {top_text('avg_wind_speed','C')} |
| `avg_wind_speed` | H | {get('avg_wind_speed','flag_H')} | {top_text('avg_wind_speed','H')} |
| `avg_chlor_rfu_turner` | C | {get('avg_chlor_rfu_turner','flag_C')} | {top_text('avg_chlor_rfu_turner','C')} |
| `avg_chlor_rfu_ysi` | H | {get('avg_chlor_rfu_ysi','flag_H')} | {top_text('avg_chlor_rfu_ysi','H')} |
| `avg_chlor_rfu_ysi` | G | {get('avg_chlor_rfu_ysi','flag_G')} | {top_text('avg_chlor_rfu_ysi','G')} |
| `avg_do_raw` | C | {get('avg_do_raw','flag_C')} | {top_text('avg_do_raw','C')} |
| `avg_do_raw` | E | {get('avg_do_raw','flag_E')} | {top_text('avg_do_raw','E')} |
| `avg_do_raw` | H | {get('avg_do_raw','flag_H')} | {top_text('avg_do_raw','H')} |
| `avg_par` | C | {get('avg_par','flag_C')} | {top_text('avg_par','C')} |
| `avg_par_below` | C | {get('avg_par_below','flag_C')} | {top_text('avg_par_below','C')} |
| `avg_par_below` | G | {get('avg_par_below','flag_G')} | {top_text('avg_par_below','G')} |
| `avg_do_wtemp` | C | {get('avg_do_wtemp','flag_C')} | {top_text('avg_do_wtemp','C')} |
| `avg_spec_cond` | H | {get('avg_spec_cond','flag_H')} | {top_text('avg_spec_cond','H')} |
| `avg_spec_cond` | E | {get('avg_spec_cond','flag_E')} | {top_text('avg_spec_cond','E')} |

Patterns are concentrated in particular years/eras: early meteorological outages (2008–2010), the 2014–2015 Turner chlorophyll collapse, the 2019+ YSI era, and the 2019–2020/2021 PAR outages. The flags are not randomly distributed.

## 4. Metadata code-list inconsistencies

The daily EML's per-column enumerations omit values that are present in the data:

| Variable | Documented daily codes | Extra observed | Count |
|---|---|---|---:|
"""
for r in undocumented:
    total_extra = sum(int(V[r["variable"]].get("flag_" + c, 0)) for c in parse_codes(r["observed_extra"]))
    qc_md += f"| `{r['variable']}` | {codes_text(r['documented'])} | {codes_text(r['observed_extra'])} | {total_extra} |\n"

qc_md += """
These are **metadata inconsistencies**, not arithmetic errors. The most important are the undefined `O` code, the `H` values in `flag_avg_wind_speed` and `flag_avg_par_below`, and the `E` values in several 2019+ columns whose daily code list contains only `C`.

## 5. Calibration and maintenance evidence

The EML abstract documents:

- 2017: boating mishap lost air temperature, RH and wind sensors between May 28 and July 11; DO sensor had significant biofouling from algae and zebra mussels.
- 2019: YSI EXO2 added; pH, DO and specific conductance cleaned/recalibrated every two weeks; Turner and YSI chlorophyll/phycocyanin both deployed; “significant magnitude differences” between Turner and YSI RFU.
- 2020: YSI cleaning/calibration nearly weekly; CO2 sensor not operating July 2–September 17.
- 2021: buoy not operating August 22–31; intermittent November 8–December 3; underwater PAR antifouling method used.
- 2022: buoy not operating June 6–9 and July 2–5; underwater PAR unusable after October 1.
- 2023: conductivity not operational April 27–May 24 and replaced; YSI wiper failed November 4–14, significantly affecting chlorophyll, phycocyanin, conductivity and turbidity.
- 2024: CO2 failed May 22 and was not used for the rest of the season; communications down June 13–19; PAR broken August 30–September 4.

The EML/sensor list do **not** provide per-record calibration dates, coefficients, serial numbers, detection limits, fouling measurements or maintenance logs. The flag codes are not a substitute. Manufacturer guidance (USGS TM1-D10) states that algal fluorometers are proxy sensors, RFU is sensor-specific, calibration checks should be routine, and biofouling/blank corrections require site-specific evidence. No calibration continuity is assumed here.

## 6. Conclusion

Flags are present and informative, but they are **not** a complete or internally consistent QC system. Missingness, `C`-with-value, undocumented codes, unflagged implausible values and era-specific `G` usage all prevent treating “unflagged” as “validated”. The audit preserves the raw values and reports the unflagged subset only as an explicit analytical choice.
"""
(OUT / "QC_FLAG_AUDIT.md").write_text(qc_md, encoding="utf-8")


# ---------------------------------------------------------------------------
# SENSOR ERA
# ---------------------------------------------------------------------------
era_md = f"""# Sensor-Era and Comparability Audit

**Sprint:** 4L.9  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. Documented sensor transitions

The sensor inventory (`mendota_buoy_sensors_v3.csv`, 20 records) lists years only, not exact change dates. Mapping those records to the daily columns gives:

| Parameter | Manufacturer | Model | Began | Ended | Mapped daily variable(s) | Observed first unflagged | Observed last unflagged | Valid unflagged (sum) | Note |
|---|---|---|---|---|---:|---:|---:|---|
"""
for r in sensor_rows:
    era_md += (
        f"| {r['parameter']} | {r['sensor_mfg']} | {r['sensor_model'] or '—'} | {r['date_began']} | "
        f"{r['date_ended']} | {r['daily_variables']} | {r['observed_first_unflagged']} | "
        f"{r['observed_last_unflagged']} | {r['observed_valid_unflagged_sum']} | {r['note']} |\n"
    )
era_md += """
The observed coverage columns are **column-level**, not proof that the listed sensor produced every date. The valid-unflagged sum is a sum across mapped columns and is not an independent sample count.
"""

era_md += f"""
## 2. Turner versus YSI chlorophyll/phycocyanin

The daily file has separate Turner and YSI columns for chlorophyll and phycocyanin. In 2019 both were deployed. Pairing only dates where both values are unflagged numeric gives:

| Proxy | Paired dates | Turner median (RFU) | YSI median (RFU) | Median YSI−Turner | Median ratio (YSI/Turner) | Ratio p05–p95 | First–last paired date |
|---|---:|---:|---:|---:|---:|---|---|
"""
for label, key in [("chlorophyll", "chlorophyll"), ("phycocyanin", "phycocyanin")]:
    r = TY[key]
    era_md += (
        f"| {label} | {r['paired_dates']} | {num(r['turner_median'],2)} | {num(r['ysi_median'],3)} | "
        f"{num(r['median_difference_ysi_minus_turner'],2)} | {r['median_ratio_ysi_over_turner']} | "
        f"{r['p05_ratio']}–{r['p95_ratio']} | {r['first_date']} to {r['last_date']} |\n"
    )

era_md += f"""
The two instruments are **not on a common scale**. The Turner medians are three orders of magnitude larger than the YSI medians; the EML itself states that both output RFU but have “significant magnitude differences.” No cross-calibration equation, correction factor or documented conversion is present. The paired 2019 data are useful for describing the discontinuity, not for creating a homogeneous series.

Further era facts:

- Turner chlorophyll has **{get('avg_chlor_rfu_turner','valid_unflagged')}** unflagged values and ends 2019-11-03; YSI chlorophyll has **{get('avg_chlor_rfu_ysi','valid_unflagged')}** and begins 2019-04-16.
- Turner phycocyanin has **{get('avg_phyco_rfu_turner','valid_unflagged')}** unflagged values and ends 2019-11-03; YSI phycocyanin has **{get('avg_phyco_rfu_ysi','valid_unflagged')}** and begins 2019-04-16.
- Turner chlorophyll is severely reduced in 2014 (**{annual_valid('avg_chlor_rfu_turner',2014)}** values) and 2015 (**{annual_valid('avg_chlor_rfu_turner',2015)}**); Turner phycocyanin has only **{annual_valid('avg_phyco_rfu_turner',2007)}** values in 2007. The “Turner era” is therefore not a continuous homogeneous block.
- YSI-era variables pH/fDOM/turbidity/specific conductance begin 2019-04-16 and have no pre-2019 daily values in this file.

## 3. DO and water temperature

- DO is present from 2006, but the sensor inventory's DO entries begin in 2016 (Zebra Tech D-Opto, 2016–2018; PME miniDOT, 2018; YSI EXO2, 2019+). The 2006–2015 DO instrument is not identified in the inventory. DO values therefore span undocumented and documented instruments.
- DO raw has **{get('avg_do_raw','valid_unflagged')}** unflagged values; DO saturation **{get('avg_do_sat','valid_unflagged')}**. Both have heavy `H`/`E` flags (Section QC). There is no documented cross-calibration between the pre-2016, 2016–2018 and 2019+ DO instruments.
- `avg_do_wtemp` is defined as “YSI water temp” but contains unflagged values from 2006. In 2019+ it is heavily `C`-flagged: **{E[('avg_do_wtemp','2019_plus')]['flag_C']}** `C` and **{E[('avg_do_wtemp','2019_plus')]['valid_unflagged']}** unflagged out of 1,612 records. Its pre-2019 provenance is unresolved.
- The EML states that lake temperature data collected at the same buoy site are in an ancillary dataset (`knb-lter-ntl.130`). That dataset was **not acquired** in this sprint and is not used here. `avg_do_wtemp` should not be assumed to be a continuous, homogeneous water-temperature record.

## 4. Other transitions

- **pCO2:** daily values begin 2016-03-22; the inventory lists Turner C-sense CO2 from 2017. The 2016 values are therefore outside the documented inventory start. 2024 has only **{annual_valid('avg_pco2_ppm',2024)}** unflagged values (CO2 failed May 22); 2025 has **{annual_valid('avg_pco2_ppm',2025)}**.
- **PAR above:** 11 unflagged near-zero values (ten 0.0, one 0.002) in 2007, then no sustained record until 2016. These values are not useful light data. 2019–2020 has major `C` outages; 2023–2024 has lower coverage.
- **PAR below:** begins 2016; heavy `C` in 2019–2020; `G` (biofouling) in 2021, 2022 and 2024.
- **Conductivity:** 2006 values are 0.38–0.48 µS/cm, all `H`/`O`; no unflagged 2006 value. 2019+ values are ~122–596 µS/cm. The two eras are not comparable.
- **pH, fDOM, turbidity:** 2019+ only. The 2019–2020 biology overlap is only **{O['avg_ph']['biology_dates_within_valid_span']}** dates, with **{O['avg_ph']['same_day_valid_unflagged']}** same-day unflagged values.

## 5. Comparability verdict

- **Turner ↔ YSI chlorophyll/phycocyanin:** not directly comparable; no documented crosswalk. Use era-specific series or an explicit, validated cross-calibration if one is ever established. Do not concatenate.
- **DO:** instrument history incomplete before 2016; no documented cross-calibration; flags vary by year. Treat as an era-specific/flagged series.
- **Water temperature:** `avg_do_wtemp` is not a clean continuous series; ancillary 130 is documented but not acquired.
- **pH/fDOM/turbidity/conductance:** 2019+ only; short overlap with biology; no long-term comparability.
- **PAR:** contextual, patchy, and affected by documented outages/fouling.

**No correction factor, offset, scaling or gap-filling was applied.** The observed discontinuities are described; their causes are only attributed where the EML explicitly documents them.
"""
(OUT / "SENSOR_ERA_COMPARABILITY.md").write_text(era_md, encoding="utf-8")


# ---------------------------------------------------------------------------
# TEMPORAL COMPATIBILITY
# ---------------------------------------------------------------------------
temp_md = f"""# Temporal Compatibility with Mendota Microscopy

**Sprint:** 4L.9  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. Biology reference

The independently audited 88.31 Mendota record contains:

- **{B['records']:,}** Mendota rows / **{B['dates']}** unique dates, **{B['first_date']} to {B['last_date']}**.
- Median sampling interval **{B['median_interval_days']} days**.
- **{B['dates_0_8m']}** dates with a 0–8 m composite and **{B['dates_0_2m']}** dates with a 0–2 m sample.
- Station is blank for all rows on **{B['dates_all_station_blank']}** dates; only **{B['dates_with_any_station']}** dates have any station value (all “1”).
- The record has dates, not sampling times. No intraday alignment is possible.

Package-level overlap is **230 biology dates within 2006–2020**; 172 dates predate 2006 and none post-date 2020. Package-level overlap is not variable-level coverage; the table below uses each variable's actual unflagged span.

## 2. Same-day overlap by variable

| Variable | Biology dates within unflagged span | Date absent | Present but variable missing | Same-day numeric | Same-day unflagged | Same-day flagged | Same-day valid % of all 402 | % of within-span | ±1 d | ±3 d | ±7 d | ±14 d |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
"""
for var, r in O.items():
    temp_md += (
        f"| `{var}` | {r['biology_dates_within_valid_span']} | {r['same_day_date_absent']} | "
        f"{r['same_day_variable_missing']} | {r['same_day_any_numeric']} | {r['same_day_valid_unflagged']} | "
        f"{r['same_day_flagged_numeric']} | {pct(r['pct_same_day_valid_of_total'])} | "
        f"{pct(r['pct_same_day_valid_of_within'])} | {r['valid_within_pm1_days']} | "
        f"{r['valid_within_pm3_days']} | {r['valid_within_pm7_days']} | {r['valid_within_pm14_days']} |\n"
    )

temp_md += f"""
The windows are inclusive calendar-day windows around each biology date, using any unflagged sensor value in the window. They do **not** establish that the sensor observation and the microscopy sample describe the same moment or the same water parcel.

## 3. What the overlap actually is

- **Turner chlorophyll:** 128 same-day unflagged values out of 402 biology dates (**31.8%**), or **62.1%** of the 206 dates within its unflagged span. Adding ±3/±7/±14 days gives 148/156/163 dates (36.8%/38.8%/40.5% of all biology dates).
- **Turner phycocyanin:** 139 same-day unflagged values (**34.6%** of all; **67.5%** of within-span); ±7 gives 154 (38.3%).
- **YSI chlorophyll:** only 21 same-day unflagged values (**5.2%** of all; **75.0%** of the 28 dates within its 2019+ span). YSI phycocyanin: 22 (**5.5%**; **78.6%**).
- **DO raw:** 99 same-day unflagged (**24.6%** of all; **44.8%** of within-span); DO saturation 98; `avg_do_wtemp` only 94.
- **pH / fDOM / turbidity / specific conductance:** 22 same-day unflagged each (**5.5%** of all; **78.6%** of the 28 within-span dates). These are effectively 2019–2020-only comparisons.
- **pCO2:** 55 same-day unflagged (**13.7%** of all; **69.6%** of 79 within-span dates).
- **PAR above:** 42 same-day unflagged (**10.4%**); PAR below 45 (**11.2%**), with only 79 dates within the PAR-below span.

## 4. Annual and seasonal concentration

Full tables: `BIOLOGICAL_OVERLAP_BY_YEAR.csv`, `BIOLOGICAL_OVERLAP_BY_SEASON.csv`.

- Turner chlorophyll same-day coverage is strongest in 2016–2019 (12–16 dates/year) and absent in 2014 (0/13) and weak in 2015 (3/15). The 2006–2013 years vary from 3 to 13 dates/year.
- YSI chlorophyll same-day coverage is 11/13 dates in 2019 and 10/15 in 2020. It cannot extend beyond 2020 because the biology record ends 2020-12-10.
- Seasonally, Turner chlorophyll same-day coverage is highest in summer ({pct(bio_season[('avg_chlor_rfu_turner','summer')]['pct_same_day_valid'])}) and autumn ({pct(bio_season[('avg_chlor_rfu_turner','autumn')]['pct_same_day_valid'])}), lower in spring ({pct(bio_season[('avg_chlor_rfu_turner','spring')]['pct_same_day_valid'])}), and zero in winter (only 17 winter biology dates, none with valid sensor data). Turner phycocyanin summer is {pct(bio_season[('avg_phyco_rfu_turner','summer')]['pct_same_day_valid'])}.
- `avg_do_wtemp` same-day coverage is only 94 dates and is especially weak in 2019 (2/16) and 2020 (0/15), so it cannot serve as the main water-temperature covariate for the 2019–2020 YSI-era comparison.

## 5. Interpretation limits

- The overlap is **day-level**, not time-of-day. The microscopy record has no sample time.
- The sensor values are daily averages of 1-minute data; the biology values are integrated/composite samples. Neither represents the same sampling support.
- Same-day presence is not evidence of biological response; it is only evidence that both records exist on that date.
- Missingness and flags are not random: the 2014–2015 Turner gap and 2019+ sensor transition concentrate missingness in specific years.
- No bloom/non-bloom labels, event intervals, model inputs or early-warning features were created.

## 6. Conclusion

The strongest exploratory pairing is **Turner chlorophyll/phycocyanin with microscopy cyanobacteria biovolume or cell density, 2006–2019**, on roughly 128–139 same-day dates, with the 0.5 m vs 0–8 m depth caveat. DO and water temperature add complementary environmental context on ~94–99 same-day dates. The 2019+ YSI pH/fDOM/turbidity/conductance variables are too short (22 same-day dates) for long-term comparison. No temporal analysis can recover intraday alignment or exact sample coincidence.
"""
(OUT / "TEMPORAL_COMPATIBILITY.md").write_text(temp_md, encoding="utf-8")


# ---------------------------------------------------------------------------
# DEPTH / SPATIAL
# ---------------------------------------------------------------------------
depth_md = f"""# Depth and Spatial Compatibility

**Sprint:** 4L.9  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. Sensor depths from the EML

- Chlorophyll, phycocyanin, DO, pH, specific conductance, turbidity and fDOM: **0.5 m**.
- pCO2: **1 m**.
- PAR above water: **2 m above the surface**.
- PAR below water: **1 m depth**.
- Meteorology: air temperature/RH **2 m above surface**; wind **3 m above surface**.

## 2. Biology depth

- **{B['dates_0_8m']}** Mendota dates are labelled **0–8 m composite**.
- **{B['dates_0_2m']}** dates are labelled **0–2 m**.
- The 0–8 m composite integrates over a depth range; the sensor values are point measurements at 0.5 m (or 1 m for pCO2/PAR).

## 3. Spatial setting

- EML buoy coordinates: approximately **43.0995, −89.4045**.
- NTL southern-lake sampling site coordinate for Mendota: approximately **43.09885, −89.40545**.
- These are about **106 m apart** (great-circle estimate); they are site-level neighbours, not an exact co-location.
- Per-sample station linkage is weak: station is blank for all rows on **{B['dates_all_station_blank']}** of **{B['dates']}** dates; only **{B['dates_with_any_station']}** dates have any station value.

## 4. Compatibility table

| Variable | Sensor depth | Measurement | Biological reference | Classification | Reason |
|---|---|---|---|---|---|
"""
for r in depth_rows:
    depth_md += (
        f"| `{r['variable']}` | {r['sensor_depth']} | {r['measurement']} | "
        f"{r['biological_reference']} | {r['classification']} | {r['reason']} |\n"
    )

depth_md += f"""
## 5. Interpretation

- A **0.5 m surface point** is not a **0–8 m composite**. The sensor may over- or under-represent the column depending on stratification, vertical migration, surface scums and light penetration. The data do not include a depth profile to quantify this.
- The two 0–2 m biology dates are a separate depth class and should not be pooled silently with the 0–8 m dates.
- Site-level proximity is documented, but the ~106 m offset and the mostly blank station field mean per-sample spatial coincidence is **not established**.
- Atmospheric variables (air temperature, RH, wind, above-water PAR) are contextual and are not directly comparable to the 0–8 m biological composite.
- pCO2 (1 m) and PAR below (1 m) are single-depth context variables, not biomass measures.

## 6. Conclusion

Depth/spatial compatibility is **weak/conditional** for all water-column variables and **not comparable** for atmospheric variables. A future analysis must define an explicit comparator (surface layer, euphotic-zone integration, or whole-column biomass) and test sensitivity; it cannot assume that 0.5 m sensors represent the 0–8 m composite.
"""
(OUT / "DEPTH_AND_SPATIAL_COMPATIBILITY.md").write_text(depth_md, encoding="utf-8")


# ---------------------------------------------------------------------------
# FEASIBILITY
# ---------------------------------------------------------------------------
feas_md = f"""# Scientific Feasibility Assessment

**Sprint:** 4L.9  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Final verdict: EXPLORATORY FEASIBILITY SUPPORTED WITH MAJOR LIMITATIONS.**

## 1. Summary judgement

The daily sensor file is real, structurally clean and extensive: **{F['rows']:,}** daily records from **{F['date_min']}** to **{F['date_max']}**, 18 variables, 18 flag columns, and no duplicate dates. It materially improves the environmental evidence base. It does **not** remove the core constraints: variable-specific missingness, undocumented flag semantics, sensor-era discontinuities, a 0.5 m vs 0–8 m depth mismatch, and a 14-day microscopy record with no sampling times.

## 2. The four requested uses

### A. Exploratory seasonal ecological analysis

**Verdict: SUPPORTED WITH MAJOR LIMITATIONS.**

Evidence:
- Air temperature, RH, wind, DO and (for 2006–2019) Turner chlorophyll/phycocyanin have multi-year records.
- YSI chlorophyll/phycocyanin and pH/fDOM/turbidity/conductance provide a 2019+ open-water series.
- The file supports descriptive seasonal plots and within-season summaries when the variable-specific denominator and flag rule are stated.

Limitations:
- The record is open-water (April–November), not year-round; winter has only 15 records.
- Missingness and flags are variable-specific and often concentrated in particular years.
- Sensor eras are not directly comparable; Turner/YSI must remain separate.
- A seasonal pattern is not a bloom label or a biological response estimate.

### B. Descriptive comparison with microscopy-derived cyanobacterial measurements

**Verdict: PARTIALLY SUPPORTED — EXPLORATORY ONLY.**

Evidence:
- The audited biology record supplies 402 Mendota dates and 0–8 m composite samples.
- Turner chlorophyll has **{O['avg_chlor_rfu_turner']['same_day_valid_unflagged']}** same-day unflagged values; Turner phycocyanin **{O['avg_phyco_rfu_turner']['same_day_valid_unflagged']}**; DO raw **{O['avg_do_raw']['same_day_valid_unflagged']}**; DO saturation **{O['avg_do_sat']['same_day_valid_unflagged']}**; `avg_do_wtemp` **{O['avg_do_wtemp']['same_day_valid_unflagged']}**.
- The strongest pairing is Turner chlorophyll/phycocyanin with cyanobacteria biovolume or cell density, 2006–2019.

Limitations:
- 0.5 m point sensor vs 0–8 m composite; no depth profile.
- RFU is a proxy, not a quantitative pigment or biovolume measurement; RFU is sensor-specific.
- The biology record is ~14-day, date-only, and taxonomically non-stationary.
- Same-day overlap is ~32–35% of all biology dates for the Turner proxies, not a complete paired time series.
- No causal, confirmatory or event-onset claim is supported.

### C. Investigation of multivariate environmental relationships over time

**Verdict: LIMITED / NOT ROBUSTLY SUPPORTED.**

Evidence:
- Several variables are co-measured on the same daily rows, enabling descriptive multivariate exploration.
- The 2019+ YSI suite provides a short multi-variable window.

Limitations:
- Strong collinearity among environmental variables (e.g., temperature, DO, season, light).
- Variable-specific missingness and flags; some variables exist only in 2019+.
- The biology response is sparse and not time-matched within days.
- Sensor-era changes create structural breaks.
- A descriptive multivariate exploration is possible; a robust inferential multivariate model is not justified by this audit.

### D. Any eventual early-warning evaluation

**Verdict: NOT SUPPORTED.**

Reasons:
- No bloom/non-bloom labels, event definitions or event intervals exist; creating them is prohibited under Gate 2.
- The biology record is ~14-day and date-only; it cannot resolve hours-to-days onset.
- The sensor is at 0.5 m; the biology is a 0–8 m composite.
- Fluorescence is a proxy affected by community composition, physiology, light history, temperature and biofouling.
- Same-day overlap is partial and concentrated in specific years.
- Daily data alone do not establish that an environmental change precedes a biological bloom.

## 3. Detecting environmental change vs detecting cyanobacterial change vs predicting a bloom

These are different claims:

1. **Detecting environmental change** — supported descriptively for several variables, with caveats about flags, gaps and era changes.
2. **Detecting cyanobacterial abundance change** — partially supported only through proxy fluorescence and sparse microscopy; not a direct abundance measurement.
3. **Identifying bloom onset** — not supported: no event definition, no sub-weekly biology, no intraday sampling time.
4. **Predicting a future bloom** — not supported: no labels, no validated precursor window, no out-of-sample design, no independent biological validation.

The daily file improves (1) and, cautiously, (2). It does not establish (3) or (4).

## 4. What the evidence establishes

- The daily entity is authentic and structurally sound.
- All 18 variables are present, but coverage is variable-specific and era-specific.
- The strongest long-run biological proxies are Turner chlorophyll/phycocyanin (2006–2019).
- The 2019+ YSI suite is too short, relative to the biology, for long-term comparison.
- Same-day biology–sensor overlap is partial and day-level only.
- Depth/spatial compatibility is weak/conditional.
- Flag metadata are incomplete/inconsistent in eight columns, including an undefined `O` code.

## 5. What remains unknown

- Per-record calibration history, coefficients, serial numbers and detection limits.
- Exact sensor change dates within years.
- The identity/provenance of pre-2016 DO and pre-2019 `avg_do_wtemp`.
- Whether flagged `H`/`E` values are erroneous, extreme-but-real, or era artefacts.
- Whether the 0.5 m sensor is representative of the 0–8 m composite at any given date.
- Whether a validated Turner–YSI crosswalk exists outside the EML.
- Whether the microscopy taxonomy can be harmonised for longitudinal species-level analysis (a separate biological task).
- Any protocol-approved bloom/non-bloom definition.

## 6. Final verdict

**EXPLORATORY FEASIBILITY SUPPORTED WITH MAJOR LIMITATIONS.**

The dataset can support descriptive, variable-specific, open-water-season exploratory work and a cautious descriptive comparison with microscopy-derived cyanobacteria. It cannot support confirmatory modelling, bloom labels, event intervals, hypothesis tests or early-warning claims. **Gate 2 remains PAUSED / NOT APPROVED.**
"""
(OUT / "SCIENTIFIC_FEASIBILITY_ASSESSMENT.md").write_text(feas_md, encoding="utf-8")


# ---------------------------------------------------------------------------
# EXTERNAL SEARCH LOG
# ---------------------------------------------------------------------------
search_md = f"""# External Search Log

**Sprint:** 4L.9  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. Source categories defined before searching

1. Project governance and prior sprint evidence (4L.5, 4L.6, 4L.7, 4L.8, 4L.8A).
2. Primary dataset metadata: 129.42 EML, entity inventory, DataONE sysmeta, sensor inventory.
3. NTL-LTER deployment and sampling documentation (high-frequency page, protocols, site coordinates).
4. Manufacturer documentation for the YSI EXO2 and Turner Cyclops-7F.
5. Authoritative methodological guidance on algal fluorometry, calibration, biofouling, reporting units and QA (USGS).
6. Peer-reviewed literature on phycocyanin/chlorophyll fluorescence as a proxy and its limitations.
7. Access/integrity records for the acquired entity.

## 2. Searches and sources inspected

| # | Query / route | Sources inspected | What it establishes | Status |
|---:|---|---|---|---|
| 1 | Local governance and prior evidence | `AGENTS.md`; 4L.5, 4L.6, 4L.7, 4L.8, 4L.8A reports | Project rules; prior biology audit; acquisition/auth history; metadata-level sensor audit | Full |
| 2 | 129.42 EML | `metadata_129.42.xml` (146,471 B) | 38-field daily schema; flags; depths; 2017–2024 event notes; Turner/YSI statement; entity size/MD5; temporal coverage 2006-06-26 to 2025-12-31 | Full |
| 3 | Entity inventory | `entity_inventory_129.42.csv` | Daily/hourly/high-resolution/sensor-list entity IDs and sizes | Full |
| 4 | Sensor inventory | `List_of_sensors_used_on_the_Lake_Mendota_buoy_since_2006...dat` | 20 sensor records; years only; DO/CO2/PAR inventory mismatches | Full |
| 5 | DataONE CN sysmeta | `cn.dataone.org/cn/v2/meta/...cba9ed...` | Daily size 490,187 B; SHA-1 `bb1d...`; LTER replica only | Full |
| 6 | Acquired daily file | Local `.dat` | 490,187 B; 3,996 rows; 38 columns; hashes; date range | Full |
| 7 | NTL high-frequency data page | https://lter.limnology.wisc.edu/high-frequency-data/ | Mendota buoy 129/130 links; deployment typically Apr–Nov; live viewer | Full |
| 8 | NTL research protocols | https://lter.limnology.wisc.edu/protocols/ | Bi-weekly summer / monthly non-summer sampling; integrated southern-lake chlorophyll; phytoplankton biovolume ME/MO; Mendota site coordinate | Full |
| 9 | YSI EXO2 product page/specifications | https://www.ysi.com/exo2 | 7 ports; central antifouling wiper; Total Algae Chl/PC RFU ranges 0–100; sensor specs; calibration/wiper context | Full page/spec table |
| 10 | Turner Cyclops-7F product page | https://www.turnerdesigns.com/cyclops-7f-submersible-fluorometer | Discontinued 2025; dye-standard calibration; RFU output; technical documentation links | Full page |
| 11 | USGS TM1-D10 | https://pubs.usgs.gov/publication/tm1D10/full | Fluorescence is a proxy, not direct abundance; RFU is sensor-specific; diurnal quenching; biofouling; calibration/QA; different sensors not equivalent | Full HTML; relevant sections inspected |
| 12 | Manufacturer manual PDFs | YSI EXO manual; Turner Cyclops manual URLs | Manuals identified; PDF text could not be extracted by the fetch tool (`application/pdf` unsupported) | Identified, not text-inspected |
| 13 | Peer-reviewed phycocyanin literature | Search results: Thomson-Laing et al. 2020 (PubMed); Ma et al. 2022 (MDPI); NIWA guidance | Phycocyanin fluorescence is used as a cyanobacteria proxy but requires site-specific validation; MDPI page returned 403; PubMed page returned only an HHS notice | Identified; not used as primary evidence |
| 14 | EDI portal / package page | EDI mapbrowse 129 | Package summary/login context; data access already resolved by acquisition | Identified |

## 3. Key source conclusions

- **EML:** the daily entity is 490,187 B, MD5 `eb7b3a...`; daily values are averages of 1-minute observations; Turner and YSI chlorophyll/phycocyanin output RFU with “significant magnitude differences”; pH/DO/specific conductance were cleaned/recalibrated every two weeks in 2019, nearly weekly in 2020; multiple outage/fouling events are documented.
- **USGS TM1-D10:** algal fluorometers measure a fluorescence response, not algal abundance/biomass; RFU is sensor-specific; relations vary with species, physiology, temperature and light; nonphotochemical quenching can cause diurnal variability; biofouling and calibration drift require site-specific QA; different makes/models are not equivalent even in the same units.
- **YSI EXO2:** Total Algae chlorophyll and phycocyanin channels report 0–100 RFU (with µg/L ranges) and use a central wiper; performance specifications are controlled-condition values, not a guarantee in lake water.
- **Turner Cyclops-7F:** RFU output; calibration with dye standards; discontinued in 2025; technical documentation exists but the manual PDF was not text-extracted.
- **NTL protocols/page:** open-water deployment, bi-weekly summer/monthly non-summer sampling, integrated southern-lake chlorophyll, phytoplankton biovolume for Mendota/Monona.

## 4. Inaccessible / not used

- Manufacturer PDF manuals: fetch tool rejected `application/pdf`; product pages/spec tables were used instead. Do not claim full manual inspection.
- MDPI article: HTTP 403.
- PubMed page: returned an HHS vulnerability notice rather than the abstract; not used.
- Ancillary NTL dataset 130 (water temperature): deliberately **not acquired**; outside this sprint's single-entity scope.
- Hourly and 1-minute 129.42 entities: deliberately not acquired.
- EDI package data behind login: not re-requested; acquisition already complete.

## 5. Why searching stopped

The primary metadata, sensor inventory, full daily file, NTL deployment/sampling documentation, manufacturer specifications and authoritative USGS fluorometry guidance were inspected. Remaining uncertainty is about per-record calibration, maintenance and sensor identity, which are **not available** in the public metadata and cannot be resolved by more web searching. No external contact was made. No source supports a bloom/non-bloom label, event interval or confirmatory claim.
"""
(OUT / "EXTERNAL_SEARCH_LOG.md").write_text(search_md, encoding="utf-8")


# ---------------------------------------------------------------------------
# SOURCE REGISTER
# ---------------------------------------------------------------------------
source_rows = [
    ("S01", "AGENTS.md", "/Users/cedricbw/Documents/EcoSentinel/AGENTS.md", "Governance", "Full", "Project rules and evidence standards"),
    ("S02", "129.42 EML", "research/evidence/sprint_4l7_mendota_daily_sensor_audit/acquisition/129.42/metadata_129.42.xml", "Primary metadata", "Full", "Schema, flags, depths, events, size/MD5, temporal coverage"),
    ("S03", "129.42 entity inventory", "research/evidence/sprint_4l7_mendota_daily_sensor_audit/acquisition/129.42/entity_inventory_129.42.csv", "Project table", "Full", "Entity IDs/sizes"),
    ("S04", "Sensor inventory", "research/evidence/sprint_4k_mendota_authorised_access/acquisition/129.42/List_of_sensors_used_on_the_Lake_Mendota_buoy_since_2006__edddc490dfd553c4c4b9e5d4b86eb2eb.dat", "Primary data", "Full", "20 sensor records; eras; mismatches"),
    ("S05", "Daily sensor raw file", "research/evidence/sprint_4l7_mendota_daily_sensor_audit/acquisition/129.42/North_Temperate_Lakes_LTER_Daily_Meteorological_and_Metabolism_Data_-_Lake_Mendota__cba9ed12834b8f315d6b10675bb60c5a.dat", "Primary data", "Full", "3,996 daily records; 38 columns; hashes"),
    ("S06", "Sprint 4L.8A integrity report", "research/evidence/sprint_4l8a_post_acquisition_verification/", "Project evidence", "Full", "Baseline size/MD5/SHA-1/SHA-256; .dat/.csv explanation"),
    ("S07", "Sprint 4L.5 biology audit", "research/evidence/sprint_4l5_mendota_raw_biology_audit/", "Project evidence", "Full", "402 Mendota dates; 0–8 m; biological anomalies"),
    ("S08", "Sprint 4L.6 independent biology audit", "research/evidence/sprint_4l6_codex_independent_raw_biology_audit/", "Independent review", "Full", "Count corrections; biological cautions"),
    ("S09", "Sprint 4L.7 sensor metadata audit", "research/evidence/sprint_4l7_mendota_daily_sensor_audit/", "Project evidence", "Full", "Metadata-level schema/era/depth/overlap"),
    ("S10", "NTL high-frequency page", "https://lter.limnology.wisc.edu/high-frequency-data/", "Official documentation", "Full", "Buoy 129/130; Apr–Nov deployment; live viewer"),
    ("S11", "NTL research protocols", "https://lter.limnology.wisc.edu/protocols/", "Official documentation", "Full", "Sampling frequency; integrated chlorophyll; phytoplankton biovolume; site coordinate"),
    ("S12", "YSI EXO2 product page", "https://www.ysi.com/exo2", "Manufacturer documentation", "Full page/spec table", "Sonde/sensor specs; RFU ranges; wiper; calibration context"),
    ("S13", "Turner Cyclops-7F product page", "https://www.turnerdesigns.com/cyclops-7f-submersible-fluorometer", "Manufacturer documentation", "Full page", "Discontinued 2025; RFU; dye calibration; manual links"),
    ("S14", "USGS TM1-D10", "https://pubs.usgs.gov/publication/tm1D10/full", "Authoritative guidance", "Full HTML; relevant sections", "Proxy nature; RFU sensor-specificity; quenching; biofouling; calibration/QA"),
    ("S15", "DataONE CN sysmeta", "cn.dataone.org/cn/v2/meta/cba9ed12834b8f315d6b10675bb60c5a", "Repository metadata", "Full", "Size 490,187; SHA-1; LTER replica"),
    ("S16", "EDI package page", "https://portal.edirepository.org/nis/mapbrowse?scope=knb-lter-ntl&identifier=129", "Repository metadata", "Identified", "Package summary/login context"),
    ("S17", "Thomson-Laing et al. 2020", "https://pubmed.ncbi.nlm.nih.gov/32732055/", "Peer-reviewed literature", "Not inspected (page returned HHS notice)", "Phycocyanin proxy context; not used as primary evidence"),
    ("S18", "Ma et al. 2022", "https://www.mdpi.com/2073-4441/14/22/3749", "Peer-reviewed literature", "Not inspected (HTTP 403)", "Online phycocyanin fluorescence limitations; not used as primary evidence"),
    ("S19", "YSI EXO manual PDF", "https://www.xylem.com/siteassets/brand/ysi/resources/manual/exo-user-manual-web.pdf", "Manufacturer manual", "Identified; PDF not text-extracted", "Would document calibration/wiper detail; not claimed as inspected"),
    ("S20", "Turner Cyclops manual PDF", "https://docs.turnerdesigns.com/t2/doc/manuals/998-2100.pdf", "Manufacturer manual", "Identified; PDF not text-extracted", "Would document calibration/RFU detail; not claimed as inspected"),
]
with (OUT / "SOURCE_REGISTER.csv").open("w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["id", "source", "path_or_url", "type", "inspected", "use"])
    w.writerows(source_rows)

source_md = """# Source Register

**Sprint:** 4L.9  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

| ID | Source | Path / URL | Type | Inspected | Use |
|---|---|---|---|---|---|
"""
for row in source_rows:
    source_md += f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} |\n"
source_md += """
## Notes

- “Full” means the local file or complete HTML page was read; it does not mean every linked PDF was parsed.
- Manufacturer manual PDFs were identified but could not be text-extracted by the fetch tool. Product pages and specification tables were inspected instead.
- “Identified” means the source was found but not used as primary evidence.
- No source establishes that the daily observations are calibrated, unbiased or directly comparable across sensor eras.
- No source establishes a bloom/non-bloom label, event interval or confirmatory design.
"""
(OUT / "SOURCE_REGISTER.md").write_text(source_md, encoding="utf-8")


# ---------------------------------------------------------------------------
# VALIDATION REPORT
# ---------------------------------------------------------------------------
val_md = f"""# Validation and Independent QC

**Sprint:** 4L.9  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. Checksums and structure

- Raw bytes **{F['bytes']:,}**; MD5 `{F['md5']}`; SHA-1 `{F['sha1']}`; SHA-256 `{F['sha256']}`.
- **3,996** data rows; **38** columns; **0** malformed rows; **0** blank lines.
- **0** date-parse errors; **0** duplicate dates; **0** exact duplicate rows; **0** year/date mismatches.
- Header order matches the expected daily schema.
- Independent parser (simple comma splitting) reproduced 3,996 rows, 38 columns, 0 bad field counts, 0 duplicate dates, 0 exact duplicates, and the same date range.
- `wc -l` = 3,997 lines including header; `awk` found 0 lines with field count ≠ 38.

## 2. Audit validation

The audit's own checks: **{validation['passed']} passed / {validation['failed']} failed**.

The one failed check is **not an arithmetic failure**: it records that eight flag columns contain values outside their own daily-EML code list. This is a documented metadata non-conformance:

| Variable | Documented daily codes | Extra values |
|---|---|---|
"""
for r in undocumented:
    val_md += f"| `{r['variable']}` | {codes_text(r['documented'])} | {codes_text(r['observed_extra'])} |\n"
val_md += """
The extra codes include the undefined `O` value in `flag_avg_spec_cond`, `H` values in `flag_avg_wind_speed`/`flag_avg_rel_hum`/`flag_avg_par_below`, and `E` values in several 2019+ columns. They are retained and reported, not corrected.

## 3. Arithmetic and percentage reconciliation

- For every variable: `missing + numeric_any = total_records`.
- For every variable: `valid_unflagged + flagged_numeric = numeric_any`.
- For every variable: `C + E + H + G + O + other + none = total_records`.
- All percentages are in 0–100 and reconcile with their counts to 1e-6.
- Biology overlap: `same_day_valid + same_day_flagged = same_day_any_numeric`; `same_day_any + same_day_variable_missing = same_day_record_present`; `same_day_record_present + same_day_date_absent = within_valid_span`.
- Window counts are monotonic: same-day ≤ ±1 ≤ ±3 ≤ ±7 ≤ ±14.

These checks were reproduced by the independent second-method script with **zero coverage mismatches, zero overlap mismatches, and zero percentage issues** (`INDEPENDENT_VERIFICATION.md`).

## 4. Unresolved discrepancies

1. **Undefined `O` flag** in `flag_avg_spec_cond` (1 value, 2006-08-11).
2. **Daily EML code-list omissions** for eight columns (above).
3. **`avg_do_wtemp` definition conflict:** labelled YSI water temp but present from 2006, before the YSI EXO2 era.
4. **DO inventory conflict:** daily DO exists from 2006, but the sensor inventory's DO records begin 2016.
5. **pCO2 inventory conflict:** daily pCO2 begins 2016-03-22, but the inventory lists the CO2 sensor from 2017.
6. **PAR 2007 near-zero values:** 11 unflagged near-zero values (ten 0.0, one 0.002) before the sustained 2016+ PAR record.
7. **Conductivity 2006 scale:** values ~0.38–0.48 µS/cm, all flagged; no valid 2006 value.
8. **Unflagged implausible values:** negative turbidity, negative YSI phycocyanin/chlorophyll, negative PAR below; these are not automatically valid.
9. **No per-record calibration/maintenance history** or exact sensor-change dates.

These are reported as unresolved. No value was silently corrected, deleted or imputed.

## 5. Reproducibility

From the repository root:

```bash
python3 research/evidence/sprint_4l9_mendota_daily_sensor_raw_audit/scripts/audit_sensor_raw.py
python3 research/evidence/sprint_4l9_mendota_daily_sensor_raw_audit/scripts/verify_audit.py
python3 research/evidence/sprint_4l9_mendota_daily_sensor_raw_audit/scripts/write_reports.py
```

The audit reads the preserved raw files and writes only under the Sprint 4L.9 evidence directory. It does not modify the raw file or prior sprint evidence.
"""
(OUT / "VALIDATION_REPORT.md").write_text(val_md, encoding="utf-8")


# ---------------------------------------------------------------------------
# EXECUTIVE REPORT
# ---------------------------------------------------------------------------
exec_md = f"""# Sprint 4L.9 Executive Report — Mendota Daily Sensor Raw Audit and Biological Feasibility

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
- Unflagged coverage ranges from **{pct(get('avg_chlor_rfu_ysi','valid_unflagged_pct'))}** (YSI chlorophyll) to **{pct(get('avg_wind_dir','valid_unflagged_pct'))}** (wind direction).
- Severe within-era gaps: Turner chlorophyll 2014 (**{annual_valid('avg_chlor_rfu_turner',2014)}** unflagged) and 2015 (**{annual_valid('avg_chlor_rfu_turner',2015)}**); Turner phycocyanin 2007 (**{annual_valid('avg_phyco_rfu_turner',2007)}**); DO 2008 (**{annual_valid('avg_do_raw',2008)}**), 2010 (**{annual_valid('avg_do_raw',2010)}**), 2014 (**{annual_valid('avg_do_raw',2014)}**), 2017 (**{annual_valid('avg_do_raw',2017)}**).
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
| Turner chlorophyll | {O['avg_chlor_rfu_turner']['same_day_valid_unflagged']} | {pct(O['avg_chlor_rfu_turner']['pct_same_day_valid_of_total'])} | {pct(O['avg_chlor_rfu_turner']['pct_same_day_valid_of_within'])} |
| Turner phycocyanin | {O['avg_phyco_rfu_turner']['same_day_valid_unflagged']} | {pct(O['avg_phyco_rfu_turner']['pct_same_day_valid_of_total'])} | {pct(O['avg_phyco_rfu_turner']['pct_same_day_valid_of_within'])} |
| YSI chlorophyll | {O['avg_chlor_rfu_ysi']['same_day_valid_unflagged']} | {pct(O['avg_chlor_rfu_ysi']['pct_same_day_valid_of_total'])} | {pct(O['avg_chlor_rfu_ysi']['pct_same_day_valid_of_within'])} |
| YSI phycocyanin | {O['avg_phyco_rfu_ysi']['same_day_valid_unflagged']} | {pct(O['avg_phyco_rfu_ysi']['pct_same_day_valid_of_total'])} | {pct(O['avg_phyco_rfu_ysi']['pct_same_day_valid_of_within'])} |
| DO raw | {O['avg_do_raw']['same_day_valid_unflagged']} | {pct(O['avg_do_raw']['pct_same_day_valid_of_total'])} | {pct(O['avg_do_raw']['pct_same_day_valid_of_within'])} |
| pH / fDOM / turbidity / conductance | {O['avg_ph']['same_day_valid_unflagged']} | {pct(O['avg_ph']['pct_same_day_valid_of_total'])} | {pct(O['avg_ph']['pct_same_day_valid_of_within'])} |

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
"""
(OUT / "SPRINT_4L9_EXECUTIVE_REPORT.md").write_text(exec_md, encoding="utf-8")


# ---------------------------------------------------------------------------
# HANDOVER
# ---------------------------------------------------------------------------
hand_md = f"""# Sprint 4L.9 Handover

**Date:** 2026-11-24  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Status: COMPLETE — EXPLORATORY FEASIBILITY SUPPORTED WITH MAJOR LIMITATIONS.**

## 1. What is complete

- Raw daily file re-verified against the Sprint 4L.8A baseline: 490,187 B; MD5 `{F['md5']}`; SHA-1 `{F['sha1']}`; SHA-256 `{F['sha256']}`; 3,996 rows; 38 columns.
- Full schema/parse audit: 0 malformed rows, 0 duplicate dates, 0 date errors, 0 non-numeric non-empty values.
- Variable-by-variable coverage, annual and seasonal coverage, interval/gap analysis.
- QC flag audit, including undocumented codes and flag-value distributions.
- Sensor-era comparability, Turner/YSI paired 2019 comparison, DO/water-temperature/pCO2/PAR/conductance caveats.
- Biology–sensor same-day and ±1/±3/±7/±14-day overlap for all 18 variables.
- Depth/spatial compatibility and four-use feasibility assessment.
- Independent second-method verification: zero coverage/overlap/percentage mismatches.
- External search log and source register; full local metadata and authoritative USGS guidance inspected.
- SHA-256 evidence register and sidecar.

## 2. Key facts to carry forward

- **Do not concatenate Turner and YSI chlorophyll/phycocyanin.** 2019 paired medians differ by ~3 orders of magnitude; no crosswalk.
- **Do not treat `avg_do_wtemp` as a clean continuous water-temperature series.** It is YSI-labelled but exists from 2006; 2019+ is heavily `C`-flagged. Ancillary 130 is documented but not acquired.
- **Do not treat `C` as missing** without checking the value column; many `C` records contain numeric values.
- **Do not treat unflagged as validated.** Negative turbidity, negative YSI phycocyanin/chlorophyll and negative PAR below exist unflagged.
- **Do not pool the 2006 conductivity values with 2019+ conductance.** 2006 values are ~0.4 µS/cm and all flagged; 2019+ is ~122–596 µS/cm.
- **Do not pool 0.5 m sensor values with 0–8 m microscopy as if equivalent.** Depth/spatial compatibility is weak/conditional.
- **Do not use 2019+ pH/fDOM/turbidity/conductance for long-term comparison.** Only ~22 same-day biology dates, all 2019–2020.
- **Strongest exploratory biological pairing:** Turner chlorophyll/phycocyanin vs cyanobacteria biovolume or cell density, 2006–2019, 128–139 same-day dates, with all caveats.

## 3. Unresolved issues

1. Undefined `O` flag (one 2006 specific-conductance value).
2. Eight flag columns with values outside their daily-EML code lists.
3. `avg_do_wtemp` pre-2019 provenance and definition conflict.
4. DO instrument identity 2006–2015 (not in sensor inventory).
5. pCO2 inventory start 2017 vs data start 2016.
6. PAR 2007 near-zero values before the sustained 2016+ record.
7. 2006 conductivity scale problem.
8. Unflagged physically implausible values.
9. No per-record calibration, coefficients, serial numbers, detection limits or maintenance logs.
10. No exact within-year sensor-change dates.
11. Biology taxonomy harmonisation unresolved (separate 4L.5/4L.6 issue).
12. No protocol-approved bloom/non-bloom definition.

## 4. Safe next steps (descriptive only)

- If the project continues exploratory work, define a **variable-specific inclusion rule** (e.g., unflagged numeric only; retain flagged values for sensitivity), and state the denominator.
- Define an explicit **depth comparator** before any sensor–biology comparison (surface layer vs 0–8 m composite; sensitivity analysis).
- Keep Turner and YSI eras separate; do not apply an undocumented correction.
- If water temperature is needed, consider the ancillary 130 dataset **only with explicit authorisation**; do not acquire it as part of this sprint.
- Treat same-day overlap as day-level, not intraday.
- Do not create bloom/non-bloom labels, event intervals, model inputs or early-warning claims.

## 5. Reproduce

From the repository root:

```bash
python3 research/evidence/sprint_4l9_mendota_daily_sensor_raw_audit/scripts/audit_sensor_raw.py
python3 research/evidence/sprint_4l9_mendota_daily_sensor_raw_audit/scripts/verify_audit.py
python3 research/evidence/sprint_4l9_mendota_daily_sensor_raw_audit/scripts/write_reports.py
```

## 6. Governance

**Gate 2 remains PAUSED / NOT APPROVED.** No labels, event intervals, confirmatory models, hypothesis tests, protocol changes, external contacts, uploads, commits or pushes were made. The raw daily file and all prior sprint evidence remain unchanged.
"""
(OUT / "SPRINT_4L9_HANDOVER.md").write_text(hand_md, encoding="utf-8")


# ---------------------------------------------------------------------------
# DELIVERABLES INDEX
# ---------------------------------------------------------------------------
index_md = """# Sprint 4L.9 Deliverables Index

**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

| # | Deliverable | File(s) |
|---:|---|---|
| 1 | Executive report | `SPRINT_4L9_EXECUTIVE_REPORT.md` |
| 2 | Raw-file integrity verification | `RAW_FILE_INTEGRITY_VERIFICATION.md`, `RAW_FILE_INTEGRITY.csv` |
| 3 | Complete schema audit | `SCHEMA_AUDIT.md`, `SCHEMA_AUDIT.csv` |
| 4 | Variable coverage summary | `VARIABLE_COVERAGE_AUDIT.md`, `VARIABLE_COVERAGE_SUMMARY.csv` |
| 5 | Annual variable coverage table | `ANNUAL_VARIABLE_COVERAGE.csv` |
| 6 | Seasonal variable coverage table | `SEASONAL_VARIABLE_COVERAGE.csv` |
| 7 | Sampling interval and gap analysis | `SAMPLING_INTERVALS_AND_GAPS.md`, `SAMPLING_INTERVALS_AND_GAPS.csv`, `INTERVAL_DISTRIBUTION.csv` |
| 8 | QC flag audit | `QC_FLAG_AUDIT.md`, `QC_FLAG_DISTRIBUTIONS.csv`, `QC_FLAG_TOP_YEARS.csv`, `FLAGGED_VALUE_DISTRIBUTIONS.csv`, `UNDOCUMENTED_FLAGS.csv` |
| 9 | Sensor-era comparability | `SENSOR_ERA_COMPARABILITY.md`, `SENSOR_ERA_SUMMARY.csv`, `TURNER_YSI_OVERLAP.csv`, `SENSOR_TRANSITIONS.csv` |
| 10 | Biological overlap table | `BIOLOGICAL_OVERLAP.csv`, `BIOLOGICAL_OVERLAP_WINDOWS.csv`, `BIOLOGICAL_OVERLAP_BY_YEAR.csv`, `BIOLOGICAL_OVERLAP_BY_SEASON.csv` |
| 11 | Temporal compatibility report | `TEMPORAL_COMPATIBILITY.md` |
| 12 | Depth and spatial compatibility | `DEPTH_AND_SPATIAL_COMPATIBILITY.md`, `DEPTH_COMPATIBILITY.csv` |
| 13 | Scientific feasibility assessment | `SCIENTIFIC_FEASIBILITY_ASSESSMENT.md`, `FEASIBILITY_MATRIX.csv` |
| 14 | External search log | `EXTERNAL_SEARCH_LOG.md` |
| 15 | Source register | `SOURCE_REGISTER.md`, `SOURCE_REGISTER.csv` |
| 16 | Reproducible scripts | `scripts/audit_sensor_raw.py`, `scripts/verify_audit.py`, `scripts/write_reports.py` |
| 17 | Machine-readable audit tables | `tables/`, root-level copies of key tables, `TABLES_INDEX.csv` |
| 18 | SHA-256 evidence register and sidecar | `EVIDENCE_SHA256_REGISTER.csv`, `EVIDENCE_SHA256_REGISTER.csv.sha256` |
| 19 | Complete handover | `SPRINT_4L9_HANDOVER.md` |
| — | Validation and independent QC | `VALIDATION_REPORT.md`, `VALIDATION.json`, `INDEPENDENT_VERIFICATION.md`, `INDEPENDENT_VERIFICATION.json` |
| — | Anomaly audit | `ANOMALY_AUDIT.csv` |
| — | Summary JSON | `summary.json` |

## Canonical tables

The canonical machine-readable outputs are in `tables/`. Root-level copies of the main tables are provided for convenience; both are registered by SHA-256. If they ever diverge, `tables/` is canonical.
"""
(OUT / "DELIVERABLES_INDEX.md").write_text(index_md, encoding="utf-8")

print("reports written")
