# Search Log — Sprint 4L.4 Mendota Literature and Method Review

**Search/review dates:** 23–24 November 2026  
**Scope:** independent literature, public institutional metadata, protocol, sensor-history, prior-art, and methodology review. Search was performed before opening or using any OpenCode Sprint 4L.3 conclusions. No dataset was downloaded. Full source list and claim limits are in `LITERATURE_AND_SOURCE_REGISTER.csv`.

## Governance and sequence

1. Read the EcoSentinel repository `AGENTS.md` and verified that the permanent research standards required by Sprint 4L.3 are present in that file.
2. Inspected permitted existing project evidence from Sprint 4E.1 and the completed Codex Sprint 4L.2 sensor-inventory review. Did not open any OpenCode Sprint 4L.3 report or conclusion. Did not inspect Sprint 4L biology acquisition outputs.
3. Searched official NTL-LTER pages and the EDI portal for biological package/protocol identity, sample design, sensor series and Mendota sonde metadata.
4. Searched original peer-reviewed literature using author/title/DOI, Lake Mendota, source-variable, method, and relevant citation-follow-up terms. Read full texts where accessible; used accessible supplements or publisher/institutional mirrors where possible.
5. Searched methodological studies and critiques concerning early-warning indicators, sampling frequency, false alarms, independent validation, and temporal nonstationarity.
6. Recorded unverified details and access failures rather than inferring from dataset titles or abstracts.

## Sources and platforms searched

