# Bootstrap and Dependence Review

**Sprint:** 4L.13  
**Status:** INDEPENDENT REVIEW — NOT APPROVAL  
**Protocol reviewed:** Sprint 4L.12, PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

> **This review does not approve the protocol or authorise analysis.**

## 1. The protocol’s proposal

The 4L.12 protocol proposes:

- **Mendota:** year-cluster bootstrap, resampling years with replacement, 2,000 replicates.
- **Buffalo Pound:** date-level bootstrap, 2,000 replicates, labelled “naive” and “anti-conservative”; plus separate 2018/2019 estimates.
- **Small strata:** no ρ if n < 10.
- **No p-values.**

The protocol correctly recognises temporal dependence and avoids p-values. The proposed resampling schemes, however, do not match the dependence structure well enough to justify the intervals as stated.

## 2. Why independence fails

### 2.1 Temporal autocorrelation

Biological observations are serially dependent:

- Mendota: median interval 14 days; seasonal cycle; multi-year trends.
- Buffalo Pound: median 4/8 days; two seasons; bloom phases.

Sensor daily values are also autocorrelated. Two dates close together are more similar than two dates far apart. An i.i.d. bootstrap over dates treats them as exchangeable and understates uncertainty.

### 2.2 Seasonal clustering

Both lakes have strong seasonal structure:

- Mendota: spring mixing, summer stratification, autumn turnover; winter ice.
- Buffalo Pound: shallow polymictic; spring/early summer and autumn bloom phases.

Dates within a season share drivers; dates across seasons do not. A bootstrap that ignores season mixes distinct states.

### 2.3 Unequal sampling

Mendota has 13–19 dates/year, uneven across seasons. Buffalo Pound has 25 dates in 2018 and 17 in 2019. The number of observations per year/season varies. Resampling dates or years changes the seasonal weighting.

### 2.4 Repeated sensor readings

The protocol correctly aggregates sensor readings to daily values. The remaining dependence is at the date level, not the minute level. This is a strength.

### 2.5 Missingness

Missingness is not random:

- sensor failures and fouling may coincide with high biomass;
- sampling may target blooms;
- winter is structurally absent.

A bootstrap cannot fix MNAR. It can only describe the included dates.

## 3. Mendota year-cluster bootstrap: critique

### 3.1 What it assumes

Resampling years with replacement treats the 14 Turner-era years as exchangeable clusters drawn from a superpopulation of years. The correlation is recomputed on the pooled resampled dates.

### 3.2 Why that is questionable

1. **Years are not exchangeable.** 2006–2019 includes sensor changes, calibration changes, different sampling frequencies, different seasonal coverage, and likely trends in lake condition. Resampling years mixes different regimes.
2. **Few clusters.** Fourteen clusters is a small number for cluster bootstrap; the bootstrap distribution is coarse and may be unstable. The cluster-bootstrap literature warns that few clusters can produce poor coverage (Cameron, Gelbach & Miller 2008; Field & Welsh 2007; MacKinnon, Nielsen & Webb 2023).
3. **Correlation is not a cluster-mean parameter.** Cluster bootstrap is most natural for statistics that aggregate cluster-level means. A pooled correlation is a nonlinear function of the joint distribution; resampling years changes the mix of within-year ranges and seasonal coverage, not just the sampling noise.
4. **Unequal cluster sizes.** Years have different n and different seasonal coverage. Resampling years with replacement gives unequal weight to years and can distort the seasonal composition.
5. **Within-year dependence remains.** Dates within a year are still autocorrelated; the year cluster captures some but not all dependence.
6. **Bootstrap interval is not a confidence interval.** The protocol calls it “descriptive,” which helps, but readers may still interpret it as a confidence interval.

### 3.3 Is there a better approach?

Options:

**(a) No interval; report a leave-one-year-out range.**
- Compute ρ with each year removed; report the minimum, maximum, and maybe median.
- This is transparent and does not pretend to a sampling distribution.
- It shows whether one year dominates.
- It is not a confidence interval.

**(b) Season-year block bootstrap.**
- Define blocks as year × season (e.g., 2006 spring, 2006 summer, ..., 2019 autumn).
- Resample blocks with replacement; preserve within-block order.
- This respects seasonal structure better than year-only resampling.
- With ~42 blocks, the bootstrap is still coarse, but more plausible than 14 years.
- It still assumes block exchangeability, which is questionable across years.

**(c) Moving-block bootstrap on the date series.**
- Resample contiguous blocks of dates with a pre-specified block length.
- Preserves local autocorrelation.
- Requires a regular or near-regular series; the dates are irregular and seasonal.
- Block length choice is arbitrary; sensitivity to block length is likely.
- Not recommended as primary.

**(d) Effective sample size / autocorrelation adjustment.**
- Pyper & Peterman (1998) review methods to adjust correlation tests for autocorrelation; Ólafsdóttir & Mudelsee (2014) provide calibrated bootstrap intervals for correlation between time series.
- These methods are designed for regular time series and often for Pearson correlation; applying them to irregular, seasonal, gappy data is not straightforward.
- Not recommended without a dedicated methodological justification.

### 3.4 Review recommendation

For Mendota:

- report ρ, n, number of years, and **leave-one-year-out range**;
- optionally report a **season-year block bootstrap** as a descriptive sensitivity, clearly labelled “descriptive, not a confidence interval”;
- do not present the year-cluster bootstrap as the primary uncertainty statement;
- state that the interval is approximate and that years are not exchangeable.

