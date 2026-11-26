#!/usr/bin/env python3
"""Reproducible, descriptive audit of the 129.42 daily Mendota sensor CSV.

No labels, event definitions, models, hypothesis tests or confirmatory analysis
are produced. The original raw file is opened read-only and never modified.
"""
import csv
import hashlib
import json
import math
import statistics
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RAW = ROOT / "research/evidence/sprint_4l7_mendota_daily_sensor_audit/acquisition/129.42/North_Temperate_Lakes_LTER_Daily_Meteorological_and_Metabolism_Data_-_Lake_Mendota__cba9ed12834b8f315d6b10675bb60c5a.dat"
BIO = ROOT / "research/evidence/sprint_4l_mendota_biology_audit/acquisition/88.31/North_Temperate_Lakes_LTER_-_Phytoplankton_-_Madison_Lakes_Area__f2de15b2fff6ae962a04c150c0a1c510.dat"
EML = ROOT / "research/evidence/sprint_4l7_mendota_daily_sensor_audit/acquisition/129.42/metadata_129.42.xml"
SENSOR_LIST = ROOT / "research/evidence/sprint_4k_mendota_authorised_access/acquisition/129.42/List_of_sensors_used_on_the_Lake_Mendota_buoy_since_2006__edddc490dfd553c4c4b9e5d4b86eb2eb.dat"
OUT = ROOT / "research/evidence/sprint_4l9_mendota_daily_sensor_raw_audit"
T = OUT / "tables"
T.mkdir(parents=True, exist_ok=True)

# expected baseline from Sprint 4L.8A
EXPECTED = {
    "bytes": 490187,
    "md5": "eb7b3a3848b27074bac4504236ccefc3",
    "sha1": "bb1d8a281a3d580cad45549551abdbaed1ae03fe",
    "sha256": "104ef1b33769bc0ad1d3e9e6dff28219b743b81ce89ee888460d2df255981343",
    "rows": 3996,
    "columns": 38,
}

# variable, flag, role, unit, broad physical bounds used only to screen implausible values
VAR_FLAGS = [
    ("avg_air_temp", "flag_avg_air_temp", "air temperature", "celsius", (-60, 60)),
    ("avg_rel_hum", "flag_avg_rel_hum", "relative humidity", "percent", (0, 100)),
    ("avg_wind_speed", "flag_avg_wind_speed", "wind speed", "m/s", (0, 80)),
    ("avg_wind_dir", "flag_avg_wind_dir", "wind direction", "degree", (0, 360)),
    ("avg_chlor_rfu_turner", "flag_avg_chlor_rfu_turner", "chlorophyll Turner proxy", "RFU", (0, None)),
    ("avg_chlor_rfu_ysi", "flag_avg_chlor_rfu_ysi", "chlorophyll YSI proxy", "RFU", (0, None)),
    ("avg_phyco_rfu_turner", "flag_avg_phyco_rfu_turner", "phycocyanin Turner proxy", "RFU", (0, None)),
    ("avg_phyco_rfu_ysi", "flag_avg_phyco_rfu_ysi", "phycocyanin YSI proxy", "RFU", (0, None)),
    ("avg_par", "flag_avg_par", "PAR above water", "umol/m2/s", (0, None)),
    ("avg_par_below", "flag_avg_par_below", "PAR below water", "umol/m2/s", (0, None)),
    ("avg_do_wtemp", "flag_avg_do_wtemp", "water temperature (YSI DO sensor)", "celsius", (-5, 50)),
    ("avg_do_sat", "flag_avg_do_sat", "DO saturation", "percent", (0, 500)),
    ("avg_do_raw", "flag_avg_do_raw", "DO concentration", "mg/L", (0, 50)),
    ("avg_pco2_ppm", "flag_avg_pco2_ppm", "pCO2", "ppm", (0, None)),
    ("avg_ph", "flag_avg_ph", "pH", "pH units", (0, 14)),
    ("avg_fdom", "flag_avg_fdom", "fDOM", "RFU/QSU", (0, None)),
    ("avg_turbidity", "flag_avg_turbidity", "turbidity", "FNU", (0, 4000)),
    ("avg_spec_cond", "flag_avg_spec_cond", "specific conductance", "uS/cm", (0, 200000)),
]
VARIABLES = [v for v, _, _, _, _ in VAR_FLAGS]


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def pct(vals, p):
    if not vals:
        return None
    s = sorted(vals)
    k = (len(s) - 1) * p
    lo = int(math.floor(k))
    hi = int(math.ceil(k))
    return s[lo] if lo == hi else s[lo] * (hi - k) + s[hi] * (k - lo)


def rnd(x, n=6):
    return None if x is None else round(float(x), n)


def season(month):
    return "winter" if month in (12, 1, 2) else "spring" if month in (3, 4, 5) else "summer" if month in (6, 7, 8) else "autumn"


def write_csv(path, rows, fieldnames=None):
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    if fieldnames is None:
        fieldnames = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)


# ---------------------------------------------------------------- parse EML
def local(tag):
    return tag.split("}")[-1]


eml_root = ET.parse(EML).getroot()
daily_defs = {}
daily_codes = {}
for dt in eml_root.iter():
    if local(dt.tag) != "dataTable":
        continue
    obj = None
    for c in dt.iter():
        if local(c.tag) == "objectName":
            obj = (c.text or "").strip()
            break
    if obj != "ntl129_1_v16.csv":
        continue
    for attr in dt.iter():
        if local(attr.tag) != "attribute":
            continue
        name = None
        definition = None
        codes = []
        for c in attr.iter():
            if local(c.tag) == "attributeName":
                name = (c.text or "").strip()
            elif local(c.tag) == "attributeDefinition":
                definition = (c.text or "").strip()
            elif local(c.tag) == "code":
                codes.append((c.text or "").strip())
        if name:
            daily_defs[name] = definition or ""
            daily_codes[name] = codes

# ---------------------------------------------------------------- parse raw
raw_bytes = RAW.read_bytes()
size = len(raw_bytes)
md5 = hashlib.md5(raw_bytes).hexdigest()
sha1 = hashlib.sha1(raw_bytes).hexdigest()
sha = sha256_bytes(raw_bytes)
text = raw_bytes.decode("utf-8")
lines = text.splitlines()
header = next(csv.reader([lines[0]]))

