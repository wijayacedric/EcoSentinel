# Mendota Standalone Viability

**Sprint:** 4L.20  
**Date:** 2026-11-26  
**Question:** Is Lake Mendota strong enough to stand alone as Stage 1?  
**Status:** Viability assessment. **No analysis authorised. Actual n unknown. D-15 NOT APPROVED.**

---

## 1. Verdict

**Yes — conditionally, as a limited exploratory measurement audit.**

Mendota is strong enough to support a **single-lake, Turner-era, two-pigment descriptive study**:

- **P2 (phycocyanin)** primary.
- **P1 (chlorophyll)** secondary descriptive comparator.
- **Turner era 2006–2019 only.**
- **Same-calendar-date co-occurrences.**
- **Spearman rank association**, n, influence diagnostics, reduced sensitivities.
- **No validation, calibration, agreement, prediction, bloom detection or early warning.**

It is **not** strong enough to support:

- a sensor validation or calibration study;
- a whole-water-column biomass claim;
- an early-warning study;
- a generalisable lake comparison;
- an award-leading originality claim.

The depth mismatch is the critical limitation. The study is defensible only if it is framed as **surface fluorescence vs depth-integrated biovolume**, not as a sensor measuring cyanobacteria.

---

## 2. Proposed standalone question

> **Among sampled dates in Lake Mendota during the Turner fluorometer era (2006–2019), what is the direction and magnitude of the rank association between daily mean surface phycocyanin fluorescence (0.5 m) and microscopy-derived cyanobacteria biovolume (0–8 m composite), and how does chlorophyll fluorescence compare descriptively?**

### Operational definitions

- **Sampled date:** a date with a reported cyanobacteria row and a same-day Turner pigment value.
- **Surface:** 0.5 m sensor depth.
- **Integrated biovolume:** sum of `biovolume_conc` for `division = Cyanophyta` across the 0–8 m tube composite.
- **Rank association:** Spearman’s rho; monotonic association only.
- **Descriptive comparison:** P1 and P2 are reported; P2 is primary; P1 is secondary; no “best sensor” selection.

---

## 3. Scientific meaning

### 3.1 Is a same-date rank association meaningful?

**Yes, but narrowly.**

A surface fluorometer is widely used as a monitoring proxy. A meaningful question is:

> Does the surface signal rank-track the integrated cyanobacteria stock on the dates when both were measured?

This is a **monitoring proxy** question. It is not:

- “Does the sensor measure cyanobacteria?”
- “Is the sensor calibrated?”
- “Can the sensor replace microscopy?”
- “Does surface fluorescence represent the whole water column?”
- “Can the sensor predict a bloom?”

The distinction matters because the sensor and the biology are not the same measurement population. The sensor is a point measurement at 0.5 m; the biology is a tube composite over 0–8 m. The study can describe whether the two rank together; it cannot establish that one measures the other.

### 3.2 Is it ecology?

**Only weakly.** The study does not test a ecological mechanism, a bloom trigger, a community interaction or a causal effect. It is a measurement-comparability audit set in a lake. That is a legitimate scientific activity, but it should not be presented as ecological research. The ecologist reviewer in 4L.19 made this point directly: “This is not really an ecological study. It is a comparison of two imperfect measurement systems.”

### 3.3 What would make it unmeaningful?

- If the depth mismatch is so large that the two variables are measuring unrelated water parcels.
- If the sampled dates are too few or too seasonally restricted.
- If the rank association is entirely driven by seasonal co-trending.
- If the QC exclusions select a narrow, unrepresentative range.
- If the sensor values are not comparable across the Turner era due to undocumented changes.

These are not established as fatal, but they are the reviewer’s decision points.

---

## 4. Independent biology

### 4.1 Strengths

- NTL-LTER phytoplankton are direct microscopy observations (Utermöhl technique, PhycoTech), not sensor-derived.
- Species-level counts and biovolume are reported.
- The 0–8 m tube composite is a standard whole-water-column sample for Mendota.
- The record spans 1995–present; the Turner overlap is 2006–2019.
- The endpoint is measurement-independent of the fluorometer.

