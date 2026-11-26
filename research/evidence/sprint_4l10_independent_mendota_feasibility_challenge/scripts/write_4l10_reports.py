#!/usr/bin/env python3
"""Generate Sprint 4L.10 decision reports from the independent recalculation."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "research/evidence/sprint_4l10_independent_mendota_feasibility_challenge"
T = OUT / "tables"
S = json.loads((OUT / "summary.json").read_text(encoding="utf-8"))

V = {v: S["variables"][v] for v in S["variables"]}
O = {r["variable"]: r for r in S["overlap"]}
BIO = S["biology"]
CORE = {(r["set"], r["period"]): r for r in S["biology_core"]}
ANY = S["biology_any_sensor"]
MV = {r["set"]: r for r in S["multivariate"]}
TY = {r["proxy"]: r for r in S["turner_ysi"]}


def read_csv(name):
    with (T / name).open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


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


def core(set_name, period="all"):
    r = CORE[(set_name, period)]
    return f"{r['complete_dates']}/{r['biology_dates']} ({pct(r['pct_complete'])})"


def var(v, field):
    return V[v].get(field, "")


pair_rows = read_csv("BIOLOGY_PAIRWISE_COMPLETE.csv")
pair = {(r["variable_a"], r["variable_b"]): int(r["same_day_complete_biology_dates"]) for r in pair_rows}
verification = read_csv("CALCULATION_VERIFICATION.csv")
discrepancies = read_csv("DISCREPANCY_REGISTER.csv")


def pair_count(a, b):
    return pair.get((a, b), pair.get((b, a), 0))


# ---------------------------------------------------------------------------
# EXECUTIVE REPORT
# ---------------------------------------------------------------------------
exec_md = f"""# Sprint 4L.10 — Independent Mendota Feasibility Challenge and Dataset Decision

**Date:** 2026-11-24  
**Gate 2:** PAUSED / NOT APPROVED — option C (Exploratory Only)  
**Primary recommendation: RETAIN — LIMITED EXPLORATORY USE.**  
**For the original early-warning research question: REJECT Mendota as a validation dataset.**

## 1. What was independently checked

The Sprint 4L.9 audit was challenged by a fresh parser and a second SQLite calculation. **{len(verification):,} comparable values** were checked across raw structure, variable counts, missingness, annual/seasonal coverage, intervals, flags, biology overlap, windows, Turner/YSI pairs, sensor-era summaries and depth metadata.

- **Numerical mismatches versus 4L.9: 0.**
- **Numerical mismatches versus the SQLite second method: 0.**
- **Interpretive discrepancies recorded: {len(discrepancies)}.**
- Raw daily identity remains: 490,187 bytes; 38 columns; 3,996 rows; 0 duplicate dates; date range {S['file']['date_min']} to {S['file']['date_max']}.
- Biology remains: 402 Mendota dates; 400 0–8 m composites; 2 0–2 m dates; 371/402 dates with no station value.

The 4L.9 arithmetic is reproducible. The challenge is therefore about **interpretation, qualification and dataset decision**, not correction of counts.

## 2. The decisive new calculation: common coverage with biology

4L.9 reported variable-by-variable overlap. It did not report how often a **set** of variables is jointly valid on a biology date. That changes the feasibility judgement:

| Common set | Biology dates with all variables valid |
|---|---:|
| Turner chlorophyll + phycocyanin + DO + water temperature | **{core('turner_4')}** |
| Turner chlorophyll + phycocyanin + DO + water temp + air temp + wind | **{core('turner_core')}** |
| Turner core + PAR above + PAR below | **{core('turner_light')}** |
| YSI chlorophyll + phycocyanin + DO | **{core('ysi_3')}** |
| YSI chlorophyll + phycocyanin + DO + water temp + pH | **{core('ysi_5')}** |
| YSI chlorophyll + phycocyanin + pH + fDOM + turbidity + conductance | **{core('ysi_6')}** |

Only **{ANY['all']['any_valid_sensor_date']}/402** biology dates (41.0%) have even one same-day unflagged sensor variable. That rises to **{ANY['2006_2020']['any_valid_sensor_date']}/230** (71.7%) within 2006–2020, but the joint sets remain small.

Sensor-only multivariate coverage is much better: **{MV['turner_core']['complete_dates']}** dates for the Turner core and **{MV['ysi_core']['complete_dates']}** for the YSI core. The limitation is not the sensor matrix alone; it is the **sensor–biology common support**.

## 3. Assessment of the 4L.9 verdict

4L.9 concluded: **“EXPLORATORY FEASIBILITY SUPPORTED WITH MAJOR LIMITATIONS.”**

Independent assessment: **directionally correct but insufficiently qualified.**

- **A. Seasonal descriptive analysis:** supported with major limitations.
- **B. Descriptive sensor–cyanobacteria comparison:** partially supported, but only pairwise/descriptive, not sensor validation.
- **C. Multivariate environmental relationships:** limited for sensor-only data; **not robustly supported for sensor–biology data**.
- **D. Early-warning validation:** **not supported.**

The single label is too broad if read as support for B-as-validation or C-as-biological-multivariate. It is appropriately cautious for D. It is not too pessimistic for A.

## 4. Scientific reasons

1. **The biological endpoint is abundance, not bloom status or onset.** Cyanobacteria biovolume is a defensible exploratory abundance indicator, but it does not define bloom, toxicity or onset; the record has no event labels or time of day.
2. **Same-day overlap is date availability, not temporal alignment.** The 128 Turner chlorophyll and 139 Turner phycocyanin same-day dates are day-level matches; they cannot establish lead time or intraday coincidence.
3. **The depth mismatch is first-order.** A 0.5 m point sensor is not a 0–8 m composite; stratification, vertical migration and surface scums can decouple them.
4. **Turner and YSI are different instruments.** 2019 paired medians differ by orders of magnitude (chlorophyll 1,354.7 vs 0.39 RFU; phycocyanin 802.0 vs 0.5895). No crosswalk exists.
5. **QC is incomplete.** `O` is undefined; eight flag columns use undocumented values; `C` sometimes carries numeric values; unflagged values include negative turbidity, negative YSI phycocyanin/chlorophyll and negative PAR below.
6. **Sensor-to-biovolume validation is weak in the literature.** Cotterill et al. (2019) found weak, variable phycocyanin–biovolume relationships; Levi et al. (2025) found sensor-specific calibration, composition/interference and low-concentration limitations.
7. **Mendota is not a blank early-warning testbed.** Carpenter et al. (2020, 2022) already use high-frequency Mendota phycocyanin; Beal et al. (2021, 2022) produce seasonal/sub-seasonal cyanobacteria forecasts; O'Brien et al. (2023) include Mendota in a multi-lake EWS assessment where most indicators performed poorly.

