# Sensor Deployment and Era Audit

**Date:** 2026-11-24T08:45:50.090661+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Sensor inventory (20 records / 13 parameter categories)

| parameter | manufacturer | model | date_began | date_ended | documented_span | transition_note |
|---|---|---|---|---|---|---|
| DO | Zebra Tech | D-Opto | 2016 | 2018 | 2016-2018 | 2018 overlap with miniDOT; exact change date not recorded. |
| DO | PME | miniDOT | 2018 | 2018 | 2018-2018 | Single-year 2018 deployment; may overlap D-Opto for intercomparison (assumption). |
| DO | YSI | EXO2 sonde sensor | 2019 | present | 2019-present (end undefined) | Major 2019 suite transition; replaces earlier DO sensors. |
| CO2 | Turner Designs | C-sense | 2017 | present | 2017-present (end undefined) | Starts 2017; no earlier buoy CO2 sensor listed. |
| pH | YSI | EXO2 sonde sensor | 2019 | present | 2019-present (end undefined) | Buoy pH starts 2019; handheld 415.2 pH exists 2014-2019. |
| fDOM | YSI | EXO2 sonde sensor | 2019 | present | 2019-present (end undefined) | Optical proxy; starts 2019. |
| Turbidity | YSI | EXO2 sonde sensor | 2019 | present | 2019-present (end undefined) | Starts 2019; no earlier buoy turbidity listed. |
| Chlor/Phyco | Turner Designs | Cyclops | 2006 | 2019 | 2006-2019 | 2006-2019; overlaps 2019 YSI; exact transition date not recorded. |
| Chlor/Phyco | YSI | EXO2 sonde sensor | 2019 | present | 2019-present (end undefined) | 2019-present; overlaps Turner in 2019; comparability unverified. |
| Conductivity | YSI |  | 2006 | 2006 | 2006-2006 | 2006 only; model field blank; gap 2007-2018. |
| Conductivity | YSI | EXO2 sonde sensor | 2019 | present | 2019-present (end undefined) | 2019-present; gap 2007-2018. |
| Water Temp | Apprise Tech | TempLine | 2006 | 2006 | 2006-2006 | 2006 only; replaced by RBR Concerto. |
| Water Temp | RBR | Concerto | 2007 | present | 2007-present (end undefined) | 2007-present; depth/chain configuration not in this file. |
| Temp/RH | RM Young | 41382 | 2006 | 2017 | 2006-2017 | 2006-2017; replaced by Vaisala. |
| Temp/RH | Vaisala | HMP110 | 2017 | present | 2017-present (end undefined) | 2017-present; 2017 overlap with RM Young. |
| Wind | Vaisala | ultrasonic | 2006 | 2012 | 2006-2012 | 2006-2012; replaced by RM Young 5106. |
| Wind | RM Young | 5106 | 2013 | present | 2013-present (end undefined) | 2013-present. |
| IR Skin Temp | Apogee | SI-111 | 2013 | present | 2013-present (end undefined) | 2013-present. |
| PAR-above | Apogee | SQ-110 | 2016 | present | 2016-present (end undefined) | 2016-present. |
| PAR-below | Apogee | SQ-111 | 2016 | present | 2016-present (end undefined) | 2016-present. |

## Major discontinuities

- **2019:** DO, chlorophyll/phycocyanin, pH, conductivity, fDOM and turbidity move to YSI EXO2. Turner and YSI chlorophyll/phycocyanin coexist in 2019; exact switch date unknown.
- **2018:** D-Opto and miniDOT both listed for DO; possible intercomparison or mid-season change.
- **2017:** temp/RH changes from RM Young 41382 to Vaisala HMP110; CO2 begins.
- **2016:** DO and PAR begin.
- **2013:** wind changes to RM Young 5106; IR skin temperature begins.
- **2007:** water temperature changes from Apprise TempLine to RBR Concerto.

## Consequences

- The daily columns `avg_chlor_rfu_turner` and `avg_chlor_rfu_ysi` are **different instruments**, not interchangeable without a cross-calibration.
- pH/fDOM/turbidity/specific conductance have only ~2019–2020 overlap with the 88.31 biology (which ends 2020); they cannot support long-term exploratory analysis.
- Water temperature/DO/chlorophyll/phycocyanin have longer potential overlap, but sensor-era mapping and QC are unresolved.
- **Do not concatenate eras** into a homogeneous series without documented crosswalks and uncertainty.

## What is not documented

Exact within-year switch dates, serial numbers, calibration coefficients, fouling/maintenance logs, and per-variable depth changes. The sensor list gives years only.
