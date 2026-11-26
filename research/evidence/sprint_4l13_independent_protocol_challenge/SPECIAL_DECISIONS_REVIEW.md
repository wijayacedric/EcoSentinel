# Special Decisions Review

**Sprint:** 4L.13  
**Status:** INDEPENDENT REVIEW — NOT APPROVAL  
**Protocol reviewed:** Sprint 4L.12, PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

> **This review does not approve the protocol or authorise analysis.**

## 1. Scope

This document reviews the special handling decisions that could materially change the results:

- the 2019-07-17 Buffalo Pound anomaly (D-09);
- Buffalo Pound replicate handling (D-08);
- `B7` fouling exclusion (part of D-05);
- negative pigment values (part of D-05);
- `H` retention (part of D-05);
- the ±1-day window (D-07).

The 15 decisions are reviewed individually in `HUMAN_DECISION_REGISTER.md`.

## 2. The 2019-07-17 anomaly (D-09)

### 2.1 Evidence

- Date: 2019-07-17 (DOY 198).
- Record: 9 taxon rows; all `REP2`; total biomass 45.81 mg m⁻³; cyanobacteria 41.02 mg m⁻³ (89.5%).
- Neighbours: 2019-07-10 total 12,587.1 mg m⁻³ (cyanobacteria 11,919.8); 2019-07-29 total 9,497.9 mg m⁻³ (cyanobacteria 6,755.2).
- The taxonomy file and group-biomass file agree.
- A same-date toxin sample exists (sample 25993), but format/units/sample identity are not verified; it is not used.
- The anomaly is not resolved as a real crash, a sampling error, a processing error, or a replicate artifact.

### 2.2 The proposed decision

4L.12 D-09:

> (a) retain and flag, exclude in sensitivity; (b) exclude from primary; (c) correct.

Recommended: **(a)**.

### 2.3 Is the decision reproducible?

Yes, if the rule is stated as a date-level flag:

- primary includes all 42 dates;
- 2019-07-17 is flagged in every output;
- sensitivity excludes it;
- no correction or imputation.

This is reproducible. The date is known; the flag is deterministic; the sensitivity is pre-specified.

### 2.4 Is it scientifically justified?

**Partially.** Retaining a documented observation is conservative: it avoids deleting data that might be a real bloom crash. But the value is so extreme relative to its neighbours, and all rows are `REP2`, that it could be a sampling/processing artifact. Retaining it in the primary analysis could dominate a rank correlation, especially with n=42.

The protocol’s approach — retain + flag + exclude in sensitivity — is a reasonable compromise. But it is incomplete without a **leverage report**:

- the rank of 2019-07-17 in the biological endpoint;
- the rank of the sensor value on that date;
- ρ with and without the date;
- whether the sign/magnitude changes materially;
- whether the date is an outlier in the sensor series too.

If ρ changes materially when the date is removed, the result is fragile and must be reported as such. If it does not, the anomaly is not influential.

### 2.5 Is it consistent with other rules?

There is a tension:

- The protocol excludes negative pigment values as physically implausible.
- The protocol excludes `B7` as fouling-affected.
- The protocol retains 2019-07-17 despite its being an unresolved extreme.

The rationales differ: negatives are treated as invalid measurement values; B7 is treated as a known fouling interval; 2019-07-17 is treated as a documented but unresolved biological observation. That distinction is defensible, but it must be stated explicitly. Otherwise a reviewer may see inconsistent data handling.

### 2.6 Alternatives

| Option | Advantage | Disadvantage |
|---|---|---|
| (a) Retain + flag + sensitivity | Preserves observation; transparent; tests influence | Extreme value may dominate ρ; result fragile |
| (b) Exclude from primary | Avoids dominance; conservative | Deletes a documented observation; could bias if real crash |
| (c) Correct/impute | Would “fix” the value | No basis; prohibited; not reproducible |
| (d) Use rank-based only and retain | Spearman limits outlier influence | Still influenced by the lowest rank; does not solve anomaly |

The review recommends **(a) with a mandatory leverage report**. Option (b) is defensible only if the human reviewers conclude the anomaly is more likely a processing artifact than a real observation; that judgement is not established by the current evidence.

### 2.7 What must not happen

- Do not interpret the anomaly as bloom termination, recovery, or non-bloom.
- Do not silently delete it.
- Do not correct it.
- Do not report a result that depends on it without showing the sensitivity.

### 2.8 Human decision

D-09 must be decided by the data custodian/scientific reviewer, with the leverage report. This review does not approve it.

## 3. Buffalo Pound replicate handling (D-08)

### 3.1 Evidence

- 2018: no `REP` field; 19 date–species groups have two rows with different densities/biomass; no replicate identifier.
- 2019: `REP1` on 12 dates, `REP2` on 5 dates, disjoint dates; not paired replicates.
- 1,222 taxon rows; 248 cyanophyte rows; not independent.