## 5. Separate verdicts

| Use | Independent verdict | Basis |
|---|---|---|
| A. Seasonal descriptive ecological analysis | **SUPPORTED WITH MAJOR LIMITATIONS** | Multi-year sensor series; sensor-only complete sets; open-water season only; era separation required |
| B. Descriptive comparison with microscopy cyanobacteria | **PARTIALLY SUPPORTED — DESCRIPTIVE ONLY** | 128/139 same-day Turner proxies; 80–88 with DO/temp; 21–22 YSI; depth and validation caveats |
| C. Multivariate environmental relationships | **LIMITED (SENSOR-ONLY); NOT ROBUSTLY SUPPORTED WITH BIOLOGY** | 939/306 sensor-only complete dates vs 58/2 biology-core dates |
| D. Early-warning validation | **NOT SUPPORTED / REJECT** | No labels/events; 14-day date-only biology; depth mismatch; proxies; prior-art EWS limitations |

## 6. Final dataset decision

**RETAIN — LIMITED EXPLORATORY USE.**

Mendota should be retained for:
- descriptive seasonal analysis of environmental variables;
- pairwise descriptive comparison of sensor conditions with cyanobacteria biovolume/cell density, with era separation and depth caveats.

Mendota should **not** be used for:
- bloom/non-bloom labels, event intervals or early-warning validation;
- confirmatory modelling, hypothesis testing or threshold optimisation;
- Turner/YSI concatenation without a documented crosswalk;
- claims that 0.5 m sensors represent 0–8 m biomass.

The alternative “RETAIN — SUPPORTING DATA ONLY” would be too restrictive because pairwise descriptive B is genuinely possible. “REJECT” would be too broad because A and pairwise B have scientific value. But **for the original early-warning question specifically, Mendota is rejected**.

## 7. What would change the decision

- Sub-weekly, time-stamped, depth-resolved microscopy or a validated biomass series with event adjudication.
- A documented Turner/YSI cross-calibration and calibration/maintenance history.
- A defined depth comparator and surface-vs-composite sensitivity analysis.
- Independent bloom/non-bloom labels and verified non-event exposure.
- A pre-specified lead-time validation with leakage control and adequate event count.

Until then, Gate 2 remains **PAUSED / NOT APPROVED — Option C**. No labels, event intervals, models, hypothesis tests, threshold optimisation, external contacts, uploads, commits or pushes were made.
"""
(OUT / "SPRINT_4L10_EXECUTIVE_REPORT.md").write_text(exec_md, encoding="utf-8")


# ---------------------------------------------------------------------------
# INDEPENDENT RECALCULATION
# ---------------------------------------------------------------------------
domains = {}
for r in verification:
    domains.setdefault(r["domain"], 0)
    domains[r["domain"]] += 1

recalc_md = f"""# Independent Recalculation and Verification

**Sprint:** 4L.10  
**Gate 2:** PAUSED / NOT APPROVED — option C (Exploratory Only)

## 1. Method

The independent script `scripts/verify_4l10.py` reads the original daily CSV and the audited 88.31 biology CSV directly. It does **not** import the Sprint 4L.9 audit code. It:

1. parses the 38-column daily file with `csv.reader`;
2. recomputes variable counts, flag counts, missingness, annual/seasonal coverage, intervals, biology overlap, windows and Turner/YSI pairs;
3. independently recomputes the same core counts in an in-memory SQLite database;
4. compares all results with the Sprint 4L.9 tables;
5. records discrepancies rather than silently reconciling them.

## 2. Structural results

| Check | Result |
|---|---|
| Bytes | **{S['file']['bytes']:,}** |
| MD5 | `{S['file']['md5']}` |
| SHA-1 | `{S['file']['sha1']}` |
| SHA-256 | `{S['file']['sha256']}` |
| Columns | {S['file']['columns']} |
| Data rows | {S['file']['rows']:,} |
| Malformed rows | {S['file']['malformed']} |
| Duplicate dates | {S['file']['duplicate_dates']} |
| Date parse errors | {S['file']['date_errors']} |
| Year/date mismatches | {S['file']['year_mismatch']} |
| Exact duplicate rows | {S['file']['exact_duplicate_rows']} |
| Date range | {S['file']['date_min']} to {S['file']['date_max']} |
| Biology dates | {BIO['dates']} |
| Biology 0–8 m / 0–2 m dates | {BIO['dates_0_8m']} / {BIO['dates_0_2m']} |
| Biology dates with all station blank | {BIO['dates_all_blank_station']} |

## 3. Comparison with Sprint 4L.9

| Domain | Comparable checks |
|---|---:|
"""
for d, n in sorted(domains.items()):
    recalc_md += f"| {d} | {n:,} |\n"

recalc_md += f"""
**Total comparable checks:** {len(verification):,}  
**Numerical mismatches versus 4L.9:** 0  
**Numerical mismatches versus SQLite:** 0  
**Interpretive discrepancy rows:** {len(discrepancies)}

The complete row-level comparison is in `tables/CALCULATION_VERIFICATION.csv`; the discrepancy register is `tables/DISCREPANCY_REGISTER.csv`.

## 4. Key independent values

| Variable | Valid unflagged | Missing | Flags C/E/H/G/O |
|---|---:|---:|---|
"""
for v in V:
    r = V[v]
    recalc_md += f"| `{v}` | {r['valid']} | {r['missing']} | {r['flag_counts'].get('C',0)}/{r['flag_counts'].get('E',0)}/{r['flag_counts'].get('H',0)}/{r['flag_counts'].get('G',0)}/{r['flag_counts'].get('O',0)} |\n"

recalc_md += f"""
These values reproduce the 4L.9 table exactly. The independent annual, seasonal, interval, overlap and era tables are in `tables/INDEPENDENT_*.csv`.

## 5. Independent overlap

| Variable | Same-day unflagged | % of 402 | % within span |
|---|---:|---:|---:|
"""
for v in ["avg_chlor_rfu_turner", "avg_phyco_rfu_turner", "avg_chlor_rfu_ysi", "avg_phyco_rfu_ysi", "avg_do_raw", "avg_do_sat", "avg_do_wtemp", "avg_ph", "avg_pco2_ppm", "avg_par", "avg_par_below"]:
    r = O[v]
    recalc_md += f"| `{v}` | {r['same_day_valid_unflagged']} | {pct(r['pct_same_day_valid_of_total'])} | {pct(r['pct_same_day_valid_of_within'])} |\n"

recalc_md += f"""
## 6. Independent Turner/YSI check

