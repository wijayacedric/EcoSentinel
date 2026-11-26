# Stage 2 Dataset Qualification Checklist

**Sprint:** 4L.19  
**Purpose:** Define the minimum evidence required before any dataset is considered qualified for the original early-warning research question.  
**Status:** Proposed checklist. **No dataset is qualified.** Müggelsee is a candidate only.

---

## 1. Decision rule

A dataset is **qualified for Stage 2** only if:

1. every **mandatory** requirement below is assessed as **PASS**;
2. any **conditional** assessment has a written justification and a bounded limitation that the independent statistical reviewer accepts;
3. no mandatory requirement is **FAIL** or **UNKNOWN** at the time of approval;
4. the data licence permits the proposed use, including derived outputs and any publication/display;
5. the dataset version, DOI and correction history are recorded;
6. the event definition is pre-specified and independent of the sensor predictor;
7. the number of independent events and non-events is counted after QC and matching.

A dataset with a **FAIL** on any mandatory requirement is **not qualified**, regardless of record length or prestige.

---

## 2. Mandatory requirements

### Q01 — Temporal coverage

| Field | Detail |
|---|---|
| Requirement | At least five years of overlapping biological and sensor data, with at least one full seasonal cycle per year and no single year dominating the event count |
| Why | The original question is about persistent change and early warning; a short or unbalanced record cannot support it |
| Evidence needed | Start/end dates; deployment gaps; seasonal coverage; number of years with both biological and sensor data |
| Assessment | Count overlapping years and seasonal coverage after matching; report gaps |
| Müggelsee status | **PASS** for coverage (phytoplankton 1979–ongoing; high-frequency sensor 2001–ongoing; weekly probe 1978–2019), but overlap and event balance not yet counted |

### Q02 — Independent bloom-event definition

| Field | Detail |
|---|---|
| Requirement | A pre-specified definition of a bloom event that does **not** use the sensor variable being tested as a predictor; includes threshold, minimum duration, separation from adjacent events, and treatment of overlapping events |
| Why | If the event label is derived from the same sensor, the analysis is circular; if the event definition is chosen after looking at the sensor, it is result-dependent |
| Evidence needed | Written event-definition protocol; biological basis; sensitivity to threshold/duration; event list with dates |
| Assessment | Review the definition before looking at associations; check that it uses independent biological/water-quality criteria |
| Müggelsee status | **FAIL / UNKNOWN** — no public event definition or event list identified |

### Q03 — Event independence and count

| Field | Detail |
|---|---|
| Requirement | At least ten independent bloom events after applying the event definition and QC; overlapping/consecutive samples from one bloom counted once; non-bloom periods sampled at comparable resolution |
| Why | The original threshold of ten events is meaningless if events are not independent or if non-bloom exposure is absent |
| Evidence needed | Event table with start/end, peak, separation; non-bloom dates; exclusion log |
| Assessment | Reconstruct events from the biological series; check separation; count non-bloom exposures by season/year |
| Müggelsee status | **UNKNOWN** — no event count; long series makes ten events plausible but not verified |

### Q04 — Biological sampling frequency and timing

| Field | Detail |
|---|---|
| Requirement | Weekly or better biological sampling during the bloom season; sample dates and times documented; sampling frequency stable enough for event-scale analysis |
| Why | Early warning depends on temporal resolution; date-only samples with unknown times cannot establish lead/lag |
| Evidence needed | Sampling calendar; sample times; frequency changes; gaps |
| Assessment | Compare sampling dates with event windows; check time-of-day documentation |
| Müggelsee status | **CONDITIONAL** — weekly growing season / biweekly ice is documented; exact sample times are not verified |

### Q05 — Taxonomic and biomass consistency