### 4.2 Weaknesses

- **Taxonomic non-stationarity:** 204 names only pre-2013, 72 only post-2013; transitions occur across 2008–2020, not only February 2013; 889 genus-field mismatches; 1,632 blank-genus records; 20 unresolved names.
- **Species-level longitudinal comparisons are not defensible** without a crosswalk. The protocol uses broad `Cyanophyta` total, which reduces but does not eliminate the problem.
- **No detection limits** are documented.
- **Repeated rows** for the same species/date may represent different variants or vegetative states; they are not necessarily duplicates.
- **Counting error and taxonomic uncertainty** are not quantified.
- **Biovolume is derived** from geometric shapes, not a direct measurement.
- **The 0–8 m composite is not a surface sample.** It integrates over a depth range; the sensor does not.

### 4.3 Independence verdict

**Measurement-independent, not perfect.** The microscopy is a genuine independent reference for the sensor, but it is not ground truth. The study should call it “microscopy-derived biovolume,” not “true biomass.”

---

## 5. Temporal sampling

### 5.1 What the record supports

- 402 Mendota dates over 1995–2020; 400 at 0–8 m; 2 at 0–2 m.
- 13–19 dates per year; median gap ~14 days; 72 gaps ≥30 days, mostly winter.
- Sampling is biweekly during the ice-free season, every 4 weeks in late autumn, and usually once in winter.
- The Turner sensor overlap is 2006–2019; 128 chlorophyll and 139 phycocyanin same-day unflagged upper bounds.

### 5.2 What it does not support

- Daily bloom onset or short-lived events.
- Lead/lag analysis at daily resolution.
- Continuous ecological dynamics.
- A claim that a daily sensor mean represents the sample moment.
- A claim that the sampled dates represent all lake conditions.

### 5.3 Temporal verdict

**Seasonal to multi-week descriptive analysis only.** The study can describe associations among sampled dates; it cannot reconstruct continuous dynamics. This is a fundamental limitation for any early-warning interpretation, but acceptable for a measurement audit.

---

## 6. Detection-conditioned population

The protocol requires at least one cyanobacteria row on a date. A sampled date with no cyanobacteria row is not treated as zero; it is excluded from the primary population and reported separately.

**Consequences:**

- The target population is “sampled dates with reported cyanobacteria,” not all lake conditions.
- Low-biomass/absent dates may be underrepresented.
- The rank association may be attenuated or inflated by the selection.
- The study cannot generalise to “the lake” or “the bloom season.”
- A zero-inclusive analysis is not permitted unless the source documents that an empty row means true zero/non-detection.

**Verdict:** acceptable only as an explicit detection-conditioned descriptive study. The report must state the population, not just “Lake Mendota.”

---

## 7. Instrument eras

### 7.1 Turner era

- Turner Cyclops 7 chlorophyll/phycocyanin, 2006–2019.
- 0.5 m.
- 128/139 same-day unflagged upper bounds.
- Coherent instrument era.
- H/C flags; no G for Turner; 4 negative phycocyanin values.

### 7.2 YSI era

- YSI EXO2, 2019–2020.
- 21/22 same-day upper bounds.
- Different instrument, range, firmware and magnitude.
- No crosswalk.
- Too small for a parallel estimate.

### 7.3 Verdict

**Turner-only.** Do not concatenate Turner and YSI. Do not use YSI as a secondary estimate in Stage 1. If the YSI era is mentioned, it is context only.

---

## 8. Depth mismatch

### 8.1 The facts

- Sensor: 0.5 m.
- Biology: 0–8 m tube composite on 400 of 402 dates.
- No depth-resolved biology in the phytoplankton dataset.
- Buoy is approximately 106 m from the NTL southern-lake sampling site; station is blank for 371/402 dates.
- The lake can stratify; deep chlorophyll maxima and buoyant cyanobacteria can decouple surface and integrated biomass.

### 8.2 Why it matters

A 0.5 m point measurement is not a 0–8 m integrated stock. The sensor may over- or under-represent the column depending on:

- stratification and mixed-layer depth;
- deep chlorophyll maxima;
- buoyant surface scums;
- vertical migration;
- light penetration and quenching;
- patchiness at the 106 m offset.

### 8.3 Can it be corrected?

**No, not with the available data.** There is no depth-resolved biology to calibrate a surface-to-composite correction. A correction would be an assumption, not a measurement.

### 8.4 Is it fatal?

- **For validation/calibration/whole-column claims:** yes.
- **For a surface-vs-composite descriptive audit:** no, if the question is framed correctly and the reviewer accepts the limitation.
- **For an award-leading ecological study:** it is a major weakness.

**Verdict:** the depth mismatch is the study’s central limitation. It must be in the title-level framing, not buried in limitations.

---

## 9. QC and actual n

### 9.1 QC issues

- `C`: sensor off; 316 Turner chlorophyll C flags; numeric C values exist. Exclude primary; report; SENS_C diagnostic.
- `H`: outside standard range; no numeric range; 54 Turner chlorophyll, 41 Turner phycocyanin. Treatment requires reviewer decision.
- `G`: suspected biofouling; no G in Turner columns. Not applicable.
- `O`: undefined; one value in specific conductance. Exclude; report.
- Undocumented codes: eight columns. Exclude primary; report.
- Negative RFU: 4 Turner phycocyanin values in 2012. Exclude primary; SENS_NEG.
- Upper RFU bound: no documented Mendota range; do not invent one; report extremes.
- Missing: exclude; no imputation.
- Station: blank for 371/402; include all eligible dates; station sensitivity.
- Daily mean: provider mean; no within-day counts; sample time unknown.

### 9.2 Actual n

The 128/139 values are **upper bounds under the strict unflagged rule**, not actual primary n. The actual n after C/H/negative/station/missing exclusions is unknown until the count-only audit.

**No count audit has been authorised or performed.** The study cannot claim a minimum n or a stable estimate until that audit is done.

### 9.3 Minimum n

The statistical reviewer must set the minimum n before estimation, after the count audit, justified by precision and dependence, not by the observed result. Seasonal strata: n<10 → no stratum rho; show points and n.

---

## 10. What a negative result would mean

A weak, null or inconsistent association could legitimately mean:

- surface phycocyanin is not a reliable rank proxy for integrated cyanobacteria biovolume in Mendota;
- the depth mismatch attenuates the association;
- seasonal co-trending dominates the pooled signal;
- taxonomic composition/pigment content varies;
- the sensor is affected by quenching, fouling or calibration drift;
- the sampled dates are too sparse or seasonally restricted.

It would **not** establish:

- that the sensor is useless;
- that cyanobacteria are absent;
- that the lake is not bloom-prone;
- that the sensor cannot be calibrated;
- that a different sensor would fail;
- that the result generalises to other lakes.

A negative result is a legitimate contribution only if the question and the population are clearly defined. It is not a contribution if it is merely “we found no correlation in a small, QC-limited sample.”

---

## 11. Final recommendation

**Retain Mendota as a standalone exploratory study, with P2 primary and P1 secondary, Turner-only, descriptive only.**

### Conditions

1. The protocol QC section is formally revised.
2. The scientific reviewer accepts the surface-vs-composite framing.
3. The statistical reviewer accepts the descriptive rho and the seasonal/influence checks.
4. The count audit establishes adequate actual n.
5. The licence/competition review is completed.
6. The student contribution is documented.
7. D-13 and D-15 are recorded through governance.

### What would change the recommendation

- Reviewers conclude the depth mismatch makes P1/P2 uninterpretable → pause.
- Actual n is too small → pause or restrict to descriptive points.
- Seasonal confounding cannot be bounded → pause.
- Licence/competition review prohibits use → pause.
- A stronger, feasible question becomes available → reconsider.

**Verdict:** Mendota is strong enough to stand alone only as a **limited exploratory measurement audit**, not as a validation, ecological process study or award-leading project. If that is not enough for the project’s goals, pause.

**No analysis was performed. No decision was approved.**