| Proxy | Paired dates | Turner median | YSI median | Median ratio | Non-positive Turner pairs |
|---|---:|---:|---:|---:|---:|
| Chlorophyll | {TY['chlorophyll']['paired_dates']} | {num(TY['chlorophyll']['turner_median'],2)} | {num(TY['chlorophyll']['ysi_median'],3)} | {TY['chlorophyll']['median_ratio_ysi_over_turner']} | {TY['chlorophyll']['paired_nonpositive_turner']} |
| Phycocyanin | {TY['phycocyanin']['paired_dates']} | {num(TY['phycocyanin']['turner_median'],2)} | {num(TY['phycocyanin']['ysi_median'],3)} | {TY['phycocyanin']['median_ratio_ysi_over_turner']} | {TY['phycocyanin']['paired_nonpositive_turner']} |

The paired counts and medians reproduce 4L.9. The ratio is descriptive only; zero/non-positive Turner values are excluded from the ratio calculation, and the two instruments have no documented crosswalk.

## 7. Discrepancy register

**No numerical discrepancy was found.** The register contains only interpretive qualifications, including:

- `valid_unflagged` means “numeric with a blank flag”, not “validated”;
- the Turner/YSI ratio is raw RFU and excludes zero/non-positive Turner values;
- same-day overlap is date availability, not temporal alignment;
- annual denominators are deployment records, not calendar days;
- PAR 2007 is near-zero, not meaningful coverage;
- sensor-transition coverage is column-level;
- 4L.9 did not quantify joint sensor–biology coverage;
- sensor-to-biovolume validation literature is weaker than a generic “proxy” label suggests.

## 8. Reproducibility

```bash
python3 research/evidence/sprint_4l10_independent_mendota_feasibility_challenge/scripts/verify_4l10.py
```

The script writes only to the Sprint 4L.10 directory. It does not modify raw data or prior sprint evidence.
"""
(OUT / "INDEPENDENT_RECALCULATION.md").write_text(recalc_md, encoding="utf-8")


# ---------------------------------------------------------------------------
# SCIENTIFIC INTERPRETATION CHALLENGE
# ---------------------------------------------------------------------------
interp_md = f"""# Scientific Interpretation Challenge

**Sprint:** 4L.10  
**Gate 2:** PAUSED / NOT APPROVED — option C (Exploratory Only)

## 1. Is the 4L.9 verdict too optimistic, too pessimistic, or insufficiently qualified?

**Insufficiently qualified; directionally correct.**

- For **A (seasonal descriptive)**, 4L.9 is appropriately cautious: multi-year daily series exist, but the record is open-water, variable-specific and era-specific.
- For **B (descriptive sensor–cyanobacteria comparison)**, 4L.9 says “partially supported”, which is defensible only if “comparison” means pairwise descriptive patterns. It becomes too optimistic if read as sensor validation or quantitative proxy calibration.
- For **C (multivariate)**, 4L.9 says “limited/not robustly supported”, which is directionally right, but the new joint-coverage calculation shows it is weaker than the label suggests for sensor–biology work: only **{core('turner_core')}** biology dates support a 7-variable Turner core, and **{core('ysi_core')}** support the 11-variable YSI core.
- For **D (early-warning validation)**, 4L.9 is correct: not supported.

Thus the overall phrase “EXPLORATORY FEASIBILITY SUPPORTED WITH MAJOR LIMITATIONS” should not be used as a green light for sensor–biology validation or early-warning work. It is a green light only for limited descriptive use.

## 2. Biological endpoint

- The microscopy data are a **separate measurement pipeline** from the buoy sensors. They are not derived from the same optical signal.
- They are **not statistically independent of the lake**: both observe the same lake on the same dates, and both are affected by spatial heterogeneity, stratification and weather.
- They measure **cyanobacterial abundance/biovolume**, not bloom status, toxicity, surface scum, or onset.
- The record has no event labels, no toxin measurements, no sample time, no detection limits and no per-row QC flags.
- Cyanobacteria biovolume is the least problematic exploratory endpoint, but it is taxonomically non-stationary: 468 nonblank taxa names, 176 nonblank genera, 204 names only pre-2013 and 72 only post-2013; 889 genus-field mismatches; 8,514 trailing-space records; 12 blank taxon rows.
- It cannot establish a lead time for a bloom because a bloom is not defined and the sampling interval is ~14 days.

## 3. Temporal alignment

- Same-day overlap means **the same calendar date has both a microscopy sample and an unflagged sensor value**. It does not mean the same hour, water parcel or depth.
- **{O['avg_chlor_rfu_turner']['same_day_valid_unflagged']}** Turner chlorophyll and **{O['avg_phyco_rfu_turner']['same_day_valid_unflagged']}** Turner phycocyanin biology dates have same-day unflagged values. This is a useful availability count, not a paired time series.
- Only **{ANY['all']['any_valid_sensor_date']}/402** biology dates have any same-day unflagged sensor variable; **{ANY['2006_2020']['any_valid_sensor_date']}/230** within 2006–2020.
- The ±1/±3/±7/±14-day windows increase coverage modestly (e.g., Turner chlorophyll ±7 = {O['avg_chlor_rfu_turner']['valid_within_pm7_days']}/402; ±14 = {O['avg_chlor_rfu_turner']['valid_within_pm14_days']}/402). They are **not lead/lag estimates**: they mix different dates, weather and seasonal states. A ±7-day “match” could easily span a bloom onset and decline.
- A sparse biology series can make a sensor change appear to “lead” a biological change simply because the next biology sample is two weeks later. The data cannot distinguish that from a true lead.

## 4. Depth mismatch

- Sensors are at 0.5 m (chlorophyll, phycocyanin, DO, pH, conductance, turbidity, fDOM), 1 m (pCO2, PAR below) or above water (PAR, meteorology).
- Biology is 0–8 m composite on 400 dates; 2 dates are 0–2 m.
- Under stratification, surface chlorophyll/phycocyanin can be higher or lower than the column composite; vertical migration and surface scums add further decoupling.
- A 0.5 m sensor can describe **surface conditions**; it cannot establish **whole-column biomass**. No depth profile is available to quantify the offset.
- The buoy and NTL sampling site are ~**{S['spatial']['site_distance_m']} m** apart; station is blank for **{BIO['dates_all_blank_station']}/402** dates. Site-level proximity is documented; per-sample spatial coincidence is not.

## 5. Instrument discontinuities

- Turner and YSI are different instruments. 2019 paired medians: chlorophyll **{num(TY['chlorophyll']['turner_median'],1)} vs {num(TY['chlorophyll']['ysi_median'],2)} RFU**; phycocyanin **{num(TY['phycocyanin']['turner_median'],1)} vs {num(TY['phycocyanin']['ysi_median'],3)} RFU**. The EML itself says “significant magnitude differences.”
- No cross-calibration equation or correction factor is present. Concatenating the eras would create an artificial step.
- Other changes: DO exists from 2006 but the inventory lists DO only from 2016; `avg_do_wtemp` is YSI-labelled but exists from 2006; pCO2 begins 2016 while the inventory says 2017; PAR has 2007 near-zero values; 2006 conductivity is ~0.4 µS/cm and all flagged.
- These transitions can produce artificial ecological signals if treated as homogeneous series.

