# Sensor-Era and Comparability Audit

**Sprint:** 4L.9  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. Documented sensor transitions

The sensor inventory (`mendota_buoy_sensors_v3.csv`, 20 records) lists years only, not exact change dates. Mapping those records to the daily columns gives:

| Parameter | Manufacturer | Model | Began | Ended | Mapped daily variable(s) | Observed first unflagged | Observed last unflagged | Valid unflagged (sum) | Note |
|---|---|---|---|---|---:|---:|---:|---|
| DO | Zebra Tech | D-Opto | 2016 | 2018 | avg_do_raw; avg_do_sat; avg_do_wtemp | 2006-07-09 | 2025-11-18 | 7075 | Daily DO values exist from 2006; sensor inventory does not list a 2006-2015 DO model. |
| DO | PME | miniDOT | 2018 | 2018 | avg_do_raw; avg_do_sat; avg_do_wtemp | 2006-07-09 | 2025-11-18 | 7075 |  |
| DO | YSI | EXO2 sonde sensor | 2019 | present | avg_do_raw; avg_do_sat; avg_do_wtemp | 2006-07-09 | 2025-11-18 | 7075 |  |
| CO2 | Turner Designs | C-sense | 2017 | present | avg_pco2_ppm | 2016-03-22 | 2025-11-18 | 1841 | Daily pCO2 values begin 2016-03-22, earlier than the inventory's 2017 start. |
| pH | YSI | EXO2 sonde sensor | 2019 | present | avg_ph | 2019-04-16 | 2025-11-18 | 1383 |  |
| fDOM | YSI | EXO2 sonde sensor | 2019 | present | avg_fdom | 2019-04-16 | 2025-11-18 | 1397 |  |
| Turbidity | YSI | EXO2 sonde sensor | 2019 | present | avg_turbidity | 2019-04-16 | 2025-11-18 | 1385 |  |
| Chlor/Phyco | Turner Designs | Cyclops | 2006 | 2019 | avg_chlor_rfu_turner; avg_phyco_rfu_turner | 2006-07-09 | 2019-11-03 | 4510 |  |
| Chlor/Phyco | YSI | EXO2 sonde sensor | 2019 | present | avg_chlor_rfu_ysi; avg_phyco_rfu_ysi | 2019-04-16 | 2025-11-18 | 2629 |  |
| Conductivity | YSI | — | 2006 | 2006 | avg_spec_cond | 2019-04-16 | 2025-11-18 | 1318 | 2006 conductivity values are flagged H/O; no unflagged 2006 value. |
| Conductivity | YSI | EXO2 sonde sensor | 2019 | present | avg_spec_cond | 2019-04-16 | 2025-11-18 | 1318 |  |
| Water Temp | Apprise Tech | TempLine | 2006 | 2006 | avg_do_wtemp | 2006-07-09 | 2025-11-18 | 1943 | No separate daily water-temperature column; avg_do_wtemp is labelled YSI water temp but exists from 2006. |
| Water Temp | RBR | Concerto | 2007 | present | avg_do_wtemp | 2006-07-09 | 2025-11-18 | 1943 | No separate daily water-temperature column; avg_do_wtemp is labelled YSI water temp but exists from 2006. |
| Temp/RH | RM Young | 41382 | 2006 | 2017 | avg_air_temp; avg_rel_hum | 2006-07-09 | 2025-11-18 | 7007 |  |
| Temp/RH | Vaisala | HMP110 | 2017 | present | avg_air_temp; avg_rel_hum | 2006-07-09 | 2025-11-18 | 7007 |  |
| Wind | Vaisala | ultrasonic | 2006 | 2012 | avg_wind_speed; avg_wind_dir | 2006-07-09 | 2025-11-18 | 7102 |  |
| Wind | RM Young | 5106 | 2013 | present | avg_wind_speed; avg_wind_dir | 2006-07-09 | 2025-11-18 | 7102 |  |
| IR Skin Temp | Apogee | SI-111 | 2013 | present |  |  |  | 0 | No daily skin-temperature column in the daily entity. |
| PAR-above | Apogee | SQ-110 | 2016 | present | avg_par | 2007-05-18 | 2025-11-18 | 1460 | Sparse unflagged PAR near-zero values (ten 0.0, one 0.002) occur in 2007 before the inventory's 2016 start. |
| PAR-below | Apogee | SQ-111 | 2016 | present | avg_par_below | 2016-03-22 | 2025-11-18 | 1410 |  |

The observed coverage columns are **column-level**, not proof that the listed sensor produced every date. The valid-unflagged sum is a sum across mapped columns and is not an independent sample count.

