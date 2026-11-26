#!/usr/bin/env python3
"""Independent second-method verification of the Sprint 4L.9 audit.

This script deliberately does not import the audit script. It uses simple
comma splitting (the daily file contains no embedded commas in data fields),
then compares key counts with the generated audit tables.
"""
import csv
import hashlib
import json
import math
import statistics
from collections import Counter
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RAW = ROOT / "research/evidence/sprint_4l7_mendota_daily_sensor_audit/acquisition/129.42/North_Temperate_Lakes_LTER_Daily_Meteorological_and_Metabolism_Data_-_Lake_Mendota__cba9ed12834b8f315d6b10675bb60c5a.dat"
BIO = ROOT / "research/evidence/sprint_4l_mendota_biology_audit/acquisition/88.31/North_Temperate_Lakes_LTER_-_Phytoplankton_-_Madison_Lakes_Area__f2de15b2fff6ae962a04c150c0a1c510.dat"
OUT = ROOT / "research/evidence/sprint_4l9_mendota_daily_sensor_raw_audit"
T = OUT / "tables"

raw = RAW.read_bytes()
text = raw.decode("utf-8")
lines = text.splitlines()
header = [h.strip('"') for h in lines[0].split('","')]
header[0] = header[0].lstrip('"')
header[-1] = header[-1].rstrip('"')
if len(header) != 38:
    raise SystemExit(f"Independent parser expected 38 columns, got {len(header)}")

data = []
bad = []
for i, line in enumerate(lines[1:], 2):
    if not line.strip():
        continue
    vals = line.split(",")
    if len(vals) != 38:
        bad.append((i, len(vals)))
        continue
    data.append(dict(zip(header, vals)))

variables = [h for h in header if not h.startswith("flag_") and h not in ("year4", "sampledate")]
flags = {v: "flag_" + v for v in variables}

independent = {}
for v in variables:
    numeric = 0
    unflagged = 0
    flagged = 0
    missing = 0
    dates = set()
    flag_counts = Counter()
    for r in data:
        rawv = r[v].strip()
        f = r[flags[v]].strip()
        flag_counts[f or "none"] += 1
        if rawv == "":
            missing += 1
            continue
        try:
            x = float(rawv)
        except ValueError:
            missing += 1
            continue
        if not math.isfinite(x):
            missing += 1
            continue
        numeric += 1
        if f:
            flagged += 1
        else:
            unflagged += 1
            dates.add(r["sampledate"])
    independent[v] = {
        "missing": missing,
        "numeric_any": numeric,
        "valid_unflagged": unflagged,
        "flagged_numeric": flagged,
        "unique_valid_dates": len(dates),
        "dates": dates,
        "flag_counts": flag_counts,
    }

# compare with audit table
mismatches = []
with (T / "VARIABLE_COVERAGE_SUMMARY.csv").open(newline="", encoding="utf-8") as fh:
    for row in csv.DictReader(fh):
        v = row["variable"]
        ind = independent[v]
        for field in ("missing", "numeric_any", "valid_unflagged", "flagged_numeric", "unique_valid_dates"):
            if int(row[field]) != ind[field]:
                mismatches.append({"variable": v, "field": field, "audit": row[field], "independent": ind[field]})

# independent biology overlap for selected variables
bio_dates = sorted({r["sampledate"] for r in csv.DictReader(BIO.open(newline="", encoding="utf-8")) if r["lakeid"] == "ME"})
row_by_date = {r["sampledate"]: r for r in data}
overlap_mismatches = []
with (T / "BIOLOGICAL_OVERLAP.csv").open(newline="", encoding="utf-8") as fh:
    for row in csv.DictReader(fh):
        v = row["variable"]
        ind = independent[v]
        ds = sorted(ind["dates"])
        first, last = (ds[0], ds[-1]) if ds else ("", "")
        within = [d for d in bio_dates if first <= d <= last]
        same_valid = 0
        same_any = 0
        same_flagged = 0
        for d in within:
            r = row_by_date.get(d)
            if not r:
                continue
            rawv = r[v].strip()
            f = r[flags[v]].strip()
            if rawv == "":
                continue
            try:
                x = float(rawv)
            except ValueError:
                continue
            if not math.isfinite(x):
                continue
            same_any += 1
            if f:
                same_flagged += 1
            else:
                same_valid += 1
        expected = {
            "biology_dates_within_valid_span": len(within),
            "same_day_any_numeric": same_any,
            "same_day_valid_unflagged": same_valid,
            "same_day_flagged_numeric": same_flagged,
        }
        for field, exp in expected.items():
            if int(row[field]) != exp:
                overlap_mismatches.append({"variable": v, "field": field, "audit": row[field], "independent": exp})

