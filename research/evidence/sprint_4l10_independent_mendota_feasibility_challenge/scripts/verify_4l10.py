#!/usr/bin/env python3
"""Sprint 4L.10 independent recalculation of the Mendota 4L.9 audit.

This script deliberately does not import the Sprint 4L.9 audit code.
It parses the raw daily and biology files directly, recomputes the key
counts, and compares them with the Sprint 4L.9 tables. A second method
(SQLite) independently recomputes the same core counts.

No raw file is modified. No labels, event intervals, models or hypothesis
tests are created.
"""
import csv
import hashlib
import json
import math
import re
import sqlite3
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
L9 = ROOT / "research/evidence/sprint_4l9_mendota_daily_sensor_raw_audit"
OUT = ROOT / "research/evidence/sprint_4l10_independent_mendota_feasibility_challenge"
T = OUT / "tables"
T.mkdir(parents=True, exist_ok=True)

VARS = [
    "avg_air_temp", "avg_rel_hum", "avg_wind_speed", "avg_wind_dir",
    "avg_chlor_rfu_turner", "avg_chlor_rfu_ysi",
    "avg_phyco_rfu_turner", "avg_phyco_rfu_ysi",
    "avg_par", "avg_par_below", "avg_do_wtemp", "avg_do_sat", "avg_do_raw",
    "avg_pco2_ppm", "avg_ph", "avg_fdom", "avg_turbidity", "avg_spec_cond",
]
FLAG = {v: "flag_" + v for v in VARS}


