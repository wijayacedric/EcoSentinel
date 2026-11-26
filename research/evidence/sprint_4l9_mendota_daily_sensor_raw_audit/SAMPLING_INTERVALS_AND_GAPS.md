# Sampling Intervals and Gaps

**Sprint:** 4L.9  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. Method

Intervals are calculated between consecutive **unflagged numeric** dates for each variable. A gap is the number of calendar days from one unflagged date to the next. Winter absence, sensor removal, sensor failure and sensor-era absence all appear as gaps; the table does not attribute cause.

## 2. Interval distribution

| Variable | Unflagged dates | Intervals | 1 d | 2–7 d | 8–14 d | 15–30 d | 31–60 d | 61–90 d | >90 d | Median | Max |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `avg_air_temp` | 3445 | 3444 | 3322 | 97 | 5 | 1 | 1 | 0 | 18 | 1.0 | 713 |
| `avg_rel_hum` | 3562 | 3561 | 3460 | 79 | 2 | 1 | 1 | 0 | 18 | 1.0 | 712 |
| `avg_wind_speed` | 3446 | 3445 | 3347 | 64 | 8 | 5 | 2 | 0 | 19 | 1.0 | 266 |
| `avg_wind_dir` | 3656 | 3655 | 3593 | 39 | 1 | 2 | 2 | 0 | 18 | 1.0 | 633 |
| `avg_chlor_rfu_turner` | 2202 | 2201 | 2102 | 72 | 9 | 4 | 0 | 1 | 13 | 1.0 | 256 |
| `avg_chlor_rfu_ysi` | 1256 | 1255 | 1137 | 100 | 8 | 3 | 1 | 0 | 6 | 1.0 | 154 |
| `avg_phyco_rfu_turner` | 2308 | 2307 | 2237 | 52 | 2 | 3 | 0 | 0 | 13 | 1.0 | 368 |
| `avg_phyco_rfu_ysi` | 1373 | 1372 | 1265 | 94 | 4 | 2 | 1 | 0 | 6 | 1.0 | 152 |
| `avg_par` | 1460 | 1459 | 1318 | 115 | 12 | 3 | 1 | 0 | 10 | 1.0 | 3221 |
| `avg_par_below` | 1410 | 1409 | 1300 | 85 | 10 | 2 | 2 | 1 | 9 | 1.0 | 315 |
| `avg_do_wtemp` | 1943 | 1942 | 1732 | 141 | 15 | 20 | 12 | 3 | 19 | 1.0 | 294 |
| `avg_do_sat` | 2483 | 2482 | 2183 | 241 | 19 | 17 | 3 | 0 | 19 | 1.0 | 294 |
| `avg_do_raw` | 2649 | 2648 | 2363 | 229 | 20 | 13 | 4 | 0 | 19 | 1.0 | 294 |
| `avg_pco2_ppm` | 1841 | 1840 | 1795 | 31 | 2 | 1 | 1 | 1 | 9 | 1.0 | 322 |
| `avg_ph` | 1383 | 1382 | 1278 | 94 | 1 | 2 | 1 | 0 | 6 | 1.0 | 152 |
| `avg_fdom` | 1397 | 1396 | 1290 | 96 | 1 | 2 | 1 | 0 | 6 | 1.0 | 152 |
| `avg_turbidity` | 1385 | 1384 | 1278 | 95 | 2 | 2 | 1 | 0 | 6 | 1.0 | 152 |
| `avg_spec_cond` | 1318 | 1317 | 1210 | 93 | 2 | 4 | 2 | 0 | 6 | 1.0 | 152 |

The median interval is **1 day** for every variable when the sensor is present. The daily file is therefore daily-resolution data, but it is **not** a continuous daily calendar: long gaps are common and are concentrated in winter, early deployment years and sensor failures.

## 3. Largest gaps

| Variable | From | To | Days |
|---|---|---|---:|
| `avg_par` | 2007-05-28 | 2016-03-22 | 3221 |
| `avg_air_temp` | 2006-07-29 | 2008-07-11 | 713 |
| `avg_rel_hum` | 2006-07-29 | 2008-07-10 | 712 |
| `avg_wind_dir` | 2006-10-17 | 2008-07-11 | 633 |
| `avg_phyco_rfu_turner` | 2007-06-24 | 2008-06-26 | 368 |
| `avg_par` | 2020-03-31 | 2021-04-01 | 366 |
| `avg_pco2_ppm` | 2024-05-21 | 2025-04-08 | 322 |
| `avg_par_below` | 2020-05-22 | 2021-04-02 | 315 |
| `avg_do_wtemp` | 2013-10-27 | 2014-08-17 | 294 |
| `avg_do_sat` | 2013-10-27 | 2014-08-17 | 294 |
| `avg_do_raw` | 2013-10-27 | 2014-08-17 | 294 |
| `avg_do_sat` | 2010-08-16 | 2011-05-19 | 276 |
| `avg_do_raw` | 2010-08-20 | 2011-05-19 | 272 |
| `avg_phyco_rfu_turner` | 2006-09-21 | 2007-06-16 | 268 |
| `avg_wind_speed` | 2009-07-17 | 2010-04-09 | 266 |
| `avg_wind_speed` | 2007-10-30 | 2008-07-12 | 256 |
| `avg_chlor_rfu_turner` | 2006-10-03 | 2007-06-16 | 256 |
| `avg_do_sat` | 2007-10-21 | 2008-06-28 | 251 |
| `avg_do_wtemp` | 2007-10-21 | 2008-06-26 | 249 |
| `avg_do_raw` | 2007-10-21 | 2008-06-26 | 249 |

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
