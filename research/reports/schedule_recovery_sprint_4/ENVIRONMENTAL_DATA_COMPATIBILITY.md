# Environmental Data Compatibility (Sprint 4)

**Date:** 2026-11-22  
**Status:** Investigation artifact. Gate 2 remains **PAUSED / NOT APPROVED — Option C (Exploratory only)**.

## Buffalo Pound primary environmental dataset (existing)

| Item | Value |
|---|---|
| Dataset | Buffalo Pound Lake buoy/meteorological data 2014-2021 |
| DOI | 10.20383/103.01100 |
| Temporal resolution | 10–15 min |
| Variables | Temp, DO, pH, conductivity, turbidity, chlorophyll-a RFU, phycocyanin RFU, met vars |
| Key constraints | Sensor flags/fouling/missingness/sensor-array changes; no nutrients in buoy dataset |

## Compatibility requirements for pairing biological candidates

| Requirement | Why it matters | Minimum evidence |
|---|---|---|
| Temporal overlap | Biological labels must align with environmental series | Documented overlapping dates/times |
| Spatial compatibility | Different stations/depths can create mismatch | Station/depth metadata; defensible proximity |
| Depth compatibility | Surface scums vs integrated samples differ | Sample depth and buoy sensor depth documented |
| Timestamp precision | Event onset/offset uncertainty depends on this | Date/time, timezone, sampling protocol |
| Method comparability | Different labs/methods can create artificial shifts | Methods, units, detection limits, QC |
| Non-event exposure | Needed for false-alarm evaluation | Defensible verified non-bloom intervals or exposure design |

## Candidate pairing assessment

| Candidate | Environmental pairing option | Compatibility | Key risks |
|---|---|---|---|
| BP-001 Painter 2022 | Buffalo Pound buoy dataset 10.20383/103.01100 (2018-2019 overlap exists) | **Promising for exploratory analysis** | Sparse biological sampling (25/17 dates); interval-censored onset; 2019-07-17 anomaly; no defensible non-event exposure established |
| BP-002 Boyer 2025 | BP buoy dataset (2017 overlap exists) | Potentially promising if raw data obtained | Raw data inaccessible; sparse dates; event boundaries uncertain |
| GL-001 NLA | NLA co-sampled water quality | Poor for HF EWS | Single-visit design; no continuous HF predictor series |
| GL-002 Cumbrian Lakes | CEH long-term monitoring + possible HF sensor datasets | Conditional | Requires identifying and verifying compatible HF environmental series and alignment |

## No silent integration rule

No alternative dataset or pairing may be silently integrated into EcoSentinel's main project. Any pairing used for analysis requires explicit provenance, compatibility assessment, and human-approved scope decision.
