# Buffalo Pound — Stage 1 Decision

**Sprint:** 4L.20  
**Date:** 2026-11-26  
**Decision:** **Remove Buffalo Pound from Stage 1.**  
**Status:** Recommendation. Not a formal decision; D-02/D-08/D-09 remain outstanding and are re-scoped as future/Stage 2 issues. No analysis authorised.

---

## 1. Decision

Buffalo Pound should **not** remain part of the proposed Stage 1 study, even as a conditional exploratory appendix.

The P3/P4 estimands should be removed from the Stage 1 protocol. The Buffalo Pound datasets and evidence should be preserved for a future Stage 2/context study if the custodian provides the missing documentation. They should not be used as a second case study in the current competition project.

This is not a judgement that the data are worthless. It is a judgement that the **cost, uncertainty and interpretational burden exceed the scientific value they add to Stage 1**.

---

## 2. Scientific contribution

### 2.1 What Buffalo Pound could add

- A **depth-aligned** sensor–biology case: YSI 6600 pigments at 0.82 m; microscopy at 0.8 m; same site.
- A **second lake** with a different trophic state, community and bloom phenology.
- A **high-frequency** sensor record (10-minute) over two open-water seasons.
- A direct link to Painter et al. (2022), which documented a mid-summer *Dolichospermum* bloom and an autumn *Planktothrix* bloom.

### 2.2 What it cannot add

- **A controlled depth comparison.** Mendota and Buffalo Pound differ in lake type, morphometry, stratification, community, instrument, period, sampling, QC and endpoint. Depth is one difference among many. The two-lake design cannot isolate it.
- **A validation or calibration.** The biomass endpoint is a derived wet-weight-equivalent quantity, not an independent absolute reference. There is no calibration crosswalk.
- **A generalisable second case.** Two seasons cannot support a generalisable sensor–biomass relationship.
- **A clean replication.** P3/P4 share the same dates and endpoint; they are not independent confirmations.
- **A robust answer when the sensor already missed a bloom.** Painter et al. (2022) report that the autumn *Planktothrix* bloom formed >60% of phytoplankton biomass but was not detected by sensor or laboratory chlorophyll. That is direct prior evidence that the sensor–biomass relationship can be weak or taxon-dependent.

### 2.3 Scientific value verdict

**Modest and conditional.** Buffalo Pound is scientifically interesting, but its contribution to Stage 1 is a **depth-aligned contrast that the design cannot interpret** and a **second lake that cannot be compared cleanly**. The value does not justify the unresolved provenance and the extra protocol/reviewer burden.

---

## 3. Data integrity

### 3.1 Biomass derivation

- `Biomass_mg_m3` is arithmetically consistent with `Cell_Volume_um3 × Cell_Density_L × 10^-6` under a 1 g cm⁻³ assumption.
- The Painter et al. (2022) methods describe species-level inverted microscopy, cell-volume measurement and shape-specific conversion to wet-weight biomass.
- The exact universal density multiplier, rounding chain, taxon-level vs sample-level computation and duplicate-row handling are **not verified from the accessible text**.
- The endpoint is not biovolume, dry mass, carbon biomass or a direct gravimetric measurement.

**Status:** broad derivation supported; exact field provenance unconfirmed. This is not enough for a primary endpoint.

### 3.2 Duplicate rows and `REP1`/`REP2`

- 2018: 19 date–species groups with two rows within the same `Sample_ID`.
- 2019: 2 duplicate groups within `REP1`.
- 2019 `REP1`: 12 dates/294 rows; `REP2`: 5 dates/111 rows; disjoint dates.
- The labels are not paired technical replicates in the supplied data.
- The source documentation does not define whether duplicates are split counts, separate counting chambers, subsamples, replacement samples or data-processing duplicates.

**Status:** unresolved. Mean-before-sum, sum and first-row are **different endpoint definitions**, not robustness checks. Choosing one by assumption would change the cyanobacteria total and potentially the association.

### 3.3 B7

- B7 is a caution interval covering the entire period between the last maintenance visit and the visit where fouling was identified.
- It is not a point-level invalidity flag.
- Automatic exclusion is not supported; retaining with a flag and a B7-exclusion sensitivity is more faithful.
- The deposited files may or may not retain B7 values; the custodian has not confirmed.

**Status:** B7 is a caution flag, not a removal flag. But the overlap with biomass and the correct treatment remain unresolved.

### 3.4 Negative and >100 RFU

- Negative pigment RFU has no documented biological meaning.
- Values above 100 RFU are outside the documented 0–100 RFU full scale; saturation/clipping/extrapolation is unknown.
- Neither can be interpreted as valid low/high biomass without custodian clarification.

**Status:** unresolved. They are not a reason to reject the entire dataset, but they are another layer of assumptions.

### 3.5 Coverage, time zone and sample times

