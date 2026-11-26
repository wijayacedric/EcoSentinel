# QC Flag Audit

**Sprint:** 4L.9  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. Documented codes

The daily EML defines, where listed:

| Code | General meaning | Where documented in the daily schema |
|---|---|---|
| `C` | Sensor off | Most flag columns |
| `E` | Sensor noisy or malfunctioning | Air temp, RH, YSI chlorophyll/phycocyanin, DO, pCO2 (but not all columns) |
| `H` | Outside of standard range | Air temp, wind direction, chlorophyll/phycocyanin, PAR, DO, specific conductance (but not all columns) |
| `G` | Sensor — suspected biofouling | YSI chlorophyll, YSI phycocyanin, PAR below water |
| `O` | **Undefined** | Not defined anywhere in the EML; one value in `flag_avg_spec_cond` |

The per-column code lists are the authoritative enumeration for each attribute. Eight columns contain values outside their own list; see Section 4.

## 2. Flag totals by variable

| Variable | Records | C | E | H | G | O | No flag | Any flag | Valid unflagged |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `avg_air_temp` | 3996 | 139 | 5 | 157 | 0 | 0 | 3695 | 301 | 3445 |
| `avg_rel_hum` | 3996 | 172 | 6 | 6 | 0 | 0 | 3812 | 184 | 3562 |
| `avg_wind_speed` | 3996 | 408 | 0 | 124 | 0 | 0 | 3464 | 532 | 3446 |
| `avg_wind_dir` | 3996 | 329 | 0 | 3 | 0 | 0 | 3664 | 332 | 3656 |
| `avg_chlor_rfu_turner` | 3996 | 316 | 0 | 54 | 0 | 0 | 3626 | 370 | 2202 |
| `avg_chlor_rfu_ysi` | 3996 | 172 | 1 | 116 | 11 | 0 | 3696 | 300 | 1256 |
| `avg_phyco_rfu_turner` | 3996 | 225 | 0 | 41 | 0 | 0 | 3730 | 266 | 2308 |
| `avg_phyco_rfu_ysi` | 3996 | 168 | 1 | 0 | 11 | 0 | 3816 | 180 | 1373 |
| `avg_par` | 3996 | 915 | 0 | 81 | 0 | 0 | 3000 | 996 | 1460 |
| `avg_par_below` | 3996 | 762 | 0 | 90 | 34 | 0 | 3110 | 886 | 1410 |
| `avg_do_wtemp` | 3996 | 1705 | 3 | 243 | 0 | 0 | 2045 | 1951 | 1943 |
| `avg_do_sat` | 3996 | 443 | 52 | 928 | 0 | 0 | 2573 | 1423 | 2483 |
| `avg_do_raw` | 3996 | 452 | 54 | 734 | 0 | 0 | 2756 | 1240 | 2649 |
| `avg_pco2_ppm` | 3996 | 235 | 16 | 0 | 0 | 0 | 3745 | 251 | 1841 |
| `avg_ph` | 3996 | 178 | 1 | 0 | 0 | 0 | 3817 | 179 | 1383 |
| `avg_fdom` | 3996 | 164 | 1 | 0 | 0 | 0 | 3831 | 165 | 1397 |
| `avg_turbidity` | 3996 | 176 | 1 | 0 | 0 | 0 | 3819 | 177 | 1385 |
| `avg_spec_cond` | 3996 | 218 | 17 | 82 | 0 | 1 | 3678 | 318 | 1318 |

## 3. What the flags actually show

### 3.1 `C` is not equivalent to missing

`C` is defined as “sensor off”, but many `C` records still contain numeric values:

- `avg_do_wtemp`: **1534** numeric `C` values and **171** missing `C` values.
- `avg_par_below`: **668** numeric `C` values.
- `avg_do_raw`: **277** numeric `C` values.
- `avg_spec_cond`: **118** numeric `C` values.
- `avg_chlor_rfu_ysi`: **113** numeric `C` values.

This means `C` cannot be used as a missing-value code without inspecting the value column. The audit excludes all flagged numeric values from `valid_unflagged`, but retains them in `numeric_any`.

### 3.2 `H` is common and not automatically an error

`H` (“outside of standard range”) is frequent:

- `avg_do_sat`: **928** `H` (23.2% of records), median flagged value 129.12%, max 221.56%.
- `avg_do_raw`: **734** `H`, median 12.21 mg/L, max 24.34 mg/L.
- `avg_air_temp`: **157** `H`, concentrated in 2008–2009 (2009:85;2008:65;2010:5).
- `avg_wind_speed`: **124** `H`, concentrated in 2009 (2009:93;2007:12;2006:7).
- `avg_spec_cond`: **82** `H`, all in 2006, with values 0.379–0.481 µS/cm; this is a scale/era problem, not a plausible freshwater conductance.
- Turner chlorophyll: **54** `H`; YSI chlorophyll: **116** `H`; PAR: **81** `H`; PAR below: **90** `H`.

`H` values are not deleted. They are reported separately and excluded from the unflagged subset. Some `H` values are plausibly real extremes (e.g., high DO), while others (2006 conductance) are clearly not on the later scale.

### 3.3 `G` is era-specific

`G` (“suspected biofouling”) appears only for:

- YSI chlorophyll: **11**
- YSI phycocyanin: **11**
- PAR below water: **34**