## 6. QC and unflagged values

- `O` is undefined; eight flag columns contain values outside their daily-EML code lists.
- `C` is not equivalent to missing: 1,534 numeric `C` values for `avg_do_wtemp`, 668 for PAR below, 277 for DO raw, 118 for conductance, 113 for YSI chlorophyll.
- `H` is common (928 DO saturation, 734 DO raw, 157 air temperature, 124 wind speed, 82 conductance). Some `H` values are plausible extremes; others (2006 conductance) are not on the later scale.
- `G` is used only for YSI chlorophyll/phycocyanin and PAR below; its absence in the Turner era does not prove absence of fouling.
- Unflagged values are not automatically accurate: negative turbidity (31), negative YSI phycocyanin (62), negative YSI chlorophyll (1), negative PAR below (3), and 2006 conductance values ~0.4 µS/cm.
- The audit’s `valid_unflagged` label is defensible only with its explicit definition. It should not be read as “validated” or “ground truth”.

## 7. Multivariate analysis

- Sensor-only complete-case coverage is reasonable for era-specific descriptive work: **{MV['turner_core']['complete_dates']}** Turner-core dates and **{MV['ysi_core']['complete_dates']}** YSI-core dates.
- Sensor–biology joint coverage is much smaller: **{core('turner_3')}** for 3 Turner variables, **{core('turner_4')}** for 4, **{core('turner_core')}** for 7; **{core('ysi_3')}** for 3 YSI variables, **{core('ysi_5')}** for 5, **{core('ysi_6')}** for 6, **{core('ysi_core')}** for 11.
- Missingness, seasonality and sensor-era changes can dominate apparent multivariate relationships. A descriptive sensor-only analysis is possible; a biological multivariate analysis is not robust.

## 8. Prior-art constraint

- Mendota already has high-frequency phycocyanin research (Carpenter et al. 2020, 2022) and seasonal/sub-seasonal cyanobacteria forecasts (Beal et al. 2021, 2022).
- O'Brien et al. (2023) found that most early-warning indicators in empirical lake data, including Mendota, did not perform better than chance; multivariate indicators were weakly superior and machine learning performed poorly.
- Phycocyanin–biovolume validation is weak/variable (Cotterill et al. 2019; Levi et al. 2025).
- Therefore, no novelty can be claimed from Mendota’s dataset alone, and no early-warning validation is justified without new biological event data and a precise contribution.

## 9. Bottom line

The 4L.9 arithmetic is solid. Its scientific caution is mostly appropriate, but its single overall verdict **overstates the joint sensor–biology support** and should be replaced by the four separate verdicts in `VERDICTS_A_D.md`. Mendota remains useful for limited descriptive work; it is not an early-warning validation dataset.
"""
(OUT / "SCIENTIFIC_INTERPRETATION_CHALLENGE.md").write_text(interp_md, encoding="utf-8")


# ---------------------------------------------------------------------------
# ENDPOINT / TEMPORAL CRITIQUE
# ---------------------------------------------------------------------------
endpoint_md = f"""# Endpoint and Temporal-Alignment Critique

**Sprint:** 4L.10  
**Gate 2:** PAUSED / NOT APPROVED — option C (Exploratory Only)

## 1. What the microscopy endpoint is

The 88.31 file is a direct microscopy export: cell counts, natural-unit counts, geometry-based biovolume and derived biomass. It is **measurement-source independent** of the buoy’s optical sensors, but it is not independent of the lake processes the sensors also observe.

It can support an exploratory **cyanobacterial abundance/biovolume** endpoint. It does **not** establish:

- bloom/non-bloom status;
- bloom onset or termination;
- toxicity or toxin-producing taxa;
- surface scum or lake-wide exposure;
- absence of a bloom elsewhere in the lake;
- a sample time within the date.

The endpoint is also taxonomically non-stationary: 468 nonblank taxa names, 176 nonblank genera, 204 names only pre-2013 and 72 only post-2013, 889 genus-field mismatches, 8,514 trailing-space records. Broad cyanobacterial totals are more defensible than species-level longitudinal comparisons, but even the broad total has historical identification and taxonomy caveats.

## 2. What same-day overlap means

The independent recount confirms:

- 402 Mendota biology dates, 1995-01-24 to 2020-12-10, median 14-day interval.
- 400 dates 0–8 m composite; 2 dates 0–2 m.
- 371/402 dates have no station value; 31 have station “1”.
- Turner chlorophyll: **{O['avg_chlor_rfu_turner']['same_day_valid_unflagged']}** same-day unflagged dates.
- Turner phycocyanin: **{O['avg_phyco_rfu_turner']['same_day_valid_unflagged']}**.
- YSI chlorophyll: **{O['avg_chlor_rfu_ysi']['same_day_valid_unflagged']}**; YSI phycocyanin **{O['avg_phyco_rfu_ysi']['same_day_valid_unflagged']}**.
- DO raw: **{O['avg_do_raw']['same_day_valid_unflagged']}**; DO saturation **{O['avg_do_sat']['same_day_valid_unflagged']}**; water temp **{O['avg_do_wtemp']['same_day_valid_unflagged']}**.

Same-day means **date availability**, not temporal alignment. The biology file has no sample time. A sensor daily average integrates 1-minute values over the day; a microscopy sample is a date-stamped composite. They are not paired observations at a known hour.

## 3. Surrounding windows

The ±1/±3/±7/±14-day windows are reported in `tables/INDEPENDENT_OVERLAP.csv`. They increase the count modestly:

- Turner chlorophyll ±7: **{O['avg_chlor_rfu_turner']['valid_within_pm7_days']}/402**; ±14: **{O['avg_chlor_rfu_turner']['valid_within_pm14_days']}/402**.
- Turner phycocyanin ±7: **{O['avg_phyco_rfu_turner']['valid_within_pm7_days']}/402**; ±14: **{O['avg_phyco_rfu_turner']['valid_within_pm14_days']}/402**.
- DO raw ±7: **{O['avg_do_raw']['valid_within_pm7_days']}/402**; ±14: **{O['avg_do_raw']['valid_within_pm14_days']}/402**.

These are **not lead/lag estimates**. A ±7-day window can span a bloom onset and decline, and it can mix different weather, stratification and seasonal states. A sparse biology series can make a sensor change appear to lead a biological change simply because the next sample is two weeks away. The data cannot distinguish that from a true lead.

## 4. Can the biology support a claimed lead time?

No.

