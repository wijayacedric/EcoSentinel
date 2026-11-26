# EcoSentinel — Scientific Weakness and Opportunity Register

**Project:** EcoSentinel  
**Date:** 2026-11-22  
**Status:** Critical review artifact. **Gate 2 NOT APPROVED / Option C — Exploratory only.**

## 1. Prioritised weakness register

| Priority | ID | Weakness | Type | Why it matters | Evidence/status | What would mitigate it |
|---|---|---|---|---|---|---|
| P0 | W1 | No independent biological ground truth for confirmatory evaluation | Scientific/evidentiary | Cannot validate bloom events; circularity risk if buoy RFU used | 0 independently reconstructed events; Boyer raw inaccessible; Painter sparse | Obtain record-level independent biological data; pre-approved biological-only event reconstruction |
| P0 | W2 | No defensible non-bloom exposure / FAR denominator | Methodological | Matched-FAR comparison impossible; false alarms undefined | Register/Gate 2 reports confirm no exposure denominator | Pre-approved non-event exposure rules; biologically supported unknown handling |
| P0 | W3 | Interval-censored sparse biological sampling | Evidentiary/statistical | Lead-time claims may be smaller than observation uncertainty | Painter 1–16 day gaps; Boyer ~5-day sampling | Interval-censored lead-time analysis; only claims larger than uncertainty |
| P1 | W4 | High confounding by seasonality/autocorrelation/common forcing | Methodological | Apparent relational signal may be trivial seasonal artifact | High-frequency buoy series; strong seasonal structure expected | Seasonal/null models, detrending/sensitivity, block/bootstrap by time, negative controls |
| P1 | W5 | Leakage risk in time-series evaluation | Methodological | Inflated performance | No approved split yet; protocol identifies risk | Event/year splits, train-only scaling, alert-rule pre-specification, leakage tests |
| P1 | W6 | Baseline insufficiency risk | Methodological | Weak baselines make novelty appear stronger | Baselines drafted but not implemented/evaluated | Strong simple baselines: persistence, univariate thresholds, rolling z-score, lagged logistic |
| P1 | W7 | Originality not sharply demonstrated | Scientific positioning | Project may look incremental | HAB forecasting/EWS literature extensive | Define narrow contribution; cite/compare directly; show where relational+matched-FAR adds value |
| P2 | W8 | Spatial/temporal alignment uncertainty | Methodological | Intake/buoy/sample mismatch can create spurious signals | BPWTP intake vs buoy; variable sample times/depths | Metadata-driven alignment rules; exclude ambiguous matches |
| P2 | W9 | Sensor quality/flag handling complexity | Data quality | Artifacts may look like signals | M/C/A2-A6/B6/B7 flags; 2019 deep-sensor limits; 2015 PAR shading | Pre-registered flag policy; sensitivity analyses |
| P2 | W10 | Small-n uncertainty / over-interpretation risk | Statistical | Even with events, inference may be weak | 2018–2019 sparse; possible few events total | Descriptive event-level reporting; interval estimates; avoid p-value overreach |
| P2 | W11 | Generalisability limited to one lake | External validity | High-level competition judges will challenge scope | Single site Buffalo Pound | Frame as single-site case study; no cross-lake claims without validation |
| P3 | W12 | Communication risk: readiness mistaken for feasibility | Project communication | Stakeholders may overestimate progress | Gate 2G improved tooling, not evidence | Explicit "technical readiness != scientific feasibility" in all reports |

## 2. Opportunity register

| ID | Opportunity | Category | Value | Cost/risk | Prerequisite | Recommendation |
|---|---|---|---|---|---|---|
| O1 | Build a rigorous exploratory sensor QA/confounding report | A. Immediate | High | Low | Existing buoy data + audit tables | Pursue |
| O2 | Pre-specify baseline suite and evaluation mock-up (no labels) | A. Immediate | High | Low | Protocol/methods register | Pursue |
| O3 | Implement leakage/split/unit tests for future pipeline | A. Immediate | High | Low | Existing codebase | Pursue |
| O4 | Create interval-censored biological observation schema (candidate-only) | A. Immediate | Medium | Medium (misuse risk) | Painter/BPWTP existing evidence | Pursue with strict "candidate, not label" guards |
| O5 | Add seasonality/null-model negative controls to analysis plan | A. Immediate | High | Low | Methods decision | Pursue |
| O6 | If Boyer 2017 raw data arrives, reconstruct candidate intervals with uncertainty | B. New evidence | Very high | Medium | Human authorization + data access | Pursue first if data arrives |
| O7 | If BPWTP/WSA phyto/biovolume records arrive, build 2014–2021 biological observation ledger | B. New evidence | Very high | Medium/High | Human authorization + data access | Pursue |
| O8 | If sufficient events exist, run matched-FAR event-level comparison with strong baselines | B. New evidence | Very high | High | Gate 2/3 approval, definitions, exposure | Pursue only after approvals |
| O9 | Decide biological event/non-event definitions and anomaly handling | C. Human decision | Critical | High if wrong | Data + expert/mentor review | Required |
| O10 | Decide acceptable claim scope for SciFest (exploratory vs confirmatory) | C. Human decision | High | Medium | Human review | Required |
| O11 | Add complex deep learning models now | D. Not worth now | Low | High | None | Defer/not worth now |
| O12 | Broaden to other lakes before Buffalo Pound ground truth solved | D. Not worth now | Low/Medium | High distraction | None | Defer |

## 3. Contradictions/tensions observed

| Tension | Description | Resolution |
|---|---|---|
| Ambition vs evidence | Long-term Option A ambition is motivating, but current evidence supports only Option C | Keep ambition explicit but never upgrade classification without evidence |
| Process maturity vs scientific validity | Gate 2G improved tooling/readiness; this can look like progress toward confirmatory claim | Separate technical readiness from scientific feasibility in every report |
| Novelty vs rigor | Pressure to be "novel" can push toward complex models; rigor requires simple baselines and defensible labels | Prioritize rigor; novelty claim must survive baseline/ablation/confounding tests |
| Data acquisition vs scope creep | More searching can feel productive but has diminishing returns | Pause broad search; focus on human-authorized institutional data and exploratory rigor |

## 4. Highest-value immediate actions (no new data)

1. **Confounding/null-model plan:** pre-specify seasonality, autocorrelation, and sensor-artifact negative controls before any future modeling.
2. **Evaluation harness design (dry-run):** define event-level data structures, alert accounting, FAR denominator logic, and leakage tests using synthetic fixtures only.
3. **Baseline-first protocol:** lock baseline suite and matched-FAR comparison rules for future approved data.
4. **Evidence ledger hardening:** continue candidate-only, interval-censored biological observation ledger with explicit uncertainty fields.