rows = []
malformed = []
blank_lines = 0
with RAW.open(newline="", encoding="utf-8") as fh:
    reader = csv.reader(fh)
    header_file = next(reader)
    if header_file != header:
        raise SystemExit("Header changed between two parsing methods")
    for line_no, vals in enumerate(reader, 2):
        if not vals or (len(vals) == 1 and not vals[0].strip()):
            blank_lines += 1
            continue
        if len(vals) != len(header):
            malformed.append({"line": line_no, "fields": len(vals)})
            continue
        rows.append(dict(zip(header, vals)))

variables = [v for v, _, _, _, _ in VAR_FLAGS]
flag_columns = [f for _, f, _, _, _ in VAR_FLAGS]
expected_header = ["year4", "sampledate"] + [x for pair in zip(variables, flag_columns) for x in pair]
schema_ok = header == expected_header

dates = []
date_errors = []
year_mismatch = []
duplicate_dates = []
seen_dates = set()
exact_rows = Counter()
var_data = {
    v: {
        "numeric": [],
        "valid": [],
        "flagged": [],
        "missing": 0,
        "nonnumeric_nonempty": 0,
        "flag_without_value": 0,
        "empty_unflagged": 0,
        "dates_valid": set(),
        "flag_counts": Counter(),
        "flag_numeric": defaultdict(list),
        "flag_missing": Counter(),
        "outside_bounds": 0,
        "outside_unflagged": 0,
        "negative_any": 0,
        "negative_valid": 0,
    }
    for v in variables
}
flag_year = defaultdict(Counter)
annual = defaultdict(lambda: {
    "records": 0, "missing": 0, "numeric_any": 0, "valid": 0, "flagged": 0,
    "flag_without_value": 0, "empty_unflagged": 0, "flags": Counter(),
})
seasonal = defaultdict(lambda: {
    "records": 0, "missing": 0, "numeric_any": 0, "valid": 0, "flagged": 0,
    "flags": Counter(),
})

for r in rows:
    dstr = (r["sampledate"] or "").strip()
    try:
        d = datetime.strptime(dstr, "%Y-%m-%d").date()
    except Exception:
        date_errors.append(dstr)
        continue
    if dstr in seen_dates:
        duplicate_dates.append(dstr)
    seen_dates.add(dstr)
    dates.append(d)
    try:
        if int(r["year4"]) != d.year:
            year_mismatch.append((r["year4"], dstr))
    except Exception:
        year_mismatch.append((r["year4"], dstr))
    exact_rows[tuple(r[k] for k in header)] += 1

    for var, flag, role, unit, bounds in VAR_FLAGS:
        raw = (r[var] or "").strip()
        f = (r[flag] or "").strip()
        rec = var_data[var]
        rec["flag_counts"][f or "none"] += 1
        flag_year[(var, d.year)][f or "none"] += 1
        a = annual[(var, d.year)]
        s = seasonal[(var, season(d.month))]
        a["records"] += 1
        s["records"] += 1
        if f:
            a["flags"][f] += 1
            s["flags"][f] += 1
        if raw == "":
            rec["missing"] += 1
            a["missing"] += 1
            s["missing"] += 1
            rec["flag_missing"][f or "none"] += 1
            if f:
                rec["flag_without_value"] += 1
                a["flag_without_value"] += 1
            else:
                rec["empty_unflagged"] += 1
                a["empty_unflagged"] += 1
            continue
        try:
            x = float(raw)
        except ValueError:
            rec["nonnumeric_nonempty"] += 1
            rec["missing"] += 1
            a["missing"] += 1
            s["missing"] += 1
            rec["flag_missing"][f or "none"] += 1
            continue
        if not math.isfinite(x):
            rec["missing"] += 1
            a["missing"] += 1
            s["missing"] += 1
            rec["flag_missing"][f or "none"] += 1
            continue
        rec["numeric"].append(x)
        rec["flag_numeric"][f or "none"].append(x)
        a["numeric_any"] += 1
        s["numeric_any"] += 1
        if x < 0:
            rec["negative_any"] += 1
        if f:
            rec["flagged"].append(x)
            a["flagged"] += 1
            s["flagged"] += 1
        else:
            rec["valid"].append(x)
            rec["dates_valid"].add(dstr)
            a["valid"] += 1
            s["valid"] += 1
            if x < 0:
                rec["negative_valid"] += 1
        lo, hi = bounds
        outside = (lo is not None and x < lo) or (hi is not None and x > hi)
        if outside:
            rec["outside_bounds"] += 1
            if not f:
                rec["outside_unflagged"] += 1

# ---------------------------------------------------------------- coverage summary
summary = []
for var, flag, role, unit, bounds in VAR_FLAGS:
    rec = var_data[var]
    valid = rec["valid"]
    ds = sorted(rec["dates_valid"])
    gaps = [
        (datetime.strptime(b2, "%Y-%m-%d").date() - datetime.strptime(a2, "%Y-%m-%d").date()).days
        for a2, b2 in zip(ds, ds[1:])
    ]
    first = ds[0] if ds else ""
    last = ds[-1] if ds else ""
    flags = rec["flag_counts"]
    total = len(rows)
    summary.append({
        "variable": var,
        "role": role,
        "unit": unit,
        "flag_column": flag,
        "first_valid_unflagged": first,
        "last_valid_unflagged": last,
        "total_records": total,
        "missing": rec["missing"],
        "missing_pct": rnd(100 * rec["missing"] / total),
        "numeric_any": len(rec["numeric"]),
        "numeric_any_pct": rnd(100 * len(rec["numeric"]) / total),
        "valid_unflagged": len(valid),
        "valid_unflagged_pct": rnd(100 * len(valid) / total),
        "flagged_numeric": len(rec["flagged"]),
        "flag_without_value": rec["flag_without_value"],
        "empty_unflagged": rec["empty_unflagged"],
        "nonnumeric_nonempty": rec["nonnumeric_nonempty"],
        "unique_valid_dates": len(ds),
        "median_interval_days": rnd(statistics.median(gaps)) if gaps else "",
        "max_interval_days": max(gaps) if gaps else "",
        "gaps_gt_7": sum(g > 7 for g in gaps),
        "gaps_gt_14": sum(g > 14 for g in gaps),
        "gaps_gt_30": sum(g > 30 for g in gaps),
        "gaps_gt_60": sum(g > 60 for g in gaps),
        "gaps_gt_90": sum(g > 90 for g in gaps),
        "min": rnd(min(valid)) if valid else "",
        "p05": rnd(pct(valid, 0.05)) if valid else "",
        "median": rnd(statistics.median(valid)) if valid else "",
        "p95": rnd(pct(valid, 0.95)) if valid else "",
        "max": rnd(max(valid)) if valid else "",
        "outside_physical_bounds": rec["outside_bounds"],
        "outside_unflagged": rec["outside_unflagged"],
        "negative_any": rec["negative_any"],
        "negative_valid": rec["negative_valid"],
        "zero_valid": sum(1 for x in valid if x == 0),
        "flag_C": flags.get("C", 0),
        "flag_E": flags.get("E", 0),
        "flag_H": flags.get("H", 0),
        "flag_G": flags.get("G", 0),
        "flag_O": flags.get("O", 0),
        "flag_other": sum(n for k, n in flags.items() if k not in ("none", "C", "E", "H", "G", "O")),
        "flag_none": flags.get("none", 0),
    })
