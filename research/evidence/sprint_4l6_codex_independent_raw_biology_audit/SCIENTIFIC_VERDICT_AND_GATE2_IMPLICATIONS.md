# Scientific verdict and Gate 2 implications

## Independent verdicts

| Question | Assessment | Basis |
|---|---|---|
| Is raw-data audit technically reproducible? | **Yes, mostly** | Independent read, hashes, dimensions, distributions and structural counts agree. |
| Are calculations correct? | **Mostly** | 469/177 include blank taxon/genus values; named nonblank counts are 468/176. Relative sums, repeats, dates and numeric results reproduce. |
| Are anomaly interpretations justified? | **Partly** | Correct to flag. Near-200 cause and zero encoding unresolved. Coelastrum is incompatible with documented units, but exact failure type is unidentifiable. |
| Is cyanobacterial biovolume a defensible primary exploratory endpoint? | **Conditionally** | Candidate volumetric indicator from microscopy, but computed/identified, taxonomically nonstationary, depth integrated, and not bloom ground truth. |
| Seasonal/multi-week exploration? | **Conditionally suitable** | Repeated long-term observations and actual biology; poor precision for short event timing, and substantial data QC still required. |
| Confirmatory original early-warning question? | **No, on this evidence** | Sparse/uneven biology, interval-censored onset, no independent bloom/non-bloom adjudication, unmatched depth/station and unresolved source anomalies. |

## Gate 2 status

Gate 2 stays **PAUSED / NOT APPROVED — Option C**. This independent audit does not authorize labels, modeling, threshold selection, or protocol change. It recommends no Gate 2 pass based on raw biological dataset 88.31 alone.

## Prior-art and originality constraint

Lake Mendota already has published season-ahead and sub-seasonal forecasts of cyanobacterial biomass/abundance using its long-term record and climate/hydroclimate predictors. Beal et al.'s sub-seasonal work forecasts the July–August seasonal mean from spring/June predictors; it is a different target/horizon than daily event onset, but it means this dataset is not an untouched forecasting testbed. Community ecology studies also use the same LTER microscopy series and describe its method, seasonal succession, rapid turnover and detection limitations. A recent broad empirical-lake early-warning study includes Mendota, although with a different deeper tube/net series and monthly processing; it reports limited empirical applicability of early warning methods. Thus a new comparison of multivariate relationship-change indicators against univariate thresholds would need a precise contribution beyond “same false-alarm rate”: distinct validated biological event endpoint, horizon, fair observation exposure, leakage-controlled held-out evaluation, and direct relation to previous season/sub-seasonal forecast studies. None is established by the raw CSV audit, so originality remains unresolved and cannot be claimed from dataset novelty.

Sources: [Beal et al., sub-seasonal cyanobacteria prediction model](https://www.sciencedirect.com/science/article/pii/S156898832100130X); [Hansen & Carey 2015](https://doi.org/10.1371/journal.pone.0115414); [O'Brien et al. 2023, empirical lake early warning signals](https://doi.org/10.1038/s41467-023-43744-8). These works differ in endpoint and horizon; they do not by themselves settle whether the proposed comparison is novel.

## Material threats to future work

1. Undefined `relative_total_biovolume` calculation and unexplained 200% groups.
2. Internally contradictory Coelastrum row and associated group.
3. Exact duplicates at MO 1999-11-22 and repeated taxon rows without replicate/sample IDs.
4. Biomass precision loss at low values and derived rather than independent endpoint.
5. Retrospective and taxonomic changes; mappings differ in authority and may represent changed identification, not just name substitution.
6. Blank station on most rows; depth exceptions; composite-vs-point sensor exposure.
7. Uneven seasonal cadence and 120-day maximum gap; no exact sampling time.
8. No independent bloom adjudication, toxicity data, detection limits, nor verified non-event exposure in this dataset.

## Evidence that could change the decision

Versioned raw laboratory export and row provenance, relative-field denominator/formula, sample/replicate/slide ID mapping, Coelastrum original measurement record and correction trail, documented source for all non-100% groups, systematic date/site/depth metadata, taxonomic correction history and validation, and an independently specified bloom endpoint with enough repeated biological sampling to bound onset and non-event time at the proposed horizon. These are evidence requests, not actions taken here.