| Field | Detail |
|---|---|
| Requirement | Documented taxonomy, cell-count and biovolume/biomass methods; taxonomic resolution changes and processor changes recorded; detection limits and counting error addressed |
| Why | A change in taxonomy or counting method can create apparent ecological change |
| Evidence needed | Methods text; taxonomic lists; processor history; detection limits; intercalibration |
| Assessment | Review methods and change points; check whether the endpoint is comparable across the series |
| Müggelsee status | **CONDITIONAL / PASS with caveats** — Utermöhl methods and biomass conversion documented; taxonomic resolution changes 1993–1995 and processor changes recorded; detection limits not fully verified |

### Q06 — Sensor variables and depth matching

| Field | Detail |
|---|---|
| Requirement | Sensor chlorophyll/phycocyanin at a depth that matches the biological sample, or a documented depth correction; sensor model, range, calibration and fouling history |
| Why | Surface fluorescence is not integrated biomass; a 1.5 m point sensor is not a 0–7 m integrated sample |
| Evidence needed | Sensor depth; biological integration depths; calibration records; fouling/maintenance log; range |
| Assessment | Compare depths; quantify mismatch; require a sensitivity or explicit limitation |
| Müggelsee status | **CONDITIONAL / likely FAIL** — high-frequency sensor at 1.5 m; phytoplankton integrated 0–4/0–7 m; weekly probe profiles 0.5–1 m; no public depth-correction evidence |

### Q07 — Spatial co-location

| Field | Detail |
|---|---|
| Requirement | Sensor and biological sampling at the same station or water parcel, or a documented spatial offset with a justification that the lake is well-mixed at the relevant scale |
| Why | A sensor 300 m or more away may sample a different water parcel, especially during blooms or stratification |
| Evidence needed | Station coordinates; distance; mixing/stratification context; concurrent spatial samples |
| Assessment | Map stations; review lake mixing; require a spatial sensitivity |
| Müggelsee status | **CONDITIONAL** — sensor station M210; phytoplankton stations M3/M5/M7/M8/M10; offset not quantified |

### Q08 — Sensor calibration, maintenance and QC

| Field | Detail |
|---|---|
| Requirement | Record-level or deployment-level calibration, maintenance, fouling and flag definitions; documented processing; known corrections |
| Why | Sensor drift, fouling and calibration changes can create or mask trends |
| Evidence needed | Calibration certificates/logs; maintenance dates; QC flags; processing code; correction history |
| Assessment | Review records; check flag semantics; quantify drift/fouling intervals |
| Müggelsee status | **UNKNOWN** — not publicly verified; data are all rights reserved |

### Q09 — Non-bloom exposure

| Field | Detail |
|---|---|
| Requirement | Non-bloom periods sampled with comparable seasonal and temporal resolution; a clear non-bloom definition; no use of “absence of bloom” as a default without sampling |
| Why | A model that compares bloom samples with unsampled periods learns season, not bloom dynamics |
| Evidence needed | Sampling calendar; non-bloom dates; detection limits; event definition |
| Assessment | Count non-bloom samples by season/year; check whether they are true negatives or unsampled |
| Müggelsee status | **CONDITIONAL / UNKNOWN** — long-term weekly sampling likely includes non-bloom dates, but no event/non-event classification is public |

### Q10 — Data access and licence

| Field | Detail |
|---|---|
| Requirement | Written permission or a licence that permits the proposed use, including analysis, derived outputs, publication and competition display |
| Why | “All rights reserved” means permission is required; an academic assumption is not a licence |
| Evidence needed | Written permission; licence terms; attribution wording; redistribution rules |
| Assessment | Legal/licence review; record the permission |
| Müggelsee status | **FAIL / UNKNOWN** — all rights reserved; request required; no permission recorded |

### Q11 — Version and correction history

| Field | Detail |
|---|---|
| Requirement | DOI, version, update history and errata recorded; the analysis uses a fixed version |
| Why | A moving dataset can change results; reproducibility requires a fixed version |
| Evidence needed | DOI/version; changelog; file hashes |
| Assessment | Record the version; hash the files; check for updates before analysis |
| Müggelsee status | **PASS** — FRED packages have DOIs and version history; exact analysis version still to be fixed |

