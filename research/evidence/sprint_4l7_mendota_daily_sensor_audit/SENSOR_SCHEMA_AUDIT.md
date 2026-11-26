# Sensor Schema Audit

**Date:** 2026-11-24T08:45:50.090661+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Source

`knb-lter-ntl.129.42` EML (146,471 B; retrieved from DataONE CN). **The raw daily CSV was not acquired**, so this is a metadata-derived schema; the actual header/encoding could not be verified.

## Daily entity schema

- 38 fields: `year4`, `sampledate`, **18 measured variables**, and **18 flag columns**.
- All values are **daily averages** of 1-minute observations (per EML).
- Daily data are not the 1-minute/high-resolution entities.

| field | eml_definition | unit_or_type | role | expected_flag_codes |
|---|---|---|---|---|
| year4 | Four-digit year | nominalYear | date | No |
| sampledate | Sample Date | date | date | No |
| avg_air_temp | average air temperature (2m above sfc) | celsius | meteorology | C;E;H |
| avg_rel_hum | average relative humidity (2m above sfc) | percent | meteorology | C;E |
| avg_wind_speed | daily average wind speed (3m above sfc) | meterPerSecond | meteorology | C |
| avg_wind_dir | average wind direction (3m above sfc) | degree | meteorology | C;H |
| avg_chlor_rfu_turner | chlorophyll a RFU, 0.5m, Turner Cyclops 7, 2006-2019 | RFU | biological proxy | C;H |
| avg_chlor_rfu_ysi | chlorophyll a RFU, 0.5m, YSI EXO2, 2019-present | RFU | biological proxy | C;H;E;G |
| avg_phyco_rfu_turner | phycocyanin RFU, 0.5m, Turner Cyclops 7, 2006-2019 | RFU | biological proxy | C;H |
| avg_phyco_rfu_ysi | phycocyanin RFU, 0.5m, YSI EXO2, 2019-present | RFU | biological proxy | C;H;E;G |
| avg_par | PAR above water (2m) | micromolePerMeterSquaredPerSecond | light | C;H |
| avg_par_below | PAR below water (1m) | micromolePerMeterSquaredPerSecond | light | C;G |
| avg_do_wtemp | water temperature, YSI DO sensor (0.5m) | celsius | water temperature | C;H |
| avg_do_sat | DO % saturation (0.5m) | percent | DO | C;E;H |
| avg_do_raw | DO mg/L (0.5m) | milligramPerLiter | DO | C;E;H |
| avg_pco2_ppm | CO2 (1m) | ppm (not explicit in EML) | carbon | C;E |
| avg_ph | pH (0.5m) | dimensionless | pH | C |
| avg_fdom | fDOM (0.5m) | RFU/ppb QSU (not explicit in EML) | optical proxy | C |
| avg_turbidity | turbidity (0.5m) | FNU (not explicit in EML) | optical | C |
| avg_spec_cond | specific conductance (0.5m) | uS/cm (not explicit in EML) | conductivity | C;H |

## Schema issues

- Two chlorophyll and two phycocyanin columns represent different sensor eras: Turner (2006–2019) and YSI EXO2 (2019–present). They must not be silently concatenated.
- pH/fDOM/turbidity/specific conductance are documented from 2019 in the sensor inventory; `avg_spec_cond` also has a 2006-only era. Actual daily coverage is not verified.
- Some EML units are absent or not explicit (chlorophyll/phycocyanin RFU, pCO2 ppm, fDOM, turbidity FNU, specific conductance). Units require package/data-dictionary confirmation.
- No calibration, serial-number, sample-depth-per-row, or detection-limit fields exist in the daily schema.
- `avg_par` is above-water (2 m); `avg_par_below` is 1 m. Neither is a biological biomass measurement.

## Conclusion

The schema is rich but **era-structured**. No raw header verification or parsing audit is possible until the daily entity is acquired.
