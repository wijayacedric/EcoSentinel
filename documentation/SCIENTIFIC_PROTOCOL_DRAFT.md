# EcoSentinel Scientific Protocol Draft

**Status:** Draft for GPT/Claude/user review (Gate 3 provisional preparation in progress)  
**Date:** 2026-11-22 (updated)  
**Gate status:** Gate 1 conditionally accepted; Gate 2 in progress; Gate 3 provisional draft only.  
**Scope:** Defines the proposed methodology for the EcoSentinel SciFest project. No modeling should be considered scientifically defensible until this protocol is reviewed and approved. **All bloom-event labels, outcome definitions, and evaluation claims dependent on Gate 2 remain provisional until independent evidence is approved.**

## 1. Research question

> Can persistent changes in relationships between freshwater environmental variables provide earlier warning of cyanobacterial blooms than conventional monitoring, at comparable false-alarm rates?

### Operational definitions (to be approved)

| Term | Proposed definition | Decision needed |
|---|---|---|
| **Bloom event** | A period when cyanobacterial risk exceeds a pre-specified threshold, based on independent evidence where possible. | **CRITICAL:** define threshold and evidence source. |
| **Early warning** | An alert issued at least *H* hours/days before bloom onset, within a defined warning window. | Choose H and warning window. |
| **Persistent change** | A relationship/statistical change exceeding a threshold for at least *P* consecutive intervals or a minimum duration. | Choose persistence rule. |
| **Comparable false-alarm rate** | Methods compared at matched false-alarm rates (or ROC/PR operating points with explicit FAR). | Choose target FAR(s). |
| **Conventional monitoring** | Baseline univariate threshold/rule-based monitoring on chlorophyll/phycocyanin/turbidity/DO as available. | Confirm baseline set. |

## 2. Data

- **Primary dataset:** Buffalo Pound Lake buoy/meteorological data, 2014–2021 (FRDR DOI 10.20383/103.01100, CC BY 4.0).
- **Raw data:** preserved unchanged in `data/raw/`.
- **Season:** ice-free deployments only; season boundaries vary by year.
- **Resolution:** 15 min (2014), 10 min (2015–2021).

### Known limitations

- No nutrients in buoy dataset; mechanistic claims limited.
- Chlorophyll and phycocyanin are RFU proxies, not lab-quantified concentrations.
- Single site (Buffalo Pound Lake); generalizability limited.
- Sensor outages/quality flags (M/C/A2/A3/A4/A5/A6/B6/B7) must be handled explicitly.
- 2019 deep sensors largely unavailable; 2015 shallow DO limited; 2021 PARW1 and deep chlorophyll RFU limited.

## 3. Bloom ground truth (CRITICAL decision)

A defensible bloom label is required before evaluation. **Do not derive labels from the same predictor signal without justification and sensitivity analysis.**

### Options to evaluate

| Option | Pros | Cons | Risk |
|---|---|---|---|
| **Independent lab/agency records** (preferred) | Independent ground truth; scientifically stronger | May be unavailable or temporally coarse | Low bias if available |
| **Phycocyanin RFU threshold** | Available in dataset | Circular if phycocyanin also used as predictor; RFU not calibrated concentration | **HIGH** |
| **Chlorophyll RFU threshold** | Available | Proxy only; circularity risk | **HIGH** |
| **Composite proxy with holdout/sensitivity** | Practical if no independent labels | Still proxy-based; must be transparent | **MEDIUM/HIGH** |
| **Expert-labeled events from multiple signals** | Uses domain judgment | Subjective; must document criteria | **MEDIUM** |

**Required:** document the chosen definition, threshold, data source, and sensitivity to alternative definitions.

## 4. Data handling rules

- Preserve raw data; all cleaning produces derived files in `data/processed/`.
- Parse `DateTime` as local/consistent timestamp; document timezone assumption.
- **M/C flags:** treat as invalid/missing unless specific review justifies otherwise.
- **A2:** PAR below range adjusted to zero - keep as valid adjusted value, document.
- **A3/A4:** inspect before use; A4 2015 underwater PAR shading requires special handling.
- **A5:** unusual rainfall may be genuine - retain with note.
- **A6/B6:** use corrected conductivity (A6) where appropriate; do not mix raw/corrected without documentation.
- **B7:** potential fouling-related pigment/turbidity spike - do not silently drop; run sensitivity analyses with/without B7 periods.
- Missing data: no blind interpolation across long gaps; use gap-aware methods and report gap impact.

## 5. Leakage prevention

- Split by **time/event**, never random row/window shuffle.
- No future information in features (rolling windows must be backward-looking only).
- Normalization/scaling parameters computed on training data only.
- No tuning on test events.
- Event-level evaluation: overlapping windows from same event not treated as independent test samples.
- Report all preprocessing steps and seeds.

## 6. Baselines (required before multivariate model)

| Baseline | Purpose |
|---|---|
| Persistence | Predict current state continues |
| Univariate phycocyanin threshold | Conventional bloom proxy |
| Univariate chlorophyll/turbidity/DO thresholds | Conventional monitoring comparators |
| Rolling z-score / simple anomaly | Simple change detector |
| Logistic regression on lagged single variables | Simple supervised baseline |

All baselines evaluated under same splits, event definitions, and FAR-matched comparison.

## 7. Candidate multivariate methods (after baselines)

Start interpretable:
- Rolling correlation/covariance change
- PCA stability / reconstruction error
- Mahalanobis distance
- Multivariate logistic regression with lagged features
- Simple change-point or regime-shift indicators

Complex models (LSTM/transformers/etc.) only if justified by data size, interpretability, and baseline outperformance.

## 8. Evaluation

Report:
- False-alarm rate (FAR)
- Missed-bloom rate / false-negative rate
- Sensitivity/recall
- Specificity
- Precision
- Lead time (median, IQR, per-event)
- Event-level detection performance
- Performance across independent years/events
- Uncertainty/confidence intervals where possible

**Primary comparison rule:** compare at comparable false-alarm rates. An earlier detector with much higher FAR is not automatically superior.

## 9. Reproducibility

- All experiments runnable from documented commands.
- Pin dependencies / record environment.
- Save configs, seeds, split definitions, and output artifacts.
- Tests for data parsing, flag handling, split integrity, and metric calculations.

## 10. Review checkpoints

- **Checkpoint A:** Audit code fixed, data quality verified.
- **Checkpoint B:** Bloom definition and evaluation protocol approved (GPT/Claude/user).
- **Checkpoint C:** Baselines implemented and evaluated.
- **Checkpoint D:** Multivariate method evaluated at matched FAR.
- **Checkpoint E:** Final SciFest package with limitations and honest results.

## 11. Immediate decisions needed

1. What is the bloom-event ground truth source/definition?
2. What warning horizon and persistence rule are scientifically meaningful?
3. What false-alarm rate(s) are acceptable for comparison?
4. Which variables are eligible predictors vs. label-related proxies?
5. How should 2019 deep-sensor outage and other major gaps be handled?