write_csv(T / "VARIABLE_COVERAGE_SUMMARY.csv", summary)


# ---------------------------------------------------------------- annual / seasonal
annual_rows = []
for (var, y), a in sorted(annual.items()):
    annual_rows.append({
        "variable": var,
        "year": y,
        "records": a["records"],
        "missing": a["missing"],
        "numeric_any": a["numeric_any"],
        "valid_unflagged": a["valid"],
        "flagged_numeric": a["flagged"],
        "flag_without_value": a["flag_without_value"],
        "empty_unflagged": a["empty_unflagged"],
        "valid_pct": rnd(100 * a["valid"] / a["records"]) if a["records"] else "",
        "flag_C": a["flags"].get("C", 0),
        "flag_E": a["flags"].get("E", 0),
        "flag_H": a["flags"].get("H", 0),
        "flag_G": a["flags"].get("G", 0),
        "flag_O": a["flags"].get("O", 0),
        "flag_other": sum(n for k, n in a["flags"].items() if k not in ("none", "C", "E", "H", "G", "O")),
    })
write_csv(T / "ANNUAL_VARIABLE_COVERAGE.csv", annual_rows)

season_rows = []
for (var, s), a in sorted(seasonal.items()):
    season_rows.append({
        "variable": var,
        "season": s,
        "records": a["records"],
        "missing": a["missing"],
        "numeric_any": a["numeric_any"],
        "valid_unflagged": a["valid"],
        "flagged_numeric": a["flagged"],
        "valid_pct": rnd(100 * a["valid"] / a["records"]) if a["records"] else "",
        "flag_C": a["flags"].get("C", 0),
        "flag_E": a["flags"].get("E", 0),
        "flag_H": a["flags"].get("H", 0),
        "flag_G": a["flags"].get("G", 0),
        "flag_O": a["flags"].get("O", 0),
        "flag_other": sum(n for k, n in a["flags"].items() if k not in ("none", "C", "E", "H", "G", "O")),
    })
write_csv(T / "SEASONAL_VARIABLE_COVERAGE.csv", season_rows)


# ---------------------------------------------------------------- intervals
gap_rows = []
interval_rows = []
for var, _, _, _, _ in VAR_FLAGS:
    ds = sorted(var_data[var]["dates_valid"])
    gaps = [
        (datetime.strptime(b2, "%Y-%m-%d").date() - datetime.strptime(a2, "%Y-%m-%d").date()).days
        for a2, b2 in zip(ds, ds[1:])
    ]
    for a2, b2, g in zip(ds, ds[1:], gaps):
        if g > 7:
            gap_rows.append({
                "variable": var, "from_date": a2, "to_date": b2, "gap_days": g,
                "gt_14": g > 14, "gt_30": g > 30, "gt_60": g > 60, "gt_90": g > 90,
            })
    buckets = {
        "interval_1d": sum(g == 1 for g in gaps),
        "interval_2_7d": sum(2 <= g <= 7 for g in gaps),
        "interval_8_14d": sum(8 <= g <= 14 for g in gaps),
        "interval_15_30d": sum(15 <= g <= 30 for g in gaps),
        "interval_31_60d": sum(31 <= g <= 60 for g in gaps),
        "interval_61_90d": sum(61 <= g <= 90 for g in gaps),
        "interval_gt_90d": sum(g > 90 for g in gaps),
    }
    interval_rows.append({
        "variable": var,
        "valid_dates": len(ds),
        "intervals": len(gaps),
        **buckets,
        "median_interval_days": rnd(statistics.median(gaps)) if gaps else "",
        "max_interval_days": max(gaps) if gaps else "",
    })
write_csv(
    T / "SAMPLING_INTERVALS_AND_GAPS.csv",
    gap_rows,
    ["variable", "from_date", "to_date", "gap_days", "gt_14", "gt_30", "gt_60", "gt_90"],
)
write_csv(T / "INTERVAL_DISTRIBUTION.csv", interval_rows)


# ---------------------------------------------------------------- QC by variable/year
qc_rows = []
for (var, y), c in sorted(flag_year.items()):
    a = annual[(var, y)]
    total = sum(c.values())
    any_flag = sum(n for k, n in c.items() if k != "none")
    qc_rows.append({
        "variable": var,
        "year": y,
        "records": total,
        "missing": a["missing"],
        "numeric_any": a["numeric_any"],
        "valid_unflagged": a["valid"],
        "flagged_numeric": a["flagged"],
        "flag_without_value": a["flag_without_value"],
        "empty_unflagged": a["empty_unflagged"],
        "flag_C": c.get("C", 0),
        "flag_E": c.get("E", 0),
        "flag_H": c.get("H", 0),
        "flag_G": c.get("G", 0),
        "flag_O": c.get("O", 0),
        "flag_other": sum(n for k, n in c.items() if k not in ("none", "C", "E", "H", "G", "O")),
        "flag_none": c.get("none", 0),
        "any_flag": any_flag,
        "pct_C": rnd(100 * c.get("C", 0) / total) if total else "",
        "pct_E": rnd(100 * c.get("E", 0) / total) if total else "",
        "pct_H": rnd(100 * c.get("H", 0) / total) if total else "",
        "pct_G": rnd(100 * c.get("G", 0) / total) if total else "",
        "pct_O": rnd(100 * c.get("O", 0) / total) if total else "",
        "pct_any_flag": rnd(100 * any_flag / total) if total else "",
        "pct_valid_unflagged": rnd(100 * a["valid"] / total) if total else "",
        "pct_flag_blank": rnd(100 * c.get("none", 0) / total) if total else "",
    })