# checksums
checksums = {
    "bytes": len(raw),
    "md5": hashlib.md5(raw).hexdigest(),
    "sha1": hashlib.sha1(raw).hexdigest(),
    "sha256": hashlib.sha256(raw).hexdigest(),
}

# structural checks
unique_dates = len({r["sampledate"] for r in data})
year_mismatch = sum(1 for r in data if int(r["year4"]) != int(r["sampledate"][:4]))
duplicate_dates = len(data) - unique_dates
exact_duplicates = len(data) - len({tuple(r[h] for h in header) for r in data})

structural = {
    "lines_including_header": len(lines),
    "data_rows": len(data),
    "bad_field_counts": len(bad),
    "header_columns": len(header),
    "unique_dates": unique_dates,
    "duplicate_dates": duplicate_dates,
    "year_mismatches": year_mismatch,
    "exact_duplicate_rows": exact_duplicates,
    "date_min": min(r["sampledate"] for r in data),
    "date_max": max(r["sampledate"] for r in data),
}

# percentage reconciliation
pct_issues = []
with (T / "VARIABLE_COVERAGE_SUMMARY.csv").open(newline="", encoding="utf-8") as fh:
    for row in csv.DictReader(fh):
        total = int(row["total_records"])
        for num_field, pct_field in [
            ("missing", "missing_pct"),
            ("numeric_any", "numeric_any_pct"),
            ("valid_unflagged", "valid_unflagged_pct"),
        ]:
            expected = round(100 * int(row[num_field]) / total, 6)
            if abs(float(row[pct_field]) - expected) > 1e-6:
                pct_issues.append({"variable": row["variable"], "pct_field": pct_field, "audit": row[pct_field], "expected": expected})

result = {
    "checksums": checksums,
    "structural": structural,
    "coverage_mismatches": mismatches,
    "overlap_mismatches": overlap_mismatches,
    "percentage_issues": pct_issues,
    "all_checks_pass": not mismatches and not overlap_mismatches and not pct_issues and not bad,
}
(OUT / "INDEPENDENT_VERIFICATION.json").write_text(json.dumps(result, indent=2), encoding="utf-8")

md = [
    "# Independent Verification",
    "",
    "This is a second-method check of the Sprint 4L.9 audit. It does not import the audit script.",
    "It parses the raw file by simple comma splitting (the data fields contain no embedded commas),",
    "then compares key counts with the generated audit tables.",
    "",
    "## Checksums",
    "",
    "| Item | Value |",
    "|---|---|",
    f"| Bytes | {checksums['bytes']:,} |",
    f"| MD5 | `{checksums['md5']}` |",
    f"| SHA-1 | `{checksums['sha1']}` |",
    f"| SHA-256 | `{checksums['sha256']}` |",
    "",
    "## Structure",
    "",
    "| Item | Value |",
    "|---|---|",
    f"| Lines including header | {structural['lines_including_header']:,} |",
    f"| Data rows | {structural['data_rows']:,} |",
    f"| Bad field counts | {structural['bad_field_counts']} |",
    f"| Columns | {structural['header_columns']} |",
    f"| Unique dates | {structural['unique_dates']:,} |",
    f"| Duplicate dates | {structural['duplicate_dates']} |",
    f"| Year mismatches | {structural['year_mismatches']} |",
    f"| Exact duplicate rows | {structural['exact_duplicate_rows']} |",
    f"| Date range | {structural['date_min']} to {structural['date_max']} |",
    "",
    "## Reconciliation",
    "",
    f"- Variable coverage mismatches: **{len(mismatches)}**",
    f"- Biology overlap mismatches: **{len(overlap_mismatches)}**",
    f"- Percentage reconciliation issues: **{len(pct_issues)}**",
    "",
]
if mismatches:
    md.append("### Coverage mismatches")
    md.append("")
    for m in mismatches:
        md.append(f"- {m}")
if overlap_mismatches:
    md.append("### Overlap mismatches")
    md.append("")
    for m in overlap_mismatches:
        md.append(f"- {m}")
if pct_issues:
    md.append("### Percentage issues")
    md.append("")
    for m in pct_issues:
        md.append(f"- {m}")
if not mismatches and not overlap_mismatches and not pct_issues:
    md.append("All independently recomputed counts and percentages reconcile with the generated audit tables.")
(OUT / "INDEPENDENT_VERIFICATION.md").write_text("\n".join(md) + "\n", encoding="utf-8")

print(json.dumps(result, indent=2))
