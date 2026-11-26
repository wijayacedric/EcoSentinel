# Variable Coverage and Limitations

**Date:** 2026-11-23T23:48:59.424593+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Reference biological coverage

88.31 phytoplankton: 1995-01-24 to 2020-12-31; Mendota 0-8 m composite; biweekly ice-free, 4-weekly late season.

## Coverage vs 88.31

"Overlap" below is the documented sensor era intersected with 88.31's 1995-2020 coverage. For "present" rows, overlap through 2020 is **conditional on continuous operation**, which the sensor file does not verify.

| Parameter | Documented sensor era | Potential overlap with 88.31 | Role for EcoSentinel | Main limitation |
|---|---|---|---|---|
| Water Temp | Apprise 2006; RBR 2007-present | 2006; 2007-2020 | Key physical driver | Depth not in sensor file; sensor replacement 2007 |
| Chlor/Phyco | Turner 2006-2019; YSI 2019-present | 2006-2019; 2019-2020 | Conventional sensor baseline/proxy | Not independent biology; Turner/YSI comparability unverified; 2019 overlap |
| DO | D-Opto 2016-2018; miniDOT 2018; YSI 2019-present | 2016-2018; 2018; 2019-2020 | Biogeochemical driver | No pre-2016; three sensor types; depth not in file |
| CO2 | Turner C-sense 2017-present | 2017-2020 | Carbon context | Short overlap; sensor start 2017 |
| pH | YSI EXO2 2019-present | 2019-2020 | Chemical driver | Only 2 years with 88.31; buoy pH starts 2019 |
| fDOM | YSI EXO2 2019-present | 2019-2020 | Optical proxy | Only 2 years; proxy |
| Turbidity | YSI EXO2 2019-present | 2019-2020 | Optical/water-quality context | Only 2 years; no earlier buoy record |
| Conductivity | YSI 2006; YSI EXO2 2019-present | 2006; 2019-2020 | Physical driver | Gap 2007-2018; model blank in 2006 |
| Temp/RH | RM Young 2006-2017; Vaisala 2017-present | 2006-2017; 2017-2020 | Meteorological context | Sensor replacement 2017 |
| Wind | Vaisala 2006-2012; RM Young 2013-present | 2006-2012; 2013-2020 | Meteorological driver | Sensor replacement 2013 |
| IR Skin Temp | Apogee 2013-present | 2013-2020 | Surface thermal context | Starts 2013; depth/field of view not in file |
| PAR-above | Apogee 2016-present | 2016-2020 | Light driver | Starts 2016 |
| PAR-below | Apogee 2016-present | 2016-2020 | Underwater light context | Starts 2016; depth not in file |

## Depths

- The sensor file **contains no depth column**.
- EML describes some depths elsewhere: chlorophyll/phycocyanin at **0.5 m**; air temperature **2 m**; wind **3 m**; PAR above ~**2 m**, below ~**1 m**.
- Water-temperature sensor depth/config (RBR Concerto) is **not stated in this file**; 130.29 is the separate thermistor-chain package.
- 88.31 is a **0-8 m composite**; comparing it to a 0.5 m sensor or a single water-temperature depth requires an explicit, documented comparator. Do not assume equivalence.

## Suitability summary

**Most suitable for exploratory comparison:** water temperature, meteorological variables (Temp/RH, wind, PAR), and chlorophyll/phycocyanin as a **conventional proxy baseline**.

**Weak/limited overlap:** DO (2016+), CO2 (2017+), IR skin temp (2013+), pH/turbidity/fDOM/conductivity (2019+ only; conductivity discontinuous).

**Not suitable as independent biological ground truth:** chlorophyll/phycocyanin RFU. They are sensor proxies and cannot replace 88.31 microscopy counts/biomass.

## Calibration and QC

- No calibration dates/coefficients, accuracy, serial numbers, or QC flags are in the sensor file.
- The raw daily/hourly/HR data are expected to carry `flag_*` columns (C/E/H) per EML, but those data have not been audited here.
- Sensor-era changes are a first-order confound for any multivariate relationship-change analysis.
