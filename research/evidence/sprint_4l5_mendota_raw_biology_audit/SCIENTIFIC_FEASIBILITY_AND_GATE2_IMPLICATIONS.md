# Scientific Feasibility and Gate 2 Implications

**Date:** 2026-11-24T07:23:09.883291+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## What became stronger

- The raw file contains 18,654 records and 402 Mendota sampling dates across 1995–2020, not merely metadata claims.
- 13–19 Mendota dates/year, median gap 14 days, make seasonal/multi-week comparisons possible.
- Species-level microscopy with cell density, biovolume and biomass is a genuine independent biological endpoint.
- Cyanobacteria are abundant and identifiable at division level (8,581 records, 127 taxa, 73.2% of summed biovolume).

## Assumptions confirmed

- Four Madison lakes; Mendota is the main record.
- Mendota samples are predominantly 0–8 m composites.
- Sampling is biweekly-ish in the ice-free season, monthly/less in winter.
- The 2013 taxonomic update is real, and same-species/date multiple rows occur.
- No QC flags or detection limits are present in the schema.

## Assumptions contradicted or weakened

- **Depth assignments are not perfectly consistent:** 40 ME 0–2m records (2002), 310 MO 0–8m records (1995/2002–2004).
- **Station IDs are mostly absent:** `sta` blank for 17,518/18,654 rows; only 2011–2012 ME and 2011 MO have `sta=1`.
- **Relative total biovolume is not uniformly a 100% composition:** 14 groups sum ~200; 3 sum 0; one outlier 283,806.87.
- **Biomass is not a clean derived field at low values:** 61 rows have biomass=0 with positive biovolume; one catastrophic Coelastrum row.
- **Taxonomy is not longitudinally stable:** 204 pre-only names, 72 post-only, 889 genus-field mismatches, transitions across 2008–2020.
- **The four-lake record is not balanced:** WI 23 dates (1996–2002), FI 1 date (1995); MO missing 2012 and sparse in 2020.

## What remains unknown

- Exact sample times and field protocol; whether all Mendota samples are 0–8 m composites.
- Why depth labels contradict metadata in 2002–2004.
- Why relative totals sum to 200 in 14 groups; whether this is aggregation/denominator/rounding.
- Whether the Coelastrum row and Actinastrum extreme are data-entry/unit errors.
- Taxonomic crosswalk/QA and detection limits; whether later taxonomist changes occurred.
- Sensor data, QC/calibration, per-channel coverage, and exact station/depth correspondence.

## Claims that could reasonably be supported (exploratory, no labels)

- Descriptive seasonal/multi-week associations between environmental variables and **cyanobacteria biovolume** or cell density.
- Independent validation/calibration of sensor chlorophyll/phycocyanin proxies against microscopy.
- Characterization of biological variability, measurement uncertainty, and sampling requirements.
- Hypothesis generation about lead times at seasonal/multi-week scales.

## Claims that would exceed the evidence

- Daily/hours-to-days early warning.
- Bloom/non-bloom event prediction or a confirmatory matched-FAR evaluation.
- A stable species-level long-term trend without a crosswalk.
- Treating 0.5 m sensor values as the 0–8m composite.
- Treating WI/FI as comparable multi-lake replicates.
- Claiming the dataset passed Gate 2.

## Potentially fatal limitations

- **Depth mismatch** (0–8m composite vs point sensors) is first-order for any sensor–biology relationship.
- **14-day biological cadence** cannot resolve short-lived bloom onset; it limits warning claims to seasonal/multi-week.
- **Taxonomic non-stationarity** undermines species-level longitudinal comparisons unless harmonized.
- **No verified non-bloom labels** prevents a confirmatory event/non-event evaluation.

These are not fatal to exploratory seasonal analysis, but they are fatal to a confirmatory early-warning claim in the current form.

## Further evidence that would change the assessment

- Field sample times, depth protocol and station logs.
- A validated taxonomic crosswalk plus QC/detection limits.
- Sensor daily/hourly data with flags, calibration and sensor-era mapping.
- Resolution of depth/relative/biomass anomalies.
- Protocol-approved event/non-bloom definitions and a matched-FAR/leakage-resistant design (Gate 2).

## Verdict

**Mendota remains a viable exploratory candidate, not a confirmatory one.** The raw data strengthen its biological value but expose substantial comparability limits. Gate 2 remains PAUSED / NOT APPROVED.