## 4. Buffalo Pound date-level bootstrap: critique

### 4.1 What it assumes

Resampling dates with replacement treats the 42 dates as exchangeable draws. The protocol labels the interval “naive” and “likely too narrow,” which is honest but not sufficient.

### 4.2 Why it is not defensible

1. **Two seasons only.** The dates come from 2018 and 2019. There is no superpopulation of seasons to resample. A date-level bootstrap cannot represent between-season variability.
2. **Serial dependence.** Dates within a season are autocorrelated; resampling individual dates breaks the temporal structure and understates uncertainty.
3. **Bloom-phase structure.** 2018 and 2019 have mid-summer and autumn bloom phases; resampling dates mixes phases and can create implausible samples.
4. **Small n.** 42 dates is small; bootstrap percentile intervals are unstable.
5. **Year-cluster bootstrap impossible.** With two clusters, resampling years gives only a few distinct resamples; the bootstrap distribution is degenerate/coarse.
6. **Season-block bootstrap weak.** Two seasons per year gives four blocks; too few for stable resampling.
7. **No reliable interval.** The data cannot support a defensible frequentist interval for ρ without strong assumptions.

### 4.3 What can be reported instead

- ρ for all 42 dates (or final n);
- ρ for 2018 and 2019 separately;
- leave-one-year-out values (2018-only, 2019-only);
- leave-one-date-out range (min/max), which shows sensitivity to individual dates;
- a clear statement: **“No reliable interval can be estimated from two seasons; the estimate is descriptive and its uncertainty is not quantified by a bootstrap.”**

The leave-one-date-out range is not a confidence interval; it is a sensitivity range. It is more honest than a naive bootstrap.

### 4.4 Review recommendation

**Do not report a Buffalo Pound bootstrap interval.** Replace D-10 with:

> For Buffalo Pound, report ρ, n, separate 2018/2019 estimates, and a leave-one-date-out sensitivity range. State that the two-season design cannot support a reliable interval. Do not use a date-level bootstrap as a primary uncertainty statement.

## 5. Small strata and n < 10

The protocol’s rule “no stratum ρ if n < 10” is reasonable as a reporting rule. It is not an ecological threshold; it is a stability guard.

However:

- n = 10 is still very small for a rank correlation; the estimate can be dominated by one or two points.
- The rule should be paired with a requirement to show points and n, not just suppress the statistic.
- The overall estimand also needs a minimum-n rule; the protocol currently has none.
- The minimum should be set by the statistical reviewer after the count audit, before estimation.

## 6. What would be needed for reliable interval estimation

A defensible interval would require:

- more independent seasons/years (e.g., ≥10 seasons with comparable sampling);
- a pre-specified dependence model (block structure, autocorrelation length);
- a simulation/coverage study for the proposed bootstrap;
- a clear target parameter (e.g., correlation in a superpopulation of seasons);
- regular sampling or a justified irregular-series method.

The current data do not meet these conditions, especially for Buffalo Pound.

## 7. Methodological sources

The review used the following methodological literature (details in `SOURCE_REGISTER.md`):

- Cameron, Gelbach & Miller (2008), *Bootstrap-Based Improvements for Inference with Clustered Errors*, Review of Economics and Statistics 90:414–427.
- Field & Welsh (2007), *Bootstrapping Clustered Data*, JRSS B 69:369–390.
- MacKinnon, Nielsen & Webb (2023), *Cluster-robust inference: A guide to empirical practice*, Journal of Econometrics 232:272–299.
- Politis & Romano (1994), *The Stationary Bootstrap*, JASA 89:1303–1313.
- Künsch (1989), *The Jackknife and the Bootstrap for General Stationary Observations*, Annals of Statistics 17:1217–1241.
- Ólafsdóttir & Mudelsee (2014), *More accurate, calibrated bootstrap confidence intervals for estimating the correlation between two time series*, Mathematical Geosciences 46:411–427.
- Pyper & Peterman (1998), *Comparison of methods to account for autocorrelation in correlation analyses of fish data*, Canadian Journal of Fisheries and Aquatic Sciences 55:2127–2140.
- Efron & Tibshirani (1993), *An Introduction to the Bootstrap*.
- Davison & Hinkley (1997), *Bootstrap Methods and Their Application*.

These sources support the general concerns; they do not provide a ready-made solution for two-season, irregular, seasonal data.

## 8. Findings

| ID | Finding | Severity |
|---|---|---|
| C1 | The protocol correctly recognises temporal dependence and avoids p-values | Pass |
| C2 | Mendota year-cluster bootstrap is questionable with 14 non-exchangeable years | **Major** |
| C3 | Buffalo Pound date-level bootstrap cannot support a reliable interval | **Critical** |
| C4 | The protocol labels the BP interval “naive” but still reports it | Major |
| C5 | Small-stratum rule is reasonable but insufficient for overall n | Moderate |
| C6 | No coverage/simulation evidence for the proposed bootstrap | Major |
| C7 | A leave-one-year-out/leave-one-date-out range would be more honest | Recommended |

## 9. Governance

- **Protocol: PROPOSED — NOT APPROVED.**
- **Gate 2: PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- No decision is approved by this review.
- No analysis is authorised until the required revisions and D-15 approval are recorded.