- The median biology interval is 14 days; maximum gap 120 days.
- There is no bloom/non-bloom event definition or independent adjudication.
- There is no verified non-event exposure.
- The sensor record is daily; the biology is date-only.
- A lead-time claim requires a defined onset, a time-matched predictor, and enough events/non-events to validate. None exists.
- Prior experimental EWS work (Pace et al. 2016; Wilkinson et al. 2018) achieved warnings 1–57/61 days before blooms under controlled enrichment and high-frequency monitoring; that does not transfer to a 14-day observational series with no event labels.

## 5. What the endpoint can and cannot support

**Can support:**
- descriptive seasonal patterns in cyanobacteria biovolume;
- pairwise descriptive comparisons with same-day sensor conditions;
- exploratory low/high abundance contrasts, with taxonomic and depth caveats.

**Cannot support:**
- bloom labels or event intervals;
- onset detection or lead-time estimation;
- sensor validation against 0–8 m biomass;
- causal attribution;
- early-warning performance claims.

## 6. What would change the endpoint assessment

- Sub-weekly, time-stamped, depth-resolved microscopy or a validated biomass series.
- A protocol-approved bloom/non-bloom definition with independent adjudication.
- Verified non-event exposure and adequate event counts.
- A taxonomic crosswalk and documented handling of the 200% groups, Coelastrum anomaly and repeated records.
"""
(OUT / "ENDPOINT_AND_TEMPORAL_ALIGNMENT_CRITIQUE.md").write_text(endpoint_md, encoding="utf-8")


# ---------------------------------------------------------------------------
# SENSOR ERA / QC CRITIQUE
# ---------------------------------------------------------------------------
sensor_md = f"""# Sensor-Era and QC Critique

**Sprint:** 4L.10  
**Gate 2:** PAUSED / NOT APPROVED — option C (Exploratory Only)

## 1. Turner versus YSI

The independent recount confirms the 2019 paired comparison:

| Proxy | Paired dates | Turner median | YSI median | Median ratio | Non-positive Turner pairs |
|---|---:|---:|---:|---:|---:|
| Chlorophyll | {TY['chlorophyll']['paired_dates']} | {num(TY['chlorophyll']['turner_median'],2)} | {num(TY['chlorophyll']['ysi_median'],3)} | {TY['chlorophyll']['median_ratio_ysi_over_turner']} | {TY['chlorophyll']['paired_nonpositive_turner']} |
| Phycocyanin | {TY['phycocyanin']['paired_dates']} | {num(TY['phycocyanin']['turner_median'],2)} | {num(TY['phycocyanin']['ysi_median'],3)} | {TY['phycocyanin']['median_ratio_ysi_over_turner']} | {TY['phycocyanin']['paired_nonpositive_turner']} |

The EML states that both output RFU but have “significant magnitude differences.” No cross-calibration equation, correction factor or conversion is present. The ratio is **descriptive only**; it excludes zero/non-positive Turner values and is not a calibration. In the 2019 paired data there were **no non-positive Turner pairs**, so the exclusion has no effect here.

**Conclusion:** Turner and YSI are demonstrably non-comparable on the raw RFU scale. Concatenating them would create an artificial ecological step.

## 2. Other sensor discontinuities

- **DO:** daily values exist from 2006, but the sensor inventory lists DO only from 2016. The 2006–2015 instrument identity is unresolved. DO flags vary strongly by year.
- **Water temperature:** `avg_do_wtemp` is labelled “YSI water temp” but exists from 2006; 2019+ is heavily `C`-flagged (1,087 `C`; 371 unflagged of 1,612). It is not a clean continuous temperature series. Ancillary 130 is documented but not acquired.
- **pCO2:** data begin 2016-03-22; inventory says 2017. 2024 has only 70 unflagged values; 2025 has 177.
- **PAR:** 11 near-zero values in 2007, then no sustained record until 2016. 2019–2020 has major outages.
- **Conductivity:** 2006 values ~0.38–0.48 µS/cm, all `H`/`O`; 2019+ ~122–596 µS/cm. Not comparable.
- **pH/fDOM/turbidity:** 2019+ only.

These transitions can produce artificial signals if treated as homogeneous. Era-specific series are mandatory.

## 3. QC findings and their materiality

- **Undefined `O`:** one value in `flag_avg_spec_cond` (2006-08-11, 0.45). Its meaning is unknown. Materiality: low for the 2019+ conductance series; it reinforces that 2006 conductance is unusable.
- **Eight flag columns use undocumented values:** `rel_hum` H (6), `wind_speed` H (124), `par_below` H (90), `do_wtemp` E (3), `ph` E (1), `fdom` E (1), `turbidity` E (1), `spec_cond` E (17) and O (1). Materiality: high for interpreting those flags; the data cannot tell us whether the undocumented code means the same thing as the generic definition.
- **`C` with numeric values:** 1,534 for `avg_do_wtemp`, 668 for PAR below, 277 for DO raw, 118 for conductance, 113 for YSI chlorophyll. `C` cannot be treated as a missingness code. The audit correctly retains these values as flagged numeric; downstream analysis must define its own rule.
- **`H`:** 928 DO saturation, 734 DO raw, 157 air temperature, 124 wind speed, 82 conductance. Some are plausible extremes (supersaturated DO); some are era artefacts (2006 conductance). Do not equate `H` with “invalid” or with “accurate”.
- **`G`:** only YSI chlorophyll/phycocyanin and PAR below. The Turner era has no `G` flags; absence of `G` is not evidence of no fouling. The EML’s 2017 DO biofouling note is not a per-record flag.
- **Unflagged but implausible:** 31 negative turbidity, 62 negative YSI phycocyanin, 1 negative YSI chlorophyll, 3 negative PAR below, 2006 conductance ~0.4 µS/cm. `valid_unflagged` is not a validation label.
- **Missingness without flags:** Turner chlorophyll 1,424 empty-unflagged; YSI chlorophyll 2,440; pH 2,434; fDOM 2,434; turbidity 2,434; conductance 2,360. Most are structural, but the file does not carry a “not deployed” code for them.

## 4. Does the audit overstate reliability?

The 4L.9 report explicitly defines `valid_unflagged` as numeric with a blank flag and says it is not proof of accuracy. That is appropriate. The risk is **label drift**: a reader may treat “valid” as “validated”. The independent challenge recommends:

- call the field **`unflagged_numeric`** in any downstream analysis;
- report flagged values alongside unflagged values in sensitivity analyses;
- do not use `C` as missing, `H` as invalid, or `G` as the only fouling indicator;
- do not treat unflagged negatives as valid.

## 5. What would change the assessment

- A documented Turner/YSI cross-calibration with uncertainty.
- Per-record calibration, maintenance, serial number and detection-limit data.
- A reconciled sensor inventory with exact deployment dates and pre-2016 DO/pre-2019 temperature provenance.
- A flag dictionary that covers every observed code for every column.