write_csv(T / "QC_FLAG_DISTRIBUTIONS.csv", qc_rows)

# ---------------------------------------------------------------- flag-value distributions
flag_value_rows = []
for var, flag, role, unit, bounds in VAR_FLAGS:
    rec = var_data[var]
    for code in ["C", "E", "H", "G", "O", "none"]:
        vals = rec["flag_numeric"].get(code, [])
        flag_value_rows.append({
            "variable": var,
            "flag": code,
            "n_records": rec["flag_counts"].get(code, 0),
            "n_numeric": len(vals),
            "n_missing": rec["flag_missing"].get(code, 0),
            "min": rnd(min(vals)) if vals else "",
            "p05": rnd(pct(vals, 0.05)) if vals else "",
            "median": rnd(statistics.median(vals)) if vals else "",
            "p95": rnd(pct(vals, 0.95)) if vals else "",
            "max": rnd(max(vals)) if vals else "",
        })
write_csv(T / "FLAGGED_VALUE_DISTRIBUTIONS.csv", flag_value_rows)

# ---------------------------------------------------------------- flag top years
top_year_rows = []
for var, _, _, _, _ in VAR_FLAGS:
    for code in ["C", "E", "H", "G", "O"]:
        entries = []
        for (v, y), c in flag_year.items():
            if v == var and c.get(code, 0):
                entries.append((y, c[code]))
        entries.sort(key=lambda x: (-x[1], x[0]))
        if entries:
            top_year_rows.append({
                "variable": var,
                "flag": code,
                "total": sum(n for _, n in entries),
                "top_years": ";".join(f"{y}:{n}" for y, n in entries[:3]),
            })
write_csv(T / "QC_FLAG_TOP_YEARS.csv", top_year_rows)


# ---------------------------------------------------------------- sensor era
era_rows = []
for var, flag, role, unit, bounds in VAR_FLAGS:
    for label, lo, hi in [("pre_2019", "0000-01-01", "2018-12-31"), ("2019_plus", "2019-01-01", "9999-12-31")]:
        vals = []
        flags = Counter()
        recs = 0
        missing = 0
        numeric_any = 0
        for r in rows:
            d = r["sampledate"]
            if not (lo <= d <= hi):
                continue
            recs += 1
            f = (r[flag] or "").strip()
            flags[f or "none"] += 1
            raw = (r[var] or "").strip()
            if raw == "":
                missing += 1
                continue
            try:
                x = float(raw)
            except Exception:
                missing += 1
                continue
            if not math.isfinite(x):
                missing += 1
                continue
            numeric_any += 1
            if f:
                continue
            vals.append(x)
        era_rows.append({
            "variable": var,
            "period": label,
            "records": recs,
            "missing": missing,
            "numeric_any": numeric_any,
            "valid_unflagged": len(vals),
            "valid_pct": rnd(100 * len(vals) / recs) if recs else "",
            "median": rnd(statistics.median(vals)) if vals else "",
            "p05": rnd(pct(vals, 0.05)) if vals else "",
            "p95": rnd(pct(vals, 0.95)) if vals else "",
            "max": rnd(max(vals)) if vals else "",
            "flag_C": flags.get("C", 0),
            "flag_E": flags.get("E", 0),
            "flag_H": flags.get("H", 0),
            "flag_G": flags.get("G", 0),
            "flag_O": flags.get("O", 0),
            "pct_any_flag": rnd(100 * sum(n for k, n in flags.items() if k != "none") / recs) if recs else "",
        })
write_csv(T / "SENSOR_ERA_SUMMARY.csv", era_rows)

# ---------------------------------------------------------------- Turner vs YSI paired overlap
turner_ysi = []
for vt, vy, label in [
    ("avg_chlor_rfu_turner", "avg_chlor_rfu_ysi", "chlorophyll"),
    ("avg_phyco_rfu_turner", "avg_phyco_rfu_ysi", "phycocyanin"),
]:
    pairs = []
    dates_both = set()
    for r in rows:
        ft = (r["flag_" + vt] or "").strip()
        fy = (r["flag_" + vy] or "").strip()
        if ft or fy:
            continue
        try:
            a = float(r[vt])
            b = float(r[vy])
        except Exception:
            continue
        if math.isfinite(a) and math.isfinite(b):
            pairs.append((a, b))
            dates_both.add(r["sampledate"])
    ratios = [b / a for a, b in pairs if a]
    turner_ysi.append({
        "variable": label,
        "paired_dates": len(dates_both),
        "paired_records": len(pairs),
        "turner_median": rnd(statistics.median([a for a, b in pairs])) if pairs else "",
        "ysi_median": rnd(statistics.median([b for a, b in pairs])) if pairs else "",
        "turner_p05": rnd(pct([a for a, b in pairs], 0.05)) if pairs else "",
        "turner_p95": rnd(pct([a for a, b in pairs], 0.95)) if pairs else "",
        "ysi_p05": rnd(pct([b for a, b in pairs], 0.05)) if pairs else "",
        "ysi_p95": rnd(pct([b for a, b in pairs], 0.95)) if pairs else "",
        "median_difference_ysi_minus_turner": rnd(statistics.median([b - a for a, b in pairs])) if pairs else "",
        "median_ratio_ysi_over_turner": rnd(statistics.median(ratios)) if ratios else "",
        "p05_ratio": rnd(pct(ratios, 0.05)) if ratios else "",
        "p95_ratio": rnd(pct(ratios, 0.95)) if ratios else "",
        "first_date": min(dates_both) if dates_both else "",
        "last_date": max(dates_both) if dates_both else "",
    })
write_csv(T / "TURNER_YSI_OVERLAP.csv", turner_ysi)


