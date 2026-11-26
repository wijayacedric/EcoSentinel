# Estimand and Sample Eligibility Review

## Reconstructed P1–P4

| ID | Sensor | Endpoint | Unit of proposed analysis | Assessment |
|---|---|---|---|---|
| P1 | Mendota Turner chlorophyll RFU | Cyanobacteria biovolume from 0–8 m microscopy composite | Same calendar date | Conditional exploratory |
| P2 | Mendota Turner phycocyanin RFU | Same Mendota endpoint | Same calendar date | Conditional exploratory |
| P3 | Buffalo Pound YSI chlorophyll RFU | Cyanobacteria supplied biomass at nominal 0.8 m | Same calendar date | Exploratory only |
| P4 | Buffalo Pound YSI phycocyanin RFU | Same Buffalo Pound endpoint | Same calendar date | Exploratory only |

4L.14 correctly calls 128/139/42/42 strict-rule upper bounds, not actual n. This review did not calculate actual n or apply eligibility rules.

## Rule audit

**Mendota biology:** date window, lake ID, depth and Cyanophyta total are intelligible. The station fallback (station 1 if available, otherwise blank) is deterministic but not a neutral decision: 31 of 402 dates have station 1 and 371 are blank per the package’s underlying audit. A dated shift between station-coded and blank records could change geographic composition. Excluding mixed stations only when station 1 is absent needs a documented source rationale and a clear unit-of-sample statement; a sensitivity with all stations is not a substitute for knowing whether those rows are replicate casts or different locations.

**Biological taxon aggregation:** “at least one cyanobacteria row” and sum of all qualifying rows does not say whether omitted/no-row means true zero, no cyanobacteria detected, not reported, or taxonomy missing. The package correctly prohibits treating missing taxon rows as zero, but eligibility with no row is excluded. This conditions the sample on detected/reported cyanobacteria and may remove biologically important low/absent dates. The endpoint is then not an all-date cyanobacteria abundance series. This is a major estimand issue. Clarify whether empty on-sample taxon lists are documented zeroes; if not, the analysis is detection-conditioned and must be named that way.

**Buffalo Pound biology:** Group-and-Phylum agreement is conservative, but the species/row aggregation rule has no resolved record semantics. Mean-before-sum assumes repeated rows represent replicate measurements of the same taxon. For 2018, two rows per date-species lack a replicate identifier; for 2019 REP1/REP2 occur on disjoint dates. `mean`, `sum`, and `first` are different estimands, not interchangeable robustness options. The source method must decide this. A mean is not supported merely because it looks plausible.

**Sensor date:** The sensor daily mean is treated as a date-level observation, but biological collection time, timezone and sample time relative to the 24-hour mean are unavailable. Same date is an administrative match, not a biologically synchronized pair. The 4L.14 wording is honest about this, but a reviewer should consider changing question's “same-day” to “same-calendar-date co-occurrence” consistently in table captions and conclusions.

**Coverage:** The Buffalo Pound rule “at least 72 of 144 and at least one valid record in each half-day” is mathematically explicit but not justified. Existing raw audits found daily record counts vary by year and may reflect deployment/reporting interval; a nominal 144 expected observations cannot be assumed for every date without confirming logger cadence and completeness. A 50% day can consist mostly of one short, unusual interval; one record per half is a very weak representativeness condition. Coverage thresholds can also preferentially exclude cloudy, fouled, maintenance or high-biomass conditions. Do not adopt until observation cadence, deployment periods, time zone, duplicate timestamps and within-day missingness mechanisms are documented. Do not calculate this now.

**Max n:** Correctly distinguished from usable n. But upper bounds based on strict unflagged overlap need a precise reference table and date-window definition; maximum n cannot establish adequate independent temporal information. A future count-only audit can show rows/dates and reason flows only after rules and authorization. No actual n was computed in this review.

## Selection and circularity risks

- Requiring observed cyanobacteria rows may select positive-detection dates, truncating the biological range and removing non-detections.
- Station fallback, coverage, B7, `C` flags and H/negative handling may select season/year and biomass ranges.
- Sensor usability can differ between chlorophyll and PC, so P1/P2 and P3/P4 need not share the same sample dates; do not describe comparisons as paired across estimands.
- Using supplied total biomass after selecting records by `Group` and `Phylum` is not circular with sensor data, but any row exclusions can alter the biological composition.
- Sensitivity analyses with alternative transformations do not repair unknown sample identity.

## Required resolution before protocol approval

1. Clarify whether no cyanobacteria records means non-detection or missing taxonomy for each source and specify whether zero abundance dates can enter.
2. Have the source custodian resolve duplicate row/replicate semantics before choosing a date total.
3. Replace or justify the 72/144 coverage rule against actual source cadence and time coverage; describe representativeness limits even if retained.
4. Clarify station/location semantics and whether sample records are independent or repeated casts.
5. State same-date is calendar co-occurrence and cannot provide synchronized validation.
6. Define season/era tables as descriptive only and do not promise Buffalo Pound sensor-era comparison.

