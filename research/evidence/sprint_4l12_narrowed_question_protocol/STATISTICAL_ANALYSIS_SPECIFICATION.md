# Statistical Analysis Specification

**Sprint:** 4L.12  
**Status:** PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Date:** 2026-11-24

> **No analysis may begin until this protocol has been reviewed and explicitly approved. This document specifies future analyses; it does not perform them.**

## 1. Purpose

This document specifies the descriptive statistical analysis for the narrowed measurement/comparability question. It is deliberately limited.

The analysis is **descriptive**, not confirmatory. It estimates rank associations and their descriptive uncertainty. It does **not** test hypotheses, fit predictive models, optimise thresholds, or validate sensors.

## 2. Analysis principles

1. **Date is the unit of analysis.** Never use 1-minute or 10-minute sensor readings as independent observations.
2. **Four primary estimands, fixed in advance.** All other analyses are secondary/exploratory.
3. **Spearman’s ρ is the primary statistic.** Pearson is secondary and only on a pre-specified log scale.
4. **No p-values, no statistical significance, no hypothesis tests.**
5. **No absolute agreement, Bland–Altman, concordance correlation, calibration, or prediction.**
6. **No pooling across lakes, instruments, or depth classes.**
7. **Report every estimate, including null/negative/weak results.** Do not select the most favourable pigment, season, or window.
8. **No thresholds or cut-offs.** No bloom threshold, RFU cut-off, “strong/weak” label, or optimized matching window.
9. **Uncertainty is descriptive.** Bootstrap intervals are labelled as such and are not population confidence claims.

## 3. Primary estimands

| ID | Lake | Era | Sensor | Biological endpoint | Max n | Statistic |
|---|---|---|---|---|---:|---|
| P1 | Mendota | Turner 2006–2019 | Chlorophyll RFU | Cyanobacteria biovolume (0–8 m) | 128 | Spearman ρ |
| P2 | Mendota | Turner 2006–2019 | Phycocyanin RFU | Cyanobacteria biovolume (0–8 m) | 139 | Spearman ρ |
| P3 | Buffalo Pound | YSI 6600 2018–2019 | Chlorophyll RFU | Cyanobacteria biomass (0.8 m) | 42 | Spearman ρ |
| P4 | Buffalo Pound | YSI 6600 2018–2019 | Phycocyanin RFU | Cyanobacteria biomass (0.8 m) | 42 | Spearman ρ |

The n values are upper bounds under the strict 4L.10 “unflagged only” rule. The primary QC rule may retain `H` values, so the final n may be larger. The final n is enumerated before estimation.

## 4. Descriptive summaries

Before any association statistic, produce:

### 4.1 Data flow

- Total biological dates in source.
- Dates inside the analysis window.
- Dates meeting the depth rule.
- Dates with any sensor record.
- Dates with a numeric sensor value.
- Dates passing the primary flag rule.
- Dates passing the Buffalo Pound coverage rule.
- Final primary n per estimand.
- Excluded dates with reasons.

### 4.2 Distributions

For each primary biological and sensor variable, by lake/era:

- n, missing, minimum, 5th percentile, median, 95th percentile, maximum;
- number of zeros and negatives;
- number of flagged values by code;
- sampling interval distribution for the biological series.

These are descriptive summaries, not tests. Do not label values as “blooms,” “outliers,” or “anomalies” unless they are in the anomaly register.

### 4.3 Scatterplots

For each primary estimand:

- scatterplot of sensor daily value (x) vs biological endpoint (y);
- points coloured by season (spring/summer/autumn) and shaped by year where useful;
- no fitted line in the primary figure; a loess smoother may be shown only as a visual aid, clearly labelled “visual smoother, not a model”;
- no log transformation in the primary figure;
- report n in the panel.

Scatterplots are descriptive. A visual pattern is not a hypothesis test.

### 4.4 Time series

For each lake, plot:

