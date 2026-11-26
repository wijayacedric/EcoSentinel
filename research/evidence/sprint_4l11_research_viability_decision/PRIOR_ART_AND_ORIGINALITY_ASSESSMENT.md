# Prior-Art and Originality Assessment

**Question under assessment:** Do persistent changes in relationships between freshwater environmental variables provide earlier warning of cyanobacterial blooms than conventional monitoring at comparable false-alarm rates?  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Assessment date:** 2026-11-24

## 1. Search scope and evidence quality

The review used project literature audits (full/abstract/status documented), EDI/NTL metadata and papers, and targeted searches for:

- freshwater cyanobacterial bloom early-warning/forecasting;
- high-frequency in situ sensor monitoring;
- multivariate and relationship-change early-warning indicators;
- matched false-alarm / true-false alarm evaluation;
- empirical EWS performance and negative results;
- Mendota and Buffalo Pound local studies.

Full-text inspection was possible for several primary sources (Gsell 2016; O’Brien 2023; Weinans 2021; Pace 2016; Levi 2025; Carpenter 2022; Buelo 2022 via abstract/analysis code and excerpts). Others were abstract/metadata-limited because publisher pages returned 403 or PDFs were not text-extractable (Recknagel 2025; Fournier 2024; Rousso 2020; Beal 2021/2022; Wilkinson 2018; Cotterill 2019). The source register records the exact status.

**Consequence:** this assessment does not claim a full systematic-review absence of prior work. It distinguishes established findings from “not found in accessible evidence.”

## 2. What is already established

| Area | Established finding | Key sources |
|---|---|---|
| Bloom drivers | Temperature, stratification, light, nutrients, hydrology, mixing and internal loading modulate cyanobacterial blooms; responses are species/context dependent | Visser et al. 2016; Painter et al. 2022/2023; Boyer et al. 2025 |
| High-frequency monitoring | HF sensors can capture short-term changes missed by weekly/biweekly sampling; phycocyanin/chlorophyll RFU are useful relative proxies | Levi et al. 2025; Carpenter et al. 2020/2022; Recknagel et al. 2025; Fournier et al. 2024 |
| HAB early warning/forecasting | Operational/experimental systems already forecast cyanobacteria or hazard exceedance at 1–28-day horizons using HF data and statistical/ML models | Recknagel et al. 2025; Fournier et al. 2024; Beal et al. 2021/2022; Rousso et al. 2020 |
| EWS for algal blooms | Resilience indicators (variance, autocorrelation) can precede experimental blooms; true/false alarm rates have been evaluated | Pace et al. 2016; Wilkinson et al. 2018; Buelo et al. 2022 |
| Empirical EWS limits | EWS often fail or disagree in natural lakes; most indicators may not beat chance; performance depends on preprocessing/resolution | Gsell et al. 2016; O’Brien et al. 2023 |
| Multivariate indicators | Many multivariate resilience indicators exist; no single method is best; performance depends on data length/resolution/noise/observed subset; cross-correlation is sensitive to unobserved variables | Weinans et al. 2021; Dakos et al. 2012 |
| Sensor validation | Phycocyanin–biovolume relationships are often weak/variable; detection limits and composition/biofouling/calibration matter; RFU is sensor-specific | Cotterill et al. 2019; Levi et al. 2025; USGS TM1-D10; YSI/Turner guidance |
| Matched-FAR | Matched false-alarm comparison is a quality requirement, not a novel method; TPR/FPR and alarm-rate evaluations already exist in algal-bloom EWS | Buelo et al. 2022; Gsell et al. 2016; O’Brien et al. 2023 |

## 3. What has been tested and found ineffective or limited

- **Generic EWS in empirical lakes:** Gsell et al. (2016) found that in 44% of 64 EWI cases the indicator failed; agreement among indicators was low; only 3/64 trends were significant in >50% of surrogate comparisons; a priori mechanism knowledge was required. O’Brien et al. (2023) found few critical transitions, most EWS not better than chance, multivariate EWS weakly superior, and a machine-learning EWS poor.
- **Autocorrelation-based EWS:** Buelo et al. (2022) found rolling-window SD provided advanced warning in most variables, while AR(1) performed poorly; the study used experimental lakes and explicit TPR/FPR. This is close to EcoSentinel’s matched-FAR idea and shows that simple variance indicators may be the stronger conventional comparator.
- **Multivariate relationship indicators:** Weinans et al. (2021) found no single multivariate indicator best; performance depends on data length, resolution, noise, observed subset and transition type; cross-correlation was most affected by unobserved variables. This directly challenges an unqualified “relationship-change” claim.
- **Phycocyanin as a biovolume proxy:** Cotterill et al. (2019) found weak (<R² 0.4), variable relationships and species-specific detection limits; Levi et al. (2025) found calibration, composition, biofouling and low-concentration limitations. A phycocyanin RFU series is not a validated biomass measurement.
- **Mendota-specific:** Carpenter et al. (2020) found two alternative stable states and stochastic transitions in phycocyanin, with annual states not correlated with annual P input; Carpenter et al. (2022) found variable 1–60-day lags and stationary extreme behaviour. This warns against simple deterministic precursor claims.

