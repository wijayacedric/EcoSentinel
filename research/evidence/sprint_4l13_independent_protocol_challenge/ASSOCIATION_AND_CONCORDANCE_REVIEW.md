# Association and Concordance Review

**Sprint:** 4L.13  
**Status:** INDEPENDENT REVIEW — NOT APPROVAL  
**Protocol reviewed:** Sprint 4L.12, PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

> **This review does not approve the protocol or authorise analysis.**

## 1. The six concepts the protocol must keep separate

| Concept | Question it answers | Statistic / method | Is it proposed? |
|---|---|---|---|
| **Rank association** | Do dates with higher sensor values tend to have higher biological values? | Spearman ρ | **Yes — primary** |
| **Linear association** | Is there a linear relationship on a chosen scale? | Pearson r | Secondary only |
| **Absolute agreement** | Do the two methods give the same value, on the same scale, with small bias? | Bland–Altman, concordance correlation, ICC | **No — not estimable** |
| **Relative agreement / concordance** | Do the methods rank dates similarly or move in the same direction? | Rank concordance; sign concordance | Partly, via Spearman; “relative concordance” is under-defined |
| **Predictive performance** | Does the sensor predict the biological endpoint on held-out data? | Calibration + validation, RMSE/MAE/accuracy | **No** |
| **Measurement validity** | Is the sensor an unbiased, calibrated measure of the biological quantity across conditions? | Calibration experiment, error model, independent validation | **No** |

The protocol’s strongest conceptual move is to refuse absolute agreement and predictive/validation claims. That passes review.

The weakest conceptual move is the phrase **“relative concordance.”** It appears in the operational definition of comparability but is not defined in the primary question document, and its added value is not demonstrated.

## 2. Spearman’s ρ: appropriateness

### 2.1 What it estimates

Spearman’s ρ is the Pearson correlation between the rank-transformed variables. It estimates the degree to which two variables are **monotonically related** — not necessarily linearly, and not in absolute agreement.

For the proposed question, this is appropriate because:

- the relationship between RFU and biovolume/biomass is expected to be monotonic but not linear;
- the endpoints are heavy-tailed;
- the sensor and biology are on different scales;
- rank association is robust to marginal outliers and does not require bivariate normality.

### 2.2 What it does not estimate

Spearman’s ρ does **not** estimate:

- absolute agreement;
- bias;
- calibration;
- predictive accuracy;
- causal effect;
- measurement validity;
- the fraction of variance explained in the original units.

A high ρ can coexist with a large multiplicative bias. A low ρ can coexist with a strong but non-monotonic relationship.

### 2.3 Limitations specific to this protocol

1. **Non-monotonicity.** If fluorescence quenches at high biomass, or if community shifts reverse the relationship, ρ can be near zero despite a real non-monotonic association. The protocol does not assess non-monotonicity.
2. **Ties.** Daily RFU values may have many ties, especially at low precision; biovolume may have zeros. Tie-corrected Spearman is required, and the number of ties should be reported.
3. **Range restriction.** If the sampled dates over-represent bloom or non-bloom conditions, ρ is range-restricted.
4. **Measurement error.** Spearman is attenuated by measurement error in either variable; the protocol cannot correct this without a measurement-error model.
5. **Temporal dependence.** Dates are serially dependent; ρ’s sampling variability is larger than an i.i.d. calculation would suggest. This is addressed (inadequately) by the bootstrap proposal.
6. **Ecological confounding.** A positive ρ may reflect season, stratification, or shared drivers, not a sensor–biology measurement relationship.
7. **Taxonomic composition.** Phycocyanin per biovolume differs among taxa; ρ may be driven by community shifts rather than sensor validity.

### 2.4 “Strength”

The question says “strength.” The protocol says not to use “strong/weak” labels, but the word remains in the question. This is inconsistent.

**Recommendation:** Replace “strength” with “direction and magnitude of Spearman’s ρ.” Report ρ and n. Do not label ρ as strong/weak/moderate unless a pre-specified, justified benchmark is provided — and none is.

## 3. Pearson on log10(1+x): secondary linear statistic

### 3.1 What the protocol proposes

Pearson’s r on `log10(1 + x)` for both variables, as a secondary scale/linearity check, no p-value.

### 3.2 Assessment

- The log transform is a reasonable way to reduce heavy-tail influence, but `log10(1+x)` is not the only option and is not derived from the measurement process.
- For RFU values, zero/negative handling is awkward: `log10(1+x)` is defined for x > −1, but negative RFU values are excluded from primary, so the transform applies only to non-negative values.
- For biovolume/biomass, `log10(1+x)` compresses high values and may make the relationship look more linear than it is.
- Pearson on a log scale still measures **linear association**, not agreement.
- The protocol does not justify why this transform, rather than no transform or a different transform, is pre-specified.

**Recommendation:** Either (a) drop Pearson entirely and rely on Spearman + scatterplots, or (b) retain it explicitly as a **scale-sensitivity check**, justify `log10(1+x)` as a variance-stabilising choice, and do not interpret it as agreement or prediction. Do not try multiple transformations.