Turner chlorophyll/phycocyanin have **no `G` flags** in the daily file even though the Turner era spans 2006–2019. The absence of `G` in the Turner era does **not** prove the absence of biofouling; it means the flag was not used for those columns. The EML's 2017 note about significant DO biofouling is a documented event, not a per-record flag.

### 3.4 Missing values often have no flag

Many missing values are “empty unflagged” rather than `C`:

- Turner chlorophyll: **1424** empty-unflagged vs 40 flag-without-value.
- YSI chlorophyll: **2440** empty-unflagged vs 59 flag-without-value.
- pH: **2434** empty-unflagged; fDOM **2434**; turbidity **2434**; specific conductance **2360**.

Most of these are structural (sensor not yet deployed or seasonally removed), but the file does not carry an explicit “not deployed” code for them. This is a QC ambiguity, not a reason to impute zeros.

### 3.5 Flag patterns by year

Representative concentrations (full table: `QC_FLAG_TOP_YEARS.csv`, `QC_FLAG_DISTRIBUTIONS.csv`):

| Variable | Flag | Total | Top years |
|---|---|---:|---|
| `avg_air_temp` | H | 157 | 2009:85;2008:65;2010:5 |
| `avg_wind_speed` | C | 408 | 2009:119;2010:110;2008:99 |
| `avg_wind_speed` | H | 124 | 2009:93;2007:12;2006:7 |
| `avg_chlor_rfu_turner` | C | 316 | 2014:147;2015:97;2007:33 |
| `avg_chlor_rfu_ysi` | H | 116 | 2021:43;2020:32;2022:24 |
| `avg_chlor_rfu_ysi` | G | 11 | 2019:7;2025:4 |
| `avg_do_raw` | C | 452 | 2014:105;2007:94;2008:63 |
| `avg_do_raw` | E | 54 | 2017:51;2007:2;2019:1 |
| `avg_do_raw` | H | 734 | 2016:137;2010:127;2017:87 |
| `avg_par` | C | 915 | 2020:224;2019:163;2007:149 |
| `avg_par_below` | C | 762 | 2020:219;2019:144;2023:125 |
| `avg_par_below` | G | 34 | 2021:12;2024:12;2022:10 |
| `avg_do_wtemp` | C | 1705 | 2020:214;2021:206;2023:198 |
| `avg_spec_cond` | H | 82 | 2006:82 |
| `avg_spec_cond` | E | 17 | 2024:16;2019:1 |

Patterns are concentrated in particular years/eras: early meteorological outages (2008–2010), the 2014–2015 Turner chlorophyll collapse, the 2019+ YSI era, and the 2019–2020/2021 PAR outages. The flags are not randomly distributed.

## 4. Metadata code-list inconsistencies

The daily EML's per-column enumerations omit values that are present in the data:

| Variable | Documented daily codes | Extra observed | Count |
|---|---|---|---:|
| `avg_rel_hum` | C, E | H | 6 |
| `avg_wind_speed` | C | H | 124 |
| `avg_par_below` | C, G | H | 90 |
| `avg_do_wtemp` | C, H | E | 3 |
| `avg_ph` | C | E | 1 |
| `avg_fdom` | C | E | 1 |
| `avg_turbidity` | C | E | 1 |
| `avg_spec_cond` | C, H | E, O | 18 |

These are **metadata inconsistencies**, not arithmetic errors. The most important are the undefined `O` code, the `H` values in `flag_avg_wind_speed` and `flag_avg_par_below`, and the `E` values in several 2019+ columns whose daily code list contains only `C`.

## 5. Calibration and maintenance evidence

The EML abstract documents:

- 2017: boating mishap lost air temperature, RH and wind sensors between May 28 and July 11; DO sensor had significant biofouling from algae and zebra mussels.
- 2019: YSI EXO2 added; pH, DO and specific conductance cleaned/recalibrated every two weeks; Turner and YSI chlorophyll/phycocyanin both deployed; “significant magnitude differences” between Turner and YSI RFU.
- 2020: YSI cleaning/calibration nearly weekly; CO2 sensor not operating July 2–September 17.
- 2021: buoy not operating August 22–31; intermittent November 8–December 3; underwater PAR antifouling method used.
- 2022: buoy not operating June 6–9 and July 2–5; underwater PAR unusable after October 1.
- 2023: conductivity not operational April 27–May 24 and replaced; YSI wiper failed November 4–14, significantly affecting chlorophyll, phycocyanin, conductivity and turbidity.
- 2024: CO2 failed May 22 and was not used for the rest of the season; communications down June 13–19; PAR broken August 30–September 4.

The EML/sensor list do **not** provide per-record calibration dates, coefficients, serial numbers, detection limits, fouling measurements or maintenance logs. The flag codes are not a substitute. Manufacturer guidance (USGS TM1-D10) states that algal fluorometers are proxy sensors, RFU is sensor-specific, calibration checks should be routine, and biofouling/blank corrections require site-specific evidence. No calibration continuity is assumed here.

## 6. Conclusion

Flags are present and informative, but they are **not** a complete or internally consistent QC system. Missingness, `C`-with-value, undocumented codes, unflagged implausible values and era-specific `G` usage all prevent treating “unflagged” as “validated”. The audit preserves the raw values and reports the unflagged subset only as an explicit analytical choice.
