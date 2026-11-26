# Revised Research Question

**Sprint:** 4L.14  
**Status:** PROPOSED — NOT APPROVED  
**Supersedes:** Sprint 4L.12 question wording for review purposes  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Date:** 2026-11-24

> **This is a proposed revision for human review. It does not approve the protocol, any of the 15 decisions, or Gate 2. No analysis is authorised.**

## 1. Why the question was revised

The Sprint 4L.12 question used four phrases that overstated the design:

- “paired observations” — the data are date-level co-occurrences, not paired measurements;
- “strength” — not a defined statistical quantity;
- “descriptive uncertainty” — Buffalo Pound cannot support a reliable interval;
- “depth-alignment setting” — implies a controlled comparison the two case studies cannot provide.

The revision addresses Sprint 4L.13 findings R-01, R-03, and R-07. It preserves the original early-warning question only as a long-term aspiration.

## 2. Revised primary question

> **In Lake Mendota (2006–2020) and Buffalo Pound Lake (2018–2019), among same-day date-level co-occurrences and analysed as two separate lake-specific case studies, what are the direction and magnitude of the rank association between surface chlorophyll and phycocyanin fluorescence and independent microscopy-derived cyanobacteria biovolume (Mendota) or cyanobacteria biomass (Buffalo Pound), and how do these associations differ descriptively across seasons and sensor eras?**

## 3. Operational definitions

### 3.1 Same-day date-level co-occurrence

A biological observation and a sensor observation are **co-occurring** when they share the same calendar date after the lake-specific date parsing rules.

This means:

- the sensor daily summary and the biological sample are from the same date;
- the biological sample time is unknown;
- the sensor value is a daily summary, not a sample-time value;
- the two observations are not from the same water parcel;
- the comparison is date-level, not paired, simultaneous, or same-time.

The phrase “paired observation” is not used in the revised protocol.

### 3.2 Rank association

The primary statistic is **Spearman’s rank correlation coefficient, ρ**, between the sensor daily value and the biological endpoint across eligible dates.

It estimates the direction and magnitude of a **monotonic** association. It does not estimate:

- absolute agreement;
- bias;
- calibration;
- predictive accuracy;
- measurement validity;
- causal effect;
- the fraction of variance explained in original units.

### 3.3 Direction and magnitude

The protocol reports:

- the sign of ρ;
- the value of ρ;
- n;
- a descriptive sensitivity range where defensible;
- the number of years/seasons contributing;
- tie counts and range restriction.

It does **not** use “strong/weak/moderate” labels unless a justified benchmark is pre-specified. None is proposed.

### 3.4 Two separate lake-specific case studies

Mendota and Buffalo Pound are analysed as **two independent case studies**. They are not pooled, not treated as a controlled comparison, and not used to validate each other.

The lakes differ in:

- lake type, morphometry, and stratification;
- biological community and phenology;
- sensor instrument, depth, calibration, and period;
- biological endpoint (biovolume vs biomass);
- sampling frequency and sample integration;
- QC systems and missingness.

Depth alignment is one difference among many. The design does **not** identify a depth effect.

### 3.5 Descriptively across seasons and sensor eras

Season and sensor era are observational strata:

- seasons: calendar spring/summer/autumn; winter only if n is adequate;
- Mendota eras: Turner 2006–2019; YSI 2019–2020;
- Buffalo Pound era: YSI 6600 2018–2019.

Strata are described, not tested. No interaction test, no causal attribution.

## 4. Candidate primary estimands

| ID | Lake / era | Sensor | Biological endpoint | Maximum possible n | Status |
|---|---|---|---|---:|---|
| P1 | Mendota / Turner | Chlorophyll RFU | Cyanobacteria biovolume (0–8 m) | 128 | Primary, conditional on n/QC |
| P2 | Mendota / Turner | Phycocyanin RFU | Cyanobacteria biovolume (0–8 m) | 139 | Primary, conditional on n/QC |
| P3 | Buffalo Pound / YSI 6600 | Chlorophyll RFU | Cyanobacteria biomass (0.8 m) | 42 | Recommended downgrade to exploratory pending D-02 |
| P4 | Buffalo Pound / YSI 6600 | Phycocyanin RFU | Cyanobacteria biomass (0.8 m) | 42 | Recommended downgrade to exploratory pending D-02 |

The n values are **upper bounds under the strict 4L.10 unflagged rule**, not actual primary n. Actual n must be enumerated after approval under the revised QC rules. See `ESTIMAND_AND_SAMPLE_ELIGIBILITY_SPECIFICATION.md`. P3/P4 are not approved as primary until the Buffalo Pound biomass derivation is verified.

The four are distinct sensor–endpoint pairs, but not independent quantities:

- P1/P2 share the Mendota endpoint and dates;
- P3/P4 share the Buffalo Pound endpoint and dates.

They must not be counted as four independent confirmations.

## 5. What the question does not ask

- Whether sensors detect blooms.
- Whether sensors provide early warning.
- Whether sensor alarms have acceptable false-alarm rates.
- Whether fluorescence is a validated toxicity measure.
- Whether surface sensors represent whole-water-column biomass.
- Whether depth alignment causes better agreement.
- Whether Turner and YSI are interchangeable.
- Whether the results generalise to other lakes.

## 6. Original early-warning question

The original question remains a long-term research aspiration:

> Can persistent changes in relationships between freshwater environmental variables provide earlier warning of cyanobacterial blooms than conventional monitoring, at comparable false-alarm rates?

It is **not** the current analysis question. It remains untestable with the available evidence because there are:

- 0 independently reconstructed bloom events;
- 0 defensible non-bloom intervals;
- no approved event/non-event definition;
- no time-stamped/sub-weekly biology;
- no matched-FAR denominator.

No part of this revised protocol authorises an early-warning analysis.

## 7. Scope of inference

The scope is:

- Lake Mendota, 2006–2020;
- Buffalo Pound Lake, 2018–2019;
- the specified sensors and depths;
- the specified biological endpoints;
- the eligible dates under the revised QC rules.

The results do **not** generalise to:

- other lakes;
- other periods;
- other sensors;
- whole-water-column biomass;
- bloom status or toxicity;
- early-warning performance.

## 8. Precision verdict

The revised question is **precise enough for human review** because:

- it uses date-level co-occurrence, not “paired”;
- it names Spearman’s ρ and its direction/magnitude;
- it treats the lakes as two case studies;
- it does not imply a depth comparison;
- it preserves the original early-warning question as an aspiration only.

It remains **conditional** on:

- actual n being enumerated;
- Buffalo Pound biomass derivation being documented;
- QC rules being operational;
- the 15 human decisions being recorded.

## 9. Governance

- **Protocol: PROPOSED — NOT APPROVED.**
- **Gate 2: PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- No analysis is authorised until the required human decisions and explicit D-15 approval are recorded.
