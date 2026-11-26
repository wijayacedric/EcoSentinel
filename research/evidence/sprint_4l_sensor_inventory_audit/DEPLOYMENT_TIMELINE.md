# Deployment Timeline — Lake Mendota Buoy Sensors (129.42)

**Date:** 2026-11-23T23:48:59.424593+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

All dates below are **as documented in the raw sensor file**. Dates are years only; no within-year dates are given. "present" is not defined and is treated as **undated**.

## Chronological starts

| Start | Parameter | Manufacturer | Model | End | Documented note |
|---:|---|---|---|---|---|
| 2006 | Conductivity | YSI | *(blank)* | 2006 | Model field blank; single year |
| 2006 | Water Temp | Apprise Tech | TempLine | 2006 | Single year |
| 2006 | Temp/RH | RM Young | 41382 | 2017 | Replaced by Vaisala |
| 2006 | Wind | Vaisala | ultrasonic | 2012 | Replaced by RM Young 5106 |
| 2006 | Chlor/Phyco | Turner Designs | Cyclops | 2019 | Replaced by YSI EXO2 |
| 2007 | Water Temp | RBR | Concerto | present | Replaces TempLine |
| 2013 | Wind | RM Young | 5106 | present | Replaces Vaisala |
| 2013 | IR Skin Temp | Apogee | SI-111 | present | New measurement |
| 2016 | DO | Zebra Tech | D-Opto | 2018 | Replaced by miniDOT/EXO2 |
| 2016 | PAR-above | Apogee | SQ-110 | present | New measurement |
| 2016 | PAR-below | Apogee | SQ-111 | present | New measurement |
| 2017 | CO2 | Turner Designs | C-sense | present | New measurement |
| 2017 | Temp/RH | Vaisala | HMP110 | present | Replaces RM Young 41382 |
| 2018 | DO | PME | miniDOT | 2018 | Overlaps D-Opto in 2018 |
| 2019 | DO | YSI | EXO2 sonde sensor | present | Major suite transition |
| 2019 | pH | YSI | EXO2 sonde sensor | present | New buoy measurement |
| 2019 | fDOM | YSI | EXO2 sonde sensor | present | New measurement |
| 2019 | Turbidity | YSI | EXO2 sonde sensor | present | New buoy measurement |
| 2019 | Chlor/Phyco | YSI | EXO2 sonde sensor | present | Overlaps Turner in 2019 |
| 2019 | Conductivity | YSI | EXO2 sonde sensor | present | Replaces 2006 sensor; gap 2007-2018 |

## Transition years and discontinuities

- **2007:** water-temperature sensor replacement.
- **2013:** wind sensor replacement; IR skin temperature begins.
- **2016:** DO and PAR begin.
- **2017:** Temp/RH replacement; CO2 begins.
- **2018:** D-Opto and miniDOT overlap.
- **2019:** the largest discontinuity — DO, chlorophyll/phycocyanin, pH, conductivity, fDOM and turbidity all move to YSI EXO2. Both Turner and YSI chlorophyll/phycocyanin are listed for 2019, but the switch date is unknown.

## Documented vs assumed

**Documented in file:** parameter, manufacturer, model, start year, end year, "present" label, blank conductivity model.

**Not documented / assumed:** exact within-year transition dates; whether overlapping sensors ran concurrently or were swapped mid-season; whether "present" means still operating at package publication (EML pubDate 2026-11-19); sensor depths; serial numbers; calibration; QC.

## Implication

A multivariate analysis spanning 2006–2025 would cross multiple sensor generations. Any apparent relationship change at 2016, 2017, 2018, 2019, or 2013 could be instrument-related unless the transition is explicitly modeled or stratified. No such modelling is performed here.
