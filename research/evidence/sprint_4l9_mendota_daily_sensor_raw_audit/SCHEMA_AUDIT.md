# Schema and Parsing Audit

**Sprint:** 4L.9  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. Structure

- **38 columns** in the exact expected order: `year4`, `sampledate`, then 18 variable/flag pairs.
- **3,996 data rows**; **0** malformed rows; **0** blank lines; **0** non-numeric non-empty values.
- `year4` is an integer field and matches `sampledate` in all rows.
- `sampledate` is an ISO `YYYY-MM-DD` date; all 3,996 values parse.
- Numeric variables are floats; flag fields are strings with values blank, `C`, `E`, `H`, `G` or `O`.
- No duplicate dates; no exact duplicate rows.
- The daily EML has **38 attribute definitions** for this entity, matching the 38 columns.

## 2. Field-level schema

| # | Column | Role | Type | Definition (EML) | Documented codes | Non-empty | Missing | Parse errors | Undocumented flag values |
|---:|---|---|---|---|---|---:|---:|---:|---:|
| 1 | `year4` | date | integer | Four-digit year | — | 3996 | 0 | 0 | 0 |
| 2 | `sampledate` | date | ISO date | Sample Date | — | 3996 | 0 | 0 | 0 |
| 3 | `avg_air_temp` | variable | float | average air temperature (2m above sfc) | — | 3691 | 305 | 0 | 0 |
| 4 | `flag_avg_air_temp` | flag | string/flag | data flags avg air temp | C,E,H | 301 | 3695 | 0 | 0 |
| 5 | `avg_rel_hum` | variable | float | average relative humidity (2m above sfc) | — | 3694 | 302 | 0 | 0 |
| 6 | `flag_avg_rel_hum` | flag | string/flag | data flags avg relative humidity | C,E | 184 | 3812 | 0 | 6 |
| 7 | `avg_wind_speed` | variable | float | daily average wind speed (3m above sfc) | — | 3882 | 114 | 0 | 0 |
| 8 | `flag_avg_wind_speed` | flag | string/flag | data flags for avg wind speed | C | 532 | 3464 | 0 | 124 |
| 9 | `avg_wind_dir` | variable | float | average of wind direction (3m above sfc) | — | 3720 | 276 | 0 | 0 |
| 10 | `flag_avg_wind_dir` | flag | string/flag | data flags for average wind direction | C,H | 332 | 3664 | 0 | 0 |
| 11 | `avg_chlor_rfu_turner` | variable | float | average of chlorophyll a (RFU) (0.5m depth), Turner Cyclops 7 fluorometer, 2006-2019 | — | 2532 | 1464 | 0 | 0 |
| 12 | `flag_avg_chlor_rfu_turner` | flag | string/flag | data flags for average chlorophyll a (RFU), Turner Cyclops 7 fluorometer | C,H | 370 | 3626 | 0 | 0 |
| 13 | `avg_chlor_rfu_ysi` | variable | float | average of chlorophyll a (RFU) (0.5m depth), YSI EXO2 sonde, 2019-present | — | 1497 | 2499 | 0 | 0 |
| 14 | `flag_avg_chlor_rfu_ysi` | flag | string/flag | data flags for average chlorophyll a (RFU), YSI EXO2 sonde | C,H,E,G | 300 | 3696 | 0 | 0 |
| 15 | `avg_phyco_rfu_turner` | variable | float | average of phycocyanin (RFU) (0.5m depth), Turner Cyclops 7 fluorometer, 2006-2019 | — | 2410 | 1586 | 0 | 0 |
| 16 | `flag_avg_phyco_rfu_turner` | flag | string/flag | data flags for average phycocyanin (RFU), Turner Cyclops 7 fluorometer | C,H | 266 | 3730 | 0 | 0 |
| 17 | `avg_phyco_rfu_ysi` | variable | float | average of phycocyanin (RFU) (0.5m depth), YSI EXO2 sonde, 2019-present | — | 1497 | 2499 | 0 | 0 |
| 18 | `flag_avg_phyco_rfu_ysi` | flag | string/flag | data flags for average phycocyanin (RFU), YSI EXO2 sonde | C,H,E,G | 180 | 3816 | 0 | 0 |
| 19 | `avg_par` | variable | float | average photosynthetically active radiation (2m above water surface) | — | 2307 | 1689 | 0 | 0 |
| 20 | `flag_avg_par` | flag | string/flag | data flags for PAR | C,H | 996 | 3000 | 0 | 0 |
| 21 | `avg_par_below` | variable | float | average of photosynthetically active radiation (1m depth) | — | 2202 | 1794 | 0 | 0 |
| 22 | `flag_avg_par_below` | flag | string/flag | data flags for avg_par_below | C,G | 886 | 3110 | 0 | 90 |
| 23 | `avg_do_wtemp` | variable | float | average of YSI water temp (0.5m depth) | — | 3723 | 273 | 0 | 0 |
| 24 | `flag_avg_do_wtemp` | flag | string/flag | data flags avg YSI water temp | C,H | 1951 | 2045 | 0 | 3 |
| 25 | `avg_do_sat` | variable | float | average of dissolved oxygen (% saturation) (0.5m depth) | — | 3729 | 267 | 0 | 0 |
| 26 | `flag_avg_do_sat` | flag | string/flag | data flags avg_do_sat | C,E,H | 1423 | 2573 | 0 | 0 |
| 27 | `avg_do_raw` | variable | float | average of dissolved oxygen (mg/L) (0.5m depth) | — | 3712 | 284 | 0 | 0 |
| 28 | `flag_avg_do_raw` | flag | string/flag | data flags for avg do raw | C,E,H | 1240 | 2756 | 0 | 0 |
| 29 | `avg_pco2_ppm` | variable | float | average of CO2 (1m depth) | — | 1985 | 2011 | 0 | 0 |
| 30 | `flag_avg_pco2_ppm` | flag | string/flag | data flags avg pCO2 | C,E | 251 | 3745 | 0 | 0 |
| 31 | `avg_ph` | variable | float | average of pH (0.5m depth) | — | 1499 | 2497 | 0 | 0 |
| 32 | `flag_avg_ph` | flag | string/flag | data flag for average pH | C | 179 | 3817 | 0 | 1 |
| 33 | `avg_fdom` | variable | float | average for fluorescent dissolved organic matter (fDOM) (0.5m depth) | — | 1515 | 2481 | 0 | 0 |
| 34 | `flag_avg_fdom` | flag | string/flag | data flag average of fDOM | C | 165 | 3831 | 0 | 1 |
| 35 | `avg_turbidity` | variable | float | average of turbidity (0.5m depth) | — | 1504 | 2492 | 0 | 0 |
| 36 | `flag_avg_turbidity` | flag | string/flag | data flags avg turbidity | C | 177 | 3819 | 0 | 1 |
| 37 | `avg_spec_cond` | variable | float | average of specific conductance (0.5m depth) | — | 1536 | 2460 | 0 | 0 |
| 38 | `flag_avg_spec_cond` | flag | string/flag | data flags for avg specific conductance | C,H | 318 | 3678 | 0 | 18 |