### Q12 — Data dictionary and reproducibility

| Field | Detail |
|---|---|
| Requirement | A data dictionary for every variable; units; missing codes; flags; processing code or a clear description |
| Why | Without a dictionary, variable meanings are guessed |
| Evidence needed | Data dictionary; metadata; code |
| Assessment | Parse and verify; document unresolved fields |
| Müggelsee status | **CONDITIONAL** — metadata PDFs exist; full data dictionary and processing code not publicly verified |

---

## 3. Additional requirements for early warning

These are specific to the original Stage 2 ambition and are **mandatory** if the question is early warning rather than description.

### E01 — Pre-specified lead time

- Define the lead time of interest (e.g., days/weeks before a bloom threshold) before analysis.
- Do not search over lead times and report the best.
- Document the biological basis for the chosen window.

### E02 — Matched false-alarm rate

- Define the false-alarm rate and the matching procedure in advance.
- Compare the candidate indicator with conventional monitoring at the same false-alarm rate.
- Do not claim “earlier” without matching false alarms.

### E03 — Out-of-sample evaluation

- Use a temporal train/test split or rolling-origin evaluation.
- Do not evaluate on the same events used to tune the indicator.
- Report performance by year/event, not only pooled.

### E04 — Non-stationarity

- Test whether the indicator–bloom relationship is stable across years, seasons and trophic states.
- Report regime changes; do not assume a constant relationship.

### E05 — Alternative explanations

- Test seasonal co-trending, autocorrelation, sampling frequency and monitoring changes as alternative explanations.
- Include a null/seasonal benchmark.

### E06 — Event definition independence

- The bloom label must not be derived from the candidate indicator.
- If the label uses chlorophyll, the candidate indicator must not be the same chlorophyll series.

### E07 — Uncertainty and decision threshold

- Provide uncertainty for the event classification and the lead-time estimate.
- Define the decision threshold and its consequences (false positives vs false negatives).

### E08 — External validation

- Ideally, validate on a second lake or a held-out period.
- If not possible, state that the result is a single-system case study.

---

## 4. Müggelsee assessment summary

| Requirement | Status | Note |
|---|---|---|
| Q01 coverage | PASS | Long records; overlap/event balance not counted |
| Q02 event definition | FAIL/UNKNOWN | No public definition |
| Q03 event independence/count | UNKNOWN | No event count |
| Q04 sampling frequency/timing | CONDITIONAL | Weekly/biweekly documented; times not verified |
| Q05 taxonomy/biomass | CONDITIONAL/PASS | Methods documented; changes recorded; detection limits partial |
| Q06 sensor depth | CONDITIONAL/FAIL | 1.5 m sensor vs integrated samples |
| Q07 spatial co-location | CONDITIONAL | Different stations; offset not quantified |
| Q08 calibration/QC | UNKNOWN | Not public |
| Q09 non-bloom exposure | CONDITIONAL/UNKNOWN | Likely sampled; no classification |
| Q10 access/licence | FAIL/UNKNOWN | All rights reserved |
| Q11 version/history | PASS | DOIs/version history |
| Q12 data dictionary | CONDITIONAL | Metadata PDFs; full dictionary/code not public |

**Result:** **NOT QUALIFIED.** At least one mandatory requirement is FAIL/UNKNOWN (Q02, Q10), and several are conditional.

---

## 5. Qualification decision record

When a dataset is proposed, record:

| Field | Response |
|---|---|
| Dataset name | |
| DOI/version | |
| Custodian/permission | |
| Date assessed | |
| Assessor | |
| Q01–Q12 status | |
| E01–E08 status (if early warning) | |
| Fatal gaps | |
| Conditional gaps and bounds | |
| Reviewer opinion | |
| Decision | Qualified / Not qualified / Conditional pending evidence |
| Reason | |

**No dataset has been recorded as qualified. Müggelsee remains a candidate.**
