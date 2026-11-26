# Variable Coverage Audit

**Sprint:** 4L.9  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. Definitions used throughout

- **Record / daily row:** one date in the acquired daily file. The file has **3,996** records on **3,996** unique dates.
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
| `avg_air_temp` | 2006-07-09 | 2025-11-18 | 305 | 7.6% | 3691 | 3445 | 86.2% | 139 | 5 | 157 | 0 | 0 | 1.0 | 713 | -10.589 | 18.691 | 32.561 |
| `avg_rel_hum` | 2006-07-09 | 2025-11-18 | 302 | 7.6% | 3694 | 3562 | 89.1% | 172 | 6 | 6 | 0 | 0 | 1.0 | 712 | 0.6 | 71.4705 | 98.698 |
| `avg_wind_speed` | 2006-07-09 | 2025-11-18 | 114 | 2.9% | 3882 | 3446 | 86.2% | 408 | 0 | 124 | 0 | 0 | 1.0 | 266 | 0.0 | 3.865 | 10.342 |
| `avg_wind_dir` | 2006-07-09 | 2025-11-18 | 276 | 6.9% | 3720 | 3656 | 91.5% | 329 | 0 | 3 | 0 | 0 | 1.0 | 633 | 0.8 | 202.05 | 359.9 |
| `avg_chlor_rfu_turner` | 2006-07-09 | 2019-11-03 | 1464 | 36.6% | 2532 | 2202 | 55.1% | 316 | 0 | 54 | 0 | 0 | 1.0 | 256 | 0.033 | 1196.5715 | 16211.542 |
| `avg_chlor_rfu_ysi` | 2019-04-16 | 2025-11-18 | 2499 | 62.5% | 1497 | 1256 | 31.4% | 172 | 1 | 116 | 11 | 0 | 1.0 | 154 | -0.094 | 0.639 | 9.463 |
| `avg_phyco_rfu_turner` | 2006-07-09 | 2019-11-03 | 1586 | 39.7% | 2410 | 2308 | 57.8% | 225 | 0 | 41 | 0 | 0 | 1.0 | 368 | -9.284 | 635.792 | 12831.178 |
| `avg_phyco_rfu_ysi` | 2019-04-16 | 2025-11-18 | 2499 | 62.5% | 1497 | 1373 | 34.4% | 168 | 1 | 0 | 11 | 0 | 1.0 | 152 | -0.224 | 0.673 | 5.269 |
| `avg_par` | 2007-05-18 | 2025-11-18 | 1689 | 42.3% | 2307 | 1460 | 36.5% | 915 | 0 | 81 | 0 | 0 | 1.0 | 3221 | 0.0 | 396.881 | 1066.721 |
| `avg_par_below` | 2016-03-22 | 2025-11-18 | 1794 | 44.9% | 2202 | 1410 | 35.3% | 762 | 0 | 90 | 34 | 0 | 1.0 | 315 | -1676.332 | 94.502 | 592.065 |
| `avg_do_wtemp` | 2006-07-09 | 2025-11-18 | 273 | 6.8% | 3723 | 1943 | 48.6% | 1705 | 3 | 243 | 0 | 0 | 1.0 | 294 | 4.085 | 20.758 | 29.581 |
| `avg_do_sat` | 2006-08-05 | 2025-11-18 | 267 | 6.7% | 3729 | 2483 | 62.1% | 443 | 52 | 928 | 0 | 0 | 1.0 | 294 | 44.435 | 103.981 | 182.442 |
| `avg_do_raw` | 2006-07-11 | 2025-11-18 | 284 | 7.1% | 3712 | 2649 | 66.3% | 452 | 54 | 734 | 0 | 0 | 1.0 | 294 | 4.479 | 9.561 | 17.234 |
| `avg_pco2_ppm` | 2016-03-22 | 2025-11-18 | 2011 | 50.3% | 1985 | 1841 | 46.1% | 235 | 16 | 0 | 0 | 0 | 1.0 | 322 | 33.901 | 258.465 | 3352.268 |
| `avg_ph` | 2019-04-16 | 2025-11-18 | 2497 | 62.5% | 1499 | 1383 | 34.6% | 178 | 1 | 0 | 0 | 0 | 1.0 | 152 | 7.0 | 8.634 | 9.308 |
| `avg_fdom` | 2019-04-16 | 2025-11-18 | 2481 | 62.1% | 1515 | 1397 | 35.0% | 164 | 1 | 0 | 0 | 0 | 1.0 | 152 | 0.049 | 7.55 | 12.84 |
| `avg_turbidity` | 2019-04-16 | 2025-11-18 | 2492 | 62.4% | 1504 | 1385 | 34.7% | 176 | 1 | 0 | 0 | 0 | 1.0 | 152 | -0.462 | 1.957 | 126.447 |
| `avg_spec_cond` | 2019-04-16 | 2025-11-18 | 2460 | 61.6% | 1536 | 1318 | 33.0% | 218 | 17 | 82 | 0 | 1 | 1.0 | 152 | 122.152 | 543.491 | 595.824 |

## 3. What the counts show

