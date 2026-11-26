# Independent Recalculation and Verification

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
| Bytes | **490,187** |
| MD5 | `eb7b3a3848b27074bac4504236ccefc3` |
| SHA-1 | `bb1d8a281a3d580cad45549551abdbaed1ae03fe` |
| SHA-256 | `104ef1b33769bc0ad1d3e9e6dff28219b743b81ce89ee888460d2df255981343` |
| Columns | 38 |
| Data rows | 3,996 |
| Malformed rows | 0 |
| Duplicate dates | 0 |
| Date parse errors | 0 |
| Year/date mismatches | 0 |
| Exact duplicate rows | 0 |
| Date range | 2006-07-09 to 2025-11-18 |
| Biology dates | 402 |
| Biology 0–8 m / 0–2 m dates | 400 / 2 |
| Biology dates with all station blank | 371 |

## 3. Comparison with Sprint 4L.9

| Domain | Comparable checks |
|---|---:|
| annual | 3,600 |
| biology | 4 |
| depth | 18 |
| era | 288 |
| flag | 90 |
| interval | 198 |
| overlap | 378 |
| seasonal | 720 |
| structure | 7 |
| turner_ysi | 10 |
| variable | 126 |

**Total comparable checks:** 5,439  
**Numerical mismatches versus 4L.9:** 0  
**Numerical mismatches versus SQLite:** 0  
**Interpretive discrepancy rows:** 10

The complete row-level comparison is in `tables/CALCULATION_VERIFICATION.csv`; the discrepancy register is `tables/DISCREPANCY_REGISTER.csv`.

## 4. Key independent values

| Variable | Valid unflagged | Missing | Flags C/E/H/G/O |
|---|---:|---:|---|
| `avg_air_temp` | 3445 | 305 | 139/5/157/0/0 |
| `avg_rel_hum` | 3562 | 302 | 172/6/6/0/0 |
| `avg_wind_speed` | 3446 | 114 | 408/0/124/0/0 |
| `avg_wind_dir` | 3656 | 276 | 329/0/3/0/0 |
| `avg_chlor_rfu_turner` | 2202 | 1464 | 316/0/54/0/0 |
| `avg_chlor_rfu_ysi` | 1256 | 2499 | 172/1/116/11/0 |
| `avg_phyco_rfu_turner` | 2308 | 1586 | 225/0/41/0/0 |
| `avg_phyco_rfu_ysi` | 1373 | 2499 | 168/1/0/11/0 |
| `avg_par` | 1460 | 1689 | 915/0/81/0/0 |
| `avg_par_below` | 1410 | 1794 | 762/0/90/34/0 |
| `avg_do_wtemp` | 1943 | 273 | 1705/3/243/0/0 |
| `avg_do_sat` | 2483 | 267 | 443/52/928/0/0 |
| `avg_do_raw` | 2649 | 284 | 452/54/734/0/0 |
| `avg_pco2_ppm` | 1841 | 2011 | 235/16/0/0/0 |
| `avg_ph` | 1383 | 2497 | 178/1/0/0/0 |
| `avg_fdom` | 1397 | 2481 | 164/1/0/0/0 |
| `avg_turbidity` | 1385 | 2492 | 176/1/0/0/0 |
| `avg_spec_cond` | 1318 | 2460 | 218/17/82/0/1 |

These values reproduce the 4L.9 table exactly. The independent annual, seasonal, interval, overlap and era tables are in `tables/INDEPENDENT_*.csv`.

## 5. Independent overlap

| Variable | Same-day unflagged | % of 402 | % within span |
|---|---:|---:|---:|
| `avg_chlor_rfu_turner` | 128 | 31.8% | 62.1% |
| `avg_phyco_rfu_turner` | 139 | 34.6% | 67.5% |
| `avg_chlor_rfu_ysi` | 21 | 5.2% | 75.0% |
| `avg_phyco_rfu_ysi` | 22 | 5.5% | 78.6% |
| `avg_do_raw` | 99 | 24.6% | 44.8% |
| `avg_do_sat` | 98 | 24.4% | 44.5% |
| `avg_do_wtemp` | 94 | 23.4% | 42.3% |
| `avg_ph` | 22 | 5.5% | 78.6% |
| `avg_pco2_ppm` | 55 | 13.7% | 69.6% |
| `avg_par` | 42 | 10.4% | 20.2% |
| `avg_par_below` | 45 | 11.2% | 57.0% |

## 6. Independent Turner/YSI check

| Proxy | Paired dates | Turner median | YSI median | Median ratio | Non-positive Turner pairs |
|---|---:|---:|---:|---:|---:|
| Chlorophyll | 156 | 1,354.74 | 0.390 | 0.000332 | 0 |
| Phycocyanin | 160 | 802.01 | 0.590 | 0.000835 | 0 |

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