Without these, the sensor record is usable only as era-specific, flag-aware descriptive data.
"""
(OUT / "SENSOR_ERA_AND_QC_CRITIQUE.md").write_text(sensor_md, encoding="utf-8")


# ---------------------------------------------------------------------------
# DEPTH CRITIQUE
# ---------------------------------------------------------------------------
depth_md = f"""# Depth-Compatibility Critique

**Sprint:** 4L.10  
**Gate 2:** PAUSED / NOT APPROVED — option C (Exploratory Only)

## 1. The mismatch

- Chlorophyll, phycocyanin, DO, pH, specific conductance, turbidity and fDOM: **0.5 m**.
- pCO2: **1 m**.
- PAR above water: **2 m above the surface**; PAR below: **1 m depth**.
- Biology: **400 dates 0–8 m composite**; **2 dates 0–2 m**.

A 0.5 m point measurement is not a 0–8 m composite. The composite integrates biomass over the upper water column; the sensor samples one stratum. Under stratification, surface chlorophyll/phycocyanin may be higher or lower than the column mean; vertical migration, surface scums, light acclimation and grazing add further decoupling.

## 2. Spatial setting

- EML buoy coordinates: approximately **43.0995, −89.4045**.
- NTL Mendota sampling-site coordinate: approximately **43.09885, −89.40545**.
- Great-circle distance: **{S['spatial']['site_distance_m']} m**.
- Station is blank for all rows on **{BIO['dates_all_blank_station']}/402** dates; only **{BIO['dates_any_station']}** dates have any station value (all “1”).

This is site-level proximity, not per-sample co-location. The ~106 m offset is small relative to the lake but not zero; the station field does not establish spatial coincidence for most samples.

## 3. What can and cannot be concluded

**Can conclude:**
- The sensor describes surface conditions at the buoy.
- The biology describes a depth-integrated sample, predominantly 0–8 m.
- Same-day comparisons are surface-vs-composite comparisons, not like-for-like biomass estimates.

**Cannot conclude:**
- That 0.5 m chlorophyll/phycocyanin is a proxy for 0–8 m cyanobacteria biovolume.
- That a surface bloom or surface scum represents the whole column.
- That a column-integrated bloom is captured at the surface.
- That the sensor–biology relationship is stable across stratification regimes.

## 4. The two 0–2 m biology dates

Two Mendota dates are labelled 0–2 m, not 0–8 m. They are a different depth class and should not be pooled silently with the 0–8 m dates. Their existence also shows that the historical depth coding is not perfectly uniform.

## 5. What would change the assessment

- Depth-resolved microscopy or chlorophyll/phycocyanin profiles at the buoy.
- A pre-specified comparator: surface layer, euphotic-zone integration, or whole-column biomass.
- A stratification metric (e.g., mixed-layer depth or surface-bottom temperature difference) to stratify the comparison.
- Station-level sample coordinates and sample times.

Until then, depth compatibility remains **weak/conditional**. The 4L.9 classification is appropriate; the practical consequence is that B cannot be a quantitative sensor validation.
"""
(OUT / "DEPTH_COMPATIBILITY_CRITIQUE.md").write_text(depth_md, encoding="utf-8")


# ---------------------------------------------------------------------------
# PRIOR ART
# ---------------------------------------------------------------------------
prior_md = f"""# Targeted Literature and Prior-Art Review

**Sprint:** 4L.10  
**Gate 2:** PAUSED / NOT APPROVED — option C (Exploratory Only)

## 1. Scope

The review targeted:

1. high-frequency freshwater sensor data and cyanobacterial monitoring;
2. phycocyanin/chlorophyll sensor validation against biological measurements;
3. multivariate environmental relationships and ecological early-warning signals;
4. Lake Mendota-specific prior work and forecasting;
5. sensor-to-biological validation and sampling-frequency limitations.

## 2. Mendota-specific prior art

### Carpenter et al. (2020), *Limnology and Oceanography Letters*

One-minute phycocyanin observations at a central Mendota station, ice-free seasons 2008–2018. Stochastic-dynamic models found two alternative stable states and random factors larger than the state difference; transitions were abrupt and apparently stochastic. Annual state magnitudes were not correlated with annual phosphorus input, but daily phycocyanin was correlated with phosphorus input, precipitation and wind at lags of 1–15 days. Multiple years of high-frequency data were needed to discern patterns in noise-dominated dynamics.

**Implication:** Mendota already has a high-frequency phycocyanin research record; the system is stochastic and not a simple deterministic bloom machine. A daily sensor–biology audit cannot claim novelty from the existence of high-frequency data.

### Carpenter et al. (2022), *PNAS*

Daily phycocyanin 2008–2021, with nighttime means (00:00–04:00 and 22:00–24:00) to minimize daytime quenching; different sensors and maintenance regimes were used across years; daily log RFU was z-scored within year. Cross-correlations of P load with phycocyanin were 13–28 days; extreme P-load events were followed by extreme phycocyanin after 1–60 days, but the best Pareto model for phycocyanin extremes was stationary with no significant precipitation/P-load effects.

**Implication:** daily averaging without nighttime selection may be biased by quenching; sensor/maintenance regimes matter; lead-time signals exist but are variable and not a validated bloom-onset rule.

### Beal et al. (2021, 2022)

Mendota has published sub-seasonal (two-month) and season-ahead cyanobacteria abundance forecasts using pre-season/climate predictors. These target seasonal abundance, not daily bloom onset.

**Implication:** Mendota is not an untouched forecasting testbed. A new early-warning claim would need a precise contribution beyond seasonal/sub-seasonal forecasting, not just a different model or matched false-alarm rate.

### O'Brien et al. (2023), *Nature Communications*

Nine long-term lake plankton datasets, including Mendota, were classified into critical transitions, non-critical transitions and stationary dynamics. Few critical transitions were found; different trophic levels changed differently; most EWS methods did not perform better than chance; multivariate EWS were weakly superior; a machine-learning EWS performed poorly. Prediction success for the best methods was around 0.59–0.71 in monthly/yearly data, not a strong operational warning.

**Implication:** empirical EWS are hard; Mendota’s inclusion in this work means a generic EWS claim is not novel. A 14-day, date-only biology series is even less suited to daily onset validation.

### Hansen & Carey (2015) and 4L.6 biological audit

The NTL phytoplankton series has been used for community ecology; the sampling is biweekly summer/monthly non-summer, 0–8 m integrated for Mendota, with microscopy and taxonomic change. The 4L.6 audit found 402 Mendota dates, 468 nonblank taxa, 176 nonblank genera, 14 relative-total groups near 200%, a catastrophic Coelastrum row, repeated records and taxonomic non-stationarity.

