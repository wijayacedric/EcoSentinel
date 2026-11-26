# QC and Missingness Independent Audit

## Overall verdict

The 4L.14 QC specification is substantially clearer than 4L.12 and appropriately preserves raw data, avoids imputation, names many flag codes, and does not automatically interpret `H` as invalid. It is **not yet a scientifically justified decision tree**. Reproducibility of a decision does not establish validity of that decision.

## Mendota

The 4L.9 raw audit documents `C` as sensor-off, `E` noisy/malfunctioning, `G` suspected biofouling, `H` outside standard range, and `O` undefined; it also finds undocumented flag values in several columns and many missing values with no flag. Numeric values with flags are common. This supports reporting the original flag and a conservative primary rule, but not assuming all flagged values are unusable or all unflagged values are valid. `G` appearing in YSI but not Turner does not establish that Turner data are free of fouling. The specified `SENS_E/G/C` “include if finite” analyses could knowingly include invalid values; name them diagnostics, not equivalent alternative datasets.

`H` retention within broad bounds preserves possible high bloom signals, but 4L.14 presents the broad bounds without a source-backed instrument or validation basis for every variable. For RFU, no Mendota upper limit is supported by this documentation. For physical variables not used in P1/P2, the bounds are largely irrelevant to primary inference and should not be presented as observed quality validation. Undefined `O` and undocumented flags should stay unresolved pending a source definition; blanket sensitivity inclusion is not scientifically informative unless separately labeled.

Negative RFU can occur due to baseline correction/noise. Keeping it as an ordinary numeric rank preserves recorded output but silently assumes rank ordering below zero has meaning for biomass. Excluding it can truncate low observations. Neither is justified by current instrument metadata. Better treatment is to mark as below/around baseline and obtain manufacturer/processing documentation; if unavailable, show results with and without as a sensitivity and avoid interpreting negative values as concentration or zero biomass.

The biology endpoint itself may contain zeros/non-detections and missing taxon records; the proposed missingness taxonomy does not establish which are true zeroes. That distinction changes the target population materially.

## Buffalo Pound

The data documentation describes `M` as missing/failure and `C` as faulty/unrealistic. `B7` covers an interval between service visits where fouling was identified. Excluding B7 is plausible for sensor quality, but the interval may overlap high biomass or particular seasonal phases. Without the authorized overlap audit, neither direction nor magnitude of selection is known. Do not claim that its sensitivity will remove bias; it only exposes dependence on the disputed interval.

The 0–100 RFU operating range is cited by the BP data paper; retaining values above it as “above range” while treating them as primary risks keeping saturated or uninterpretable readings. A primary rule should follow the data documentation/manufacturer definition of “range” and whether the range means expected signal, output scale, or measurement limit. Until resolved, >100 is unresolved, not demonstrably a valid rank.

### Daily coverage rule

The 50%/two-half rule is the largest QC concern. The raw BP audit found per-day counts vary (2018 range 121–144; 2019 42–131), so 144 may not be the correct expected denominator for every date/collection period. Requiring ≥72 of 144 could reject days with valid shorter deployment windows, or accept a day with only half-day coverage. At least one observation in each half does not represent the full-day distribution. Daily means over different time windows may not be comparable and differ from Mendota provider daily summaries with undocumented within-day counts. Coverage may correlate with maintenance, fouling, weather or field sampling. Do not approve this rule without establishing deployment schedule, timestamps/time zone, expected interval by date, and a reasoned measure of temporal coverage.

## Missingness reporting

The categories structural/temporal/equipment/QC/biological/analytical/unknown are useful as an initial scheme, but flags alone cannot distinguish all causes. The first-reason hierarchy can hide co-occurring reasons; retain a multi-reason record and report each category. The planned included-vs-excluded biological distributions are helpful, but should be described only after authorization and cannot prove missing-at-random assumptions.

## Must revise

1. Document sensor-specific meaning and range of negative/above-range fluorescence.
2. Revisit 50% coverage against date-specific expected intervals and daily-mean representativeness.
3. Keep B7 overlap unresolved until approved review; do not presume the exclusion is unbiased.
4. Verify all flag codes against original EML/data dictionary, distinguish missing from flagged numeric values, and retain multi-reason exclusions.
5. Clarify biological zeros, absent rows and taxonomic non-detections.
6. State that this QC system defines an analysis population, not “clean/true” measurements.

