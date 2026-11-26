# Temporal Compatibility with Mendota Microscopy

**Sprint:** 4L.9  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. Biology reference

The independently audited 88.31 Mendota record contains:

- **9,401** Mendota rows / **402** unique dates, **1995-01-24 to 2020-12-10**.
- Median sampling interval **14.0 days**.
- **400** dates with a 0–8 m composite and **2** dates with a 0–2 m sample.
- Station is blank for all rows on **371** dates; only **31** dates have any station value (all “1”).
- The record has dates, not sampling times. No intraday alignment is possible.

Package-level overlap is **230 biology dates within 2006–2020**; 172 dates predate 2006 and none post-date 2020. Package-level overlap is not variable-level coverage; the table below uses each variable's actual unflagged span.

## 2. Same-day overlap by variable

| Variable | Biology dates within unflagged span | Date absent | Present but variable missing | Same-day numeric | Same-day unflagged | Same-day flagged | Same-day valid % of all 402 | % of within-span | ±1 d | ±3 d | ±7 d | ±14 d |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `avg_air_temp` | 222 | 56 | 20 | 146 | 131 | 15 | 32.6% | 59.0% | 142 | 152 | 157 | 163 |
| `avg_rel_hum` | 222 | 56 | 20 | 146 | 137 | 9 | 34.1% | 61.7% | 146 | 154 | 157 | 164 |
| `avg_wind_speed` | 222 | 56 | 10 | 156 | 135 | 21 | 33.6% | 60.8% | 139 | 153 | 162 | 169 |
| `avg_wind_dir` | 222 | 56 | 20 | 146 | 143 | 3 | 35.6% | 64.4% | 147 | 154 | 159 | 167 |
| `avg_chlor_rfu_turner` | 206 | 52 | 3 | 151 | 128 | 23 | 31.8% | 62.1% | 136 | 148 | 156 | 163 |
| `avg_chlor_rfu_ysi` | 28 | 4 | 1 | 23 | 21 | 2 | 5.2% | 75.0% | 23 | 23 | 25 | 25 |
| `avg_phyco_rfu_turner` | 206 | 52 | 9 | 145 | 139 | 6 | 34.6% | 67.5% | 143 | 151 | 154 | 160 |
| `avg_phyco_rfu_ysi` | 28 | 4 | 1 | 23 | 22 | 1 | 5.5% | 78.6% | 23 | 23 | 25 | 25 |
| `avg_par` | 208 | 47 | 93 | 68 | 42 | 26 | 10.4% | 20.2% | 45 | 46 | 51 | 52 |
| `avg_par_below` | 79 | 12 | 0 | 67 | 45 | 22 | 11.2% | 57.0% | 46 | 47 | 52 | 55 |
| `avg_do_wtemp` | 222 | 56 | 14 | 152 | 94 | 58 | 23.4% | 42.3% | 111 | 127 | 137 | 160 |
| `avg_do_sat` | 220 | 55 | 14 | 151 | 98 | 53 | 24.4% | 44.5% | 116 | 138 | 149 | 165 |
| `avg_do_raw` | 221 | 56 | 15 | 150 | 99 | 51 | 24.6% | 44.8% | 114 | 135 | 147 | 166 |
| `avg_pco2_ppm` | 79 | 12 | 4 | 63 | 55 | 8 | 13.7% | 69.6% | 57 | 59 | 63 | 65 |
| `avg_ph` | 28 | 4 | 1 | 23 | 22 | 1 | 5.5% | 78.6% | 23 | 23 | 25 | 25 |
| `avg_fdom` | 28 | 4 | 1 | 23 | 22 | 1 | 5.5% | 78.6% | 23 | 23 | 25 | 25 |
| `avg_turbidity` | 28 | 4 | 1 | 23 | 22 | 1 | 5.5% | 78.6% | 23 | 23 | 25 | 25 |
| `avg_spec_cond` | 28 | 4 | 1 | 23 | 22 | 1 | 5.5% | 78.6% | 23 | 23 | 25 | 25 |

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
- Seasonally, Turner chlorophyll same-day coverage is highest in summer (75.3%) and autumn (78.7%), lower in spring (47.4%), and zero in winter (only 17 winter biology dates, none with valid sensor data). Turner phycocyanin summer is 87.1%.
- `avg_do_wtemp` same-day coverage is only 94 dates and is especially weak in 2019 (2/16) and 2020 (0/15), so it cannot serve as the main water-temperature covariate for the 2019–2020 YSI-era comparison.

## 5. Interpretation limits

- The overlap is **day-level**, not time-of-day. The microscopy record has no sample time.
- The sensor values are daily averages of 1-minute data; the biology values are integrated/composite samples. Neither represents the same sampling support.
- Same-day presence is not evidence of biological response; it is only evidence that both records exist on that date.
- Missingness and flags are not random: the 2014–2015 Turner gap and 2019+ sensor transition concentrate missingness in specific years.
- No bloom/non-bloom labels, event intervals, model inputs or early-warning features were created.

## 6. Conclusion

The strongest exploratory pairing is **Turner chlorophyll/phycocyanin with microscopy cyanobacteria biovolume or cell density, 2006–2019**, on roughly 128–139 same-day dates, with the 0.5 m vs 0–8 m depth caveat. DO and water temperature add complementary environmental context on ~94–99 same-day dates. The 2019+ YSI pH/fDOM/turbidity/conductance variables are too short (22 same-day dates) for long-term comparison. No temporal analysis can recover intraday alignment or exact sample coincidence.
