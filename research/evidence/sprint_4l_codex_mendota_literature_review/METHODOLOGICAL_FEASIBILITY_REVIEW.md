# Methodological Feasibility Review

## Scope

This is a design critique, not an analysis. No event labels or intervals were built, no sample counts or detector performance were calculated, and no protocol changes are proposed. Recommendations below identify evidence needed for a future readiness decision.

## 1. Outcome and event definition

An independently measured microscopy outcome is plausible: published Mendota work reports taxonomic identifications, cell densities and calculated biovolume. Before any confirmatory evaluation, one endpoint must be specified from the exact package fields. It should state the taxonomic scope, abundance metric, aggregation, treatment of uncertain/unresolved taxa, zero and below-detection values, unit, threshold source, and whether the event means a cyanobacterial abundance episode, a harmful bloom, a toxin event, or another management event. These outcomes are not synonymous.

The reference event cannot be defined from phycocyanin/chlorophyll if those channels are predictors or baselines. Nor should a continuous high phycocyanin interval be treated as independent biological truth when microscopy is the intended endpoint. If no independent threshold can be justified, the project can evaluate prediction of continuous abundance at sample times (a different estimand), but it cannot claim independent bloom-event warning.

## 2. Interval-censored onset and unequal biological intervals

With discrete visits, if the outcome is below a criterion at one visit and above at a later visit, the onset is only bounded between visits; its exact time is unknown. Missing visits widen the bound; brief episodes between visits may never be observed. Biweekly peak-season and monthly non-summer sampling therefore do not support point-dated onset unless an independent continuous reference exists. Any onset uncertainty comparable to or longer than a claimed warning horizon undermines the claim that one method warned earlier.

Observation exposure should be explicit. Event-free time cannot simply include all dates without positive/negative biological coverage. The last confirmed sample below threshold and first above are not proof of the unobserved interval's state. Non-bloom intervals should be defined conservatively from valid observation support, with seasonal windows, missingness, and sampling effort accounted for. If the research aim treats continuous periods between samples as observed non-events, the reference data do not establish that assumption.

## 3. Depth and spatial mismatch

Microscopy is a deep-hole 0–8 m integrated sample. Published pigment sensors are suspended at one point near the surface; sensor depth is inconsistent across sources (1.0 m in the 2020 paper, 0.5 m in EML documentation referenced by the independent sensor inventory). A buoy near the deep hole is not a lake-wide sampling design. Cyanobacteria may be vertically stratified, surface-accumulate, advect, or form localized shoreline scums. A detector trained against a single composite must be described as predicting that composite-site endpoint, not all-lake/public-health blooms. Depth/time-specific pairing and a representativeness justification are required.

## 4. Seasonality, autocorrelation, and ecological nonstationarity

Mendota is strongly seasonal. NTL sampling is seasonal and sensor deployment is ice-free/seasonal. Temperature, stratification, pigment, oxygen, wind and biology co-vary with season and physical mixing. A relationship-change alarm may detect predictable seasonal transitions rather than unusual bloom risk. Seasonal baselines, calendar eligibility, and seasonal phase need to be specified without allowing future data to leak into current estimates.

Independent ecological changes are also documented: the Mendota record includes large drought/nutrient variation, spring phytoplankton succession changes, and invasion-associated shifts in Cyanobacteria phenology and food-web state (Carey et al. 2016; Rohwer et al. 2023). Such shifts may be biologically meaningful but violate a stationary calibration assumption. Sensor replacement, maintenance and fouling can create a second, non-biological form of change. A relationship-change signal may respond to either; it needs source attribution safeguards and explicit handling of known instrument eras.

## 5. Sensor outcomes and conventional comparators

Chlorophyll and phycocyanin fluorescence are natural operational comparators because they are conventional water-quality monitoring signals and have high-frequency availability. But the current instrument transition in 2019 is documented to change RFU magnitude substantially. A fair threshold comparison needs calibration/homogenization evidence or a detector and baseline restricted to compatible measurement eras. Chlorophyll is not cyanobacteria-specific; phycocyanin is a proxy, not cell count, taxonomic composition, or toxin.

Single-variable thresholds must be chosen using training data (or a defensible external threshold) and then frozen for held-out evaluation. Persistence-based alarm rules, rolling quantiles, EWMA/CUSUM or other conventional methods are reasonable comparators only if an authorized protocol defines them. Their available measurement histories differ: a model with only 2019–2020 pH/turbidity cannot be compared on the same exposure to a long-era temperature baseline without restricting all methods to common support or clearly separating comparisons.