## 4. What remains unresolved

The following remain unresolved, but their absence is **not** evidence of novelty:

1. Whether any published study tests the exact combination of **persistent relationship/coupling changes + independent biological event adjudication + interval-censored onset + matched-FAR evaluation** in cyanobacteria.
2. Whether relationship-change indicators add value over strong univariate/variance baselines at matched FAR in real lakes.
3. Whether the relationship-change signal survives seasonality, autocorrelation, hydrology/management, sensor artefacts and depth mismatch.
4. Whether a two-lake sensor–microscopy measurement comparison (Mendota vs Buffalo Pound) has been published in this exact form.

Full-text review of Recknagel 2025, Fournier 2024, Rousso 2020 and related studies is still needed before any strong originality claim. The accessible evidence already shows high topical overlap.

## 5. What specific contribution could EcoSentinel make?

**Not** a claim of a new early-warning algorithm or a new sensor. The only defensible near-term contributions are:

- **A rigorous measurement/comparability study:** how well surface sensor proxies represent independent cyanobacteria biovolume in Mendota (0.5 m vs 0–8 m) and Buffalo Pound (0.8 m vs 0.8 m), stratified by season, sensor era and QC. This addresses a core blocker and can produce a negative/limited result.
- **A feasibility/evidence-gap study:** what would be required to test relational early warning, with a reproducible audit of labels, exposure, temporal resolution and matched-FAR design. This is methodologically useful but meta-scientific.
- **A negative result** if the original question could be tested: relational indicators do not outperform conventional monitoring at matched FAR. This is not currently possible because the labels/exposure do not exist.

A “relationship-change early-warning method” contribution is **not** currently defensible: it is not differentiated from existing multivariate EWS/forecasting, and it cannot be validated on the available data.

## 6. Distinguishability from prior art

| Candidate difference | Distinguishable? | Assessment |
|---|---|---|
| Using Mendota/Buffalo Pound data | Weak | Both systems already studied; site novelty is weak. |
| Using high-frequency sensors | No | Established in HAB monitoring/forecasting. |
| Using multivariate models | No | Established; many variants. |
| Using rolling correlation/coupling change | Potentially, but unproven | Weinans et al. evaluated related multivariate indicators; application to cyanobacteria with independent labels is not confirmed. |
| Matched-FAR comparison | No, as novelty | Quality requirement; Buelo et al. already reports TPR/FPR for algal-bloom EWS. |
| Independent biological labels + interval-censored onset | Potentially meaningful, but unmet | The project does not have them; prior studies may. |
| Two-lake depth/era measurement contrast | Potentially modest | A local measurement contribution, not an early-warning method. |

## 7. Source-quality assessment

| Source | Type | Access | Use |
|---|---|---|---|
| Gsell et al. 2016, PNAS | Peer-reviewed empirical EWS | Full PMC | Strong negative evidence on EWS reliability |
| O’Brien et al. 2023, Nature Communications | Peer-reviewed empirical EWS | Full HTML | Strong negative evidence; Mendota included |
| Weinans et al. 2021, Scientific Reports | Peer-reviewed simulation/methods | Full HTML | Multivariate indicator limits |
| Pace et al. 2016, PNAS | Peer-reviewed whole-lake experiment | Full PMC | Proof-of-concept EWS; controlled |
| Buelo et al. 2022, Ecological Applications | Peer-reviewed EWS/algal blooms | Abstract/excerpts + analysis code; publisher 403 | Closest matched-alarm-rate algal EWS |
| Recknagel et al. 2025, Water Research | Peer-reviewed HF+ML early warning | Abstract/metadata; full 403 | Close comparator; high overlap |
| Fournier et al. 2024, Water Research | Peer-reviewed LSTM forecasting | Abstract/metadata; full 403 | Close comparator; PC proxy target |
| Rousso et al. 2020, Water Research | Systematic review | Abstract/metadata; full 403 | Field landscape; validation gaps |
| Carpenter et al. 2020/2022 | Peer-reviewed Mendota HF phycocyanin | 2020 abstract; 2022 full PMC | Local prior art; stochasticity/sensor changes |
| Cotterill et al. 2019 | Peer-reviewed sensor validation | Abstract; full 403 | Weak/variable phycocyanin–biovolume |
| Levi et al. 2025 | Peer-reviewed sensor validation | Full PMC | Calibration/biofouling/composition limits |
| USGS TM1-D10 | Authoritative technical guidance | Full HTML | RFU/proxy/QA principles |
| Beal et al. 2021/2022 | Peer-reviewed Mendota forecasts | Search-indexed/4L.6; full 403 | Seasonal/sub-seasonal prior art |

## 8. Bottom line

The field is crowded. High-frequency cyanobacterial early warning, multivariate indicators, matched false-alarm evaluation and EWS for algal blooms all exist. EcoSentinel’s **original combination** may be a modest methodological gap, but it is not established as novel, and it is not testable with the current evidence. The project cannot claim originality from matched FAR, a new algorithm, or the Mendota/Buffalo Pound datasets alone.

The strongest realistic contribution is a **narrowed measurement/comparability study**, not an early-warning validation.
