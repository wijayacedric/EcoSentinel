# Sprint 4L.10 External Search Log

**Gate 2:** PAUSED / NOT APPROVED — option C (Exploratory Only)

## 1. Source categories defined before searching

1. Project governance and prior Sprint 4L.5–4L.9 evidence.
2. Primary raw data and metadata: daily 129.42, biology 88.31, EML, sensor inventory.
3. Lake Mendota high-frequency sensor and phytoplankton research.
4. Phycocyanin/chlorophyll fluorometry validation and manufacturer guidance.
5. Freshwater cyanobacteria early-warning and forecasting literature.
6. Empirical ecological early-warning-signal literature.
7. Sampling-frequency and sensor-to-biological validation literature.

## 2. Queries and routes

| # | Query / route | Sources inspected | What it establishes | Status |
|---:|---|---|---|---|
| 1 | Local governance and prior evidence | `AGENTS.md`; 4L.5–4L.9 reports, scripts, tables | Reproducible audit basis; prior constraints; no weakened governance | Full |
| 2 | Raw daily and biology files | 129.42 daily `.dat`; 88.31 biology `.dat` | 3,996 daily rows; 402 biology dates; hashes; overlap | Full |
| 3 | EML/sensor inventory | 129.42 EML; sensor list | 38 fields; depths; flags; sensor eras; inventory mismatches | Full |
| 4 | “high-frequency sensors cyanobacteria bloom early warning freshwater lake” | Carpenter 2020 (HERO); Carpenter 2022 (PNAS/PMC); Recknagel 2025 (PubMed/search); NOAA/EPA pages | Mendota HF phycocyanin; stochastic states; HF+ML early warning active field | Mixed full/abstract |
| 5 | “Lake Mendota buoy cyanobacteria phycocyanin high-frequency data research” | NTL high-frequency page; Carpenter 2020; Carpenter 2022; Carpenter & Brock 2024; Beal 2021/2022 | Mendota already has HF phycocyanin and seasonal/sub-seasonal forecasts | Mixed |
| 6 | “phycocyanin fluorescence sensor validation lake cyanobacteria limitations” | Cotterill 2019 (abstract); Levi 2025 (full PMC); USGS TM1-D10 (full); YSI/Turner pages | Weak/variable phycocyanin–biovolume relationships; calibration/composition/biofouling limitations | Mixed |
| 7 | “phytoplankton bloom early warning signals high frequency lake sensor validation” | O'Brien 2023 (full Nature); Pace 2016 (full PMC); Wilkinson 2018 (abstract); Recknagel 2025 | EWS possible in controlled experiments; empirical performance often poor; Mendota included in O'Brien | Mixed |
| 8 | Manufacturer technical guidance | YSI EXO2 page; YSI algae-sensor blog; Turner Cyclops-7F page | RFU relative/sensor-specific; 6-series vs EXO differences; wiper/calibration context | Full |
| 9 | Temperature/quenching/sensor morphology | Hodges 2018; Rousso 2021; Watras 2017 (abstract/metadata) | Temperature, light-induced quenching, manufacturer/morphology effects | Abstract-level |
| 10 | Mendota forecasting prior art | Beal 2021/2022 records; 4L.6 search log | Two-month/season-ahead forecasts; not daily onset | Search-indexed/4L.6 |
| 11 | Mendota phytoplankton methods | NTL protocols; Hansen & Carey 2015 via 4L.6; 4L.5/4L.6 | Biweekly summer/monthly non-summer; 0–8 m integrated; taxonomic change | Full via project evidence |

## 3. Key findings

- Lake Mendota is not a blank early-warning testbed. Carpenter et al. (2020, 2022) already use 1-minute/daily phycocyanin; Beal et al. (2021, 2022) already produce seasonal/sub-seasonal cyanobacteria forecasts; O'Brien et al. (2023) include Mendota in a multi-lake empirical EWS assessment.
- The Mendota phycocyanin system is stochastic: Carpenter et al. (2020) found two alternative states with random factors larger than the state difference; annual states were not correlated with annual P input, while daily values correlated with P/precip/wind at 1–15-day lags.
- Carpenter et al. (2022) used nighttime means to reduce quenching, z-scored within year, and documented different sensors/maintenance regimes; this is directly relevant to the 4L.9 daily-average approach.
- Cotterill et al. (2019) found the phycocyanin–biovolume relationship generally weak (<R² 0.4), variable among lakes/years, with species-specific detection limits above alert thresholds for two of four species.
- Levi et al. (2025) found sensor-specific calibration, biofouling/composition/equipment effects, low-concentration limitations, and the value of nighttime data and high-frequency sampling; but also that high-frequency sensors can capture events missed by biweekly/monthly sampling.
- O'Brien et al. (2023) found few critical transitions and most EWS not better than chance; multivariate EWS weakly superior, machine learning poor.
- USGS TM1-D10 and manufacturer guidance agree that RFU is sensor-specific and not a direct abundance measure.

## 4. Inaccessible / not fully inspected

- Wiley/ESA/Taylor & Francis/ScienceDirect article pages returned 403 for several papers. Where possible, full HTML/PMC versions were used. Otherwise the source is marked abstract/search-indexed.
- Manufacturer manual PDFs (YSI EXO, Turner Cyclops) were identified but not text-extracted because the fetch tool rejected `application/pdf`.
- Kara et al. (2012) primary PDF was identified but not text-extracted; its Lake Mendota result is cited only as reported by Levi et al. (2025).
- Carpenter & Brock (2024), Beal et al. (2021/2022), Wilkinson et al. (2018), Recknagel (2025) were not fully text-inspected in this sprint; they are used only for the specific prior-art claims visible in abstracts/search-indexed records and, for Beal, the 4L.6 search log.
- No original microscope slides, lab sheets, sensor calibration records or maintenance logs were available.
- No external contact was made.

## 5. Why searching stopped

The primary data/metadata, the full Mendota-specific phycocyanin paper available via PMC (Carpenter et al. 2022), full USGS guidance, manufacturer technical pages, full Levi et al. sensor-validation study, and the full O'Brien et al. EWS analysis were inspected. Remaining limitations are data/metadata gaps (event labels, sample times, depth-resolved biology, calibration history), not a shortage of search results. More literature cannot create the missing biological event data.