# ---------------------------------------------------------------- anomaly audit
anomaly_rows = []
for var, flag, role, unit, bounds in VAR_FLAGS:
    rec = var_data[var]
    outside_examples = []
    negative_examples = []
    for r in rows:
        raw = (r[var] or "").strip()
        if raw == "":
            continue
        try:
            x = float(raw)
        except Exception:
            continue
        if not math.isfinite(x):
            continue
        f = (r[flag] or "").strip()
        lo, hi = bounds
        if (lo is not None and x < lo) or (hi is not None and x > hi):
            if len(outside_examples) < 8:
                outside_examples.append(f"{r['sampledate']}={x:g}({f or 'unflagged'})")
        if x < 0 and len(negative_examples) < 8:
            negative_examples.append(f"{r['sampledate']}={x:g}({f or 'unflagged'})")
    anomaly_rows.append({
        "variable": var,
        "unit": unit,
        "bounds_low": bounds[0] if bounds[0] is not None else "",
        "bounds_high": bounds[1] if bounds[1] is not None else "",
        "outside_physical_bounds": rec["outside_bounds"],
        "outside_unflagged": rec["outside_unflagged"],
        "negative_any": rec["negative_any"],
        "negative_valid": rec["negative_valid"],
        "zero_valid": sum(1 for x in rec["valid"] if x == 0),
        "outside_examples": "; ".join(outside_examples),
        "negative_examples": "; ".join(negative_examples),
    })
write_csv(T / "ANOMALY_AUDIT.csv", anomaly_rows)


# ---------------------------------------------------------------- biology dates
bio_rows = []
with BIO.open(newline="", encoding="utf-8") as fh:
    for r in csv.DictReader(fh):
        if r["lakeid"] == "ME":
            bio_rows.append(r)
bio_dates = sorted({r["sampledate"] for r in bio_rows})
bio_set = set(bio_dates)
bio_depth_by_date = defaultdict(set)
bio_station_by_date = defaultdict(set)
for r in bio_rows:
    bio_depth_by_date[r["sampledate"]].add(r["depth_range"])
    bio_station_by_date[r["sampledate"]].add((r["sta"] or "").strip())
bio_date_objs = [datetime.strptime(d, "%Y-%m-%d").date() for d in bio_dates]
bio_gaps = [(b - a).days for a, b in zip(bio_date_objs, bio_date_objs[1:])]
bio_summary = {
    "records": len(bio_rows),
    "dates": len(bio_dates),
    "first_date": bio_dates[0] if bio_dates else "",
    "last_date": bio_dates[-1] if bio_dates else "",
    "median_interval_days": rnd(statistics.median(bio_gaps)) if bio_gaps else "",
    "dates_0_8m": sum(1 for d in bio_dates if bio_depth_by_date[d] == {"0-8m"}),
    "dates_0_2m": sum(1 for d in bio_dates if bio_depth_by_date[d] == {"0-2m"}),
    "dates_with_any_station": sum(1 for d in bio_dates if any(s for s in bio_station_by_date[d])),
    "dates_all_station_blank": sum(1 for d in bio_dates if not any(s for s in bio_station_by_date[d])),
    "year_counts": dict(sorted(Counter(d[:4] for d in bio_dates).items())),
}

# same-day and window overlap
row_by_date = {r["sampledate"]: r for r in rows}
overlap = []
by_year = []
by_season = []
window_rows = []
for var, flag, role, unit, bounds in VAR_FLAGS:
    ds = sorted(var_data[var]["dates_valid"])
    first = ds[0] if ds else ""
    last = ds[-1] if ds else ""
    within = [d for d in bio_dates if first <= d <= last] if ds else []
    valid_set = var_data[var]["dates_valid"]

    same_absent = 0
    same_present = 0
    same_missing = 0
    same_missing_flagged = 0
    same_missing_unflagged = 0
    same_any = 0
    same_flagged = 0
    same_valid = 0
    for d in within:
        r = row_by_date.get(d)
        if r is None:
            same_absent += 1
            continue
        same_present += 1
        raw = (r[var] or "").strip()
        f = (r[flag] or "").strip()
        if raw == "":
            same_missing += 1
            if f:
                same_missing_flagged += 1
            else:
                same_missing_unflagged += 1
            continue
        try:
            x = float(raw)
        except Exception:
            same_missing += 1
            if f:
                same_missing_flagged += 1
            else:
                same_missing_unflagged += 1
            continue
        if not math.isfinite(x):
            same_missing += 1
            if f:
                same_missing_flagged += 1
            else:
                same_missing_unflagged += 1
            continue
        same_any += 1
        if f:
            same_flagged += 1
        else:
            same_valid += 1

    def window_any(d, days):
        dd = datetime.strptime(d, "%Y-%m-%d").date()
        for k in range(-days, days + 1):
            if (dd + timedelta(days=k)).isoformat() in valid_set:
                return True
        return False

    windows = {}
    for days in (1, 3, 7, 14):
        windows[days] = sum(1 for d in within if window_any(d, days))

    overlap.append({
        "variable": var,
        "role": role,
        "first_valid_unflagged": first,
        "last_valid_unflagged": last,
        "biology_dates_total": len(bio_dates),
        "biology_dates_within_valid_span": len(within),
        "same_day_date_absent": same_absent,
        "same_day_record_present": same_present,
        "same_day_variable_missing": same_missing,
        "same_day_missing_flagged": same_missing_flagged,
        "same_day_missing_unflagged": same_missing_unflagged,
        "same_day_any_numeric": same_any,
        "same_day_valid_unflagged": same_valid,
        "same_day_flagged_numeric": same_flagged,
        "same_day_missing_or_absent": same_absent + same_missing,
        "pct_same_day_valid_of_total": rnd(100 * same_valid / len(bio_dates)) if bio_dates else "",
        "pct_same_day_valid_of_within": rnd(100 * same_valid / len(within)) if within else "",
        "valid_within_pm1_days": windows[1],
        "valid_within_pm3_days": windows[3],
        "valid_within_pm7_days": windows[7],
        "valid_within_pm14_days": windows[14],
        "pct_pm1_of_total": rnd(100 * windows[1] / len(bio_dates)) if bio_dates else "",
        "pct_pm3_of_total": rnd(100 * windows[3] / len(bio_dates)) if bio_dates else "",
        "pct_pm7_of_total": rnd(100 * windows[7] / len(bio_dates)) if bio_dates else "",
        "pct_pm14_of_total": rnd(100 * windows[14] / len(bio_dates)) if bio_dates else "",
        "pct_pm3_of_within": rnd(100 * windows[3] / len(within)) if within else "",
        "pct_pm7_of_within": rnd(100 * windows[7] / len(within)) if within else "",
    })
    window_rows.append({
        "variable": var,
        "within_valid_span": len(within),
        "same_day_valid": same_valid,
        "pm1_valid": windows[1],
        "pm3_valid": windows[3],
        "pm7_valid": windows[7],
        "pm14_valid": windows[14],
        "pct_same_day_of_total": rnd(100 * same_valid / len(bio_dates)) if bio_dates else "",
        "pct_pm1_of_total": rnd(100 * windows[1] / len(bio_dates)) if bio_dates else "",
        "pct_pm3_of_total": rnd(100 * windows[3] / len(bio_dates)) if bio_dates else "",
        "pct_pm7_of_total": rnd(100 * windows[7] / len(bio_dates)) if bio_dates else "",
        "pct_pm14_of_total": rnd(100 * windows[14] / len(bio_dates)) if bio_dates else "",
    })
    for y in range(1995, 2021):
        bd = [d for d in within if d.startswith(str(y))]
        sv = sum(1 for d in bd if d in valid_set)
        sa = sum(1 for d in bd if d in row_by_date and (row_by_date[d][var] or "").strip())
        by_year.append({
            "variable": var, "year": y, "biology_dates": len(bd),
            "same_day_any_numeric": sa, "same_day_valid": sv,
            "pct_same_day_valid": rnd(100 * sv / len(bd)) if bd else "",
        })
    for s in ["winter", "spring", "summer", "autumn"]:
        bd = [d for d in within if season(datetime.strptime(d, "%Y-%m-%d").month) == s]
        sv = sum(1 for d in bd if d in valid_set)
        by_season.append({
            "variable": var, "season": s, "biology_dates": len(bd),
            "same_day_valid": sv, "pct_same_day_valid": rnd(100 * sv / len(bd)) if bd else "",
        })