- NTL-LTER: [Research Protocols](https://lter.limnology.wisc.edu/protocols/), [Core Datasets](https://lter.limnology.wisc.edu/core-datasets/), [High Frequency Data](https://lter.limnology.wisc.edu/high-frequency-data/), buoy/program pages, project-plan and archived-protocol PDFs.
- EDI/PASTA: official target package DOI `10.6073/pasta/bd03330e83fc52a5442bb39e131c95e9` / `knb-lter-ntl.88.31`, and official buoy / sonde package links as cataloged by NTL-LTER.
- Original peer-reviewed sources: PLOS ONE, Journal of Plankton Research, Limnology and Oceanography Letters, PNAS/PMC, Nature Communications, Water Research, Harmful Algae, Freshwater Biology/peer-reviewed forecasting outlets, Ecology and Evolution, Ecological Indicators.
- Publisher/institutional repository mirrors for full texts when direct publisher pages were blocked; DOI/Crossref-style title queries to validate citations.

## Search queries executed (representative exact strings)

### Dataset, sampling and methods

- `site:portal.edirepository.org Lake Mendota phytoplankton 88.31 NTL-LTER EML`
- `"knb-lter-ntl.88.31" phytoplankton`
- `Lake Mendota phytoplankton monitoring protocol biovolume sampling 0-8 m NTL LTER`
- `Lake Mendota phytoplankton long term record methods microscopy biovolume 1995 NTL`
- `Lake Mendota phytoplankton taxonomy biovolume Utermohl method cell density NTL phytoplankton dataset species identification`
- `Lake Mendota high frequency buoy chlorophyll phycocyanin sensor calibration NTL LTER methods`
- `Lake Mendota buoy high frequency data chlorophyll phycocyanin Pace 2017 data methodology`
- `site:lter.limnology.wisc.edu "Lake Mendota Buoy" high frequency data`
- `Mendota buoy chlorophyll phycocyanin fluorescence 2019 YSI Turner calibration`
- `Lake Mendota buoy high frequency monitoring buoy 1 minute temperature profile phycocyanin paper`

### Mendota prior art

- `Lake Mendota cyanobacteria forecasting sub-seasonal Beal 2021 102100`
- `Lake Mendota cyanobacteria biomass forecasting Beal 2021 training validation cross validation annual forecast metrics`
- `Lake Mendota cyanobacteria bloom early warning regime shift phytoplankton literature`
- `"Mendota" "early warning" cyanobacteria time series high frequency`
- `"Lake Mendota" "multivariate" "early warning" phytoplankton`
- `"Long-range dependence and extreme values of precipitation, phosphorus load, and Cyanobacteria" Mendota DOI`
- `Lake Mendota high frequency precipitation phosphorus Cyanobacteria cross correlations lag 1 15 days Carpenter 2022`
- `"Algal bloom forecasting with time-frequency analysis" Mendota DOI`
- `"Development of a sub-seasonal cyanobacteria prediction model" cross-validation`
- `Lake Mendota phytoplankton phenology 20 year time series cyanobacteria Hansen Carey 2015 2016`

### General methodology and comparators

- `multivariate early warning signals cross correlations ecological time series original article`
- `EWSNet early warning signals time series data lakes Nature Communications 2023 Burthe limited applicability empirical lake data`
- `sampling interval early warning indicators ecological time series frequency biological sampling temporal resolution study lakes`
- `ecological early warning signals validation sampling frequency temporal resolution biweekly monthly measurement errors paper lakes`
- `ecological early warning signals false alarms predict persistence ecological time series validation tradeoffs`
- `matched false-alarm ecological early warning indicators false alarm rates`
- `Timing matters Sampling frequency early-warning indicators food web components virtual lake`
- `Lake monitoring snapshot surveys high-frequency monitoring lake phytoplankton cadence`

## Search coverage and evidence reached

| Research area | Sources reviewed | Evidence coverage | Remaining limitation |
|---|---|---|---|
| Mendota biological methods | NTL protocols, archived protocol PDF, Hansen & Carey 2015 full text, Carey et al. 2016 full PDF, NTL core catalog | Depth composite, historic cadence, microscopy/taxonomic resolution, counts/biovolume, seasonality and historical method statements | No exact 88.31 entities, current schema, complete year-by-year method history, detection limits, or raw data inspected. |
| Buoy/environmental sensors | NTL high-frequency and core catalog, SSEC buoy page, NTL draft core plan, Carpenter et al. 2020 full text/supplement link, Codex 4L.2 sensor inventory review | Catalog dates/variables; high-frequency pigment deployment; sensor-era changes, explicit fouling/loss and maintenance examples | No raw timestamps, missingness, QC flags, calibration coefficients, or continuous-coverage audit. |
| Prior art | Mendota forecasting, high-frequency pigment, lagged extreme dependence, phytoplankton time-series and phenology studies | Direct overlap in multiple portions of the proposed domain established | Exact detector specification and exhaustive citation matrix of its precise method were not supplied; novelty cannot be certified. |
| Multivariate EWS and general lake methods | Gsell et al. 2016 full text/PDF, Burthe et al. 2023 full text and methods, Mantzouki 2018, Heger et al. 2023 | Evidence on preprocessing sensitivity, low performance, multivariate-vs-univariate comparison and sampling-frequency tradeoffs | These study transition predictions rather than the exact bloom-warning estimand. |
| Validation design | Primary articles plus methodological critiques on stationarity, sampling cadence, false-positive evaluation, held-out temporal data | Established why common outcomes, origin, horizon, exposure, frozen training thresholds, interval censoring and event-level uncertainty are necessary | No project protocol implementation audited; no event counts or precision calculations performed. |

## Access failures and incomplete source material

- The EDI `knb-lter-ntl.88.31` web landing request returned HTTP 403. NTL-LTER's own Core Datasets page states that package values and metadata now require sign-in. This task explicitly prohibited duplicating acquisition work; no repeat acquisition or raw-data download was attempted. Consequently all exact 88.31 schema/coverage claims remain unresolved.
- The NTL public Protocols page says protocols are being updated and asks users to request older protocols. Full historical version-by-version methods are not all public in the reviewed materials.
- Some publisher pages (notably ScienceDirect and PMC) blocked direct full-text opens. Publisher search results and accessible institutional/full-text copies were used to identify sources; claims requiring unavailable details are marked unresolved. This applies particularly to the full methods/supplement of the 2022 WLSTM Mendota forecast and package-by-package derivation of “biomass.”
- The 2022 PNAS supplementary link was identified but not fully extracted in this review. No conclusions depend on unpublished details from that supplement.

## Inclusion and exclusion

Included sources had direct Mendota monitoring/method relevance, original empirical evidence, official dataset/protocol provenance, or direct methods relevance to sampling/early-warning validity. General HAB models in other lakes, generic sensor marketing, public media, and secondary summaries were excluded from evidentiary claims. A few search results served only to locate primary sources and are not cited as evidence.

## Search stop rule and honesty statement

Defined categories (biology, sensor history, Mendota direct prior art, general multivariate EWS, sampling frequency, validation constraints) were searched across official project pages, repository metadata, original research and method papers. The main remaining incompleteness is not lack of search effort but (i) access-controlled package-level metadata/data, (ii) unretrieved historical protocol versions, and (iii) absence of an exact EcoSentinel detector specification for a fully closed novelty search. This review is **PARTIALLY COMPLETE**: literature-level feasibility is documented, but it does not certify package-level readiness or exact-method novelty. Completion requires the authenticated package audit, historical methods, and exact detector specification with a closed targeted literature comparison.