def sha256_file(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


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


def fnum(x):
    if x is None or x == "":
        return None
    try:
        v = float(x)
    except Exception:
        return None
    return v if math.isfinite(v) else None


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


def read_rows(path):
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.reader(fh)
        header = next(reader)
        rows = []
        malformed = 0
        for vals in reader:
            if not vals or (len(vals) == 1 and not vals[0].strip()):
                continue
            if len(vals) != len(header):
                malformed += 1
                continue
            rows.append(dict(zip(header, vals)))
    return header, rows, malformed


# ---------------------------------------------------------------- raw parse
raw_bytes = RAW.read_bytes()
header, rows, malformed = read_rows(RAW)
if len(header) != 38:
    raise SystemExit(f"Expected 38 columns; got {len(header)}")

date_errors = []
duplicate_dates = []
seen = set()
year_mismatch = []
exact = Counter()
daily_dates = []
row_by_date = {}
for r in rows:
    d = (r.get("sampledate") or "").strip()
    try:
        dt = datetime.strptime(d, "%Y-%m-%d").date()
    except Exception:
        date_errors.append(d)
        continue
    daily_dates.append(d)
    if d in seen:
        duplicate_dates.append(d)
    seen.add(d)
    row_by_date[d] = r
    try:
        if int(r.get("year4")) != dt.year:
            year_mismatch.append(d)
    except Exception:
        year_mismatch.append(d)
    exact[tuple(r[k] for k in header)] += 1

# ---------------------------------------------------------------- biology parse
bio_rows = []
with BIO.open(newline="", encoding="utf-8") as fh:
    for r in csv.DictReader(fh):
        if r.get("lakeid") == "ME":
            bio_rows.append(r)
bio_dates = sorted({r["sampledate"] for r in bio_rows})
bio_set = set(bio_dates)
bio_depth = defaultdict(set)
bio_station = defaultdict(set)
for r in bio_rows:
    bio_depth[r["sampledate"]].add((r.get("depth_range") or "").strip())
    bio_station[r["sampledate"]].add((r.get("sta") or "").strip())
bio_date_objs = [datetime.strptime(d, "%Y-%m-%d").date() for d in bio_dates]
bio_gaps = [(b - a).days for a, b in zip(bio_date_objs, bio_date_objs[1:])]
bio_summary = {
    "records": len(bio_rows),
    "dates": len(bio_dates),
    "first": bio_dates[0] if bio_dates else "",
    "last": bio_dates[-1] if bio_dates else "",
    "median_interval_days": rnd(statistics.median(bio_gaps)) if bio_gaps else None,
    "dates_0_8m": sum(1 for d in bio_dates if bio_depth[d] == {"0-8m"}),
    "dates_0_2m": sum(1 for d in bio_dates if bio_depth[d] == {"0-2m"}),
    "dates_any_station": sum(1 for d in bio_dates if any(x for x in bio_station[d])),
    "dates_all_blank_station": sum(1 for d in bio_dates if not any(x for x in bio_station[d])),
    "year_counts": dict(sorted(Counter(d[:4] for d in bio_dates).items())),
}

# ---------------------------------------------------------------- variable stats
var_stats = {}
for v in VARS:
    rec = {
        "missing": 0,
        "nonnumeric": 0,
        "numeric_any": 0,
        "valid": 0,
        "flagged": 0,
        "flag_counts": Counter(),
        "flag_numeric": defaultdict(list),
        "flag_missing": Counter(),
        "valid_dates": set(),
        "first": "",
        "last": "",
    }
    for r in rows:
        rawv = (r.get(v) or "").strip()
        f = (r.get(FLAG[v]) or "").strip()
        rec["flag_counts"][f or "none"] += 1
        if rawv == "":
            rec["missing"] += 1
            rec["flag_missing"][f or "none"] += 1
            continue
        try:
            x = float(rawv)
        except ValueError:
            rec["nonnumeric"] += 1
            rec["missing"] += 1
            rec["flag_missing"][f or "none"] += 1
            continue
        if not math.isfinite(x):
            rec["missing"] += 1
            rec["flag_missing"][f or "none"] += 1
            continue
        rec["numeric_any"] += 1
        rec["flag_numeric"][f or "none"].append(x)
        if f:
            rec["flagged"] += 1
        else:
            rec["valid"] += 1
            rec["valid_dates"].add(r["sampledate"])
    ds = sorted(rec["valid_dates"])
    rec["first"] = ds[0] if ds else ""
    rec["last"] = ds[-1] if ds else ""
    rec["unique_valid_dates"] = len(ds)
    var_stats[v] = rec

# ---------------------------------------------------------------- annual / seasonal
annual = defaultdict(lambda: {
    "records": 0, "missing": 0, "numeric_any": 0, "valid": 0, "flagged": 0,
    "flags": Counter(),
})
seasonal = defaultdict(lambda: {
    "records": 0, "missing": 0, "numeric_any": 0, "valid": 0, "flagged": 0,
    "flags": Counter(),
})
for r in rows:
    d = r["sampledate"]
    dt = datetime.strptime(d, "%Y-%m-%d").date()
    for v in VARS:
        rawv = (r.get(v) or "").strip()
        f = (r.get(FLAG[v]) or "").strip()
        a = annual[(v, dt.year)]
        s = seasonal[(v, season(dt.month))]
        a["records"] += 1
        s["records"] += 1
        if f:
            a["flags"][f] += 1
            s["flags"][f] += 1
        x = fnum(rawv)
        if x is None:
            a["missing"] += 1
            s["missing"] += 1
        else:
            a["numeric_any"] += 1
            s["numeric_any"] += 1
            if f:
                a["flagged"] += 1
                s["flagged"] += 1
            else:
                a["valid"] += 1
                s["valid"] += 1

# ---------------------------------------------------------------- intervals
interval_rows = []
for v in VARS:
    ds = sorted(var_stats[v]["valid_dates"])
    gaps = [
        (datetime.strptime(b, "%Y-%m-%d").date() - datetime.strptime(a, "%Y-%m-%d").date()).days
        for a, b in zip(ds, ds[1:])
    ]
    interval_rows.append({
        "variable": v,
        "valid_dates": len(ds),
        "intervals": len(gaps),
        "interval_1d": sum(g == 1 for g in gaps),
        "interval_2_7d": sum(2 <= g <= 7 for g in gaps),
        "interval_8_14d": sum(8 <= g <= 14 for g in gaps),
        "interval_15_30d": sum(15 <= g <= 30 for g in gaps),
        "interval_31_60d": sum(31 <= g <= 60 for g in gaps),
        "interval_61_90d": sum(61 <= g <= 90 for g in gaps),
        "interval_gt_90d": sum(g > 90 for g in gaps),
        "median_interval_days": rnd(statistics.median(gaps)) if gaps else "",
        "max_interval_days": max(gaps) if gaps else "",
    })
write_csv(T / "INDEPENDENT_INTERVALS.csv", interval_rows)

# ---------------------------------------------------------------- overlap
overlap_rows = []
for v in VARS:
    ds = sorted(var_stats[v]["valid_dates"])
    first = ds[0] if ds else ""
    last = ds[-1] if ds else ""
    within = [d for d in bio_dates if first <= d <= last] if ds else []
    absent = 0
    present = 0
    missing = 0
    missing_flagged = 0
    missing_unflagged = 0
    any_numeric = 0
    flagged = 0
    valid = 0
    for d in within:
        r = row_by_date.get(d)
        if r is None:
            absent += 1
            continue
        present += 1
        rawv = (r.get(v) or "").strip()
        f = (r.get(FLAG[v]) or "").strip()
        x = fnum(rawv)
        if x is None:
            missing += 1
            if f:
                missing_flagged += 1
            else:
                missing_unflagged += 1
            continue
        any_numeric += 1
        if f:
            flagged += 1
        else:
            valid += 1

    valid_set = var_stats[v]["valid_dates"]
    windows = {}
    for days in (1, 3, 7, 14):
        n = 0
        for d in within:
            dt = datetime.strptime(d, "%Y-%m-%d").date()
            if any((dt + timedelta(days=k)).isoformat() in valid_set for k in range(-days, days + 1)):
                n += 1
        windows[days] = n

    overlap_rows.append({
        "variable": v,
        "first_valid_unflagged": first,
        "last_valid_unflagged": last,
        "biology_dates_total": len(bio_dates),
        "biology_dates_within_valid_span": len(within),
        "same_day_date_absent": absent,
        "same_day_record_present": present,
        "same_day_variable_missing": missing,
        "same_day_missing_flagged": missing_flagged,
        "same_day_missing_unflagged": missing_unflagged,
        "same_day_any_numeric": any_numeric,
        "same_day_valid_unflagged": valid,
        "same_day_flagged_numeric": flagged,
        "same_day_missing_or_absent": absent + missing,
        "pct_same_day_valid_of_total": rnd(100 * valid / len(bio_dates)) if bio_dates else "",
        "pct_same_day_valid_of_within": rnd(100 * valid / len(within)) if within else "",
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
write_csv(T / "INDEPENDENT_OVERLAP.csv", overlap_rows)

# ---------------------------------------------------------------- Turner / YSI
turner_ysi = []
for vt, vy, label in [
    ("avg_chlor_rfu_turner", "avg_chlor_rfu_ysi", "chlorophyll"),
    ("avg_phyco_rfu_turner", "avg_phyco_rfu_ysi", "phycocyanin"),
]:
    pairs = []
    paired_dates = set()
    nonpositive_turner = 0
    for r in rows:
        ft = (r.get(FLAG[vt]) or "").strip()
        fy = (r.get(FLAG[vy]) or "").strip()
        if ft or fy:
            continue
        a = fnum(r.get(vt))
        b = fnum(r.get(vy))
        if a is None or b is None:
            continue
        pairs.append((a, b))
        paired_dates.add(r["sampledate"])
        if a <= 0:
            nonpositive_turner += 1
    ratios = [b / a for a, b in pairs if a != 0]
    turner_ysi.append({
        "proxy": label,
        "paired_dates": len(paired_dates),
        "paired_records": len(pairs),
        "paired_nonpositive_turner": nonpositive_turner,
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
        "first_date": min(paired_dates) if paired_dates else "",
        "last_date": max(paired_dates) if paired_dates else "",
    })
write_csv(T / "TURNER_YSI_RECHECK.csv", turner_ysi)

# ---------------------------------------------------------------- multivariate common coverage
valid_sets = {v: var_stats[v]["valid_dates"] for v in VARS}
all_dates = sorted(set(row_by_date))
pair_rows = []
for a in VARS:
    for b in VARS:
        n = len(valid_sets[a] & valid_sets[b])
        pair_rows.append({"variable_a": a, "variable_b": b, "complete_dates": n})
write_csv(T / "PAIRWISE_COMPLETE_CASES.csv", pair_rows)

multivariate_sets = {
    "turner_3": ["avg_chlor_rfu_turner", "avg_phyco_rfu_turner", "avg_do_raw"],
    "turner_4": ["avg_chlor_rfu_turner", "avg_phyco_rfu_turner", "avg_do_raw", "avg_do_wtemp"],
    "turner_core": ["avg_chlor_rfu_turner", "avg_phyco_rfu_turner", "avg_do_raw", "avg_do_sat", "avg_do_wtemp", "avg_air_temp", "avg_wind_speed"],
    "turner_light": ["avg_chlor_rfu_turner", "avg_phyco_rfu_turner", "avg_do_raw", "avg_do_sat", "avg_do_wtemp", "avg_air_temp", "avg_wind_speed", "avg_par", "avg_par_below"],
    "ysi_3": ["avg_chlor_rfu_ysi", "avg_phyco_rfu_ysi", "avg_do_raw"],
    "ysi_5": ["avg_chlor_rfu_ysi", "avg_phyco_rfu_ysi", "avg_do_raw", "avg_do_wtemp", "avg_ph"],
    "ysi_6": ["avg_chlor_rfu_ysi", "avg_phyco_rfu_ysi", "avg_ph", "avg_fdom", "avg_turbidity", "avg_spec_cond"],
    "ysi_core": ["avg_chlor_rfu_ysi", "avg_phyco_rfu_ysi", "avg_do_raw", "avg_do_sat", "avg_do_wtemp", "avg_ph", "avg_fdom", "avg_turbidity", "avg_spec_cond", "avg_air_temp", "avg_wind_speed"],
    "ysi_light": ["avg_chlor_rfu_ysi", "avg_phyco_rfu_ysi", "avg_do_raw", "avg_do_sat", "avg_do_wtemp", "avg_ph", "avg_fdom", "avg_turbidity", "avg_spec_cond", "avg_air_temp", "avg_wind_speed", "avg_par", "avg_par_below"],
}
multivariate_rows = []
for name, members in multivariate_sets.items():
    common = set.intersection(*(valid_sets[v] for v in members)) if members else set()
    multivariate_rows.append({
        "set": name,
        "members": ";".join(members),
        "n_members": len(members),
        "complete_dates": len(common),
        "first_complete": min(common) if common else "",
        "last_complete": max(common) if common else "",
    })
write_csv(T / "MULTIVARIATE_COVERAGE.csv", multivariate_rows)

# biology dates with n valid sensor variables
bio_multi = []
count_dist = Counter()
for d in bio_dates:
    r = row_by_date.get(d)
    if r is None:
        count_dist[0] += 1
        bio_multi.append({"date": d, "n_valid_sensor_variables": 0, "variables": ""})
        continue
    vals = []
    for v in VARS:
        if (r.get(FLAG[v]) or "").strip():
            continue
        if fnum(r.get(v)) is not None:
            vals.append(v)
    count_dist[len(vals)] += 1
    bio_multi.append({"date": d, "n_valid_sensor_variables": len(vals), "variables": ";".join(vals)})
write_csv(T / "BIOLOGY_MULTIVARIATE_COVERAGE.csv", bio_multi)

# pairwise complete biology-sensor dates
bio_valid_sets = {}
for v in VARS:
    s = set()
    for d in bio_dates:
        r = row_by_date.get(d)
        if r is None:
            continue
        if (r.get(FLAG[v]) or "").strip():
            continue
        if fnum(r.get(v)) is not None:
            s.add(d)
    bio_valid_sets[v] = s
bio_pair_rows = []
for a in VARS:
    for b in VARS:
        bio_pair_rows.append({
            "variable_a": a,
            "variable_b": b,
            "same_day_complete_biology_dates": len(bio_valid_sets[a] & bio_valid_sets[b]),
        })
write_csv(T / "BIOLOGY_PAIRWISE_COMPLETE.csv", bio_pair_rows)

# core-set coverage on biology dates, overall and by period
biology_core_rows = []
for name, members in multivariate_sets.items():
    for label, lo, hi in [("all", "0000", "9999"), ("2006_2020", "2006", "2020"), ("2019_2020", "2019", "2020")]:
        period_dates = [d for d in bio_dates if lo <= d[:4] <= hi]
        complete = [d for d in period_dates if all(d in bio_valid_sets[v] for v in members)]
        biology_core_rows.append({
            "set": name,
            "period": label,
            "biology_dates": len(period_dates),
            "complete_dates": len(complete),
            "pct_complete": rnd(100 * len(complete) / len(period_dates)) if period_dates else "",
            "first_complete": min(complete) if complete else "",
            "last_complete": max(complete) if complete else "",
        })
write_csv(T / "BIOLOGY_CORE_COVERAGE.csv", biology_core_rows)

# ---------------------------------------------------------------- spatial / depth
def local(tag):
    return tag.split("}")[-1]


eml_defs = {}
eml_codes = {}
for dt in ET.parse(EML).getroot().iter():
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
            eml_defs[name] = definition or ""
            eml_codes[name] = codes


def depth_from_definition(text):
    m = re.search(r"\(([0-9.]+)\s*m\s+depth\)", text or "", re.I)
    if m:
        return m.group(1) + " m"
    m = re.search(r"\(([0-9.]+)\s*m\s+above", text or "", re.I)
    if m:
        return m.group(1) + " m above water"
    return ""


depth_rows = []
for v in VARS:
    depth_rows.append({
        "variable": v,
        "definition": eml_defs.get(v, ""),
        "sensor_depth": depth_from_definition(eml_defs.get(v, "")),
        "flag_column": FLAG[v],
        "documented_codes": ",".join(eml_codes.get(FLAG[v], [])),
    })
write_csv(T / "SPATIAL_DEPTH_RECHECK.csv", depth_rows)

# haversine
lat1, lon1 = 43.0995, -89.4045
lat2, lon2 = 43.09885, -89.40545
R = 6371000
p1, p2 = math.radians(lat1), math.radians(lat2)
dp = math.radians(lat2 - lat1)
dl = math.radians(lon2 - lon1)
hav = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
site_distance_m = 2 * R * math.asin(math.sqrt(hav))

# ---------------------------------------------------------------- method 2: SQLite
con = sqlite3.connect(":memory:")
cur = con.cursor()
cols = ["sampledate TEXT PRIMARY KEY", "year4 INTEGER"]
for v in VARS:
    cols.append(f'"{v}" REAL')
    cols.append(f'"{FLAG[v]}" TEXT')
cur.execute("CREATE TABLE daily (" + ",".join(cols) + ")")
placeholders = ",".join(["?"] * (2 + 2 * len(VARS)))
for r in rows:
    vals = [r["sampledate"], int(r["year4"])]
    for v in VARS:
        vals.append(fnum(r.get(v)))
        vals.append((r.get(FLAG[v]) or "").strip() or None)
    cur.execute(f"INSERT INTO daily VALUES ({placeholders})", vals)
cur.execute("CREATE TABLE bio_dates (sampledate TEXT PRIMARY KEY)")
cur.executemany("INSERT INTO bio_dates VALUES (?)", [(d,) for d in bio_dates])
con.commit()

sqlite_stats = {}
for v in VARS:
    q = f'''SELECT
        COUNT(*),
        SUM(CASE WHEN "{v}" IS NULL THEN 1 ELSE 0 END),
        SUM(CASE WHEN "{v}" IS NOT NULL THEN 1 ELSE 0 END),
        SUM(CASE WHEN "{v}" IS NOT NULL AND ("{FLAG[v]}" IS NULL OR "{FLAG[v]}"='') THEN 1 ELSE 0 END),
        SUM(CASE WHEN "{v}" IS NOT NULL AND "{FLAG[v]}" IS NOT NULL AND "{FLAG[v]}"<>'' THEN 1 ELSE 0 END),
        COUNT(DISTINCT CASE WHEN "{v}" IS NOT NULL AND ("{FLAG[v]}" IS NULL OR "{FLAG[v]}"='') THEN sampledate END)
        FROM daily'''
    total, missing, numeric, valid, flagged, unique_valid = cur.execute(q).fetchone()
    flags = {}
    for f, n in cur.execute(f'SELECT COALESCE("{FLAG[v]}", ""), COUNT(*) FROM daily GROUP BY COALESCE("{FLAG[v]}", "")'):
        flags[f] = n
    sqlite_stats[v] = {
        "total": total,
        "missing": missing or 0,
        "numeric_any": numeric or 0,
        "valid": valid or 0,
        "flagged": flagged or 0,
        "unique_valid_dates": unique_valid or 0,
        "flag_counts": flags,
    }

# SQLite same-day overlap
sqlite_overlap = {}
for v in VARS:
    first = var_stats[v]["first"]
    last = var_stats[v]["last"]
    if first and last:
        within = cur.execute("SELECT COUNT(*) FROM bio_dates WHERE sampledate BETWEEN ? AND ?", (first, last)).fetchone()[0]
        present = cur.execute("SELECT COUNT(*) FROM bio_dates b JOIN daily d ON b.sampledate=d.sampledate WHERE b.sampledate BETWEEN ? AND ?", (first, last)).fetchone()[0]
        any_num = cur.execute(f'''SELECT COUNT(*) FROM bio_dates b JOIN daily d ON b.sampledate=d.sampledate
            WHERE b.sampledate BETWEEN ? AND ? AND d."{v}" IS NOT NULL''', (first, last)).fetchone()[0]
        valid = cur.execute(f'''SELECT COUNT(*) FROM bio_dates b JOIN daily d ON b.sampledate=d.sampledate
            WHERE b.sampledate BETWEEN ? AND ? AND d."{v}" IS NOT NULL AND (d."{FLAG[v]}" IS NULL OR d."{FLAG[v]}"='')''', (first, last)).fetchone()[0]
        flagged = cur.execute(f"""SELECT COUNT(*) FROM bio_dates b JOIN daily d ON b.sampledate=d.sampledate
            WHERE b.sampledate BETWEEN ? AND ? AND d."{v}" IS NOT NULL AND d."{FLAG[v]}" IS NOT NULL AND d."{FLAG[v]}" <> ''""", (first, last)).fetchone()[0]
    else:
        within = present = any_num = valid = flagged = 0
    sqlite_overlap[v] = {
        "biology_dates_within_valid_span": within,
        "same_day_record_present": present,
        "same_day_any_numeric": any_num,
        "same_day_valid_unflagged": valid,
        "same_day_flagged_numeric": flagged,
    }

# SQLite paired Turner/YSI
sqlite_turner_ysi = {}
for vt, vy, label in [
    ("avg_chlor_rfu_turner", "avg_chlor_rfu_ysi", "chlorophyll"),
    ("avg_phyco_rfu_turner", "avg_phyco_rfu_ysi", "phycocyanin"),
]:
    n_dates, n_records = cur.execute(f'''SELECT COUNT(DISTINCT sampledate), COUNT(*) FROM daily
        WHERE "{vt}" IS NOT NULL AND ("{FLAG[vt]}" IS NULL OR "{FLAG[vt]}"='')
          AND "{vy}" IS NOT NULL AND ("{FLAG[vy]}" IS NULL OR "{FLAG[vy]}"='')''').fetchone()
    sqlite_turner_ysi[label] = {"paired_dates": n_dates, "paired_records": n_records}

# ---------------------------------------------------------------- comparisons to 4L9
def read_csv_dict(path):
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def same_num(a, b, tol=1e-6):
    if a in (None, "") and b in (None, ""):
        return True
    try:
        return abs(float(a) - float(b)) <= tol
    except Exception:
        return str(a) == str(b)


verification = []
discrepancies = []


def add_check(domain, item, l9, indep, method2=None, note=""):
    m9 = same_num(l9, indep)
    m2 = True if method2 is None else same_num(indep, method2)
    verification.append({
        "domain": domain,
        "item": item,
        "4l9_value": l9,
        "independent_value": indep,
        "sqlite_value": "" if method2 is None else method2,
        "match_4l9": m9,
        "match_sqlite": m2,
        "note": note,
    })
    if not m9:
        discrepancies.append({
            "id": f"D{len(discrepancies)+1:03d}",
            "domain": domain,
            "item": item,
            "4l9_value": l9,
            "independent_value": indep,
            "difference": f"{l9} vs {indep}",
            "severity": "numeric",
            "interpretation": "Numerical mismatch; investigate before using either value.",
            "action": "Do not reconcile silently.",
        })


# variable coverage
l9_var = {r["variable"]: r for r in read_csv_dict(L9 / "tables/VARIABLE_COVERAGE_SUMMARY.csv")}
for v in VARS:
    l9 = l9_var[v]
    ind = var_stats[v]
    sq = sqlite_stats[v]
    add_check("variable", f"{v}.missing", l9["missing"], ind["missing"], sq["missing"])
    add_check("variable", f"{v}.numeric_any", l9["numeric_any"], ind["numeric_any"], sq["numeric_any"])
    add_check("variable", f"{v}.valid_unflagged", l9["valid_unflagged"], ind["valid"], sq["valid"])
    add_check("variable", f"{v}.flagged_numeric", l9["flagged_numeric"], ind["flagged"], sq["flagged"])
    add_check("variable", f"{v}.unique_valid_dates", l9["unique_valid_dates"], ind["unique_valid_dates"], sq["unique_valid_dates"])
    add_check("variable", f"{v}.first_valid", l9["first_valid_unflagged"], ind["first"])
    add_check("variable", f"{v}.last_valid", l9["last_valid_unflagged"], ind["last"])
    for code in ["C", "E", "H", "G", "O"]:
        add_check("flag", f"{v}.{code}", l9["flag_" + code], ind["flag_counts"].get(code, 0), sq["flag_counts"].get(code, 0))

# annual
l9_annual = {(r["variable"], r["year"]): r for r in read_csv_dict(L9 / "tables/ANNUAL_VARIABLE_COVERAGE.csv")}
for (v, y), a in sorted(annual.items()):
    r = l9_annual.get((v, str(y)))
    if not r:
        discrepancies.append({
            "id": f"D{len(discrepancies)+1:03d}", "domain": "annual", "item": f"{v}.{y}",
            "4l9_value": "MISSING", "independent_value": "present", "difference": "row absent",
            "severity": "numeric", "interpretation": "Annual row missing from 4L.9 table.",
            "action": "Investigate.",
        })
        continue
    add_check("annual", f"{v}.{y}.records", r["records"], a["records"])
    add_check("annual", f"{v}.{y}.missing", r["missing"], a["missing"])
    add_check("annual", f"{v}.{y}.numeric_any", r["numeric_any"], a["numeric_any"])
    add_check("annual", f"{v}.{y}.valid", r["valid_unflagged"], a["valid"])
    add_check("annual", f"{v}.{y}.flagged", r["flagged_numeric"], a["flagged"])
    for code in ["C", "E", "H", "G", "O"]:
        add_check("annual", f"{v}.{y}.{code}", r["flag_" + code], a["flags"].get(code, 0))

# seasonal
l9_season = {(r["variable"], r["season"]): r for r in read_csv_dict(L9 / "tables/SEASONAL_VARIABLE_COVERAGE.csv")}
for (v, s), a in sorted(seasonal.items()):
    r = l9_season.get((v, s))
    if not r:
        discrepancies.append({
            "id": f"D{len(discrepancies)+1:03d}", "domain": "seasonal", "item": f"{v}.{s}",
            "4l9_value": "MISSING", "independent_value": "present", "difference": "row absent",
            "severity": "numeric", "interpretation": "Seasonal row missing from 4L.9 table.",
            "action": "Investigate.",
        })
        continue
    add_check("seasonal", f"{v}.{s}.records", r["records"], a["records"])
    add_check("seasonal", f"{v}.{s}.missing", r["missing"], a["missing"])
    add_check("seasonal", f"{v}.{s}.numeric_any", r["numeric_any"], a["numeric_any"])
    add_check("seasonal", f"{v}.{s}.valid", r["valid_unflagged"], a["valid"])
    add_check("seasonal", f"{v}.{s}.flagged", r["flagged_numeric"], a["flagged"])
    for code in ["C", "E", "H", "G", "O"]:
        add_check("seasonal", f"{v}.{s}.{code}", r["flag_" + code], a["flags"].get(code, 0))

# intervals
l9_int = {r["variable"]: r for r in read_csv_dict(L9 / "tables/INTERVAL_DISTRIBUTION.csv")}
for r in interval_rows:
    v = r["variable"]
    a = l9_int[v]
    for f in ["valid_dates", "intervals", "interval_1d", "interval_2_7d", "interval_8_14d", "interval_15_30d", "interval_31_60d", "interval_61_90d", "interval_gt_90d", "median_interval_days", "max_interval_days"]:
        add_check("interval", f"{v}.{f}", a[f], r[f])

# overlap
l9_ov = {r["variable"]: r for r in read_csv_dict(L9 / "tables/BIOLOGICAL_OVERLAP.csv")}
for r in overlap_rows:
    v = r["variable"]
    a = l9_ov[v]
    for f in [
        "biology_dates_within_valid_span", "same_day_date_absent", "same_day_record_present",
        "same_day_variable_missing", "same_day_missing_flagged", "same_day_missing_unflagged",
        "same_day_any_numeric", "same_day_valid_unflagged", "same_day_flagged_numeric",
        "valid_within_pm1_days", "valid_within_pm3_days", "valid_within_pm7_days", "valid_within_pm14_days",
        "pct_same_day_valid_of_total", "pct_same_day_valid_of_within",
        "pct_pm1_of_total", "pct_pm3_of_total", "pct_pm7_of_total", "pct_pm14_of_total",
    ]:
        add_check("overlap", f"{v}.{f}", a[f], r[f])
    sq = sqlite_overlap[v]
    add_check("overlap", f"{v}.sqlite_within", r["biology_dates_within_valid_span"], sq["biology_dates_within_valid_span"], sq["biology_dates_within_valid_span"])
    add_check("overlap", f"{v}.sqlite_same_valid", r["same_day_valid_unflagged"], sq["same_day_valid_unflagged"], sq["same_day_valid_unflagged"])

# Turner/YSI
l9_ty = {r["variable"]: r for r in read_csv_dict(L9 / "tables/TURNER_YSI_OVERLAP.csv")}
for r in turner_ysi:
    label = r["proxy"]
    a = l9_ty[label]
    for f in ["paired_dates", "paired_records", "turner_median", "ysi_median", "median_ratio_ysi_over_turner"]:
        method2 = sqlite_turner_ysi[label].get(f) if f in sqlite_turner_ysi[label] else None
        add_check("turner_ysi", f"{label}.{f}", a[f], r[f], method2)

# era
l9_era = {(r["variable"], r["period"]): r for r in read_csv_dict(L9 / "tables/SENSOR_ERA_SUMMARY.csv")}
for v in VARS:
    for label, lo, hi in [("pre_2019", "0000-01-01", "2018-12-31"), ("2019_plus", "2019-01-01", "9999-12-31")]:
        vals = []
        flags = Counter()
        missing = 0
        numeric_any = 0
        for r in rows:
            if not (lo <= r["sampledate"] <= hi):
                continue
            f = (r.get(FLAG[v]) or "").strip()
            flags[f or "none"] += 1
            x = fnum(r.get(v))
            if x is None:
                missing += 1
            else:
                numeric_any += 1
                if not f:
                    vals.append(x)
        a = l9_era[(v, label)]
        add_check("era", f"{v}.{label}.valid", a["valid_unflagged"], len(vals))
        add_check("era", f"{v}.{label}.missing", a["missing"], missing)
        add_check("era", f"{v}.{label}.numeric_any", a["numeric_any"], numeric_any)
        for code in ["C", "E", "H", "G", "O"]:
            add_check("era", f"{v}.{label}.{code}", a["flag_" + code], flags.get(code, 0))

# depth
l9_depth = {r["variable"]: r for r in read_csv_dict(L9 / "tables/DEPTH_COMPATIBILITY.csv")}
for r in depth_rows:
    v = r["variable"]
    if v in l9_depth:
        add_check("depth", f"{v}.sensor_depth", l9_depth[v]["sensor_depth"], r["sensor_depth"])

# structural
add_check("structure", "rows", 3996, len(rows))
add_check("structure", "columns", 38, len(header))
add_check("structure", "malformed", 0, malformed)
add_check("structure", "duplicate_dates", 0, len(duplicate_dates))
add_check("structure", "date_errors", 0, len(date_errors))
add_check("structure", "year_mismatch", 0, len(year_mismatch))
add_check("structure", "exact_duplicate_rows", 0, sum(v - 1 for v in exact.values() if v > 1))
add_check("biology", "dates", 402, len(bio_dates))
add_check("biology", "dates_0_8m", 400, bio_summary["dates_0_8m"])
add_check("biology", "dates_0_2m", 2, bio_summary["dates_0_2m"])
add_check("biology", "dates_all_blank_station", 371, bio_summary["dates_all_blank_station"])

# Write verification table
write_csv(T / "CALCULATION_VERIFICATION.csv", verification)

# Add interpretive discrepancies even if no numeric mismatch
interpretive = [
    ("I001", "interpretation", "valid_unflagged label", "Used as 'valid'", "Means only numeric with blank flag; unflagged values can be physically implausible.", "The term can overstate reliability; prefer 'unflagged numeric'.", "Retain with explicit definition."),
    ("I002", "interpretation", "Turner/YSI ratio", "Median ratio reported", "Ratio is raw RFU ratio on paired dates; zero/non-positive Turner values are excluded from ratio.", "Descriptive only; not a calibration.", "Do not use as correction."),
    ("I003", "interpretation", "same-day overlap", "Date match", "Date-only biology; no sampling time; same-day is not temporal alignment.", "Could overstate temporal correspondence.", "Use as availability, not lead/lag."),
    ("I004", "interpretation", "annual coverage denominator", "Daily records", "Denominator is deployment records, not calendar days.", "Seasonal/open-water interpretation only.", "State denominator."),
    ("I005", "interpretation", "PAR 2007", "First unflagged 2007", "Eleven near-zero values before sustained 2016 record.", "Not meaningful PAR coverage.", "Treat PAR as 2016+."),
    ("I006", "interpretation", "sensor transitions", "Column-level coverage", "Observed first/last is column-level, not proof a listed sensor produced every date.", "Sensor identity before 2016/2019 unresolved.", "Do not infer sensor-specific calibration."),
    ("I007", "interpretation", "overall verdict", "Exploratory feasibility supported with major limitations", "A/B are possible descriptively; C limited; D not supported.", "Verdict is broadly correct but could be read as stronger than warranted for B/C.", "Separate A-D verdicts; reject D."),
    ("I008", "interpretation", "multivariate common coverage", "Not quantified in 4L.9", "Complete-case counts show limited multi-variable overlap, especially with biology.", "C is weaker than a generic 'multivariate exploratory' label suggests.", "Report complete-case counts."),
    ("I009", "interpretation", "phycocyanin sensor validation", "RFU proxy", "Literature shows weak/variable sensor-to-biovolume relationships and detection-limit issues.", "B is descriptive only; not quantitative validation.", "No sensor calibration claim."),
    ("I010", "interpretation", "early warning", "Not supported", "No labels/events; 14-day biology; no time-of-day; depth mismatch.", "D correctly rejected.", "No early-warning validation."),
]
for row in interpretive:
    if not any(d["id"] == row[0] for d in discrepancies):
        discrepancies.append({
            "id": row[0], "domain": row[1], "item": row[2], "4l9_value": row[3],
            "independent_value": row[4], "difference": "interpretive", "severity": "interpretation",
            "interpretation": row[5], "action": row[6],
        })

write_csv(T / "DISCREPANCY_REGISTER.csv", discrepancies)

# ---------------------------------------------------------------- independent tables
var_rows = []
for v in VARS:
    r = var_stats[v]
    var_rows.append({
        "variable": v,
        "first_valid_unflagged": r["first"],
        "last_valid_unflagged": r["last"],
        "missing": r["missing"],
        "numeric_any": r["numeric_any"],
        "valid_unflagged": r["valid"],
        "flagged_numeric": r["flagged"],
        "unique_valid_dates": r["unique_valid_dates"],
        "flag_C": r["flag_counts"].get("C", 0),
        "flag_E": r["flag_counts"].get("E", 0),
        "flag_H": r["flag_counts"].get("H", 0),
        "flag_G": r["flag_counts"].get("G", 0),
        "flag_O": r["flag_counts"].get("O", 0),
        "flag_none": r["flag_counts"].get("none", 0),
    })
write_csv(T / "INDEPENDENT_VARIABLE_COUNTS.csv", var_rows)

annual_rows = []
for (v, y), a in sorted(annual.items()):
    annual_rows.append({
        "variable": v, "year": y, "records": a["records"], "missing": a["missing"],
        "numeric_any": a["numeric_any"], "valid_unflagged": a["valid"],
        "flagged_numeric": a["flagged"],
        "flag_C": a["flags"].get("C", 0), "flag_E": a["flags"].get("E", 0),
        "flag_H": a["flags"].get("H", 0), "flag_G": a["flags"].get("G", 0),
        "flag_O": a["flags"].get("O", 0),
    })
write_csv(T / "INDEPENDENT_ANNUAL_COVERAGE.csv", annual_rows)

season_rows = []
for (v, s), a in sorted(seasonal.items()):
    season_rows.append({
        "variable": v, "season": s, "records": a["records"], "missing": a["missing"],
        "numeric_any": a["numeric_any"], "valid_unflagged": a["valid"],
        "flagged_numeric": a["flagged"],
        "flag_C": a["flags"].get("C", 0), "flag_E": a["flags"].get("E", 0),
        "flag_H": a["flags"].get("H", 0), "flag_G": a["flags"].get("G", 0),
        "flag_O": a["flags"].get("O", 0),
    })
write_csv(T / "INDEPENDENT_SEASONAL_COVERAGE.csv", season_rows)

flag_rows = []
for v in VARS:
    for code, n in sorted(var_stats[v]["flag_counts"].items()):
        flag_rows.append({
            "variable": v, "flag": code, "records": n,
            "pct": rnd(100 * n / len(rows)) if rows else "",
        })
write_csv(T / "INDEPENDENT_FLAG_COUNTS.csv", flag_rows)

# ---------------------------------------------------------------- summary
numeric_mismatches = sum(1 for x in verification if not x["match_4l9"])
sqlite_mismatches = sum(1 for x in verification if not x["match_sqlite"])
bio_any_sensor = {}
for label, lo, hi in [("all", "0000", "9999"), ("2006_2020", "2006", "2020"), ("2019_2020", "2019", "2020")]:
    period_dates = [d for d in bio_dates if lo <= d[:4] <= hi]
    any_valid = [d for d in period_dates if any(d in bio_valid_sets[v] for v in VARS)]
    bio_any_sensor[label] = {
        "biology_dates": len(period_dates),
        "any_valid_sensor_date": len(any_valid),
        "pct_any_valid": rnd(100 * len(any_valid) / len(period_dates)) if period_dates else "",
    }
summary = {
    "file": {
        "path": str(RAW.relative_to(ROOT)),
        "bytes": len(raw_bytes),
        "md5": hashlib.md5(raw_bytes).hexdigest(),
        "sha1": hashlib.sha1(raw_bytes).hexdigest(),
        "sha256": hashlib.sha256(raw_bytes).hexdigest(),
        "columns": len(header),
        "rows": len(rows),
        "malformed": malformed,
        "duplicate_dates": len(duplicate_dates),
        "date_errors": len(date_errors),
        "year_mismatch": len(year_mismatch),
        "exact_duplicate_rows": sum(v - 1 for v in exact.values() if v > 1),
        "date_min": min(daily_dates) if daily_dates else "",
        "date_max": max(daily_dates) if daily_dates else "",
    },
    "biology": bio_summary,
    "variables": var_stats,
    "annual": {f"{v}|{y}": a for (v, y), a in annual.items()},
    "seasonal": {f"{v}|{s}": a for (v, s), a in seasonal.items()},
    "intervals": interval_rows,
    "overlap": overlap_rows,
    "turner_ysi": turner_ysi,
    "multivariate": multivariate_rows,
    "biology_multivariate_distribution": dict(sorted(count_dist.items())),
    "biology_core": biology_core_rows,
    "biology_any_sensor": bio_any_sensor,
    "spatial": {
        "site_distance_m": rnd(site_distance_m, 1),
        "biology_dates_0_8m": bio_summary["dates_0_8m"],
        "biology_dates_0_2m": bio_summary["dates_0_2m"],
        "biology_dates_all_blank_station": bio_summary["dates_all_blank_station"],
        "biology_dates_any_station": bio_summary["dates_any_station"],
        "depths": depth_rows,
    },
    "verification": {
        "checks": len(verification),
        "numeric_mismatches_vs_4l9": numeric_mismatches,
        "numeric_mismatches_vs_sqlite": sqlite_mismatches,
        "discrepancy_rows": len(discrepancies),
    },
}
# convert sets/counters for JSON
def jsonable(o):
    if isinstance(o, set):
        return sorted(o)
    if isinstance(o, Counter):
        return dict(o)
    raise TypeError(type(o))

(OUT / "summary.json").write_text(json.dumps(summary, indent=2, default=jsonable), encoding="utf-8")

print(json.dumps({
    "rows": len(rows),
    "biology_dates": len(bio_dates),
    "verification_checks": len(verification),
    "numeric_mismatches_vs_4l9": numeric_mismatches,
    "numeric_mismatches_vs_sqlite": sqlite_mismatches,
    "discrepancy_rows": len(discrepancies),
    "multivariate": multivariate_rows,
    "biology_multivariate_distribution": dict(sorted(count_dist.items())),
    "biology_core": biology_core_rows,
    "biology_any_sensor": bio_any_sensor,
    "site_distance_m": rnd(site_distance_m, 1),
}, indent=2, default=jsonable))