- biological endpoint over time (points and connecting line, with gaps visible);
- sensor series over the same dates (separate panel or secondary axis, clearly labelled);
- flag/exclusion markers.

Do not interpolate across gaps. Do not connect across years with a continuous line if that implies continuity.

## 5. Primary statistic: Spearman’s rank correlation

### 5.1 Definition

For each primary estimand, compute Spearman’s ρ between the sensor daily value and the biological endpoint across lake–date observations.

- Use average ranks for ties.
- Use the standard formula with tie correction, or `scipy.stats.spearmanr`.
- Report n, ρ, and a descriptive interval.
- Do not report a p-value.
- Do not describe ρ as “agreement,” “accuracy,” “validation,” or “prediction.”

### 5.2 Why Spearman

- The relationships are expected to be monotonic but not necessarily linear.
- The endpoints are heavy-tailed and may contain extreme values.
- RFU and biovolume/biomass are on different scales; rank association avoids assuming a common linear scale.
- The data have unequal sampling intervals and seasonal structure; a rank statistic is more robust than Pearson to marginal outliers.
- Spearman does not require bivariate normality.

### 5.3 What Spearman does not tell us

- It does not measure absolute agreement.
- It does not measure bias.
- It does not measure predictive accuracy.
- It does not establish causality.
- It does not establish that the sensor is a validated biomass measurement.
- A high ρ can coexist with a large multiplicative bias.

## 6. Secondary linear statistic: log-scale Pearson

### 6.1 Definition

For each primary estimand, compute Pearson’s r on `log10(1 + x)` for both variables, provided the primary values are non-negative. Report r and n. Do not report a p-value.

### 6.2 Why secondary only

- Pearson assumes a linear relationship and is sensitive to outliers.
- The raw relationships are expected to be nonlinear and heteroscedastic.
- The log transform is a pre-specified scale check, not a search for the “best” transformation.
- If the log-Pearson and Spearman results disagree in direction, report the disagreement; do not choose the more favourable statistic.

### 6.3 No other transformations

Do not try square-root, Box–Cox, inverse, or other transformations to improve the correlation. Do not select a transformation after seeing results.

## 7. Agreement, calibration, and prediction: explicitly not assessed

The following are **not** computed:

- Bland–Altman bias and limits of agreement;
- Lin’s concordance correlation coefficient;
- intraclass correlation;
- calibration slope/intercept;
- conversion factor from RFU to biovolume/biomass;
- predictive R², RMSE, MAE, accuracy, sensitivity, specificity, AUC;
- bloom-detection accuracy;
- false-alarm rate;
- lead time.

**Reason:** RFU and biovolume/biomass are different quantities on different scales; there is no validated conversion; the data are not a paired calibration experiment; and the study is not a predictive evaluation.

If a reviewer requires an agreement statistic, the correct response is that the data cannot support one, not that a correlation should be relabelled as agreement.

## 8. Uncertainty

### 8.1 Mendota: year-cluster bootstrap

- Resample years with replacement (up to 14 Turner-era years; a year with fewer than two primary dates cannot contribute and is reported).
- Within each selected year, include all primary dates for that year.
- Compute ρ on the pooled resampled dates.
- Repeat 2,000 times.
- Report the 2.5th and 97.5th percentiles as a **descriptive 95% bootstrap interval**.
- If a resampled sample has fewer than 10 dates or no variation, discard that replicate and report the number of valid replicates.
- This interval respects within-year dependence but not full within-season autocorrelation. State that limitation.

### 8.2 Buffalo Pound: date-level bootstrap and year separation

- Resample dates with replacement (42 dates; or the final primary n).
- Compute ρ; repeat 2,000 times; report the 2.5th and 97.5th percentiles.
- Label this a **naive date-level interval**, likely too narrow because dates are serially dependent and come from only two years.
- Also report ρ separately for 2018 and 2019 (leave-one-year-out descriptive stability check), with n for each.
- Do not use the naive interval to claim precision.