## 2. Turner versus YSI chlorophyll/phycocyanin

The daily file has separate Turner and YSI columns for chlorophyll and phycocyanin. In 2019 both were deployed. Pairing only dates where both values are unflagged numeric gives:

| Proxy | Paired dates | Turner median (RFU) | YSI median (RFU) | Median YSI−Turner | Median ratio (YSI/Turner) | Ratio p05–p95 | First–last paired date |
|---|---:|---:|---:|---:|---:|---|---|
| chlorophyll | 156 | 1,354.74 | 0.390 | -1,354.33 | 0.000332 | 0.00021–0.000826 | 2019-04-17 to 2019-11-02 |
| phycocyanin | 160 | 802.01 | 0.590 | -800.91 | 0.000835 | -0.00026–0.002269 | 2019-04-17 to 2019-11-02 |

The two instruments are **not on a common scale**. The Turner medians are three orders of magnitude larger than the YSI medians; the EML itself states that both output RFU but have “significant magnitude differences.” No cross-calibration equation, correction factor or documented conversion is present. The paired 2019 data are useful for describing the discontinuity, not for creating a homogeneous series.

Further era facts:

- Turner chlorophyll has **2202** unflagged values and ends 2019-11-03; YSI chlorophyll has **1256** and begins 2019-04-16.
- Turner phycocyanin has **2308** unflagged values and ends 2019-11-03; YSI phycocyanin has **1373** and begins 2019-04-16.
- Turner chlorophyll is severely reduced in 2014 (**14** values) and 2015 (**70**); Turner phycocyanin has only **6** values in 2007. The “Turner era” is therefore not a continuous homogeneous block.
- YSI-era variables pH/fDOM/turbidity/specific conductance begin 2019-04-16 and have no pre-2019 daily values in this file.

## 3. DO and water temperature

- DO is present from 2006, but the sensor inventory's DO entries begin in 2016 (Zebra Tech D-Opto, 2016–2018; PME miniDOT, 2018; YSI EXO2, 2019+). The 2006–2015 DO instrument is not identified in the inventory. DO values therefore span undocumented and documented instruments.
- DO raw has **2649** unflagged values; DO saturation **2483**. Both have heavy `H`/`E` flags (Section QC). There is no documented cross-calibration between the pre-2016, 2016–2018 and 2019+ DO instruments.
- `avg_do_wtemp` is defined as “YSI water temp” but contains unflagged values from 2006. In 2019+ it is heavily `C`-flagged: **1087** `C` and **371** unflagged out of 1,612 records. Its pre-2019 provenance is unresolved.
- The EML states that lake temperature data collected at the same buoy site are in an ancillary dataset (`knb-lter-ntl.130`). That dataset was **not acquired** in this sprint and is not used here. `avg_do_wtemp` should not be assumed to be a continuous, homogeneous water-temperature record.

## 4. Other transitions

- **pCO2:** daily values begin 2016-03-22; the inventory lists Turner C-sense CO2 from 2017. The 2016 values are therefore outside the documented inventory start. 2024 has only **70** unflagged values (CO2 failed May 22); 2025 has **177**.
- **PAR above:** 11 unflagged near-zero values (ten 0.0, one 0.002) in 2007, then no sustained record until 2016. These values are not useful light data. 2019–2020 has major `C` outages; 2023–2024 has lower coverage.
- **PAR below:** begins 2016; heavy `C` in 2019–2020; `G` (biofouling) in 2021, 2022 and 2024.
- **Conductivity:** 2006 values are 0.38–0.48 µS/cm, all `H`/`O`; no unflagged 2006 value. 2019+ values are ~122–596 µS/cm. The two eras are not comparable.
- **pH, fDOM, turbidity:** 2019+ only. The 2019–2020 biology overlap is only **28** dates, with **22** same-day unflagged values.

## 5. Comparability verdict

- **Turner ↔ YSI chlorophyll/phycocyanin:** not directly comparable; no documented crosswalk. Use era-specific series or an explicit, validated cross-calibration if one is ever established. Do not concatenate.
- **DO:** instrument history incomplete before 2016; no documented cross-calibration; flags vary by year. Treat as an era-specific/flagged series.
- **Water temperature:** `avg_do_wtemp` is not a clean continuous series; ancillary 130 is documented but not acquired.
- **pH/fDOM/turbidity/conductance:** 2019+ only; short overlap with biology; no long-term comparability.
- **PAR:** contextual, patchy, and affected by documented outages/fouling.

**No correction factor, offset, scaling or gap-filling was applied.** The observed discontinuities are described; their causes are only attributed where the EML explicitly documents them.
