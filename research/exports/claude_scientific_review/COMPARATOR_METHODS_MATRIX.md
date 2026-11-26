# Comparator Methods Matrix

**Status:** Abstract/metadata-level matrix only. Full texts/supplements not accessible in-session (2026-11-22). Cells marked **Unverified** require full-text review.

| Dimension | Recknagel et al. 2025 (WR 287:124514) | Fournier et al. 2024 (WR 267:122553) | Rousso et al. 2020 (WR 182:115959) | EcoSentinel proposal (current) |
|---|---|---|---|---|
| **Citation verified** | Yes (Crossref, PubMed PMID 40925059) | Yes (Crossref, PubMed PMID 39388977) | Yes (Crossref, PubMed PMID 32531494) | N/A |
| **Research objective** | Intelligible ML early warning of CyanoHAB hazard exceedance (abstract) | Effective EWS for cyanobacterial bloom forecasting with incomplete spatio-temporal data (abstract) | Systematic review of CyanoHAB forecasting/predictive models (abstract) | Test whether persistent relationship changes give earlier warning than conventional monitoring at comparable FAR |
| **Prediction/detection target** | 5-day-ahead forecast of total cyanobacteria; hazard-level exceedance (abstract) | PC alarm level 10 µg PC/L; horizons 4-28 days (abstract) | N/A (review) | Independently adjudicated biological bloom events (proposed; no labels approved) |
| **Ecosystem/location** | Lake Müggelsee, Germany | Inland waters; site not named in abstract | Global freshwater lakes (review) | Buffalo Pound Lake, Saskatchewan, Canada |
| **Sampling/data** | 11 years hourly/daily HFISD (abstract) | 6 years incomplete high-frequency spatio-temporal multiparametric probe data (abstract) | Included studies vary | 2014-2021 high-frequency buoy/meteorological data |
| **Biological ground truth** | "State variables for cyanobacteria require in situ measured data..." (abstract); independence unclear | PC fluorescence proxy as target/alarm basis (abstract) | Varies across reviewed studies | Required to be independent biological evidence; currently unavailable (Gate 2 blocker) |
| **Environmental predictors** | WT, TURB, pH, PHYCO named (abstract) | Multiparametric probes incl. PC fluorescence (abstract) | Varies | Temp, DO, pH, conductivity, turbidity, chl RFU, phycocyanin RFU, met vars (no nutrients) |
| **Relationship-change indicators** | Not mentioned in abstract | Not mentioned in abstract | Unverified across reviewed studies | Core proposal: rolling correlation/covariance/coupling-change indicators |
| **Conventional baselines** | Unverified (not in abstract) | 6 models compared incl. LR/RF/LSTM; skill vs displaced signal (abstract) | Varies; lack of standardization noted (abstract) | Required: persistence, univariate thresholds, simple anomaly/multivariate baselines |
| **False-alarm evaluation** | Unverified | Accuracy/F1/Kappa reported; FAR not explicit (abstract) | Unverified; metrics standardization lacking (abstract) | Primary: matched-FAR comparison |
| **Missed-event evaluation** | Unverified | Not explicitly reported (abstract) | Unverified | Required: missed-event rate/event-level sensitivity |
| **Lead-time evaluation** | Fixed 5-day-ahead horizon (abstract); lead-time distribution unverified | Horizons 4-28 days; "16-28 days in advance" skill (abstract) | Unverified | Required: interval-censored lead-time bounds against independent onset |
| **Temporal validation** | Training vs unseen data mentioned (abstract) | Forecast horizons evaluated (abstract); split design unverified | Unverified | Required: temporal/event-based, no random leakage |
| **Independent event validation** | Unverified | Unverified | Unverified | Required if Gate 2 unblocks |
| **Confounding controls** | Unverified | Unverified | Unverified | Required: seasonality, hydrology/management, sensor artefacts, autocorrelation nulls |
| **Uncertainty reporting** | Not stated in abstract | Not stated in abstract | Unverified | Required |

## Key matrix caveat
The closest topical comparator (Recknagel 2025) may contain validation/baseline details not visible in abstract. No cell above should be treated as a full-text-confirmed absence unless explicitly stated in accessible full text.