### 8.3 Small strata

- If a stratum has n < 10, do not compute a stratum-specific ρ. Show the points, n, and a note that the stratum is too small for a stable rank correlation.
- This is a reporting rule, not an ecological threshold.

### 8.4 No p-values

Do not report p-values, asterisks, “significant,” “non-significant,” or “trend toward significance.” The analysis is descriptive. A bootstrap interval that includes zero is not a “non-significant result”; it is a description of uncertainty.

## 9. Seasonal analysis

### 9.1 Season definition

Use calendar seasons:

- Spring: March–May.
- Summer: June–August.
- Autumn: September–November.
- Winter: December–February.

The data are predominantly open-water; winter is absent or very sparse. Report winter n; if n < 10, show points only.

### 9.2 Primary seasonal question

For each primary estimand, compute ρ within each season with n ≥ 10. Report:

- n per season;
- ρ per season;
- descriptive interval only if the stratum has enough clusters/dates for the bootstrap;
- a note that seasonal strata are observational, not randomized.

### 9.3 No interaction test

Do not test a season × sensor interaction. Do not claim that a seasonal difference is statistically significant. Describe the pattern and its consistency across sensitivity analyses.

### 9.4 Lake-specific open-water windows

As a sensitivity, repeat the seasonal analysis using:

- Mendota: ice-off to November (the buoy deployment season).
- Buffalo Pound: May–October (the biological season).

This checks whether calendar-season results are driven by the arbitrary season boundaries.

## 10. Sensor-era analysis

### 10.1 Mendota

- Turner era: 2006–2019; P1/P2.
- YSI era: 2019–2020; Q1.
- 2019 transition: both instruments may have values on the same biology date. Compute each separately. Do not average.
- Report Turner and YSI side by side. Do not fit a conversion.

### 10.2 Buffalo Pound

- One shallow YSI 6600 era: 2018–2019.
- Do not treat 2018 and 2019 as instrument eras; they are biological years with the same shallow sonde family.
- Do not use the deep YSI 6920 as a second era.

### 10.3 No era pooling

Never concatenate Turner and YSI in one correlation. Never concatenate Mendota and Buffalo Pound instruments.

## 11. Secondary and exploratory analyses

These are pre-specified but subordinate. They must be labelled “secondary” or “exploratory” in every table and figure.

| ID | Analysis | Statistic | Status |
|---|---|---|---|
| Q1 | Mendota YSI chlorophyll/phycocyanin vs biovolume, 2019–2020 | Spearman ρ; n ≈ 21/22 | Secondary; small n |
| Q2 | Cyanobacteria cell density vs pigments, both lakes | Spearman ρ | Secondary |
| Q3 | Total phytoplankton biovolume/biomass vs chlorophyll, both lakes | Spearman ρ | Secondary |
| Q4 | Non-cyanobacteria biovolume/biomass vs chlorophyll, both lakes | Spearman ρ | Secondary |
| Q5 | Phycocyanin vs chlorophyll as cyanobacteria indicators | Side-by-side ρ; no formal test | Secondary |
| Q6 | Seasonal variation of P1–P4 | Stratified ρ | Secondary |
| Q7 | Turner vs YSI same-day descriptive comparison, Mendota 2019 | Ratios, ranks, n; no calibration | Secondary |
| Q8 | Genus-specific subsets | Spearman ρ only if an approved crosswalk exists | Exploratory; not approved |
| Q9 | Relative concordance of first differences | Proportion of concordant signs; n pairs | Exploratory |
| Q10 | Cross-lake side-by-side comparison | Descriptive table; no pooled statistic | Exploratory |

### 11.1 Relative concordance (Q9)

For consecutive biological dates within the same year and season:

- compute the sign of the change in the biological endpoint;
- compute the sign of the change in the sensor daily value between the same two dates;
- count concordant pairs (excluding zero changes);
- report the proportion and the number of pairs.

This is an **exploratory** measure of directional correspondence. It is not agreement, not prediction, and not a test. Irregular intervals mean the magnitude of change is not comparable across pairs; only the sign is used.

### 11.2 Genus-specific subsets (Q8)

Not approved. If a dated crosswalk is later approved, genus-level analyses remain exploratory and must report the mapping, the number of taxa affected, and the taxonomic uncertainty. Do not infer toxicity from genus.

## 12. Dependence and autocorrelation

- Biological observations are serially dependent within seasons and years.
- Sensor daily values are autocorrelated.
- The effective sample size is closer to the number of independent sampling occasions than to the number of days.
- Do not treat 42 Buffalo Pound dates as 42 independent events across two years; they are 42 sampling dates within two seasons.
- Do not treat 128 Mendota dates as 128 independent draws across 14 years; they are clustered by year and season.
- The year-cluster bootstrap (Mendota) and year-separated estimates (Buffalo Pound) are the minimum dependence adjustments.
- No formal autocorrelation correction, generalized least squares, mixed model, or time-series model is proposed. Those would be models, and the study is descriptive.
- Report the lag-1 autocorrelation of the biological series and sensor series as a descriptive diagnostic, not as a model input.
- If the lag-1 autocorrelation is high, state that the descriptive intervals are likely too narrow.

## 13. Missingness and selection

- No imputation.
- Report the missingness taxonomy and flow table.
- Compare included vs excluded dates by year and month, and by the available biological endpoint, descriptively.
- Do not test whether included and excluded dates differ.
- Discuss MNAR risks: bloom-targeted sampling, fouling-related failures, seasonal deployment, depth mismatch, taxonomic selection, instrument transitions, date-only sampling.
- The observed association applies to the included dates, not to all days in the lake.

## 14. Multiplicity and pre-specification

- Four primary estimands.
- No p-values, so no alpha correction.
- The risk is **selective emphasis**, not Type I error. It is controlled by:
  - fixing the four primary estimands before analysis;
  - reporting all estimates, including null/negative results;
  - labelling all secondary/exploratory analyses;
  - not selecting the “best” pigment, season, window, or transformation for the headline;
  - reporting sensitivity analyses alongside the primary.
- Do not run a grid of correlations and report only the largest.

## 15. Small sample sizes

- Mendota Turner: max 128/139 dates over 14 years.
- Mendota YSI: max 21/22 dates over 2 years.
- Buffalo Pound: max 42 dates over 2 seasons.
- Seasonal strata: often 10–20 dates; winter near zero.
- Precision is limited. Report n and intervals; do not overinterpret.
- No power calculation is proposed, because the study is descriptive and there is no hypothesis test.
- If n is too small for a stable estimate, say so. Do not substitute a different endpoint or window to increase n.

## 16. Sensitivity analyses

Every primary estimand must be reported under the following pre-specified sensitivities:

| Sensitivity | Rule | Purpose |
|---|---|---|
| S-A | Strict unflagged: exclude all flags, including `H` | Matches 4L.10 counts; tests whether `H` retention matters |
| S-B | Flagged-inclusive: include `C`/`E`/`G` numeric values if physically plausible | Tests whether flag exclusion drives the result |
| S-C | Negative-inclusive: include negative pigment values | Stress test; not a valid primary |
| S-D | ±1-day window | Tests date-matching sensitivity |
| S-E | Buffalo Pound B7-inclusive | Tests fouling exclusion |
| S-F | Buffalo Pound 2019-07-17 excluded | Tests single-date anomaly leverage |
| S-G | Buffalo Pound replicate sum / first row | Tests unresolved replicate structure |
| S-H | Mendota station-1 subset | Tests station metadata sensitivity, if n permits |
| S-I | Lake-specific open-water season | Tests calendar-season boundary sensitivity |
| S-J | Log-Pearson | Tests linearity/scale sensitivity |

