# Evidence Limitations — Sensor Inventory

## Source boundary

This review used the complete named source file only, plus the already documented NTL-LTER phytoplankton dataset description for conceptual compatibility. It did not read Sprint 4L.1 outputs, fetch other datasets, or inspect raw sensor or biological records.

Source size is 1,039 bytes; SHA256 is `255dc9a279f1acb4a3588f697e91f206c5466b9ef2c47166b9b6204002b117d5`. The CSV has 20 sensor entries. The transcription records the source values; it does not add inferred fields.

## Evidence this file lacks

- Exact dates, days/months, time zone, coordinates, mooring location changes or station/depth for each instrument.
- Sample/record interval, data file names, raw measurements, record counts, completeness, uptime, gaps, detection limits, or missing-value conventions.
- Sensor service, calibration, fouling, factory changes, firmware, maintenance, QC flags, accuracy, precision, units or uncertainty.
- Whether replacement sensors were deployed in parallel, whether sensors overlap, and whether measurements were cross-calibrated.
- Semantics of ambiguous labels (`Chlor/Phyco`, `Temp/RH`, `IR Skin Temp`, `CO2`), measured medium/units, or how any derived products were calculated.
- A timestamped join to NTL-LTER phytoplankton samples, the depth of the biological composite by sample, or an eligible non-event observation period.
- Any biological measurement, taxonomic identity, cyanobacterial cell density, biovolume, bloom onset, event status, or toxin concentration.

## Specific ambiguities

- DO has three records, including two instruments within the calendar year 2018 and a new EXO2 row from 2019. Exact transition/overlap cannot be inferred from year labels.
- Chlor/Phyco changes from Cyclops through 2019 to EXO2 from 2019; overlapping year may hide sequence, parallel operation or mixed processing.
- Conductivity is listed in 2006 with no model and then 2019–present. The absence of 2007–2018 entries does not prove data were absent.
- Water Temp, Temp/RH and Wind have apparently consecutive or overlapping year boundaries but not exact dates.
- `present` has no inventory version date. It should not be read as proof of current continuous operation.
- Several values are combined names or broad labels. For example, the file does not state whether “Chlor/Phyco” represents two channels, combined outputs, or their units.

## Interpretation boundary

Statements about possible environmental predictors are hypotheses about variable relevance, not findings about data availability or effect. Comparing sensor histories with 88.31 requires actual timestamped values, sample support, units and QC. Sensor fluorescence cannot become independent biological ground truth merely because it covaries with microscopy. No assessment of actual missingness, event exposure, warning performance or Gate 2 readiness can be made from the inventory alone.
