# Scientific Evidence Requirements

**Purpose:** Define what evidence would be required to test the original research question properly, and what is realistically obtainable under current constraints.  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. Minimum evidence package for the original question

| Requirement | Minimum evidence | Current status | Realistic obtainability within current constraints |
|---|---|---|---|
| **Independent bloom events** | Multi-year, independently measured biological observations with a pre-approved biological-only event definition; enough events to evaluate detection and missed-event rates | **0 reconstructed events** from accessible evidence; Buffalo Pound candidate observations only; Mendota no labels | **Low.** Buffalo Pound has 2 seasons; no documented reply or additional years. Mendota rejected for validation. New dataset search/contact prohibited. |
| **Defensible non-bloom exposure** | Verified non-event periods with adequate coverage and explicit unknown/censored handling | **0 defensible non-bloom intervals**; missing/unsampled periods are unknown, not non-bloom | **Low.** Requires new biological sampling across non-bloom seasons; not present. |
| **Temporal resolution for onset/lead time** | Time-stamped, sub-weekly or event-triggered biology; onset/termination bounds smaller than the claimed lead-time effect | Buffalo Pound 1–16-day gaps, no sample times; Mendota 14-day median, date-only | **Low–medium.** Existing data cannot resolve few-day lead times; new sampling needed. |
| **Depth alignment** | Depth-resolved biology or an explicitly justified comparator; sensor depth matched to biological support | Mendota 0.5 m sensor vs 0–8 m composite; Buffalo Pound 0.8 m vs 0.8 m but cross-site/protocol differences | **Medium for Buffalo Pound** (depth matched), **low for Mendota** (composite mismatch; no profile). |
| **Sensor comparability** | Documented calibration, maintenance, serial numbers, detection limits, Turner/YSI crosswalk, QC dictionary | No per-record calibration; Turner/YSI no crosswalk; `O` undefined; 8 flag columns with undocumented values | **Low–medium.** Some can be documented from external metadata; no guarantee of availability. |
| **Strong conventional baselines** | Pre-specified persistence, univariate threshold, rolling z-score, simple multivariate baselines, same data/splits/exposure | Protocol drafts baseline categories; no approved operational definitions or real evaluation | **High (design) / low (execution)** — design is feasible; execution requires labels/exposure. |
| **Matched-FAR evaluation** | Pre-specified FAR target/operating points, event-level and observation-level accounting, uncertainty | No exposure denominator; no approved operating points; no real matched-FAR result | **Low now; feasible after labels/exposure and protocol approval.** |
| **Leakage-resistant validation** | Temporal/event/year splits, train-only scaling, no future information, event-grouped CV, pre-registered rules | Gate 2H synthetic prototype has guards and tests; real-data design not approved | **High (design) / pending real data.** |
| **Adequate independent events** | Enough events/years to estimate event-level sensitivity, FAR, lead time and uncertainty | 0 events; 42 Buffalo Pound dates; Mendota 402 dates but rejected for validation | **Low.** No quantitative power calculation is defensible now. |
| **Interpretable and honest negative results** | Pre-specified reporting of negative/inconclusive outcomes, limitations, uncertainty | Project documents strongly require this | **High.** This is a strength. |

## 2. Conditions before Gate 2 could be reconsidered

Gate 2 should not be reconsidered until:

1. independent biological data are accessible and verified for multiple years, including non-bloom periods;
2. a biological-only event/non-event definition is pre-approved;
3. onset/termination are interval-censored with uncertainty smaller than the claimed lead time;
4. sensor–biology depth/spatial alignment is documented and defensible;
5. sensor calibration/comparability and QC rules are documented;
6. a strong baseline suite and matched-FAR design are pre-registered;
7. independent events and exposure are sufficient for a meaningful evaluation;
8. leakage-resistant splits and uncertainty reporting are approved;
9. a human Gate 2/3 review explicitly approves the protocol.

## 3. What is not sufficient

- More high-frequency sensor rows from the same site;
- more derived taxonomy matrices or group biomass from the same samples;
- using phycocyanin/chlorophyll RFU as ground truth;
- interpolating sparse biology into daily labels;
- treating unknown periods as non-bloom;
- a synthetic evaluation prototype, however well tested;
- a more complex model, a different algorithm, or matched FAR alone;
- a single-site case study with 2 seasons and 42 dates;
- a retrospective phase description that was partly informed by buoy sensors.

## 4. Realistic evidence routes under current constraints

| Route | What it would provide | Status | Constraint |
|---|---|---|---|
| Buffalo Pound researcher reply with additional years, non-bloom sampling, raw counts, station/depth/QC | Potential multi-year independent biology | **No documented reply; not assumed** | No external contact; pending |
| BPWTP/WSA historical phytoplankton/cell counts/lab chlorophyll | Potential additional biological record | **Unverified/request-only** | No contact; access uncertain |
| Boyer 2025 SI/raw 2017 data | Additional 2017 biology | **Not obtained** | Request-only; no contact |
| Mendota 88.31 + 129.42 | 402 dates + sensor data | **Available but rejected for validation** | 14-day, no labels, depth mismatch, sensor proxies |
| New dataset search | New candidate | **Prohibited in this sprint** | Not authorised; would be broad dataset hunting |
| Synthetic/proxy labels | No independent ground truth | **Rejected** | Circular/invalid |

## 5. Conclusion

The original question requires evidence that the project does not currently possess. The gap is not a matter of more analysis or a better algorithm; it is a matter of **independent biological events, non-event exposure, temporal resolution, and measurement alignment**. Until those exist, the original question is not testable at confirmatory standard.
