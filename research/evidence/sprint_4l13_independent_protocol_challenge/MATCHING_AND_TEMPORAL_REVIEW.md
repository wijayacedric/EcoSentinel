# Matching and Temporal Review

**Sprint:** 4L.13  
**Status:** INDEPENDENT REVIEW — NOT APPROVAL  
**Protocol reviewed:** Sprint 4L.12, PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

> **This review does not approve the protocol or authorise analysis.**

## 1. The proposed matching rule

The 4L.12 protocol proposes:

- **Primary:** same calendar date only.
- **Mendota:** provider daily mean of 1-minute observations.
- **Buffalo Pound:** mean of valid 10-minute values, with ≥50% coverage and both halves of the day represented.
- **Sensitivity:** ±1-day window only; no ±3/±7/±14-day windows; no lag/lead analysis.

The intent — conservative date-level matching, no interpolation, no lead/lag — is correct. The wording **“paired observations”** is not.

## 2. Same-day is not paired

A “paired observation” in measurement science implies:

- the same sample, or a known temporal/spatial pairing;
- a known time interval between measurements;
- a defined pairing structure that supports a paired analysis.

Here:

- the biological data have a date but **no sample time**;
- the sensor value is a **daily summary** of many readings;
- the biological sample represents an unknown time within the day;
- the sensor and sample are not the same water parcel;
- Mendota’s sensor and sampling site are ~105.7 m apart;
- Buffalo Pound’s buoy and biological site are not independently co-located.

Therefore, “same-day” means **date-level co-occurrence**, not a paired measurement. The protocol should use that term everywhere.

### 2.1 Why this matters

If the protocol says “paired,” readers may expect:

- a paired test;
- a within-day comparison;
- a measurement-error model;
- a known time lag.

None is possible. The claims matrix prohibits those interpretations, but the question wording should not invite them in the first place.

## 3. Sensor daily summaries

### 3.1 Mendota

- The provider daily value is an average of 1-minute observations.
- The daily file does not include the number of valid minutes, so within-day coverage is unknown.
- The daily average includes daylight quenching and nighttime values.
- No nighttime-only value can be reconstructed from the daily file.
- The 2019 YSI era has both Turner and YSI values on some dates; they are separate.

**Consequence:** Mendota’s sensor value is a full-day average with unknown weighting and unknown quenching. It is not a sample-time-matched value.

### 3.2 Buffalo Pound

- 10-minute values; 2018 and 2019 are 10-minute cadence.
- The protocol requires ≥50% of expected values (≥72/144) and both halves of the day represented.
- The primary daily mean still includes diel quenching; a nighttime median is proposed as sensitivity.

**Consequence:** The Buffalo Pound daily mean is better documented than Mendota’s, but it is still a full-day average. The nighttime sensitivity is useful but not a primary comparison because Mendota cannot match it.

### 3.3 Asymmetry

The protocol compares:

- Mendota: provider daily mean, unknown coverage, 1-minute base;
- Buffalo Pound: analyst-computed daily mean, known coverage, 10-minute base.

This is a structural asymmetry. It cannot be removed without acquiring Mendota high-resolution data (not authorised) or degrading Buffalo Pound to an unknown-coverage mean (not desirable). The protocol should state the asymmetry explicitly, not just in a footnote.

## 4. The ±1-day sensitivity

### 4.1 What it does

If a same-day sensor value is missing, the protocol uses the nearest sensor date within ±1 day; if both adjacent days are valid, it averages them.

### 4.2 Problems

1. **It is not a clean sensitivity.** It changes both the matching rule and the sample composition. A difference between primary and ±1-day results could be due to date mismatch, added dates, or both.
2. **It can mix ecological states.** A bloom can rise or fall within one day; a ±1-day window can pair a biological sample with a different state.
3. **It is asymmetric.** Same-day values are always preferred; adjacent-day values are used only when same-day is missing. The resulting sample is a mixture of same-day and adjacent-day pairs.
4. **It can rescue a null result.** If the primary association is weak but the ±1-day association is stronger, the protocol must not present the latter as “robustness.” It is a different question.
5. **It adds researcher degrees of freedom.** The team could be tempted to emphasize the window that looks better. The protocol pre-specifies it, which helps, but it still creates a second estimand.

### 4.3 Recommendation

- Keep same-day as the only primary matching rule.
- Treat ±1-day as an **exploratory temporal-window analysis**, not a robustness check.
- Label it “±1-day date-window co-occurrence,” not “sensitivity” or “agreement.”
- Do not use it to claim the primary result is robust; report both and state the difference in sample composition.
- Consider dropping it entirely if the human reviewers want the cleanest possible design.

## 5. Missing sample times and diel cycles

### 5.1 What is lost

Without sample times, the protocol cannot:

- align the sensor to the biological sampling hour;
- separate daytime quenching from nighttime fluorescence;
- resolve diel vertical migration;
- distinguish a morning sample from an afternoon sample;
- estimate a within-day lag.

### 5.2 What this means for the results

The results are **date-level associations between a daily sensor summary and a date-stamped biological sample**. They are not:

- same-time comparisons;
- same-parcel comparisons;
- diel-cycle analyses;
- lead/lag analyses;
- onset/termination analyses.

The protocol says this in the claims matrix; the question wording must match.

## 6. What the results could establish

At most:

- whether dates with higher daily sensor fluorescence also tend to have higher microscopy-derived cyanobacteria abundance;
- whether that date-level rank association differs descriptively across seasons, sensor eras, and the two lake settings;
- how sensitive the association is to QC, matching window, and the 2019-07-17 anomaly.

## 7. What the results could not establish

- same-time agreement;
- absolute agreement;
- calibration;
- prediction;
- bloom onset/termination;
- lead time;
- early warning;
- whole-water-column biomass;
- causal effect of depth alignment;
- generalisation to other lakes.

## 8. Findings

| ID | Finding | Severity |
|---|---|---|
| E1 | Same-day matching is conservative and appropriate in intent | Pass |
| E2 | “Paired observations” overstates the design | **Major** |
| E3 | Daily sensor summaries include unknown diel quenching; Mendota cannot do nighttime | Major |
| E4 | ±1-day sensitivity is ambiguous and should be exploratory, not a robustness claim | Moderate–Major |
| E5 | No sample times; no lead/lag/onset possible | Pass (protocol says so) but wording must align |
| E6 | Mendota/Buffalo Pound daily-summary asymmetry is structural | Moderate |

## 9. Required changes

1. Replace “paired observations” with “same-day date-level co-occurrence.”
2. State the daily-summary asymmetry explicitly in the question and methods.
3. Label ±1-day as exploratory; do not use it to claim robustness.
4. Keep the prohibition on lag/lead/onset.
5. Add a sentence: “A same-day match is not a same-time or same-parcel measurement.”

## 10. Governance

- **Protocol: PROPOSED — NOT APPROVED.**
- **Gate 2: PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- No decision is approved by this review.
- No analysis is authorised until the required revisions and D-15 approval are recorded.
