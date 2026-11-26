# Independent Lake Mendota Buoy Sensor Inventory Audit

**Review date:** 23 November 2026  
**Gate 2:** PAUSED / NOT APPROVED  
**Scope:** Independent, read-only assessment of the named `.dat` source file. Sprint 4L.1 outputs were not read. No other data were downloaded.

## Source verification

- **Source:** `/Users/cedricbw/Documents/EcoSentinel/research/evidence/sprint_4k_mendota_authorised_access/acquisition/129.42/List_of_sensors_used_on_the_Lake_Mendota_buoy_since_2006__edddc490dfd553c4c4b9e5d4b86eb2eb.dat`
- **Size:** 1,039 bytes.
- **SHA256:** `255dc9a279f1acb4a3588f697e91f206c5466b9ef2c47166b9b6204002b117d5`
- **Contents:** CSV-formatted text with a header and 20 sensor records. I read the complete file directly. The transcription in `CODEX_SENSOR_TRANSCRIPTION.csv` preserves the five source columns and all 20 rows, including the blank model value for the 2006 conductivity entry.

## What the inventory documents

| Parameter as written | Manufacturer / model as written | Listed years | Independent interpretation / potential comparison to phytoplankton 88.31 |
|---|---|---|---|
| DO | Zebra Tech / D-Opto; PME / miniDOT; YSI / EXO2 sonde sensor | 2016–2018; 2018 only; 2019–present | Dissolved oxygen is a potential environmental predictor. Three instrument eras are listed; two entries share 2018. Sensor depth, units, exact change dates and cross-calibration are absent. |
| CO2 | Turner Designs / C-sense | 2017–present | Potential carbon/metabolism context. The inventory does not state whether the measured medium is water or air, units, depth, or how output was processed. |
| pH | YSI / EXO2 sonde sensor | 2019–present | Potential water-chemistry predictor; only nominally available from 2019 in this list. |
| fDOM | YSI / EXO2 sonde sensor | 2019–present | Potential dissolved-organic-matter predictor; excitation/emission, units, sensor depth and QC are not listed. |
| Turbidity | YSI / EXO2 sonde sensor | 2019–present | Potential optical/water-quality predictor; units and sensor position are missing. |
| Chlor/Phyco | Turner Designs / Cyclops; YSI / EXO2 sonde sensor | 2006–2019; 2019–present | Likely chlorophyll/phycocyanin channels or combined label, but the source does not define channel structure, units, calibration or split. Pigment signals could be predictors/conventional alarms; they are not independent biological ground truth for a pigment-derived outcome. |
| Conductivity | YSI / model blank; YSI / EXO2 sonde sensor | 2006 only; 2019–present | Potential ionic/physical predictor. The inventory has no model for 2006 and no row for 2007–2018; this is an inventory gap, not proof of absent measurements. |
| Water Temp | Apprise Tech / TempLine; RBR / Concerto | 2006; 2007–present | Strong environmental candidate if water depth and quality are known. The inventory suggests successive instrument eras but does not prove uninterrupted records or comparable calibration. |
| Temp/RH | RM Young / 41382; Vaisala / HMP110 | 2006–2017; 2017–present | Air temperature and relative humidity are likely implied; exact variables, units, height and overlap/replacement timing are not specified. |
| Wind | Vaisala / ultrasonic; RM Young / 5106 | 2006–2012; 2013–present | Potential meteorological predictor. Wind height, direction/speed outputs, units and data intervals are absent. |
| IR Skin Temp | Apogee / SI-111 | 2013–present | Likely infrared surface-skin temperature; the target surface, viewing geometry, height and calibration are not documented. |
| PAR-above / PAR-below | Apogee / SQ-110; Apogee / SQ-111 | 2016–present | Potential light forcing/transmission context. Above/below pairing could support an attenuation measure only if simultaneous timestamps, geometry, units, placement and calibration are known. |

The list uses year-only dates. “Present” is copied as written; the file has no explicit inventory-as-of date, month/day boundaries, deployment gaps or confirmation that “present” means valid observations continue through the current date.

## Sensor changes and methodological discontinuities

**Documented facts:** the inventory lists apparent instrument transitions for DO (D-Opto/miniDOT to EXO2 around 2018–2019), chlorophyll/phycocyanin (Cyclops to EXO2 in 2019), water temperature (TempLine in 2006, Concerto from 2007), air temperature/humidity (RM Young to Vaisala in 2017), and wind (Vaisala through 2012, RM Young from 2013). Conductivity has an entry only for 2006 and again from 2019. pH, fDOM and turbidity appear only from 2019; CO2 from 2017; PAR from 2016; IR skin temperature from 2013.

**Interpretation:** these entries identify potential points where units, calibration, response time, sensor depth, firmware, processing or measurement error may change. A single cross-era time series should not be assumed homogeneous without calibration/maintenance records and overlap tests. The 2018 dual DO entries could indicate an overlap, a transition within the year, or coarse year coding; the file cannot distinguish these explanations. The 2017/2019 shared years for meteorological and pigment changes are similarly ambiguous.

**Caution:** no sensor’s listed deployment establishes gap-free operation, successful QC, exact deployment dates, or valid values for the entire year range. Conversely, an absent inventory row does not establish that no measurements exist.

## Comparison with phytoplankton dataset 88.31

The previously documented NTL-LTER 88.31 phytoplankton record is a taxonomic microscopy dataset with cell/natural-unit density and calculated biovolume, collected as a 0–8 m composite at approximately biweekly cadence in peak season and less often outside it. That biology can be compared conceptually with environmental conditions at corresponding sample dates, but this sensor inventory does not verify any actual overlap or common support.

Potentially comparable predictor classes include water temperature, dissolved oxygen, pH, conductivity, turbidity, fDOM, CO2, PAR and meteorological conditions (wind, air temperature/humidity, infrared surface temperature). Their scientific usability depends on finding timestamped sensor observations, exact units and depths, quality flags, deployment coverage, and an explicit mapping from buoy point/depth to the integrated 0–8 m biology. Buoy chlorophyll/phycocyanin may be conventional monitoring predictors, but using them as the independent biological endpoint would be circular or proxy-based. No environmental value should be substituted for microscopy cell density/biovolume.

**Potential calendar-period overlap only:** if 88.31 version 31 ends in 2020 as previously described, several listed sensor eras intersect that broad biology period. Newer sensors listed from 2019 onward have at most nominal 2019–2020 overlap with that version. This is not evidence that measurements exist on the sample dates or that the sensor states are comparable to a 0–8 m composite.

## Verdict

**The inventory establishes a nominal sensor roster and approximate year-level history for 20 records. It supports statements that the buoy program lists these variables/instruments in those years, subject to source ambiguity.** It does **not** establish uninterrupted temporal coverage, valid or complete observations, sampling cadence, sensor depth, exact locations, data units, calibration, missingness, QA/QC, cross-instrument continuity, or any biological event information. It cannot establish adequate paired exposure or readiness for a confirmatory comparison.

**Next evidence required:** a source-linked deployment/maintenance and calibration history; sensor data dictionaries and units; per-channel timestamp/QC/availability summaries; sensor depths and coordinates by period; transition/overlap validation for replacement instruments; and an exact date/depth/position crosswalk to 88.31 sample records. These are recommendations only; no such material was acquired in this read-only review. Gate 2 remains PAUSED / NOT APPROVED.