## 3. Flag-code inconsistencies

The daily EML gives a per-column enumerated code list. Eight columns contain values outside their own documented list:

| Variable | Documented daily codes | Extra values observed | Count |
|---|---|---|---:|
| `avg_rel_hum` | C, E | H | 6 |
| `avg_wind_speed` | C | H | 124 |
| `avg_par_below` | C, G | H | 90 |
| `avg_do_wtemp` | C, H | E | 3 |
| `avg_ph` | C | E | 1 |
| `avg_fdom` | C | E | 1 |
| `avg_turbidity` | C | E | 1 |
| `avg_spec_cond` | C, H | E, O | 18 |

The most consequential case is `flag_avg_spec_cond`: the daily EML lists only `C,H`, but the data contain **17 `E`** values and **one `O`** value (2006-08-11, specific conductance 0.45). `O` has no definition anywhere in the EML. `flag_avg_par_below` lists `C,G` in the daily table but contains **90 `H`** values; the hourly table's code list includes `H`, suggesting a daily-metadata omission rather than a data error. `flag_avg_wind_speed` lists only `C` but contains **124 `H`** values.

## 4. Other metadata inconsistencies relevant to interpretation

- **`avg_do_wtemp`** is defined as “average of YSI water temp (0.5m depth)”, yet unflagged values exist from 2006-07-09, long before the YSI EXO2 deployment in 2019. The pre-2019 temperature provenance is unresolved.
- **DO** values exist from 2006, but the sensor inventory's DO records begin in 2016. The inventory does not identify a 2006–2015 DO sensor.
- **pCO2** values begin 2016-03-22, while the sensor inventory lists the Turner C-sense CO2 sensor from 2017.
- **PAR** has 11 unflagged near-zero values (ten 0.0 and one 0.002) in 2007-05-18 to 2007-05-28, before the inventory's 2016 PAR start and before the sustained PAR record. These values are not useful as environmental light data.
- **Conductivity** has 2006 values around 0.38–0.48 µS/cm, all flagged `H` or `O`; there are no unflagged 2006 conductivity values.

## 5. Conclusion

The file is structurally clean and fully parseable. The flag metadata are **not** complete or internally consistent for every column, and several sensor-era definitions conflict with observed coverage. These are documented as data-quality limitations; they are not silently corrected.
