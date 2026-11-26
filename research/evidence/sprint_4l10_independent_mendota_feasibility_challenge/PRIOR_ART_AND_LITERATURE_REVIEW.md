# Targeted Literature and Prior-Art Review

**Sprint:** 4L.10  
**Gate 2:** PAUSED / NOT APPROVED — option C (Exploratory Only)

## 1. Scope

The review targeted:

1. high-frequency freshwater sensor data and cyanobacterial monitoring;
2. phycocyanin/chlorophyll sensor validation against biological measurements;
3. multivariate environmental relationships and ecological early-warning signals;
4. Lake Mendota-specific prior work and forecasting;
5. sensor-to-biological validation and sampling-frequency limitations.

## 2. Mendota-specific prior art

### Carpenter et al. (2020), *Limnology and Oceanography Letters*

One-minute phycocyanin observations at a central Mendota station, ice-free seasons 2008–2018. Stochastic-dynamic models found two alternative stable states and random factors larger than the state difference; transitions were abrupt and apparently stochastic. Annual state magnitudes were not correlated with annual phosphorus input, but daily phycocyanin was correlated with phosphorus input, precipitation and wind at lags of 1–15 days. Multiple years of high-frequency data were needed to discern patterns in noise-dominated dynamics.

**Implication:** Mendota already has a high-frequency phycocyanin research record; the system is stochastic and not a simple deterministic bloom machine. A daily sensor–biology audit cannot claim novelty from the existence of high-frequency data.

### Carpenter et al. (2022), *PNAS*

Daily phycocyanin 2008–2021, with nighttime means (00:00–04:00 and 22:00–24:00) to minimize daytime quenching; different sensors and maintenance regimes were used across years; daily log RFU was z-scored within year. Cross-correlations of P load with phycocyanin were 13–28 days; extreme P-load events were followed by extreme phycocyanin after 1–60 days, but the best Pareto model for phycocyanin extremes was stationary with no significant precipitation/P-load effects.

**Implication:** daily averaging without nighttime selection may be biased by quenching; sensor/maintenance regimes matter; lead-time signals exist but are variable and not a validated bloom-onset rule.

### Beal et al. (2021, 2022)

Mendota has published sub-seasonal (two-month) and season-ahead cyanobacteria abundance forecasts using pre-season/climate predictors. These target seasonal abundance, not daily bloom onset.

**Implication:** Mendota is not an untouched forecasting testbed. A new early-warning claim would need a precise contribution beyond seasonal/sub-seasonal forecasting, not just a different model or matched false-alarm rate.

### O'Brien et al. (2023), *Nature Communications*

Nine long-term lake plankton datasets, including Mendota, were classified into critical transitions, non-critical transitions and stationary dynamics. Few critical transitions were found; different trophic levels changed differently; most EWS methods did not perform better than chance; multivariate EWS were weakly superior; a machine-learning EWS performed poorly. Prediction success for the best methods was around 0.59–0.71 in monthly/yearly data, not a strong operational warning.

**Implication:** empirical EWS are hard; Mendota’s inclusion in this work means a generic EWS claim is not novel. A 14-day, date-only biology series is even less suited to daily onset validation.

### Hansen & Carey (2015) and 4L.6 biological audit

The NTL phytoplankton series has been used for community ecology; the sampling is biweekly summer/monthly non-summer, 0–8 m integrated for Mendota, with microscopy and taxonomic change. The 4L.6 audit found 402 Mendota dates, 468 nonblank taxa, 176 nonblank genera, 14 relative-total groups near 200%, a catastrophic Coelastrum row, repeated records and taxonomic non-stationarity.

**Implication:** the biology is a genuine long-term record but not a clean, event-labelled, daily ground truth.

## 3. Sensor validation literature

### Cotterill et al. (2019), *New Zealand Journal of Marine and Freshwater Research*

Compared a handheld Cyclops-7 phycocyanin sensor with cyanobacteria biovolume across five lakes and a river (2016 n=121; 2017 n=63) and four species in the laboratory. The phycocyanin–biovolume relationship was generally weak (<R²=0.4) and varied among lakes and years, except at high biovolume. Detection limits differed among species; the biovolume detection limit was above alert thresholds for two of four species. The sensor was judged to have limited utility, possibly useful for on-site confirmation of alert-level exceedances.