- The longest-running variables are meteorological and DO-related: air temperature, relative humidity, wind, and DO have records from 2006. Turner chlorophyll/phycocyanin also run 2006–2019. YSI chlorophyll/phycocyanin, pH, fDOM, turbidity and specific conductance are effectively 2019+ series; pCO2 is 2016+; PAR is 2016+ apart from sparse 2007 near-zero values.
- Missingness ranges from **2.9%** (wind speed) to **62.5%** (YSI chlorophyll). The high values for 2019+ variables are largely **structural**: the sensor did not exist in the earlier record, not a failure on a deployed day.
- Unflagged coverage is strongest for wind direction (91.5%), relative humidity (89.1%), wind speed (86.2%) and air temperature (86.2%). It is weakest for YSI chlorophyll (31.4%), specific conductance (33.0%), pH (34.6%), fDOM (35.0%) and turbidity (34.7%).
- Turner chlorophyll has only **2202** unflagged values (55.1%) despite its 2006–2019 label; Turner phycocyanin has **2308** (57.8%). Both have major within-era gaps.
- YSI chlorophyll has **1256** unflagged values; YSI phycocyanin **1373**. Both are 2019+ only.
- DO raw has **2649** unflagged values (66.3%), but its flags are heavy: **734 `H`**, **54 `E`** and **452 `C`**. DO saturation has **928 `H`** values. Flagged DO values are often high (H median 12.21 mg/L), consistent with supersaturation/range flags, but the data do not provide a per-value reason.
- `avg_do_wtemp` has only **1943** unflagged values (48.6%) and **1705 `C`** flags, with only **7** unflagged values in 2020. Its definition as “YSI water temp” conflicts with pre-2019 values. It should not be treated as a continuous homogeneous water-temperature series.

## 4. Annual and seasonal coverage

The full tables are `ANNUAL_VARIABLE_COVERAGE.csv` and `SEASONAL_VARIABLE_COVERAGE.csv`. Key patterns:

- The file contains **3,996** records over **7,073** calendar days (56.5%). It is an **open-water deployment series**, not a year-round daily calendar.
- Month counts: March 37, April 265, May 493, June 525, July 600, August 609, September 591, October 563, November 298, December 15; **no January or February records**.
- Winter has only **15** records in total. Seasonal comparisons are therefore open-water-season comparisons, not annual-cycle comparisons.
- Early meteorological coverage is patchy: air temperature has **0** unflagged values in 2007 and only **51** in 2008; wind speed has **20** in 2008 and **2** in 2009.
- Turner chlorophyll collapses in 2014 (**14** unflagged of **162**) and 2015 (**70** of **169**). Turner phycocyanin has only **6** unflagged values in 2007.
- DO raw is weak in 2008 (**18** of **137**), 2010 (**59** of **196**), 2014 (**50** of **162**) and 2017 (**62** of **200**).
- YSI-era variables are present only from 2019; pH/fDOM/turbidity/specific conductance have about **33–35%** unflagged coverage over the whole file and only the 2019–2020 biology overlap.

## 5. Implausible and anomalous values

The broad screening bounds are listed in `ANOMALY_AUDIT.csv`; they are not regulatory thresholds.

| Variable | Screening issue | Count | Examples / note |
|---|---|---:|---|
| `avg_turbidity` | Negative FNU, unflagged | **31** | 2025-05-25 to 2025-06-02; last record 2025-11-18 = −0.427; physical turbidity cannot be negative |
| `avg_phyco_rfu_ysi` | Negative RFU, unflagged | **62** | 2019-05-29 onwards; near-zero offset likely but unresolved |
| `avg_chlor_rfu_ysi` | Negative RFU, unflagged | **1** | one unflagged negative |
| `avg_par_below` | Negative PAR, unflagged | **3** | 2025-04-08 to 2025-04-10, −920 to −1,676 µmol/m²/s; physically implausible |
| `avg_phyco_rfu_turner` | Negative RFU, unflagged | **4** | 2012-06-10 to 2012-06-16 |
| `avg_spec_cond` | 2006 values ~0.38–0.48 µS/cm | 83 numeric | All `H`/`O`; no unflagged 2006 value. The 2019+ series is ~122–596 µS/cm. |
| `avg_chlor_rfu_turner` | Extreme high RFU | max 16,211.54 | Turner RFU scale is sensor-specific; extreme values are not labelled as blooms |
| `avg_phyco_rfu_turner` | Extreme high RFU | max 12,831.18 | same caveat |
| `avg_do_raw` / `avg_do_sat` | High values with `H` | max 17.23 mg/L / 182.44% | High DO can be real; `H` is a range flag, not proof of error |
| `avg_air_temp` | Negative values | 50 unflagged | Plausible winter air temperatures; not an anomaly |

**No values were deleted, truncated, winsorised, imputed or relabelled.** The raw file remains unchanged.

## 6. Conclusion

Daily records are present for all 18 variables, but coverage is **variable-specific and era-specific**. Some variables have long, reasonably continuous records; others exist only in the 2019+ YSI era or have severe within-era gaps. Missingness is not zero, flags are not a complete QC system, and unflagged values are not automatically accurate. Any exploratory analysis must state its variable-specific denominator and exclusion rule.