**Implication:** the biology is a genuine long-term record but not a clean, event-labelled, daily ground truth.

## 3. Sensor validation literature

### Cotterill et al. (2019), *New Zealand Journal of Marine and Freshwater Research*

Compared a handheld Cyclops-7 phycocyanin sensor with cyanobacteria biovolume across five lakes and a river (2016 n=121; 2017 n=63) and four species in the laboratory. The phycocyanin–biovolume relationship was generally weak (<R²=0.4) and varied among lakes and years, except at high biovolume. Detection limits differed among species; the biovolume detection limit was above alert thresholds for two of four species. The sensor was judged to have limited utility, possibly useful for on-site confirmation of alert-level exceedances.

**Implication:** a phycocyanin RFU series is not a validated cyanobacteria biovolume measurement. B can be descriptive, not quantitative validation.

### Levi et al. (2025), *Open Research Europe*

Validated 24 chlorophyll and 12 phycocyanin Cyclops-7F sensors in mesocosms. Fluorescence was affected by biofouling, phytoplankton composition, equipment and low concentrations; calibration varied; high phycocyanin interfered with chlorophyll; nighttime data were used to reduce quenching; high-frequency sensors captured events missed by biweekly/monthly sampling. The authors emphasize site-specific calibration and caution that in-vivo measurements are semi-quantitative.

**Implication:** high-frequency sensors can reveal short-term change, but only with calibration/QC; the Mendota daily averages without nighttime selection and without calibration cannot be treated as validated biomass.

### USGS TM1-D10 (Foster et al. 2022)

Algal fluorometers measure a fluorescence response, not algal abundance/biomass; RFU is sensor-specific; relationships vary with species, physiology, temperature and light; nonphotochemical quenching causes diurnal variability; biofouling and calibration drift require site-specific QA; different makes/models are not equivalent even in the same units.

### YSI technical guidance (2019/2021)

YSI notes that 6-series and EXO phycocyanin sensors use different technologies, ranges and firmware; RFU is a relative unit; users should read trends/patterns rather than absolute values; turbidity, CDOM/fDOM and biofouling can interfere.

### Hodges et al. (2018), Rousso et al. (2021), Watras et al. (2017)

These studies (identified; abstract/metadata-level in this sprint) report manufacturer-, temperature- and morphology-dependent phycocyanin fluorescence, light-induced quenching errors, and the need for temperature compensation. They reinforce the same conclusion: RFU is not a universal abundance unit.

## 4. Early-warning literature

- **Pace et al. (2016), PNAS:** whole-lake nutrient-enrichment experiment; resilience indicators (SD, autocorrelation) gave alarms 17 days before the bloom maximum; stopping nutrients reversed the bloom. This required controlled enrichment, a reference lake, high-frequency pigments and a pre-specified decision rule.
- **Wilkinson et al. (2018), Ecological Monographs:** early-warning signals preceded cyanobacterial blooms in multiple whole-lake experiments, 1–57/61 days before blooms; context-dependent.
- **O'Brien et al. (2023):** empirical lake EWS often poor; most indicators not better than chance; multivariate weakly superior.
- **Recknagel (2025):** high-frequency in situ monitoring plus intelligible machine learning for Lake Müggelsee; identified as prior art, full text not accessible in this environment. It confirms that HF sensor + ML early warning is an active field, not a Mendota-specific novelty.

**Implication:** early warning is possible in controlled/high-frequency settings, but the Mendota record lacks the event definition, time-stamped biology and validation design needed to claim it. A matched false-alarm rate alone is not novelty.

## 5. What legitimate opportunity remains?

Mendota offers:

1. **A descriptive seasonal analysis** of environmental variables, with era-specific sensor series.
2. **A pairwise descriptive comparison** of Turner chlorophyll/phycocyanin (or DO/temperature) with cyanobacteria biovolume/cell density, explicitly framed as surface-vs-composite and proxy-based.
3. **A methods/measurement paper** on sensor–biology comparability, if framed as a negative/limited validation rather than a bloom forecast.

It does **not** offer a legitimate early-warning validation opportunity without new biological event data, time-stamped/depth-resolved sampling and an independent adjudication protocol.

## 6. Novelty caution

Do not claim novelty from:

- using Mendota high-frequency data (already done by Carpenter et al.);
- seasonal/sub-seasonal cyanobacteria forecasting (already done by Beal et al.);
- generic EWS indicators (O'Brien et al. tested them, including Mendota);
- matched false-alarm rates alone;
- a new model class without a validated event endpoint and fair evaluation.

A defensible contribution would need a precise, evidence-based gap: e.g., a validated sub-weekly bloom-onset endpoint, a sensor cross-calibration with uncertainty, or a depth-resolved surface-to-composite comparison. None is established by the current data.
"""
(OUT / "PRIOR_ART_AND_LITERATURE_REVIEW.md").write_text(prior_md, encoding="utf-8")


# ---------------------------------------------------------------------------
# VERDICTS A-D
# ---------------------------------------------------------------------------
verdict_md = f"""# Independent Verdicts for Uses A–D

**Sprint:** 4L.10  
**Gate 2:** PAUSED / NOT APPROVED — option C (Exploratory Only)

## A. Seasonal descriptive ecological analysis

**Verdict: SUPPORTED WITH MAJOR LIMITATIONS — RETAIN FOR LIMITED EXPLORATORY USE.**

Evidence:
- 3,996 daily records, 2006-07-09 to 2025-11-18, 18 variables.
- Sensor-only complete-case coverage: **{MV['turner_core']['complete_dates']}** Turner-core dates; **{MV['ysi_core']['complete_dates']}** YSI-core dates.
- Multi-year air temperature, RH, wind, DO, Turner chlorophyll/phycocyanin; 2016+ pCO2/PAR; 2019+ YSI suite.

Limitations:
- Open-water season only; 15 winter records; no January/February.
- Variable-specific gaps, flags and sensor eras.
- Daily averages, not nighttime/quality-controlled fluorescence.
- No causal or confirmatory inference.

## B. Descriptive comparison with microscopy cyanobacterial measurements

**Verdict: PARTIALLY SUPPORTED — DESCRIPTIVE/PAIRWISE ONLY; NOT SENSOR VALIDATION.**

Evidence:
- Turner chlorophyll **{O['avg_chlor_rfu_turner']['same_day_valid_unflagged']}** and phycocyanin **{O['avg_phyco_rfu_turner']['same_day_valid_unflagged']}** same-day unflagged dates.
- Turner chlorophyll + phycocyanin + DO: **{core('turner_3')}**; + water temperature: **{core('turner_4')}**.
- YSI chlorophyll **{O['avg_chlor_rfu_ysi']['same_day_valid_unflagged']}**; YSI phycocyanin **{O['avg_phyco_rfu_ysi']['same_day_valid_unflagged']}**; YSI 3-variable set **{core('ysi_3')}**.
- Pairwise counts: Turner chl+phyco **{pair_count('avg_chlor_rfu_turner','avg_phyco_rfu_turner')}**; Turner chl+DO **{pair_count('avg_chlor_rfu_turner','avg_do_raw')}**; Turner phyco+DO **{pair_count('avg_phyco_rfu_turner','avg_do_raw')}**; YSI chl+phyco **{pair_count('avg_chlor_rfu_ysi','avg_phyco_rfu_ysi')}**.

Limitations:
- 0.5 m point vs 0–8 m composite; no depth profile.
- RFU proxies; weak/variable sensor–biovolume relationships in the literature.
- 14-day, date-only, taxonomically non-stationary biology.
- Only 58/402 biology dates for a 7-variable Turner core; 2/402 for an 11-variable YSI core.
- Cannot validate sensors quantitatively or claim causation.

## C. Multivariate environmental relationship exploration

**Verdict: LIMITED FOR SENSOR-ONLY DESCRIPTIVE WORK; NOT ROBUSTLY SUPPORTED FOR SENSOR–BIOLOGY MULTIVARIATE ANALYSIS.**

Evidence:
- Sensor-only: 939 Turner-core dates and 306 YSI-core dates; descriptive environmental multivariate work is possible within era.
- Sensor–biology: 58/402 Turner-core dates, 2/402 YSI-core dates; 3-variable Turner 79/402, 4-variable 64/402; YSI 3-variable 16/402, 5-variable 2/402, 6-variable 21/402.
- Common support is too small for stable multivariate biological relationships.

Limitations:
- Collinearity, seasonality, missingness and sensor-era changes can dominate.
- No confirmatory modelling or hypothesis testing is authorised.
- A sensor-only descriptive analysis is not a biological early-warning analysis.

## D. Early-warning validation

**Verdict: NOT SUPPORTED — REJECT FOR THE ORIGINAL RESEARCH QUESTION.**

Reasons:
- No bloom/non-bloom labels or event intervals.
- Biology is ~14-day, date-only, 0–8 m composite; no onset time.
- Sensor is 0.5 m; depth mismatch.
- No verified non-event exposure.
- No lead-time validation design.
- Prior art: empirical EWS often poor; Mendota already used for HF phycocyanin and seasonal forecasts.

## Summary table

| Use | Verdict | Retain? |
|---|---|---|
| A. Seasonal descriptive | Supported with major limitations | **Yes — limited** |
| B. Descriptive sensor–cyanobacteria | Partially supported, pairwise/descriptive | **Yes — limited** |
| C. Multivariate | Limited sensor-only; not robust with biology | **Only sensor-only descriptive** |
| D. Early-warning validation | Not supported | **No — reject** |

## Bottom line

The four uses must not be collapsed. A and pairwise B justify **RETAIN — LIMITED EXPLORATORY USE**. C does not justify a biological multivariate programme. D is rejected for the original early-warning question.
"""
(OUT / "VERDICTS_A_D.md").write_text(verdict_md, encoding="utf-8")


# ---------------------------------------------------------------------------
# FINAL DECISION
# ---------------------------------------------------------------------------
decision_md = f"""# Final Mendota Dataset Decision

**Sprint:** 4L.10  
**Gate 2:** PAUSED / NOT APPROVED — option C (Exploratory Only)

## Recommendation

# RETAIN — LIMITED EXPLORATORY USE

**Scope of retention:**
- descriptive seasonal analysis of environmental variables;
- pairwise descriptive comparison of sensor conditions with cyanobacteria biovolume/cell density, with Turner/YSI eras kept separate and the 0.5 m vs 0–8 m limitation stated.

**Explicit rejection:**
- Mendota is **rejected for the original early-warning research question** and for any confirmatory bloom/non-bloom evaluation.
- No labels, event intervals, predictive models, threshold optimisation or hypothesis tests are authorised.

## Why not “supporting data only”?

Pairwise descriptive B is genuinely possible: {pair_count('avg_chlor_rfu_turner','avg_phyco_rfu_turner')} biology dates have both Turner chlorophyll and phycocyanin, {pair_count('avg_chlor_rfu_turner','avg_do_raw')} have Turner chlorophyll and DO, and {pair_count('avg_phyco_rfu_turner','avg_do_raw')} have Turner phycocyanin and DO. That is enough for cautious descriptive comparison, not for validation. Calling it “supporting only” would understate a legitimate exploratory use.

## Why not “reject”?

A has clear value: the sensor record supports descriptive seasonal analysis with {MV['turner_core']['complete_dates']} Turner-core and {MV['ysi_core']['complete_dates']} YSI-core sensor-only complete dates. A blanket rejection would be too pessimistic for that use.

## Why not “retain for early warning”?

D fails on every necessary condition: no event definition, no time-stamped biology, no depth-resolved biology, no independent bloom adjudication, no verified non-event exposure, no validated sensor crosswalk, and weak sensor-to-biovolume literature. Prior art already covers Mendota high-frequency phycocyanin and seasonal/sub-seasonal forecasting. A new early-warning claim would be neither novel nor testable with the current data.

## Conditions of retention

1. Keep Turner and YSI eras separate; no undocumented correction.
2. Use era-specific, variable-specific denominators; report `unflagged_numeric`, not “validated”.
3. Treat 0.5 m sensors as surface conditions, not 0–8 m biomass.
4. Use pairwise or small (2–4 variable) descriptive comparisons; do not pretend the 7/11-variable biological multivariate sets are adequate.
5. Do not create bloom/non-bloom labels, event intervals or early-warning features.
6. State that the biology is 14-day, date-only and taxonomically non-stationary.
7. Do not claim novelty from matched false-alarm rates or from the existence of Mendota high-frequency data.

## What evidence would change the decision

- Sub-weekly, time-stamped, depth-resolved microscopy or a validated biomass series.
- A protocol-approved bloom/non-bloom definition with independent adjudication and verified non-event exposure.
- A documented Turner/YSI cross-calibration and per-record calibration/maintenance history.
- A defined depth comparator and surface-vs-composite sensitivity analysis.
- A pre-specified, leakage-controlled lead-time validation with adequate event counts.

Without these, the decision remains **RETAIN — LIMITED EXPLORATORY USE**, with **D rejected**.

## Governance

Gate 2 remains **PAUSED / NOT APPROVED — option C**. No labels, event intervals, models, hypothesis tests, threshold optimisation, protocol changes, external contacts, uploads, commits or pushes were made. Raw data and prior evidence remain unchanged.
"""
(OUT / "FINAL_DATASET_DECISION.md").write_text(decision_md, encoding="utf-8")

print("reports written")