write_csv(T / "BIOLOGICAL_OVERLAP.csv", overlap)
write_csv(T / "BIOLOGICAL_OVERLAP_WINDOWS.csv", window_rows)
write_csv(T / "BIOLOGICAL_OVERLAP_BY_YEAR.csv", by_year)
write_csv(T / "BIOLOGICAL_OVERLAP_BY_SEASON.csv", by_season)


# ---------------------------------------------------------------- schema audit
schema_rows = []
for i, h in enumerate(header):
    role = "date" if h in ("year4", "sampledate") else ("flag" if h.startswith("flag_") else "variable")
    if h == "year4":
        dtype = "integer"
        parse_errors = len(year_mismatch)
        nonempty = len(rows)
        missing = 0
        invalid_codes = 0
    elif h == "sampledate":
        dtype = "ISO date"
        parse_errors = len(date_errors)
        nonempty = len(rows)
        missing = 0
        invalid_codes = 0
    elif role == "flag":
        dtype = "string/flag"
        nonempty = sum(1 for r in rows if (r[h] or "").strip())
        missing = len(rows) - nonempty
        allowed = set(daily_codes.get(h, []))
        invalid_codes = sum(1 for r in rows if (r[h] or "").strip() and (r[h] or "").strip() not in allowed)
        parse_errors = 0
    else:
        dtype = "float"
        nonempty = sum(1 for r in rows if (r[h] or "").strip())
        missing = len(rows) - nonempty
        parse_errors = var_data[h]["nonnumeric_nonempty"]
        invalid_codes = 0
    schema_rows.append({
        "position": i + 1,
        "column": h,
        "role": role,
        "dtype": dtype,
        "definition": daily_defs.get(h, ""),
        "documented_codes": ",".join(daily_codes.get(h, [])),
        "nonempty": nonempty,
        "missing": missing,
        "parse_errors": parse_errors,
        "undocumented_flag_values": invalid_codes,
    })
write_csv(T / "SCHEMA_AUDIT.csv", schema_rows)


# ---------------------------------------------------------------- source-derived tables
# sensor inventory + observed coverage
sensor_rows = []
sensor_to_vars = {
    "DO": ["avg_do_raw", "avg_do_sat", "avg_do_wtemp"],
    "CO2": ["avg_pco2_ppm"],
    "pH": ["avg_ph"],
    "fDOM": ["avg_fdom"],
    "Turbidity": ["avg_turbidity"],
    "Chlor/Phyco": ["avg_chlor_rfu_turner", "avg_phyco_rfu_turner", "avg_chlor_rfu_ysi", "avg_phyco_rfu_ysi"],
    "Conductivity": ["avg_spec_cond"],
    "Water Temp": ["avg_do_wtemp"],
    "Temp/RH": ["avg_air_temp", "avg_rel_hum"],
    "Wind": ["avg_wind_speed", "avg_wind_dir"],
    "PAR-above": ["avg_par"],
    "PAR-below": ["avg_par_below"],
}
if SENSOR_LIST.exists():
    with SENSOR_LIST.open(newline="", encoding="utf-8") as fh:
        for s in csv.DictReader(fh):
            param = (s.get("parameter") or "").strip()
            model = (s.get("sensor_model") or "").strip()
            mfg = (s.get("sensor_mfg") or "").strip()
            began = (s.get("date_began") or "").strip()
            ended = (s.get("date_ended") or "").strip()
            mapped = sensor_to_vars.get(param, [])
            if param == "Chlor/Phyco":
                if "Turner" in mfg:
                    mapped = ["avg_chlor_rfu_turner", "avg_phyco_rfu_turner"]
                elif "YSI" in mfg:
                    mapped = ["avg_chlor_rfu_ysi", "avg_phyco_rfu_ysi"]
            note = ""
            if param == "DO" and began == "2016":
                note = "Daily DO values exist from 2006; sensor inventory does not list a 2006-2015 DO model."
            elif param == "CO2" and began == "2017":
                note = "Daily pCO2 values begin 2016-03-22, earlier than the inventory's 2017 start."
            elif param == "PAR-above" and began == "2016":
                note = "Sparse unflagged PAR near-zero values (ten 0.0, one 0.002) occur in 2007 before the inventory's 2016 start."
            elif param == "Water Temp":
                note = "No separate daily water-temperature column; avg_do_wtemp is labelled YSI water temp but exists from 2006."
            elif param == "Conductivity" and ended == "2006":
                note = "2006 conductivity values are flagged H/O; no unflagged 2006 value."
            elif param == "IR Skin Temp":
                note = "No daily skin-temperature column in the daily entity."
            mapped_summaries = [next((x for x in summary if x["variable"] == var), None) for var in mapped]
            mapped_summaries = [x for x in mapped_summaries if x]
            firsts = [x["first_valid_unflagged"] for x in mapped_summaries if x["first_valid_unflagged"]]
            lasts = [x["last_valid_unflagged"] for x in mapped_summaries if x["last_valid_unflagged"]]
            sensor_rows.append({
                "parameter": param,
                "sensor_mfg": mfg,
                "sensor_model": model,
                "date_began": began,
                "date_ended": ended,
                "daily_variables": "; ".join(mapped),
                "observed_first_unflagged": min(firsts) if firsts else "",
                "observed_last_unflagged": max(lasts) if lasts else "",
                "observed_valid_unflagged_sum": sum(int(x["valid_unflagged"]) for x in mapped_summaries),
                "coverage_note": "Column-level observed coverage; not proof this sensor produced every listed date.",
                "note": note,
            })