**Implication:** a phycocyanin RFU series is not a validated cyanobacteria biovolume measurement. B can be descriptive, not quantitative validation.

### Levi et al. (2025), *Open Research Europe*

Validated 24 chlorophyll and 12 phycocyanin Cyclops-7F sensors in mesocosms. Fluorescence was affected by biofouling, phytoplankton composition, equipment and low concentrations; calibration varied; high phycocyanin interfered with chlorophyll; nighttime data were used to reduce quenching; high-frequency sensors captured events missed by biweekly/monthly sampling. The authors emphasize site-specific calibration and caution that in-vivo measurements are semi-quantitative.

**Implication:** high-frequency sensors can reveal short-term change, but only with calibration/QC; the Mendota daily averages without nighttime selection and without calibration cannot be treated as validated biomass.

### USGS TM1-D10 (Foster et al. 2022)

Algal fluorometers measure a fluorescence response, not algal abundance/biomass; RFU is sensor-specific; relationships vary with species, physiology, temperature and light; nonphotochemical quenching causes diurnal variability; biofouling and calibration drift require site-specific QA; different makes/models are not equivalent even in the same units.

### YSI technical guidance (2019/2021)

YSI notes that 6-series and EXO phycocyanin sensors use different technologies, ranges and firmware; RFU is a relative unit; users should read trends/patterns rather than absolute values; turbidity, CDOM/fDOM and biofouling can interfere.

### Hodges et al. (2018), Rousso et al. (2021), Watras et al. (2017)

These studies (identified; abstract/metadata-level in this sprint) report manufacturer-, temperature- and morphology-dependent phycocyanin fluorescence, light-induced quenching errors, and the need for temperature compensation. They reinforce the same conclusion: RFU is not a universal abundance unit.

## 4. Early-warning literature

- **Pace et al. (2016), PNAS:** whole-lake nutrient-enrichment experiment; resilience indicators (SD, autocorrelation) gave alarms 17 days before the bloom maximum; stopping nutrients reversed the bloom. This required controlled enrichment, a reference lake, high-frequency pigments and a pre-specified decision rule.
- **Wilkinson et al. (2018), Ecological Monographs:** early-warning signals preceded cyanobacterial blooms in multiple whole-lake experiments, 1–57/61 days before blooms; context-dependent.
- **O'Brien et al. (2023):** empirical lake EWS often poor; most indicators not better than chance; multivariate weakly superior.
- **Recknagel (2025):** high-frequency in situ monitoring plus intelligible machine learning for Lake Müggelsee; identified as prior art, full text not accessible in this environment. It confirms that HF sensor + ML early warning is an active field, not a Mendota-specific novelty.

**Implication:** early warning is possible in controlled/high-frequency settings, but the Mendota record lacks the event definition, time-stamped biology and validation design needed to claim it. A matched false-alarm rate alone is not novelty.

## 5. What legitimate opportunity remains?

Mendota offers:

1. **A descriptive seasonal analysis** of environmental variables, with era-specific sensor series.
2. **A pairwise descriptive comparison** of Turner chlorophyll/phycocyanin (or DO/temperature) with cyanobacteria biovolume/cell density, explicitly framed as surface-vs-composite and proxy-based.
3. **A methods/measurement paper** on sensor–biology comparability, if framed as a negative/limited validation rather than a bloom forecast.

It does **not** offer a legitimate early-warning validation opportunity without new biological event data, time-stamped/depth-resolved sampling and an independent adjudication protocol.

## 6. Novelty caution

Do not claim novelty from:

- using Mendota high-frequency data (already done by Carpenter et al.);
- seasonal/sub-seasonal cyanobacteria forecasting (already done by Beal et al.);
- generic EWS indicators (O'Brien et al. tested them, including Mendota);
- matched false-alarm rates alone;
- a new model class without a validated event endpoint and fair evaluation.

A defensible contribution would need a precise, evidence-based gap: e.g., a validated sub-weekly bloom-onset endpoint, a sensor cross-calibration with uncertainty, or a depth-resolved surface-to-composite comparison. None is established by the current data.
