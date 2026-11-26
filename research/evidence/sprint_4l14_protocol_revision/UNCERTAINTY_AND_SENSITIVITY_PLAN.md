# Uncertainty and Sensitivity Plan

**Sprint:** 4L.14  
**Status:** PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Date:** 2026-11-24

> **No analysis is authorised. This is a plan for descriptive sensitivity reporting, not a calculation.**

## 1. Purpose

This document implements Sprint 4L.13 revision R-04. It replaces the original bootstrap plan with a defensible descriptive approach that does not claim more precision than the data support.

The key distinction:

- a **confidence interval** is an inferential statement about a target parameter;
- a **descriptive sensitivity range** describes how an estimate changes under pre-specified resampling/leave-one-out schemes.

The revised protocol reports **descriptive sensitivity ranges**, not confidence intervals, unless a future approved method justifies otherwise.

## 2. Why the original bootstrap plan is revised

### 2.1 Mendota

The original plan used a year-cluster bootstrap with 14 Turner-era years.

Problems:

- years are not exchangeable (sensor era, sampling, seasonal coverage, climate, lake condition);
- 14 clusters is few; the bootstrap distribution is coarse;
- cluster bootstrap is most natural for cluster-level means, not a pooled rank correlation;
- unequal within-year n and seasonal coverage can distort the resampled composition;
- within-year autocorrelation remains;
- the result may look like a confidence interval even if labelled descriptive.

### 2.2 Buffalo Pound

The original plan used a date-level bootstrap with 42 dates, labelled “naive” and “anti-conservative.”

Problems:

- only two seasons; no superpopulation of seasons;
- dates are serially dependent;
- date-level resampling breaks the temporal structure;
- year-cluster bootstrap with two clusters is degenerate;
- season-block bootstrap has only four blocks;
- no reliable interval can be estimated from two seasons.

## 3. Revised Mendota approach

### 3.1 Primary uncertainty statement

Report:

- Spearman ρ;
- n;
- number of years and seasons contributing;
- **leave-one-year-out range**: compute ρ with each year removed; report minimum, maximum, and median of the resulting values;
- a statement that years are not exchangeable and the range is a sensitivity description, not a confidence interval.

The leave-one-year-out range is a **descriptive stability check**. It shows whether one year dominates the estimate. It does not estimate sampling uncertainty.

### 3.2 Optional season-year block sensitivity

If feasible, report a **season-year block bootstrap** as a descriptive sensitivity:

- blocks: year × season (e.g., 2006 spring, 2006 summer, 2006 autumn, ...);
- resample blocks with replacement;
- preserve within-block order;
- 2,000 replicates;
- report the 2.5th/97.5th percentiles of the resampled ρ distribution.

Requirements:

- at least two eligible dates per block for the block to contribute;
- report the number of blocks and the number of valid replicates;
- label the interval **“descriptive season-year block sensitivity, not a confidence interval”**;
- do not use it as a primary uncertainty statement.

Feasibility is not assumed. If blocks are too sparse or the distribution is degenerate, report that the sensitivity could not be computed and use the leave-one-year-out range only.

### 3.3 What is not reported

- no primary year-cluster confidence interval;
- no p-values;
- no claim that resampling solves limited independent temporal coverage;
- no “95% confidence” language for the descriptive range.

## 4. Revised Buffalo Pound approach

### 4.1 Primary uncertainty statement

Report:

- Spearman ρ for all eligible dates;
- n;
- separate ρ for 2018 and 2019;
- **leave-one-date-out range**: compute ρ with each eligible date removed; report minimum, maximum, and median;
- a statement that two seasons cannot support a reliable interval.

### 4.2 What is not reported

- no date-level bootstrap interval;
- no year-cluster bootstrap interval;
- no “95% confidence interval”;
- no claim that the two-season estimate is precise.

### 4.3 Why this is more honest