## 4. Absolute agreement: correctly refused

The protocol states that absolute agreement is not estimable because RFU and biovolume/biomass are different quantities on different scales, with no conversion. This is correct.

The review agrees with the following prohibitions:

- Bland–Altman bias/limits;
- Lin’s concordance correlation;
- ICC;
- calibration slope/intercept;
- conversion factor;
- predictive R²/RMSE/MAE/accuracy.

A rank correlation is not a substitute for agreement. The protocol should continue to say so explicitly.

## 5. “Relative concordance”: definition and critique

### 5.1 The 4L.12 definition

The only mathematical definition appears in `STATISTICAL_ANALYSIS_SPECIFICATION.md` §11.1:

> For consecutive biological dates within the same year and season:
> - compute the sign of the change in the biological endpoint;
> - compute the sign of the change in the sensor daily value between the same two dates;
> - count concordant pairs (excluding zero changes);
> - report the proportion and the number of pairs.

Formally, for consecutive dates \(t_i, t_{i+1}\):

\[
\Delta B_i = B_{i+1} - B_i,\qquad \Delta S_i = S_{i+1} - S_i
\]

A pair is concordant if \(\operatorname{sign}(\Delta B_i) = \operatorname{sign}(\Delta S_i) \neq 0\). The proposed statistic is:

\[
C = \frac{\#\{\text{concordant pairs}\}}{\#\{\text{concordant} + \text{discordant pairs}\}}
\]

with zero-change pairs excluded.

### 5.2 Problems

1. **Not defined in the primary question.** The question says “rank association + relative concordance,” but the formula is only in the statistical specification. A reader of the question cannot know what it means.
2. **Irregular intervals.** Mendota biology is ~14 days; Buffalo Pound is 4–16 days. A sign change over 4 days is treated the same as a sign change over 16 days. The statistic is not comparable across pairs or lakes.
3. **Seasonal trends.** Both variables may rise in spring and fall in autumn, producing high concordance from seasonal co-trend rather than measurement comparability. The protocol says “within season,” but seasonal windows are wide.
4. **Sensor noise near zero.** Sign changes of RFU near the baseline may be noise; sign changes of biovolume near zero may be detection noise.
5. **Zero-change exclusion.** Excluding zero changes can bias the proportion; the rule for near-zero changes is undefined.
6. **Dependence.** Consecutive pairs share dates and are serially dependent; the proportion’s uncertainty is not addressed.
7. **Added value.** Spearman ρ already captures monotonic association. Sign concordance adds a coarse directional check, but not a distinct measurement concept. It may be useful as a descriptive exploratory statistic, but it does not deserve a place in the operational definition of comparability.
8. **Claim risk.** A high concordance proportion may be misread as “agreement” or “the sensor tracks change,” which the data cannot support.

### 5.3 What would be required to retain it

If the team insists on retaining “relative concordance,” the protocol must:

- define it in the primary question document;
- state the formula, tie/zero rule, and seasonal stratification;
- justify why it adds information beyond Spearman;
- report n pairs and a descriptive range;
- label it **exploratory**;
- prohibit “agreement,” “tracking,” and “validation” language.

Even then, the review sees little added value.

### 5.4 Recommendation

**Remove “relative concordance” from the operational definition of comparability.** Replace it with:

> Comparability is operationalised as the direction and magnitude of Spearman’s rank association between same-day sensor values and microscopy-derived abundance, with n and a descriptive uncertainty statement.

If a directional check is desired, retain sign concordance as an **exploratory secondary** analysis, not as a primary definition.

## 6. Recommended reporting for association

For each primary estimand, report:

- n dates;
- number of years/seasons contributing;
- Spearman ρ (tie-corrected);
- number/percentage of tied values in each variable;
- descriptive interval or range (see bootstrap review);
- scatterplot with points, no fitted line (or a clearly labelled visual smoother);
- range/IQR of both variables;
- a statement that ρ is a rank association, not agreement/validation/prediction.

Do not report:

- “strong/weak/moderate” labels without a pre-specified benchmark;
- p-values;
- R² as “variance explained” in a causal sense;
- “agreement” or “accuracy”;
- a regression equation as a calibration.

## 7. Findings

| ID | Finding | Severity |
|---|---|---|
| B1 | The six concepts are mostly well separated; absolute agreement/prediction correctly refused | Pass |
| B2 | “Strength” remains undefined in the question | Major |
| B3 | “Relative concordance” is under-defined and adds little | Major |
| B4 | Pearson log is arbitrary and unnecessary unless justified | Minor–Moderate |
| B5 | Non-monotonicity is not assessed | Moderate |
| B6 | Ties and range restriction are not explicitly reported | Moderate |
| B7 | Claims matrix correctly prohibits agreement/validation language | Pass |

## 8. Governance

- **Protocol: PROPOSED — NOT APPROVED.**
- **Gate 2: PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- No decision is approved by this review.
- No analysis is authorised until the required revisions and D-15 approval are recorded.