### 3.2 The proposed decision

Mean before summing, with sum and first-row sensitivity.

### 3.3 Assessment

- If the duplicate rows are **replicate counts**, mean is appropriate.
- If they are **split samples/variants**, sum may be appropriate.
- Without a replicate ID, neither is certain.
- The mean rule is a reasonable default for replicate counts, but it is an assumption, not a documented fact.
- The sensitivity analyses are essential.

**Recommendation:** Accept mean only as an explicit “replicate assumption”; require the source method to confirm whether the duplicates are replicates. If the source method cannot be verified, report both and do not treat either as definitive.

## 4. `B7` fouling exclusion (D-05)

### 4.1 Evidence

- `B7` marks a spike/decrease pattern after a site visit, interpreted as fouling.
- It is an interval flag, not a point flag.
- 604 B7 flags in 2014, 803 in 2020 (outside the 2018–2019 biology window; the relevant counts are in 2018–2019).
- Fouling may be more likely during high biomass.

### 4.2 Assessment

Excluding B7 from primary is defensible for data quality, but it may systematically remove high-biomass dates. The protocol includes a B7-inclusive sensitivity, which is necessary.

**Recommendation:** Quantify B7 overlap with biomass before primary analysis:

- n B7 dates;
- median/IQR biomass on B7 vs non-B7 dates;
- ρ with/without B7;
- whether B7 is concentrated in one season/year.

If B7 dates are high biomass, the primary result is conditional on excluding high-biomass periods; state this.

## 5. Negative pigment values (D-05)

### 5.1 Evidence

- Mendota: 31 negative turbidity, 62 negative YSI phycocyanin, 1 negative YSI chlorophyll, 3 negative PAR below; Turner phycocyanin has 4 unflagged negatives; YSI phycocyanin has 62.
- Buffalo Pound: negatives may occur; the protocol excludes them.
- Negative RFU can be baseline noise, blank subtraction, or below-detection signal. Technical sources disagree on whether negative fluorescence is invalid or simply low signal; some studies replace negative phycocyanin with zero because it is below detection.

### 5.2 Assessment

Excluding all negatives from primary is a strong choice. It can:

- truncate the low end of the sensor distribution;
- inflate rank correlations;
- bias seasonal comparisons if negatives cluster in low-biomass seasons;
- remove legitimate near-zero observations.

**Recommendation:** Either:

- retain negatives in primary as observed RFU values, with exclusion as sensitivity; or
- exclude negatives only if a documented instrument-specific blank/noise threshold shows they are invalid.

The current rule needs explicit justification and a report of its effect on n and ρ.

## 6. `H` retention (D-05)

### 6.1 Evidence

- `H` means “outside standard range,” not “invalid.”
- Turner chlorophyll 54 `H`, phycocyanin 41 `H`; YSI chlorophyll 116 `H`; YSI phycocyanin 0 `H`.
- Some `H` values are plausible high blooms; some may be absurd.

### 6.2 Assessment

Retaining `H` is directionally correct: excluding all `H` would truncate high values and bias against blooms. But “if plausible” is not reproducible.

**Recommendation:** Provide exact bounds and a rule for above-range values. Retain `H` within physical bounds; exclude absurd values; run strict-unflagged sensitivity.

## 7. ±1-day window (D-07)

### 7.1 Evidence

- Date-only biology; same-day matching is already a compromise.
- ±1-day adds dates but changes the sample composition.
- It is not a clean robustness check.

### 7.2 Assessment

Keep as **exploratory only**; do not use it to claim robustness. Consider dropping if the reviewers want the cleanest design.

## 8. Findings

| ID | Finding | Severity |
|---|---|---|
| H1 | 2019-07-17 retention is reproducible but incomplete without leverage reporting | **Major** |
| H2 | The anomaly is potentially influential at n=42 | Major |
| H3 | Replicate mean is an assumption, not a documented fact | Major |
| H4 | B7 exclusion may remove high-biomass dates; overlap not quantified | Major |
| H5 | Negative-value exclusion is not clearly justified | Major |
| H6 | `H` retention is directionally correct but not operational | Major |
| H7 | ±1-day window should be exploratory, not a robustness claim | Moderate |

## 9. Required changes

1. Add a mandatory 2019-07-17 leverage report.
2. Verify the Buffalo Pound replicate design; report mean/sum/first.
3. Quantify B7 overlap with biomass.
4. Justify or reverse negative-value exclusion.
5. Provide exact `H` bounds.
6. Label ±1-day as exploratory.

## 10. Governance

- **Protocol: PROPOSED — NOT APPROVED.**
- **Gate 2: PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- No special decision is approved by this review.
- No analysis is authorised until the required revisions and D-15 approval are recorded.
