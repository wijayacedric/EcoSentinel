# Current Project State — Sprint 4L.11

**Assessment date:** 2026-11-24  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Status:** Assessment only; no protocol change, labels, modelling, acquisition or external contact.

## 1. Research question and approved scope

The project question remains unchanged:

> Can persistent changes in relationships between freshwater environmental variables provide earlier warning of cyanobacterial blooms than conventional monitoring, at comparable false-alarm rates?

The current protocol is `documentation/SCIENTIFIC_PROTOCOL_DRAFT.md`. It defines the question but leaves the critical operational definitions unresolved: bloom event, non-bloom exposure, early-warning horizon, persistence rule, false-alarm target, conventional monitoring baseline, event/non-event adjudication, and splits. The protocol is not approved for confirmatory work.

Current governance permits exploratory/descriptive work only. It prohibits:

- bloom/non-bloom labels or event intervals;
- confirmatory modelling, hypothesis testing or threshold optimisation;
- protocol or research-question changes without separate approval;
- new dataset acquisition or external contact;
- uploads, publication, commits or pushes;
- modification of raw data or prior evidence.

## 2. Current evidence status by candidate

| Candidate | Verified biological evidence | Environmental evidence | Current status |
|---|---|---|---|
| **Buffalo Pound Lake, SK** | Species-level microscopy 2018 (25 dates) and 2019 (17 dates); **42 date-level observations**; 0.8 m depth; no verified non-bloom season | 8 buoy files, 2014–2021, 10-min (2014: 15-min), 68 variables | **Exploratory only / pending researcher clarification.** 2 biological seasons, interval-censored 1–16-day gaps, unresolved 2019-07-17 anomaly, no non-bloom exposure. Not confirmatory-ready. |
| **Lake Mendota, WI** | 402 microscopy dates, 1995–2020; 400 0–8 m composites, 2 0–2 m; 468 nonblank taxa names; taxonomic non-stationarity; anomalies | 129.42 daily sensor data 2006–2025; 3,996 records; 18 variables; Turner/YSI eras | **RETAIN — LIMITED EXPLORATORY USE; REJECT for original early-warning validation.** Same-day overlap: 128 Turner chlorophyll, 139 Turner phycocyanin, 99 DO raw; only 58/402 biology dates support a 7-variable Turner core and 2/402 support an 11-variable YSI core. 0.5 m sensors vs 0–8 m composite. |
| **Greifensee, CH** | Classifier-derived biology; no independent cell counts/biovolume validation | High-frequency CTD/meteo/nutrients, 2018–2023 | **Exploratory only.** Not independent biological ground truth. |
| **Western Lake Erie, USA/Canada** | Literature-level pigments/toxins; no verified cell counts/biovolume | Discrete weekly/biweekly; no verified HF buoy pairing; NCEI access blocked | **Low-priority backup.** Not confirmatory-ready. |

No candidate currently supports a confirmatory test of the original question.

## 3. Buffalo Pound correspondence status

The project records state that an academic contact forwarded the original enquiry to University of Saskatchewan / University of Regina researchers, and `research/reports/schedule_recovery_sprint_2/INSTITUTIONAL_EVIDENCE_STATUS.md` records a **user-reported request sent** to Helen Baulch, Kristin Painter, Blair Kardash, Scott Higgins and the Saskatchewan Water Security Agency. The repository does **not** contain a send date, confirmation, reply, data summary or access terms:

- `research/evidence/sprint_4h_researcher_response_readiness/` describes Buffalo Pound as **PENDING researcher clarification**, not rejected.
- `GATE2_REQUIREMENT_TRACKER.csv` still records the additional biological data as **not assumed** and the status as pending.
- `UPDATED_DATASET_COMPARISON_MATRIX.csv` states: “Referred U Saskatchewan/U Regina researchers may hold additional years, archived slides, non-bloom sampling, raw counts, station/depth/QC docs. **NOT ASSUMED.**”
- `institutional_response_tracking_template.csv` remains `not_contacted_or_unknown`; no response date, data summary, terms or referral contacts are recorded.
- The Schedule Recovery Sprint 2 record explicitly says the repository lacks send-date/confirmation/response documentation and that silence is not rejection.
- No `.eml`, reply file, correspondence log or data-transfer record was found in the project tree.
- No additional years, non-bloom sampling or higher-frequency biology are present in the verified Buffalo Pound files.

**Assessment:** Requests are **reported sent by the user**, but no reply or data development is documented. If a reply exists outside the repository, it is not available to this assessment. Buffalo Pound remains **pending/exploratory**; no additional data are assumed. No further contact was initiated.

## 4. Gate 2 / Gate 2H state

- Gate 2 remains **PAUSED / NOT APPROVED — Option C**.
- The Gate 2H executable evaluation prototype is a **synthetic/software** artifact: 51/51 tests pass, but it has **no real biological labels, no reconstructed events, no non-bloom exposure, and no empirical matched-FAR result**.
- Technical readiness has improved; scientific feasibility has not.
- The project has 0 independently reconstructed biological bloom events from accessible evidence and 0 defensible non-bloom intervals for matched-FAR evaluation.

## 5. Prior-art state

The field already contains:

- high-frequency in situ cyanobacterial early-warning/forecasting systems (e.g. Recknagel et al. 2025; Fournier et al. 2024);
- early-warning-signal (EWS) tests for algal blooms with true/false alarm rates (Buelo et al. 2022);
- empirical EWS assessments showing low reliability and low agreement (Gsell et al. 2016; O’Brien et al. 2023);
- multivariate resilience/relationship indicators with scenario-dependent performance (Weinans et al. 2021);
- Mendota-specific high-frequency phycocyanin research (Carpenter et al. 2020, 2022) and seasonal/sub-seasonal forecasts (Beal et al. 2021, 2022);
- sensor-validation studies showing weak/variable phycocyanin–biovolume relationships (Cotterill et al. 2019; Levi et al. 2025).

Matched false-alarm rate is a quality requirement, not a standalone novelty. The exact combination of persistent relationship-change indicators, independent biological events, interval-censored onset, and matched-FAR evaluation in cyanobacteria is **not confirmed as novel**; full-text comparator gaps remain.

## 6. Unresolved decisions

The Gate 2G methods register remains unresolved on:

- biological-only event definition;
- candidate vs approved event distinction;
- interval-censored onset/termination;
- 2019-07-17 anomaly handling;
- non-bloom exposure definition;
- spatial alignment;
- temporal alignment/window;
- independent event separation;
- train/validation/test splits;
- matched-FAR design;
- missed-event evaluation;
- lead-time definition;
- conventional baseline definition;
- QC-flag handling;
- uncertainty estimation;
- external data terms;
- Gate 2 approval criteria.

## 7. Current bottom line

The project is scientifically well documented and technically prepared, but the original question is **not currently testable** with the available evidence. The dominant blockers are biological event/non-event validity, temporal resolution, measurement comparability, and the absence of a real matched-FAR evaluation. Buffalo Pound remains pending; Mendota is retained only for limited exploratory use; no confirmatory candidate exists.

The strategic decision is therefore about whether to preserve, narrow, pivot or pause — not whether to approve Gate 2.