Do not add a sensitivity analysis after seeing the primary result unless it is reported as post hoc and its status is explicit.

## 17. No thresholds or optimisation

- No bloom/non-bloom threshold.
- No RFU cut-off.
- No “low/high biomass” grouping.
- No optimized matching window.
- No optimized pigment ratio.
- No optimized seasonal boundary.
- No model selection, hyperparameter tuning, or cross-validation.
- No “best” subset selected to maximize ρ.

If a reviewer asks for a threshold-based analysis, the response is that thresholds are outside the approved scope and would require a separate protocol and independent event definition.

## 18. Software and reproducibility

### 18.1 Environment

- Python 3.11+ with pandas, numpy, scipy, matplotlib; or R 4.4+ with base stats and ggplot2.
- Record exact versions in `session_info.txt`.
- No notebooks with hidden state; scripts only.
- Raw data read-only.
- Derived tables and figures written to a separate output directory; SHA-256 registered.

### 18.2 Script order

1. `01_load_and_validate.py` — verify file hashes, schema, dates, duplicates; no analysis.
2. `02_build_analysis_populations.py` — apply inclusion/exclusion, QC, matching; write flow table and date lists.
3. `03_descriptive_summaries.py` — distributions, missingness, intervals.
4. `04_primary_associations.py` — Spearman, bootstrap, log-Pearson.
5. `05_secondary_exploratory.py` — Q1–Q10.
6. `06_sensitivity.py` — S-A to S-J.
7. `07_figures.py` — scatterplots, time series.
8. `08_report_tables.py` — final tables.

### 18.3 Analysis lock

- After approval, the protocol and scripts are frozen.
- Any deviation is recorded in `DEVIATIONS_LOG.md` with date, reason, and impact.
- A deviation that changes an estimand, endpoint, or inclusion rule requires renewed human approval.
- The final report must include a “deviations from protocol” section, even if empty.

### 18.4 Code review

- A second person reviews the analysis scripts before execution.
- The reviewer checks: no Turner/YSI concatenation; no cross-lake pooling; no sensor-reading-level n; no p-values; no threshold optimisation; correct flag handling; correct date parsing; correct bootstrap unit.

## 19. Interpretation limits

- ρ is a rank association, not agreement.
- ρ is not a calibration.
- ρ is not a prediction.
- ρ is not causal.
- A positive ρ does not mean the sensor is a validated biomass measure.
- A negative or near-zero ρ does not mean the sensor is useless; it may mean the sensor is measuring a different quantity, depth, or community.
- Seasonal and era differences are observational.
- Cross-lake differences are confounded by lake, period, instrument, community, sampling, and endpoint.
- Results apply to the included dates, not to all days or all lakes.

## 20. Reporting checklist

The final analysis report must contain:

- [ ] Data flow table from source dates to primary n.
- [ ] Flag/missingness table by variable, year, season.
- [ ] Included vs excluded comparison.
- [ ] Descriptive statistics for all primary variables.
- [ ] Scatterplots for P1–P4.
- [ ] Time-series plots for each lake.
- [ ] Spearman ρ table for P1–P4 with n and descriptive interval.
- [ ] Log-Pearson table for P1–P4.
- [ ] Seasonal ρ table.
- [ ] Era comparison table.
- [ ] Secondary/exploratory tables, clearly labelled.
- [ ] Sensitivity table S-A to S-J.
- [ ] Anomaly list.
- [ ] Calibration/detection-limit statement.
- [ ] Claims matrix compliance check.
- [ ] Deviations log.
- [ ] Session info and SHA-256 register.

## 21. Governance

- **Gate 2 remains PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- No correlation, plot, model, hypothesis test, threshold, or derived dataset is produced in this sprint.
- No analysis may begin until the protocol is reviewed and explicitly approved.
