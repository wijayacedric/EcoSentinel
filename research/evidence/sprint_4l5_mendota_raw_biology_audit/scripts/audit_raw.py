#!/usr/bin/env python3
"""Reproducible non-confirmatory audit of the Mendota phytoplankton CSV.

Reads the raw file read-only. Writes machine-readable tables to ../tables/
and a summary JSON to ../summary.json. No labels, event intervals or models.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
import re
import statistics
from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path

RAW = Path("research/evidence/sprint_4l_mendota_biology_audit/acquisition/88.31/"
           "North_Temperate_Lakes_LTER_-_Phytoplankton_-_Madison_Lakes_Area__"
           "f2de15b2fff6ae962a04c150c0a1c510.dat")
OUT = Path("research/evidence/sprint_4l5_mendota_raw_biology_audit")
TABLES = OUT / "tables"
EXPECTED_HEADER = ["lakeid", "year4", "sampledate", "sta", "depth_range",
                   "division", "taxa_name", "gald", "cells_per_nu", "nu_per_ml",
                   "cells_per_ml", "biovolume_conc", "biomass_conc",
                   "relative_total_biovolume", "genus"]
NUMERIC = ["gald", "cells_per_nu", "nu_per_ml", "cells_per_ml",
           "biovolume_conc", "biomass_conc", "relative_total_biovolume"]
LAKES = ["ME", "MO", "WI", "FI"]
MONTH_NAMES = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def md5(path: Path) -> str:
    h = hashlib.md5()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def pct(values: list[float], p: float) -> float | None:
    if not values:
        return None
    s = sorted(values)
    k = (len(s) - 1) * p
    lo = int(math.floor(k))
    hi = int(math.ceil(k))
    if lo == hi:
        return s[lo]
    return s[lo] * (hi - k) + s[hi] * (k - lo)


def rnd(x: float | None, nd: int = 6) -> float | None:
    return None if x is None else round(float(x), nd)


def season(month: int) -> str:
    return {12: "winter", 1: "winter", 2: "winter",
            3: "spring", 4: "spring", 5: "spring",
            6: "summer", 7: "summer", 8: "summer",
            9: "autumn", 10: "autumn", 11: "autumn"}[month]


def main() -> int:
    TABLES.mkdir(parents=True, exist_ok=True)
    raw_bytes = RAW.read_bytes()
    size = len(raw_bytes)
    checksum_md5 = md5(RAW)
    checksum_sha = sha256(RAW)
    bom = raw_bytes[:3] == b"\xef\xbb\xbf"
    crlf = raw_bytes.count(b"\r\n")
    lf = raw_bytes.count(b"\n")
    decode_error = None
    try:
        text = raw_bytes.decode("utf-8")
    except UnicodeDecodeError as exc:
        decode_error = str(exc)
        text = raw_bytes.decode("utf-8", errors="replace")

    # Structural parsing
    f = text.splitlines()
    header = next(csv.reader([f[0]])) if f else []
    header_match = header == EXPECTED_HEADER
    rows = []
    malformed = []
    blank = 0
    for i, line in enumerate(f[1:], start=2):
        if not line.strip():
            blank += 1
            continue
        try:
            vals = next(csv.reader([line]))
        except Exception as exc:
            malformed.append({"line": i, "error": str(exc)[:160]})
            continue
        if len(vals) != len(EXPECTED_HEADER):
            malformed.append({"line": i, "fields": len(vals),
                              "preview": line[:160]})
            continue
        rows.append(dict(zip(EXPECTED_HEADER, vals)))

    # Type parsing
    parse_errors = Counter()
    year_mismatch = []
    dates_by_lake = defaultdict(set)
    records_by_lake = Counter()
    depth_by_lake = defaultdict(Counter)
    sta_by_lake = defaultdict(Counter)
    month_counts = Counter()
    season_counts = Counter()
    annual = defaultdict(lambda: {"records": 0, "dates": set(), "months": set()})
    mendota_annual = defaultdict(lambda: {"records": 0, "dates": set(), "months": set(),
                                         "taxa": set(), "genera": set(), "cyano": 0, "records_per_date": Counter()})
    numeric_values = {k: [] for k in NUMERIC}
    numeric_by_lake = {k: defaultdict(list) for k in NUMERIC}
    numeric_errors = Counter()
    zeros_by_var_lake = defaultdict(Counter)
    exact_rows = Counter()
    key_groups = defaultdict(list)
    date_taxon_groups = defaultdict(list)
    genus_mismatch = []
    trailing_taxa = 0
    double_space_taxa = 0
    leading_taxa = 0
    resolution_names = set()
    division_counts = Counter()
    taxa_names = set()
    genus_names = set()
    tx_records = Counter()
    tx_first = {}
    tx_last = {}
    tx_lakes = defaultdict(set)
    tx_dates = defaultdict(set)
    tx_genus = defaultdict(set)
    tx_div = defaultdict(set)
    tx_raw_variants = defaultdict(set)
    tx_genus_raw_variants = defaultdict(set)
    date_objs = {}
    row_date = []
    lake_dates = defaultdict(set)
    lake_rows = Counter()
    lake_taxa = defaultdict(set)
    lake_genera = defaultdict(set)
    cyano_rows = Counter()
    sta_by_lake_depth = Counter()

    for r in rows:
        lake = (r["lakeid"] or "").strip()
        lake_rows[lake] += 1
        records_by_lake[lake] += 1
        raw_taxa = r["taxa_name"]
        taxa = raw_taxa.strip()
        raw_genus = r["genus"]
        genus = raw_genus.strip()
        division = (r["division"] or "").strip()
        depth = (r["depth_range"] or "").strip()
        sta = (r["sta"] or "").strip()
        depth_by_lake[lake][depth] += 1
        sta_by_lake[lake][sta] += 1
        sta_by_lake_depth[(lake, depth, sta)] += 1
        division_counts[division] += 1
        if raw_taxa != raw_taxa.rstrip():
            trailing_taxa += 1
        if raw_taxa != raw_taxa.lstrip():
            leading_taxa += 1
        if "  " in raw_taxa:
            double_space_taxa += 1
        if raw_taxa != raw_taxa.strip() or raw_genus != raw_genus.strip():
            pass
        try:
            year = int(r["year4"])
        except Exception:
            parse_errors["year4"] += 1
            year = None
        try:
            d = datetime.strptime(r["sampledate"].strip(), "%Y-%m-%d").date()
        except Exception:
            parse_errors["sampledate"] += 1
            d = None
        if d is None:
            continue
        date_objs[r["sampledate"]] = d
        row_date.append(d)
        dates_by_lake[lake].add(d)
        lake_dates[lake].add(d)
        annual[(lake, d.year)]["records"] += 1
        annual[(lake, d.year)]["dates"].add(d)
        annual[(lake, d.year)]["months"].add(d.month)
        month_counts[(d.year, d.month)] += 1
        season_counts[season(d.month)] += 1
        if year is not None and year != d.year:
            year_mismatch.append({"lakeid": lake, "year4": year,
                                  "sampledate": d.isoformat()})
        if lake == "ME":
            mendota_annual[d.year]["records"] += 1
            mendota_annual[d.year]["dates"].add(d)
            mendota_annual[d.year]["months"].add(d.month)
            mendota_annual[d.year]["taxa"].add(taxa)
            mendota_annual[d.year]["genera"].add(genus)
            if division == "Cyanophyta":
                mendota_annual[d.year]["cyano"] += 1
                mendota_annual[d.year]["records_per_date"][d.isoformat()] += 1
        if lake == "ME":
            cyano_rows[division] += 1
        lake_taxa[lake].add(taxa)
        lake_genera[lake].add(genus)
        taxa_names.add(taxa)
        genus_names.add(genus)
        tx_records[taxa] += 1
        tx_lakes[taxa].add(lake)
        tx_dates[taxa].add(d.isoformat())
        tx_genus[taxa].add(genus)
        tx_div[taxa].add(division)
        tx_raw_variants[taxa].add(raw_taxa)
        tx_genus_raw_variants[taxa].add(raw_genus)
        tx_first.setdefault(taxa, d)
        tx_last[taxa] = d
        first = taxa.split()[0] if taxa else ""
        if genus and first and first.casefold() != genus.casefold():
            genus_mismatch.append({"taxa_name": raw_taxa, "taxa_clean": taxa,
                                   "genus": raw_genus, "division": division})
        if re.search(r"\b(sp\.?|spp\.?|var\.?|cf\.?|aff\.?|unidentified|unknown)\b",
                     taxa, re.IGNORECASE):
            resolution_names.add(taxa)
        numeric_ok = True
        for var in NUMERIC:
            raw = (r[var] or "").strip()
            if raw == "":
                numeric_errors[var] += 1
                numeric_ok = False
                continue
            try:
                val = float(raw)
            except ValueError:
                numeric_errors[var] += 1
                numeric_ok = False
                continue
            numeric_values[var].append(val)
            numeric_by_lake[var][lake].append(val)
            if val == 0:
                zeros_by_var_lake[var][lake] += 1
        if numeric_ok:
            exact_rows[tuple(r[k] for k in EXPECTED_HEADER)] += 1
        key_groups[(lake, d.isoformat(), sta, depth, taxa)].append(r)
        date_taxon_groups[(lake, d.isoformat(), taxa)].append(r)

    # Coverage/summary
    by_lake = []
    for lake in LAKES:
        ds = sorted(dates_by_lake.get(lake, set()))
        recs = lake_rows.get(lake, 0)
        by_lake.append({
            "lakeid": lake, "records": recs, "unique_dates": len(ds),
            "first_date": ds[0].isoformat() if ds else "",
            "last_date": ds[-1].isoformat() if ds else "",
            "depth_values": dict(depth_by_lake.get(lake, {})),
            "sta_values": dict(sta_by_lake.get(lake, {})),
            "unique_taxa": len(lake_taxa.get(lake, set())),
            "unique_genera": len(lake_genera.get(lake, set())),
        })
    overall_dates = sorted(set(row_date))
    coverage = {
        "rows": len(rows),
        "columns": len(EXPECTED_HEADER),
        "unique_dates": len(overall_dates),
        "first_date": overall_dates[0].isoformat() if overall_dates else "",
        "last_date": overall_dates[-1].isoformat() if overall_dates else "",
        "by_lake": by_lake,
        "month_counts": {f"{y}-{m:02d}": n for (y, m), n in sorted(month_counts.items())},
        "season_counts": dict(season_counts),
    }

    # Annual coverage tables
    annual_rows = []
    for (lake, year), rec in sorted(annual.items()):
        ds = sorted(rec["dates"])
        gaps = [(ds[i + 1] - ds[i]).days for i in range(len(ds) - 1)]
        annual_rows.append({
            "lakeid": lake, "year": year, "records": rec["records"],
            "unique_dates": len(ds),
            "first_date": ds[0].isoformat(), "last_date": ds[-1].isoformat(),
            "months_present": ";".join(str(m) for m in sorted(rec["months"])),
            "median_gap_days": statistics.median(gaps) if gaps else "",
            "max_gap_days": max(gaps) if gaps else "",
        })
    with (TABLES / "ANNUAL_SAMPLING_COVERAGE.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(annual_rows[0].keys()))
        w.writeheader(); w.writerows(annual_rows)

    mendota_rows = []
    for year, rec in sorted(mendota_annual.items()):
        ds = sorted(rec["dates"])
        gaps = [(ds[i + 1] - ds[i]).days for i in range(len(ds) - 1)]
        mendota_rows.append({
            "year": year, "records": rec["records"], "unique_dates": len(ds),
            "first_date": ds[0].isoformat(), "last_date": ds[-1].isoformat(),
            "months_present": ";".join(str(m) for m in sorted(rec["months"])),
            "median_gap_days": statistics.median(gaps) if gaps else "",
            "max_gap_days": max(gaps) if gaps else "",
            "unique_taxa": len(rec["taxa"]), "unique_genera": len(rec["genera"]),
            "cyanophyta_records": rec["cyano"],
            "median_records_per_date": statistics.median(
                rec["records_per_date"].values()) if rec["records_per_date"] else "",
        })
    with (TABLES / "MENDOTA_RECORD_COVERAGE.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(mendota_rows[0].keys()))
        w.writeheader(); w.writerows(mendota_rows)

    # Sampling intervals
    intervals = []
    for lake in LAKES:
        ds = sorted(dates_by_lake.get(lake, set()))
        for a, b in zip(ds, ds[1:]):
            intervals.append({
                "lakeid": lake, "from_date": a.isoformat(), "to_date": b.isoformat(),
                "gap_days": (b - a).days, "pre_post_2013": "pre" if a < date(2013, 2, 1) else "post",
                "season_from": season(a.month), "season_to": season(b.month),
                "long_gap_ge_30": (b - a).days >= 30,
                "long_gap_ge_60": (b - a).days >= 60,
                "long_gap_ge_90": (b - a).days >= 90,
            })
    with (TABLES / "SAMPLING_INTERVALS_AND_GAPS.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(intervals[0].keys()))
        w.writeheader(); w.writerows(intervals)
    gap_summary = {}
    for lake in LAKES:
        g = [x["gap_days"] for x in intervals if x["lakeid"] == lake]
        gap_summary[lake] = {
            "n": len(g), "median": statistics.median(g) if g else None,
            "mean": rnd(statistics.mean(g)) if g else None,
            "min": min(g) if g else None, "max": max(g) if g else None,
            "ge30": sum(v >= 30 for v in g), "ge60": sum(v >= 60 for v in g),
            "ge90": sum(v >= 90 for v in g),
        }

    # Numeric stats
    quality_rows = []
    for var in NUMERIC:
        for scope in ["all"] + LAKES:
            vals = numeric_values[var] if scope == "all" else numeric_by_lake[var].get(scope, [])
            if not vals:
                continue
            zeros = sum(v == 0 for v in vals)
            quality_rows.append({
                "variable": var, "scope": scope, "n": len(vals),
                "missing": 0, "zeros": zeros,
                "negative": sum(v < 0 for v in vals),
                "nonfinite": sum(not math.isfinite(v) for v in vals),
                "min": rnd(min(vals)), "p01": rnd(pct(vals, 0.01)),
                "p05": rnd(pct(vals, 0.05)), "p25": rnd(pct(vals, 0.25)),
                "median": rnd(statistics.median(vals)), "p75": rnd(pct(vals, 0.75)),
                "p95": rnd(pct(vals, 0.95)), "p99": rnd(pct(vals, 0.99)),
                "max": rnd(max(vals)), "mean": rnd(statistics.mean(vals)),
                "sd": rnd(statistics.pstdev(vals)),
            })
    with (TABLES / "BIOLOGICAL_VARIABLE_QUALITY.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(quality_rows[0].keys()))
        w.writeheader(); w.writerows(quality_rows)

    # Numeric extremes (top 10 per variable)
    extremes = []
    for var in NUMERIC:
        recs = []
        for r in rows:
            try:
                recs.append((float(r[var]), r))
            except ValueError:
                pass
        for val, r in sorted(recs, key=lambda x: x[0], reverse=True)[:10]:
            extremes.append({
                "variable": var, "value": rnd(val), "lakeid": r["lakeid"],
                "sampledate": r["sampledate"], "depth_range": r["depth_range"],
                "division": r["division"], "taxa_name": r["taxa_name"],
                "cells_per_ml": r["cells_per_ml"], "biovolume_conc": r["biovolume_conc"],
                "biomass_conc": r["biomass_conc"],
            })
    with (TABLES / "NUMERIC_EXTREMES.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(extremes[0].keys()))
        w.writeheader(); w.writerows(extremes)

    # Arithmetic consistency
    cell_rel = []
    bio_rel = []
    rel_dev = []
    rel_groups = defaultdict(list)
    for r in rows:
        try:
            expected = float(r["cells_per_nu"]) * float(r["nu_per_ml"])
            actual = float(r["cells_per_ml"])
            if expected != 0:
                cell_rel.append(abs(actual - expected) / abs(expected))
        except ValueError:
            pass
        try:
            b = float(r["biovolume_conc"]); m = float(r["biomass_conc"])
            if b != 0:
                bio_rel.append(abs(m - b * 1e-6) / abs(b * 1e-6))
        except ValueError:
            pass
        rel_groups[(r["lakeid"], r["sampledate"], r["sta"], r["depth_range"])].append(r)
    for key, rs in rel_groups.items():
        total = sum(float(x["biovolume_conc"]) for x in rs)
        if total != 0:
            for x in rs:
                expected = float(x["biovolume_conc"]) / total * 100
                rel_dev.append(abs(float(x["relative_total_biovolume"]) - expected))
    consistency = {
        "cells_per_ml_vs_cells_per_nu_x_nu_per_ml": {
            "n": len(cell_rel), "max_abs_rel_error": rnd(max(cell_rel)),
            "n_rel_error_gt_0.01": sum(x > 0.01 for x in cell_rel),
            "n_rel_error_gt_0.001": sum(x > 0.001 for x in cell_rel),
        },
        "biomass_vs_biovolume_x_1e-6": {
            "n": len(bio_rel), "max_abs_rel_error": rnd(max(bio_rel)),
            "n_rel_error_gt_0.01": sum(x > 0.01 for x in bio_rel),
            "n_rel_error_gt_0.001": sum(x > 0.001 for x in bio_rel),
        },
        "relative_total_biovolume_vs_group_sum": {
            "n": len(rel_dev), "max_abs_percentage_point_deviation": rnd(max(rel_dev)),
            "n_abs_dev_gt_0.01_pp": sum(x > 0.01 for x in rel_dev),
            "n_abs_dev_gt_1_pp": sum(x > 1 for x in rel_dev),
        },
    }

    # Taxonomy inventory
    inv = []
    for taxa, n in tx_records.most_common():
        first = taxa.split()[0] if taxa else ""
        genus_values = sorted(tx_genus[taxa])
        genus_match = any(first.casefold() == g.casefold() for g in genus_values) if first else None
        flags = []
        if any(v != v.rstrip() for v in tx_raw_variants[taxa]): flags.append("trailing_space")
        if any("  " in v for v in tx_raw_variants[taxa]): flags.append("double_space")
        if genus_match is False: flags.append("genus_field_mismatch")
        if re.search(r"\b(sp\.?|spp\.?|var\.?|cf\.?|aff\.?|unidentified|unknown)\b", taxa, re.IGNORECASE):
            flags.append("unresolved_or_infraspecific")
        inv.append({
            "taxa_name_clean": taxa,
            "taxa_name_raw_variants": "|".join(sorted(tx_raw_variants[taxa])),
            "genus_values": "|".join(genus_values),
            "divisions": "|".join(sorted(tx_div[taxa])),
            "records": n, "lakes": "|".join(sorted(tx_lakes[taxa])),
            "first_date": tx_first[taxa].isoformat(), "last_date": tx_last[taxa].isoformat(),
            "n_dates": len(tx_dates[taxa]),
            "genus_first_token_match": genus_match,
            "flags": ";".join(flags),
        })
    with (TABLES / "TAXONOMIC_NAME_INVENTORY.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(inv[0].keys()))
        w.writeheader(); w.writerows(inv)

    # Taxonomy name changes pre/post 2013
    pre_names = {r["taxa_name"].strip() for r in rows if r["sampledate"] < "2013-02-01"}
    post_names = {r["taxa_name"].strip() for r in rows if r["sampledate"] >= "2013-02-01"}
    changes = []
    for taxa in sorted((pre_names - post_names) | (post_names - pre_names)):
        subset = [r for r in rows if r["taxa_name"].strip() == taxa]
        changes.append({
            "taxa_name_clean": taxa, "status": "only_pre_2013" if taxa in pre_names - post_names else "only_post_2013",
            "records": len(subset), "first_date": min(r["sampledate"] for r in subset),
            "last_date": max(r["sampledate"] for r in subset),
            "divisions": "|".join(sorted({r["division"] for r in subset})),
        })
    with (TABLES / "TAXONOMIC_NAME_CHANGES.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(changes[0].keys()))
        w.writeheader(); w.writerows(changes)

    # Explicit synonym/nomenclature pattern counts
    patterns = {
        "Melosira": r"\bmelosira\b",
        "Aulacoseira": r"\baulacoseira\b",
        "Oscillatoria": r"\boscillatoria\b",
        "Pseudanabaena/Psuedanabaena": r"\b(?:pseudanabaena|psuedanabaena)\b",
        "Synedra tenera": r"synedra tenera",
        "Synedra filiformis": r"synedra filiformis",
        "Phacotus": r"\bphacotus\b",
        "Phormidium mucicola": r"phormidium mucicola",
        "Glenodinium": r"\bglenodinium\b",
        "Chrysococcus": r"\bchrysococcus\b",
        "Microcystis": r"\bmicrocystis\b",
        "Cylindrospermopsis raciborskii": r"cylindrospermopsis raciborskii",
        "Anabaenopsis raciborskii": r"anabaenopsis raciborskii",
        "Erkenia": r"\berkenia\b",
    }
    syn_rows = []
    for label, pat in patterns.items():
        regex = re.compile(pat, re.IGNORECASE)
        subset = [r for r in rows if regex.search(r["taxa_name"])]
        by_year = Counter(r["sampledate"][:4] for r in subset)
        for year, n in sorted(by_year.items()):
            syn_rows.append({"pattern": label, "year": year, "records": n})
    with (TABLES / "SYNONYM_PATTERN_COUNTS.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["pattern", "year", "records"])
        w.writeheader(); w.writerows(syn_rows)

    # Duplicates
    exact_dups = []
    for key, count in exact_rows.items():
        if count > 1:
            d = dict(zip(EXPECTED_HEADER, key))
            d["duplicate_count"] = count
            exact_dups.append(d)
    with (TABLES / "EXACT_DUPLICATE_ROWS.csv").open("w", newline="", encoding="utf-8") as fh:
        fields = EXPECTED_HEADER + ["duplicate_count"]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader(); w.writerows(exact_dups)

    dup_groups = []
    for (lake, d, sta, depth, taxa), rs in key_groups.items():
        if len(rs) > 1:
            cells = [float(x["cells_per_ml"]) for x in rs]
            bio = [float(x["biovolume_conc"]) for x in rs]
            dup_groups.append({
                "lakeid": lake, "sampledate": d, "sta": sta, "depth_range": depth,
                "taxa_name_clean": taxa, "n_rows": len(rs),
                "n_distinct_cells_per_ml": len(set(cells)),
                "n_distinct_biovolume_conc": len(set(bio)),
                "cells_min": rnd(min(cells)), "cells_max": rnd(max(cells)),
                "biovolume_min": rnd(min(bio)), "biovolume_max": rnd(max(bio)),
                "genus_values": "|".join(sorted({x["genus"].strip() for x in rs})),
                "division_values": "|".join(sorted({x["division"].strip() for x in rs})),
            })
    with (TABLES / "DUPLICATE_GROUPS.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(dup_groups[0].keys()))
        w.writeheader(); w.writerows(dup_groups)

    # Depth/station table
    depth_station = []
    for (lake, depth, sta), n in sorted(sta_by_lake_depth.items()):
        depth_station.append({"lakeid": lake, "depth_range": depth, "sta": sta, "records": n})
    with (TABLES / "DEPTH_STATION_COUNTS.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["lakeid", "depth_range", "sta", "records"])
        w.writeheader(); w.writerows(depth_station)

    # Schema comparison
    with (TABLES / "SCHEMA_COMPARISON.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh); w.writerow(["expected_column", "actual_column", "match"])
        for i, col in enumerate(EXPECTED_HEADER):
            actual = header[i] if i < len(header) else ""
            w.writerow([col, actual, col == actual])

    summary = {
        "file": {
            "path": str(RAW), "bytes": size, "md5": checksum_md5, "sha256": checksum_sha,
            "bom": bom, "crlf_count": crlf, "lf_count": lf,
            "decoding_error": decode_error, "header": header, "header_match": header_match,
            "header_columns": len(header), "rows": len(rows), "malformed_rows": len(malformed),
            "blank_lines": blank, "parse_errors": dict(parse_errors),
            "year_mismatch_count": len(year_mismatch),
        },
        "coverage": coverage,
        "gaps": gap_summary,
        "numeric": {
            "variables": NUMERIC,
            "errors": dict(numeric_errors),
            "zeros_by_variable_lake": {k: dict(v) for k, v in zeros_by_var_lake.items()},
            "consistency": consistency,
        },
        "taxonomy": {
            "distinct_taxa_clean": len(taxa_names),
            "distinct_genera_clean": len(genus_names),
            "divisions": dict(division_counts),
            "trailing_space_records": trailing_taxa,
            "leading_space_records": leading_taxa,
            "double_space_records": double_space_taxa,
            "genus_mismatch_records": len(genus_mismatch),
            "genus_mismatch_examples": genus_mismatch[:10],
            "unresolved_names": len(resolution_names),
            "pre_names": len(pre_names), "post_names": len(post_names),
            "only_pre": len(pre_names - post_names), "only_post": len(post_names - pre_names),
        },
        "duplicates": {
            "exact_duplicate_groups": len(exact_dups),
            "exact_duplicate_rows": sum(x["duplicate_count"] for x in exact_dups),
            "key_duplicate_groups": len(dup_groups),
            "key_duplicate_rows": sum(x["n_rows"] for x in dup_groups),
            "max_group_size": max((x["n_rows"] for x in dup_groups), default=1),
        },
        "depth": {
            "by_lake": {lake: dict(depth_by_lake[lake]) for lake in LAKES},
            "sta_by_lake": {lake: dict(sta_by_lake[lake]) for lake in LAKES},
            "mendota_non_0_8": sum(1 for r in rows if r["lakeid"] == "ME" and r["depth_range"] != "0-8m"),
        },
    }
    (OUT / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    # compact console summary
    print(json.dumps({
        "file": summary["file"],
        "coverage": {"rows": len(rows), "unique_dates": len(overall_dates),
                     "first": coverage["first_date"], "last": coverage["last_date"],
                     "by_lake": {x["lakeid"]: {k: x[k] for k in ("records", "unique_dates", "first_date", "last_date")} for x in by_lake}},
        "gaps": gap_summary,
        "taxonomy": summary["taxonomy"],
        "duplicates": summary["duplicates"],
        "depth": summary["depth"],
        "consistency": consistency,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
