# Prior-Art and Novelty Assessment

## Search scope and interpretation

The review searched NTL-LTER/EDI catalog and protocol pages, original papers indexed by DOI/title, peer-reviewed Mendota forecasting and high-frequency studies, freshwater EWS research and critiques, temporal-sampling literature, and relevant supplementary material where accessible. Search strings and access limitations are recorded in `SEARCH_LOG.md`; source details are in `LITERATURE_AND_SOURCE_REGISTER.csv`.

“Earlier warning” in EcoSentinel should be distinguished from (a) estimating same-time phytoplankton abundance, (b) one-step prediction of a continuous pigment series, (c) seasonal average forecasting, and (d) early-warning indicators for long-lasting critical transitions. These have different targets, origins, horizons and false-alarm units. Literature overlap is material, but not necessarily complete identity of estimand.

## Direct Mendota prior art

### Seasonal/subseasonal biomass prediction

Beal et al. developed Mendota summer cyanobacteria biomass forecasts from seasonal predictors and reported a sub-seasonal model forecasting July–August average biomass using June information ([Harmful Algae 108, 102100, 2021, DOI 10.1016/j.hal.2021.102100](https://doi.org/10.1016/j.hal.2021.102100)). Beal et al. then examined whether season-ahead forecasts improve beach management, including forecast skill and beach-closure outcomes ([DOI 10.1080/10402381.2022.2084799](https://doi.org/10.1080/10402381.2022.2084799)). This substantially overlaps cyanobacteria warning and forecast framing, but the forecast origin is seasonal and target is seasonal abundance/management risk, rather than a rolling relationship-change signal evaluated at matched false-alarm rates against independent microscopy event onset.

### High-frequency pigment dynamics and lagged environmental relationships

Carpenter et al. used minute-resolution Mendota phycocyanin and chlorophyll sensors during 2008–2018. Their drift-diffusion-jump models report abrupt low/high pigment regimes and noise-dominated dynamics; daily phycocyanin was correlated with phosphorus input, precipitation and wind at lags of about 1–15 days ([Limnology and Oceanography Letters, 2020, DOI 10.1002/lol2.10152](https://doi.org/10.1002/lol2.10152)). This is direct overlap with high-frequency sensor records, short lags and variable relationships, but pigment is both the response and the biological proxy in that work. It does not provide continuous independent microscopy validation of bloom onset.

Carpenter et al. analyzed daily precipitation, discharge, phosphorus load and phycocyanin records and found lagged associations, with P-load extremes followed by phycocyanin extremes at variable delays of 1–60 days within years ([PNAS 119:e2214343119, 2022, DOI 10.1073/pnas.2214343119](https://doi.org/10.1073/pnas.2214343119)). A follow-on analysis of high-frequency phycocyanin during 2019–2021 reports YSI EXO2 sensors at 1.0 m below the buoy, cleaning/calibration every 1–2 weeks, and minute-resolution wind and temperature alongside pigment ([DOI 10.1002/ecs2.4903](https://doi.org/10.1002/ecs2.4903)). Together these studies demonstrate that Mendota environmental-pigment relationships and lag structure have already been investigated; they also show variable delays and continued post-2019 analysis in the new sensor era. A new analysis must differentiate itself from lagged cross-correlation/association, and show that it predicts independent biological exceedance prospectively rather than explains co-variation retrospectively.

### Continuous-series forecasting

Liu et al. presented a wavelet-preprocessed LSTM (WLSTM) for algal bloom forecasting using Mendota data and reported one-step predictions at hourly, daily and monthly resolutions ([Water Research 219:118591, 2022, DOI 10.1016/j.watres.2022.118591](https://doi.org/10.1016/j.watres.2022.118591)). This is a close prior-art challenge for high-frequency Mendota algal prediction. It appears to forecast an algal signal/abundance series; it is not equivalent to a prospective event-warning evaluation against independent species-resolved microscopy. Full methods, data source, split scheme, target and leakage handling must be reviewed before asserting a precise difference. This article lowers any broad novelty claim for “using multivariate/time-series patterns to forecast Mendota algae.”

### Long-term phytoplankton succession and ecology

Beversdorf et al. monitored Mendota weekly in 2010–2011 and paired cyanobacterial community profiles with environmental conditions and measured microcystin; their study illustrates both denser targeted sampling and the difference between taxonomy, abundance and toxin event endpoints ([PLOS ONE, 2013, DOI 10.1371/journal.pone.0056103](https://doi.org/10.1371/journal.pone.0056103)). Hansen and Carey analyzed the 1995–2011 species-level Mendota record and characterized seasonal/long-term phytoplankton and fish dynamics ([PLOS ONE, 2015, DOI 10.1371/journal.pone.0115414](https://doi.org/10.1371/journal.pone.0115414)). Carey et al. analyzed 16 years of biweekly Mendota phytoplankton data with wavelets to identify shifts in seasonal succession and periodicity ([Journal of Plankton Research 38:27–40, 2016, DOI 10.1093/plankt/fbv116](https://doi.org/10.1093/plankt/fbv116)). Rohwer et al. paired a 20-year microbial series with phytoplankton counts, environmental context and cyanotoxin series; they identified Cyanobacteria phenology shifts associated with invasive species and season-specific changes ([PNAS 120:e2211796120, 2023, DOI 10.1073/pnas.2211796120](https://doi.org/10.1073/pnas.2211796120)). These support long-term biological endpoint plausibility and show that seasonality, invasion and community composition vary materially; none is an exact matched false-alarm test of EcoSentinel's claimed warning signal.

## Broader multivariate early-warning literature

Gsell et al. evaluated early-warning indicators in natural aquatic ecosystems and emphasized mechanism, variable selection, signal detection and controls for false positives; the case studies did not provide comprehensive control systems for false alarms ([PNAS, 2016, DOI 10.1073/pnas.1608242113](https://doi.org/10.1073/pnas.1608242113)). Burthe et al. analyzed multi-trophic plankton data from nine lakes, comparing univariate, multivariate and machine-learning methods over monthly/yearly series; few transitions were classified as critical, outcomes were sensitive to preprocessing, multivariate results were only weakly superior, and most approaches did not clearly exceed chance ([Nature Communications 14:7712, 2023, DOI 10.1038/s41467-023-43744-8](https://doi.org/10.1038/s41467-023-43744-8)). This work is highly relevant to the broader “multivariate early warning” claim. Its endpoint is persistent whole-ecosystem critical transition, not cyanobacterial bloom forecasting at a chosen horizon, so it does not settle EcoSentinel's specific question. It does establish that multivariate status alone is not a novelty or performance argument.

Mantzouki et al. discuss the limits and complementarity of routine snapshot sampling and high-frequency observations in lakes ([Frontiers in Ecology and Evolution 6:201, 2018, DOI 10.3389/fevo.2018.00201](https://doi.org/10.3389/fevo.2018.00201)). Heger et al. demonstrate that sampling frequency affects ecological early-warning detection in a virtual lake and argue that measurement cadence must be matched to process timescale ([Ecological Indicators 153:110424, 2023, DOI 10.1016/j.ecolind.2023.110424]). These method papers make outcome cadence a core feasibility question, not a minor limitation.

## Novelty finding

**Broad originality is unsupported.** Mendota studies already use high-frequency pigment records; estimate lagged relationships with environmental variables; forecast seasonal, sub-seasonal and continuous algal dynamics; and study changes in multi-species/plankton signals. General multivariate EWS methods have also been directly compared in empirical lakes.

**A narrower contribution may remain, but is conditional.** It would require all of the following to be truly distinct and prespecified:

1. the exact EcoSentinel signal quantifies a defined persistence of changes in relationships among environmental variables, rather than a known cross-correlation, regression, anomaly, or EWS statistic;
2. independent species/taxon-based microscopy defines a biologically meaningful cyanobacterial abundance outcome, without fluorescence leakage into the reference;
3. all methods are evaluated from the same prediction origin, fixed warning horizon, eligibility/exposure time, independent event definition, and alarm suppression/deduplication rule;
4. thresholds and preprocessing are selected only within training years; held-out years are not used in threshold selection or feature design;
5. conventional single-variable thresholds and persistence/rolling baselines are genuinely fair (same inputs where appropriate, comparable tuning budget, matched false-alarm definition); and
6. performance is reported with uncertainty and event-level—not minute-sample-level—independence.

Matched false-alarm rates are a sensible evaluation criterion, but not novel by themselves. The contribution would be an empirical, operational comparison under independent biological validation, if the exact literature check confirms no prior study has done that. I have not found an exact Mendota paper with this complete design in the searched sources; absence from this search is not proof of absence. The proposed method and the complete reference set have not been provided here, which limits a definitive novelty audit.

## Prior-art verdict

Existing literature substantially overlaps with each broad component and limits broad novelty. An exact-method claim remains unresolved because the EcoSentinel indicator is not detailed in this review request and direct comparable literature may exist outside the searched corpus. Preserve a novelty statement as “potentially distinct comparison” until a documented, method-by-method citation matrix is complete. Do not claim “first,” “novel” or “unprecedented.”