write_csv(T / "SENSOR_TRANSITIONS.csv", sensor_rows)

# depth compatibility
depth_rows = [
    ("avg_chlor_rfu_turner", "0.5 m", "chlorophyll RFU", "0-8 m composite", "weak/conditional", "surface point vs column composite; Turner-only era"),
    ("avg_chlor_rfu_ysi", "0.5 m", "chlorophyll RFU", "0-8 m composite", "weak/conditional", "surface point vs column composite; YSI-era only"),
    ("avg_phyco_rfu_turner", "0.5 m", "phycocyanin RFU", "0-8 m composite", "weak/conditional", "surface point vs column composite; Turner-only era"),
    ("avg_phyco_rfu_ysi", "0.5 m", "phycocyanin RFU", "0-8 m composite", "weak/conditional", "surface point vs column composite; YSI-era only"),
    ("avg_do_wtemp", "0.5 m", "water temperature", "0-8 m composite", "weak/conditional", "surface point vs column composite; pre-2019 provenance ambiguous"),
    ("avg_do_sat", "0.5 m", "DO % saturation", "0-8 m composite", "weak/conditional", "surface point vs column composite"),
    ("avg_do_raw", "0.5 m", "DO mg/L", "0-8 m composite", "weak/conditional", "surface point vs column composite"),
    ("avg_ph", "0.5 m", "pH", "0-8 m composite", "weak/conditional", "surface point vs column composite; short overlap"),
    ("avg_spec_cond", "0.5 m", "specific conductance", "0-8 m composite", "weak/conditional", "surface point vs column composite; short overlap"),
    ("avg_turbidity", "0.5 m", "turbidity", "0-8 m composite", "weak/conditional", "surface point vs column composite; short overlap"),
    ("avg_fdom", "0.5 m", "fDOM", "0-8 m composite", "weak/conditional", "surface point vs column composite; short overlap"),
    ("avg_pco2_ppm", "1 m", "pCO2", "0-8 m composite", "weak/conditional", "single depth; no direct biological counterpart"),
    ("avg_par_below", "1 m", "underwater PAR", "0-8 m composite", "weak/conditional", "light context, not biomass; short overlap"),
    ("avg_par", "2 m above water", "above-water PAR", "0-8 m composite", "not comparable", "atmospheric context"),
    ("avg_air_temp", "2 m above water", "air temperature", "0-8 m composite", "not comparable", "atmospheric context"),
    ("avg_rel_hum", "2 m above water", "relative humidity", "0-8 m composite", "not comparable", "atmospheric context"),
    ("avg_wind_speed", "3 m above water", "wind speed", "0-8 m composite", "not comparable", "atmospheric context"),
    ("avg_wind_dir", "3 m above water", "wind direction", "0-8 m composite", "not comparable", "atmospheric context"),
]
write_csv(
    T / "DEPTH_COMPATIBILITY.csv",
    [
        {
            "variable": v, "sensor_depth": d, "measurement": m, "biological_reference": b,
            "classification": c, "reason": r,
        }
        for v, d, m, b, c, r in depth_rows
    ],
)

# feasibility matrix
feasibility_rows = [
    {
        "use": "A. Exploratory seasonal ecological analysis",
        "verdict": "SUPPORTED WITH MAJOR LIMITATIONS",
        "evidence": "3,996 daily records, 2006-2025; open-water seasonal coverage; 18 variables; meteorology/water temp/DO/chlorophyll/phycocyanin have multi-year records.",
        "limitations": "Not year-round; variable-specific gaps; flag/missingness; sensor-era changes; Turner/YSI non-comparability.",
    },
    {
        "use": "B. Descriptive comparison with microscopy cyanobacteria",
        "verdict": "PARTIALLY SUPPORTED / EXPLORATORY ONLY",
        "evidence": "402 Mendota microscopy dates; 128 Turner chlorophyll and 139 Turner phycocyanin same-day unflagged dates; 94-99 same-day DO/water-temp dates.",
        "limitations": "0.5 m sensor vs 0-8 m composite; RFU proxies; 14-day biology; no sampling time; YSI era only 21-22 same-day dates; no causal inference.",
    },
    {
        "use": "C. Multivariate environmental relationships over time",
        "verdict": "LIMITED / NOT ROBUSTLY SUPPORTED",
        "evidence": "Multiple co-measured variables; 2019-2020 short overlap for pH/fDOM/turbidity/conductance.",
        "limitations": "Collinearity, missingness, flags, era discontinuities, sparse biology, short overlap; descriptive only.",
    },
    {
        "use": "D. Eventual early-warning evaluation",
        "verdict": "NOT SUPPORTED",
        "evidence": "Daily environmental series exist.",
        "limitations": "No bloom/non-bloom labels or event intervals; 14-day biology; no time-of-day; surface vs composite; proxies not independent; no pre-bloom design.",
    },
]
write_csv(T / "FEASIBILITY_MATRIX.csv", feasibility_rows)


# ---------------------------------------------------------------- validation
checks = []


def check(name, expected, actual, passed, note=""):
    checks.append({
        "check": name, "expected": expected, "actual": actual,
        "pass": bool(passed), "note": note,
    })


