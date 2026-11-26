# Environmental Predictor Comparison

**Date:** 2026-11-23T23:18:29.122618+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Buffalo Pound buoy — VERIFIED

- **Source:** FRDR `10.20383/103.01100`; 8 annual CSVs (2014-2021), locally preserved, SHA256 verified this mission.
- **Variables (68 columns incl. flags):** air temp, RH, wind speed/direction, rainfall, barometric pressure, PAR (air/0.62 m/0.78 m), water temp (0.54/1.06/1.56/2.56/3.56 m + 0.8/2.8 m), pH, DO (mg/L and % sat), specific conductivity + raw, turbidity, chlorophyll RFU, blue-green phycocyanin RFU (0.8 m and 2.8 m).
- **Cadence:** 2014 = 15-min (8,015 rows); 2015-2021 = 10-min (16,836-22,023 rows/year).
- **Coverage:** 2014-06-11 to 2021-10-07, ice-free seasons only (no winter).
- **Quality flags:** every measured variable has an adjacent `_Flag` column; `data_flags.csv` documents codes; README documents sensor fouling, gaps, and 2017/2018 conductivity corrections.
- **Predictor sufficiency:** strong multivariate set at 10-min resolution, including the key EcoSentinel variables (temp, DO, pH, conductivity, turbidity, pigments as proxies, meteorology).
- **Limitations:** chlorophyll/phycocyanin are RFU sensor proxies, not calibrated biomass; single buoy site; ice-free only; fouling/gaps.

## Lake Mendota — CORROBORATED (metadata), DATA BLOCKED

- **129.9 (HF meteo/DO/Chl/PC):** EML lists `air_temp, rel_hum, wind_speed, wind_dir, chlor, phycocyanin, opt_do_raw, opt_dosat_raw, opt_wtemp` with flags; high-frequency. **This is the predictor set the mission needed**, but it was missing from the original target list (only 130.29 temperature was included).
- **130.29:** daily/hourly/high-resolution water temperature only; flags; 2006-2019; 2015 HR entity missing on CN.
- **415.2:** routine Microbial Observatory temp/DO/pH/specific conductance/barometer (YSI 2014-2019) + non-Poseidon temp/DO; likely discrete.
- **Data access:** all data bytes auth-blocked (CN object 404, PASTA 403).
- **Assessment:** potentially excellent multivariate coverage (129), but unverified and inaccessible.

## Western Lake Erie — CORROBORATED (literature), NO FILES

- Discrete CTD/lab variables at sampling; wind/wave from THLO1/GLOS buoys only.
- No evidence of a co-located HF multivariate buoy record paired to biological stations.
- NCEI raw access unavailable.

## Greifensee — VERIFIED (prior audit)

- ERIC 000C8P CTD/meteo/nutrients; high-frequency CTD/meteo, discrete nutrients. Paired with classifier-derived biology only.

## Comparison

| Candidate | Multivariate HF predictors | Verified local access | Main weakness |
|---|---|---|---|
| Buffalo Pound | Yes (10-min, 68 vars) | Yes | sensor proxies; ice-free only; single site |
| Lake Mendota | Yes per metadata (129.9) | No (auth) | access-blocked; 2015 HR gap |
| Lake Erie | No demonstrated HF multivariate buoy | No | discrete sampling; no cell endpoint |
| Greifensee | Yes (CTD/meteo) | Yes | biology not independent |