- Daily record counts vary 121–144 (2018) and 42–131 (2019).
- No date-specific expected cadence.
- No time-zone statement.
- No partial-day handling.
- BP_YSI profile casts suggest late-morning/early-afternoon visits on most dates, but the phytoplankton sample time is not documented.
- The fixed 72/144 coverage rule is withdrawn.

**Status:** unresolved. A daily mean may not represent the biological sample day.

### 3.6 Calibration and maintenance

- Pigment sensors were calibrated at the start and end of seasons with a two-point rhodamine standard.
- Pre/post-maintenance values were used to assess fouling and drift.
- No per-record coefficients or complete maintenance log are supplied.

**Status:** partial. Adequate for a descriptive audit only with explicit limitations, not for a primary sensor–biomass claim.

### 3.7 Licence and version

- Biological dataset: CC BY-NC-SA 4.0.
- Buoy dataset: CC BY 4.0.
- Different repositories, different licences, different QC systems.
- The FRDR record notes a newer version; the link returned 404 during 4L.19.
- Combined derived use and competition display require a written licence review.

**Status:** unresolved. Removing Buffalo Pound removes the CC BY-NC-SA/ShareAlike complication from Stage 1.

---

## 4. Methodological cost

| Cost | Assessment |
|---|---|
| Unresolved decisions | D-02, D-05 (B7/coverage/negative/>100), D-08, D-09, parts of D-06/D-07, D-14 |
| Additional QC complexity | Duplicate/REP, biomass derivation, B7 interval, coverage/time zone, negative/>100 RFU, calibration |
| Endpoint incompatibility | Biomass vs biovolume; not poolable; not convertible |
| Multiplicity | P3/P4 add two more estimates sharing one endpoint/dates |
| Interpretation risk | Two seasons; sensor missed an autumn bloom; no non-bloom baseline |
| Reviewer burden | A second lake, second endpoint, second licence, second QC system |
| Custodian dependency | No response; no custody confirmation; no data dictionary |
| Competition risk | More complexity, weaker narrative, more ways for a judge to find an unresolved issue |

**Conclusion:** the methodological cost is high and the scientific gain is modest. The current project cannot afford both.

---

## 5. Why not keep it as a conditional exploratory appendix?

A conditional appendix sounds harmless, but it is not free:

1. It keeps the protocol dependent on an external custodian who has not responded.
2. It keeps the CC BY-NC-SA licence in the package.
3. It keeps B7/coverage/duplicate/biomass questions alive for reviewers.
4. It invites a two-lake narrative that the data cannot support.
5. It adds length and complexity to the report book and poster without adding a clean result.
6. It creates a temptation to interpret P3/P4 if they look interesting, despite their unresolved provenance.

If the custodian later provides a complete data dictionary and the project has time, Buffalo Pound can be revisited as a **separate** study. It should not be a conditional part of Stage 1.

---

## 6. What would change the decision

Buffalo Pound could be reconsidered for Stage 1 only if **all** of the following are true:

1. The custodian provides a written data dictionary defining duplicate rows and `REP1`/`REP2`.
2. The custodian confirms the exact `Biomass_mg_m3` derivation, density, rounding and corrections.
3. The custodian confirms B7 retention and the correct treatment.
4. The custodian documents negative and >100 RFU handling.
5. The custodian documents date-specific cadence, time zone and partial-day handling.
6. The phytoplankton sample times are documented or bounded.
7. The sensor configuration/calibration/maintenance records are available.
8. A written licence review permits the intended combined use and competition display.
9. Independent reviewers accept P3/P4 as exploratory, not primary.
10. The project has enough time to add a second lake without weakening the Mendota core.

That is a high bar. It is not met now, and the project should not wait for it.

---

## 7. What happens to D-02, D-08 and D-09?

They remain in the governance record but are **re-scoped**:

- **D-02 (Buffalo Pound endpoint):** not applicable to Stage 1; future Buffalo Pound/Stage 2 decision.
- **D-08 (replicate handling):** not applicable to Stage 1; future Buffalo Pound/Stage 2 decision.
- **D-09 (2019-07-17 anomaly):** not applicable to Stage 1; preserve the evidence and flag for any future use.

They are not “resolved” or “approved.” They are removed from the Stage 1 critical path. This distinction must be recorded.

---

## 8. Final recommendation

**Remove Buffalo Pound from Stage 1.**

- Stage 1 becomes Mendota-only.
- P3/P4 are removed from the Stage 1 estimand set.
- The Buffalo Pound evidence is preserved for a future Stage 2/context study.
- No further custodian contact is made in this sprint.
- No Buffalo Pound analysis is performed.

**Why:** the dataset is scientifically interesting but not defensible enough, documented enough or cost-effective enough to remain part of a time-limited Stage 1 project whose core question can be answered with Mendota alone.

**No decision is approved. No analysis is authorised.**