check("raw bytes", EXPECTED["bytes"], size, size == EXPECTED["bytes"])
check("raw MD5", EXPECTED["md5"], md5, md5 == EXPECTED["md5"])
check("raw SHA-1", EXPECTED["sha1"], sha1, sha1 == EXPECTED["sha1"])
check("raw SHA-256", EXPECTED["sha256"], sha, sha == EXPECTED["sha256"])
check("data rows", EXPECTED["rows"], len(rows), len(rows) == EXPECTED["rows"])
check("columns", EXPECTED["columns"], len(header), len(header) == EXPECTED["columns"])
check("schema order", True, schema_ok, schema_ok)
check("malformed rows", 0, len(malformed), len(malformed) == 0)
check("blank lines", 0, blank_lines, blank_lines == 0)
check("date parse errors", 0, len(date_errors), len(date_errors) == 0)
check("duplicate dates", 0, len(duplicate_dates), len(duplicate_dates) == 0)
check("year mismatches", 0, len(year_mismatch), len(year_mismatch) == 0)
check("exact duplicate rows", 0, sum(v - 1 for v in exact_rows.values() if v > 1), sum(v - 1 for v in exact_rows.values() if v > 1) == 0)
check("nonnumeric nonempty values", 0, sum(x["nonnumeric_nonempty"] for x in summary), sum(x["nonnumeric_nonempty"] for x in summary) == 0)

arithmetic_ok = True
for r in summary:
    total = int(r["total_records"])
    if int(r["missing"]) + int(r["numeric_any"]) != total:
        arithmetic_ok = False
    if int(r["valid_unflagged"]) + int(r["flagged_numeric"]) != int(r["numeric_any"]):
        arithmetic_ok = False
    flags = sum(int(r["flag_" + k]) for k in ["C", "E", "H", "G", "O"]) + int(r["flag_other"]) + int(r["flag_none"])
    if flags != total:
        arithmetic_ok = False
check("coverage arithmetic", True, arithmetic_ok, arithmetic_ok)

overlap_ok = True
for r in overlap:
    if int(r["same_day_valid_unflagged"]) + int(r["same_day_flagged_numeric"]) != int(r["same_day_any_numeric"]):
        overlap_ok = False
    if int(r["same_day_any_numeric"]) + int(r["same_day_variable_missing"]) != int(r["same_day_record_present"]):
        overlap_ok = False
    if int(r["same_day_record_present"]) + int(r["same_day_date_absent"]) != int(r["biology_dates_within_valid_span"]):
        overlap_ok = False
    if not (int(r["valid_within_pm1_days"]) <= int(r["valid_within_pm3_days"]) <= int(r["valid_within_pm7_days"]) <= int(r["valid_within_pm14_days"])):
        overlap_ok = False
check("overlap arithmetic and window monotonicity", True, overlap_ok, overlap_ok)

pct_ok = True
for r in summary:
    for k in ("missing_pct", "numeric_any_pct", "valid_unflagged_pct"):
        if r[k] != "" and not (0 <= float(r[k]) <= 100):
            pct_ok = False
for r in overlap:
    for k in ("pct_same_day_valid_of_total", "pct_same_day_valid_of_within", "pct_pm1_of_total", "pct_pm3_of_total", "pct_pm7_of_total", "pct_pm14_of_total", "pct_pm3_of_within", "pct_pm7_of_within"):
        if r[k] != "" and not (0 <= float(r[k]) <= 100):
            pct_ok = False
check("percentages in 0-100", True, pct_ok, pct_ok)

# undocumented flag codes against daily EML
undocumented = []
for var, flag, role, unit, bounds in VAR_FLAGS:
    allowed = set(daily_codes.get(flag, []))
    actual = {k for k in var_data[var]["flag_counts"] if k != "none"}
    extra = sorted(actual - allowed)
    if extra:
        undocumented.append({"variable": var, "flag_column": flag, "documented": sorted(allowed), "observed_extra": extra})
check("undocumented flag codes", "none", len(undocumented), len(undocumented) == 0, "See UNDOCUMENTED_FLAGS.csv; daily EML code lists are incomplete for several columns.")

write_csv(T / "UNDOCUMENTED_FLAGS.csv", undocumented)

validation = {
    "checks": checks,
    "passed": sum(1 for c in checks if c["pass"]),
    "failed": sum(1 for c in checks if not c["pass"]),
    "documented_flag_exceptions": undocumented,
}
(OUT / "VALIDATION.json").write_text(json.dumps(validation, indent=2), encoding="utf-8")

summary_json = {
    "file": {
        "bytes": size,
        "md5": md5,
        "sha1": sha1,
        "sha256": sha,
        "header_columns": len(header),
        "rows": len(rows),
        "malformed": len(malformed),
        "blank_lines": blank_lines,
        "date_errors": len(date_errors),
        "duplicate_dates": len(duplicate_dates),
        "exact_duplicate_rows": sum(v - 1 for v in exact_rows.values() if v > 1),
        "year_mismatches": len(year_mismatch),
        "schema_ok": schema_ok,
        "date_min": min(dates).isoformat() if dates else "",
        "date_max": max(dates).isoformat() if dates else "",
        "unique_dates": len(set(dates)),
        "years": sorted(set(d.year for d in dates)),
        "calendar_span_days": (max(dates) - min(dates)).days + 1 if dates else None,
        "record_fraction_of_span": rnd(len(rows) / ((max(dates) - min(dates)).days + 1)) if dates else None,
        "month_counts": dict(sorted(Counter(d.strftime("%m") for d in dates).items())),
    },
    "eml": {
        "bytes": len(EML.read_bytes()),
        "sha256": sha256_bytes(EML.read_bytes()),
        "daily_attributes": len(daily_defs),
    },
    "biology": bio_summary,
    "variables": summary,
    "era": era_rows,
    "turner_ysi": turner_ysi,
    "overlap": overlap,
    "windows": window_rows,
    "validation": {
        "passed": validation["passed"],
        "failed": validation["failed"],
        "checks": checks,
    },
}
(OUT / "summary.json").write_text(json.dumps(summary_json, indent=2, default=str), encoding="utf-8")

print(json.dumps({
    "file": summary_json["file"],
    "biology": bio_summary,
    "validation": summary_json["validation"],
    "undocumented_flags": undocumented,
}, indent=2, default=str))
