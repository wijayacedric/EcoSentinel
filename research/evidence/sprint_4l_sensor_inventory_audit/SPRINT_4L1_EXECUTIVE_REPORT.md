# Sprint 4L.1 Executive Report — Mendota Sensor Inventory Structural Audit

**Date:** 2026-11-23T23:48:59.424593+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. File verification

- Path: `research/evidence/sprint_4k_mendota_authorised_access/acquisition/129.42/List_of_sensors_used_on_the_Lake_Mendota_buoy_since_2006__edddc490dfd553c4c4b9e5d4b86eb2eb.dat`
- Exists: **yes**; size **1,039 bytes** exactly.
- SHA256 (independent): **`255dc9a279f1acb4a3588f697e91f206c5466b9ef2c47166b9b6204002b117d5`**
- MD5 (independent): **`6e5c2a9204fe7e9e15a319a0344ebff0`**
- Acquisition provenance SHA256: **`255dc9a279f1acb4a3588f697e91f206c5466b9ef2c47166b9b6204002b117d5`** — **matches**.
- EML `<authentication method="MD5">`: **`6e5c2a9204fe7e9e15a319a0344ebff0`** — **matches**.
- Provenance note "no EML checksum" is a **parser-field artifact** (our inventory parser looked for `<checksum>`, while this EML uses `<authentication>`), not an integrity failure. No raw file was modified.

## 2. Format and structure

- CSV text; comma-delimited; quoted fields; **CRLF** line endings; no BOM.
- **21 lines** = 1 header + **20 sensor records**.
- **5 columns**: `parameter, sensor_mfg, sensor_model, date_began, date_ended`.
- **13 distinct parameter categories**; **9 manufacturers**.
- EML object name: `mendota_buoy_sensors_v3.csv`; local filename is acquisition-renamed; bytes preserved.

## 3. Content

The complete inventory is transcribed in `SENSOR_INVENTORY_TRANSCRIPTION.csv`. Key documented facts:

- **Water Temp:** Apprise Tech TempLine (2006 only) → RBR Concerto (2007–present).
- **DO:** Zebra Tech D-Opto (2016–2018), PME miniDOT (2018), YSI EXO2 (2019–present).
- **Chlor/Phyco:** Turner Designs Cyclops (2006–2019) → YSI EXO2 (2019–present).
- **Conductivity:** YSI, model blank (2006 only) → YSI EXO2 (2019–present); **no 2007–2018 buoy conductivity** in this list.
- **pH, fDOM, Turbidity:** YSI EXO2, **2019–present** only.
- **CO2:** Turner Designs C-sense, 2017–present.
- **Temp/RH:** RM Young 41382 (2006–2017) → Vaisala HMP110 (2017–present).
- **Wind:** Vaisala ultrasonic (2006–2012) → RM Young 5106 (2013–present).
- **IR Skin Temp:** Apogee SI-111, 2013–present.
- **PAR above/below:** Apogee SQ-110/SQ-111, 2016–present.

## 4. Replacements and discontinuities

- **2019 is a major transition year**: DO, chlorophyll/phycocyanin, pH, conductivity, fDOM, turbidity move to YSI EXO2. Turner and YSI chlorophyll/phycocyanin are both listed for 2019, but the within-year switch date is not recorded.
- **2018**: D-Opto and miniDOT both listed; possible intercomparison or mid-season change.
- **2017**: RM Young and Vaisala Temp/RH both listed; CO2 begins.
- **2013**: wind sensor replacement and IR skin temperature begin.
- **2016**: DO and PAR sensors begin.
- **2007**: water temperature sensor replacement.

## 5. Calibration and depth

- **No calibration dates, coefficients, accuracy, serial numbers, or depths** appear in this file.
- EML describes some depths elsewhere (e.g., chlorophyll/phycocyanin 0.5 m; air temp 2 m; wind 3 m), but the sensor inventory itself does not carry depth per row. Do not assume a common depth.
- No QC-flag definitions are in this file.

## 6. Suitability for comparison with 88.31

- **Best long-overlap physical variable:** water temperature (RBR Concerto, 2007–present) and meteorological variables (2006–present).
- **Conventional sensor baseline:** Turner chlorophyll/phycocyanin (2006–2019) and YSI (2019–present) — proxies, **not independent biological ground truth**.
- **Limited overlap:** DO (2016+), CO2 (2017+), PAR (2016+), IR skin temp (2013+); pH/turbidity/fDOM/conductivity (2019+) overlap 88.31 only for 2019–2020.
- **Depth mismatch:** 88.31 is a 0–8 m composite; sensor chlorophyll/phycocyanin is documented at 0.5 m; water-temperature depth is not in this file. Alignment requires explicit comparator definition.

## 7. Verdict

The file is **structurally verified and internally consistent**. It documents sensor eras but **not exact transition dates, depths, serials, calibration, or QC**. It is sufficient to characterize likely discontinuities and variable suitability, not to prove measurement comparability.

**Gate 2 remains PAUSED / NOT APPROVED — Option C (Exploratory Only).** No labels, modelling, or confirmatory analysis.
