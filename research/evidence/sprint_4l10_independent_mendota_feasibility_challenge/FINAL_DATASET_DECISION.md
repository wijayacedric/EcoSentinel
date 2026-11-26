# Final Mendota Dataset Decision

**Sprint:** 4L.10  
**Gate 2:** PAUSED / NOT APPROVED — option C (Exploratory Only)

## Recommendation

# RETAIN — LIMITED EXPLORATORY USE

**Scope of retention:**
- descriptive seasonal analysis of environmental variables;
- pairwise descriptive comparison of sensor conditions with cyanobacteria biovolume/cell density, with Turner/YSI eras kept separate and the 0.5 m vs 0–8 m limitation stated.

**Explicit rejection:**
- Mendota is **rejected for the original early-warning research question** and for any confirmatory bloom/non-bloom evaluation.
- No labels, event intervals, predictive models, threshold optimisation or hypothesis tests are authorised.

## Why not “supporting data only”?

Pairwise descriptive B is genuinely possible: 123 biology dates have both Turner chlorophyll and phycocyanin, 80 have Turner chlorophyll and DO, and 85 have Turner phycocyanin and DO. That is enough for cautious descriptive comparison, not for validation. Calling it “supporting only” would understate a legitimate exploratory use.

## Why not “reject”?

A has clear value: the sensor record supports descriptive seasonal analysis with 939 Turner-core and 306 YSI-core sensor-only complete dates. A blanket rejection would be too pessimistic for that use.

## Why not “retain for early warning”?

D fails on every necessary condition: no event definition, no time-stamped biology, no depth-resolved biology, no independent bloom adjudication, no verified non-event exposure, no validated sensor crosswalk, and weak sensor-to-biovolume literature. Prior art already covers Mendota high-frequency phycocyanin and seasonal/sub-seasonal forecasting. A new early-warning claim would be neither novel nor testable with the current data.

## Conditions of retention

1. Keep Turner and YSI eras separate; no undocumented correction.
2. Use era-specific, variable-specific denominators; report `unflagged_numeric`, not “validated”.
3. Treat 0.5 m sensors as surface conditions, not 0–8 m biomass.
4. Use pairwise or small (2–4 variable) descriptive comparisons; do not pretend the 7/11-variable biological multivariate sets are adequate.
5. Do not create bloom/non-bloom labels, event intervals or early-warning features.
6. State that the biology is 14-day, date-only and taxonomically non-stationary.
7. Do not claim novelty from matched false-alarm rates or from the existence of Mendota high-frequency data.

## What evidence would change the decision

- Sub-weekly, time-stamped, depth-resolved microscopy or a validated biomass series.
- A protocol-approved bloom/non-bloom definition with independent adjudication and verified non-event exposure.
- A documented Turner/YSI cross-calibration and per-record calibration/maintenance history.
- A defined depth comparator and surface-vs-composite sensitivity analysis.
- A pre-specified, leakage-controlled lead-time validation with adequate event counts.

Without these, the decision remains **RETAIN — LIMITED EXPLORATORY USE**, with **D rejected**.

## Governance

Gate 2 remains **PAUSED / NOT APPROVED — option C**. No labels, event intervals, models, hypothesis tests, threshold optimisation, protocol changes, external contacts, uploads, commits or pushes were made. Raw data and prior evidence remain unchanged.