A leave-one-date-out range shows how much the estimate depends on individual dates, including 2019-07-17. It does not pretend to represent sampling variability across seasons. The absence of a reliable interval is a finding about the design, not a failure to compute one.

## 5. Small-n and overall-n rules

### 5.1 Seasonal strata

- n < 10: no stratum ρ; show points and n.
- n ≥ 10: report ρ; descriptive range only if the leave-one-out/block structure is feasible.

### 5.2 Overall estimand

The protocol must pre-specify a minimum n for reporting an overall ρ. The exact number must be set by the statistical reviewer after the count audit and before estimation, justified by precision/dependence.

If the minimum is not met:

- show points and n;
- do not compute ρ;
- return to human review if the estimand cannot be supported.

No minimum is set in this sprint because actual n is unknown.

## 6. Descriptive vs inferential language

| Term | Use in this protocol |
|---|---|
| **Confidence interval** | **Not used** for the primary estimates |
| **Descriptive sensitivity range** | Used: leave-one-year-out, leave-one-date-out, season-year block percentiles |
| **Bootstrap interval** | Only as a labelled descriptive sensitivity (Mendota season-year block), never for Buffalo Pound |
| **Standard error** | Not used |
| **p-value** | Not used |
| **Statistical significance** | Not used |
| **Precision** | Described by n, range, and sensitivity; not by a CI |

## 7. Sensitivity analyses

Every primary estimand is reported under the following pre-specified sensitivities:

| ID | Sensitivity | Purpose |
|---|---|---|
| S-A | Strict unflagged: exclude all `H` | Reproduces 4L.10 counts; tests H retention |
| S-B | Flagged-inclusive: include `C`/`E`/`G` numeric values if within bounds | Tests flag exclusion |
| S-C | Negative-excluded: exclude negative RFU | Tests low-signal truncation |
| S-D | ±1-day date-window co-occurrence | Exploratory only; not a robustness claim |
| S-E | Buffalo Pound B7-inclusive | Tests fouling exclusion |
| S-F | Buffalo Pound 2019-07-17 excluded | Tests single-date leverage |
| S-G | Buffalo Pound replicate sum / first row | Tests replicate assumption |
| S-H | Mendota station-1 subset | Tests station metadata sensitivity |
| S-I | Lake-specific open-water season | Tests calendar-season boundaries |

Rules:

- report all sensitivities, including contradictory ones;
- do not select the “best” sensitivity for the headline;
- do not add a sensitivity after seeing the primary result unless it is reported as post hoc;
- do not use a sensitivity to “rescue” a null primary result.

## 8. Log-Pearson decision

The 4L.12 protocol included Pearson on `log10(1+x)` as a secondary scale check. The 4L.13 review found the transform arbitrary.

**Revised decision: remove Pearson/log-Pearson entirely.** The protocol relies on Spearman + scatterplots. This avoids an arbitrary transformation and reinforces that the question is rank association, not linear agreement.

If a future protocol wants a linear scale check, it must justify the transformation in advance and label it secondary; it is not part of this protocol.

## 9. What would be needed for reliable intervals

A defensible interval would require:

- more independent seasons/years (e.g., ≥10 comparable seasons);
- a pre-specified dependence model/block structure;
- a coverage/simulation study for the proposed bootstrap;
- a clear target parameter;
- regular sampling or a justified irregular-series method.

The current data do not meet these conditions, especially Buffalo Pound.

## 10. Residual uncertainty

- Mendota: 14 non-exchangeable years; leave-one-year-out range is not a sampling distribution.
- Buffalo Pound: two seasons; no reliable interval; leave-one-date-out range is a sensitivity, not a CI.
- Both: temporal autocorrelation, seasonal clustering, missingness, and date-only biology remain.
- The 2019-07-17 leverage plan is separate (`2019_07_17_LEVERAGE_PLAN.md`).

## 11. Governance

- **Protocol: PROPOSED — NOT APPROVED.**
- **Gate 2: PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- No analysis is authorised until the required human decisions and explicit D-15 approval are recorded.