## 6. Leakage and validation

Minute-level rows are not independent test cases. Randomly splitting timestamps places adjacent autocorrelated samples from the same bloom, season, or sensor deployment in train and test. Threshold tuning on the full period, choosing a detector after inspecting test years, using future normalization/seasonal averages, or deciding event thresholds after viewing alarms all leak information. Rolling indicators should be computed strictly from data available as of each origin, with a predeclared minimum history and no centered filters or backward interpolation.

The primary temporal test should hold out whole years or temporally contiguous blocks; threshold and hyperparameter selection must occur only in training years, preferably nested/blocked. If a lake-generalization claim is made, Mendota alone cannot test it; a held-out lake with harmonized endpoint and measurement design would be necessary. With only one lake, inference is about its observed record and should avoid claims of general freshwater performance.

Events, not sensor timestamps, are the independent units for event sensitivity and lead time. Alarm days within the same episode must be deduplicated under a prespecified rule. Uncertainty should account for event-level clustering, seasons, year-to-year variability, interval censoring, and threshold-estimation uncertainty. Use confidence/credible intervals and calibration as appropriate, with limitations stated.

## 7. Common false-alarm comparison

A “matched false-alarm rate” is undefined without its denominator and unit. It could mean false alarms per eligible non-event day, per independent non-event episode, or proportion of non-event origins alerted. These yield different operating points when alerts persist. Each method must share:

- biological endpoint and independent adjudication rule;
- prediction origin schedule and eligibility/exposure denominator;
- forecast horizon and permissible warning window;
- treatment of onset interval uncertainty and censoring;
- alarm persistence, merging/deduplication and cooldown rule;
- held-out years and calibration subset; and
- definition of a false alarm and uncertainty method.

Thresholds should be chosen from training-only predictions at an operating point, then assessed on untouched years. Comparing apparent test-set performance at a threshold tuned to test false alarms biases the result. If the goal is exactly matched test false-alarm rates, report this as a prespecified operating-point comparison with confidence intervals; do not hide that thresholds were tuned or imply prospective deployment performance from retrospective matching.

## 8. Number of independent events and non-event exposure

The number of sensor minutes is not the number of blooms. Independent event count is a property of the endpoint criterion and sampling years and must be established without tuning the criterion to get a convenient answer. This review does not estimate it because event classification and data acquisition are prohibited. Do not invent a universal minimum-event count. Before Gate 2, show how the actual number of independent event episodes, interval widths, held-out years, non-event exposure, and possible false alarms determine uncertainty and test power/precision for the intended claim. If uncertainty is too wide to distinguish meaningful warning improvement from chance, re-scope to exploratory description through governance, not after seeing results.

## 9. Is there a feasible design?

**Plausible only conditionally.** The most credible pathway is a restricted-period, era-aware retrospective comparison of a fully specified relationship-change alert and a small prespecified set of conventional/persistence baselines against an independent microscopy abundance event. Use only common biological and sensor support with known QC, a horizon longer than the effective sampling interval, blocked held-out years, training-only threshold selection, interval-censored onset handling, and event-level uncertainty. This is a conceptual feasibility pathway, not a protocol change or authorization.

The design becomes unsuitable for confirmatory early-warning claims if (i) version-specific microscopy fields cannot distinguish abundance and taxa, (ii) event criteria cannot be set independently of predictors, (iii) most onsets are unresolved on a scale as wide as the proposed horizon, (iv) independent events/non-event exposure are too sparse for a meaningful operating-point estimate, or (v) valid common sensor/biology support collapses after era/QC restrictions. These findings would not invalidate Mendota as an ecological record; they would invalidate this particular confirmatory estimand.

## Minimum evidence before readiness review

- Authenticated exact biological package, schema, version, temporal coverage, methods and QC.
- A pre-analysis endpoint specification sourced independently of predictor data.
- Observation-effort and non-event support rules that do not treat unsampled time as verified negative.
- Full matched coverage/measurement-era table, exact station/depth and sensor calibration/QC records.
- Literature novelty table comparing exact methods and outcome definitions.
- Blinded event/exposure feasibility counts and interval widths, with event-level uncertainty/precision calculations; no arbitrary count threshold.
- A frozen validation and threshold-selection plan using held-out years and explicit false-alarm denominator.

**Feasibility assessment:** promising, but not confirmatory-ready. Sparse independent biology and single-site representativeness are structural limits; missing package metadata/QC, endpoint definition, calibration and exact overlap are resolvable evidence gaps.
