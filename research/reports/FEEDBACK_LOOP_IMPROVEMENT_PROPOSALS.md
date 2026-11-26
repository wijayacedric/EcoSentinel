# EcoSentinel — Feedback Loop Improvement Proposals

**Project:** EcoSentinel  
**Date:** 2026-11-22  
**Status:** Critical feedback loop (second-pass completed). **Gate 2 NOT APPROVED. Option C — Exploratory only. No labels/modeling/Gate 4.**

## 1. Prioritised findings (from Reviews 1–5)

| Rank | Finding | Severity | Why it matters | Immediate action possible? |
|---|---|---|---|---|
| 1 | No independent biological ground truth / no non-bloom exposure | Critical | Confirmatory hypothesis cannot be tested; FAR/lead-time invalid | No - requires new evidence + human decisions |
| 2 | Interval-censored biological sampling limits lead-time claims | Critical | Apparent early warning may be within observation uncertainty | Partly - can pre-specify interval-censored handling |
| 3 | Confounding by seasonality/autocorrelation/sensor artifacts | High | False positive relational signals likely | Yes - design null/negative controls and sensitivity plan |
| 4 | Leakage and evaluation-design risk | High | Inflated performance easy in high-frequency time series | Yes - pre-specify splits, alert accounting, tests |
| 5 | Originality/positioning vulnerable | High | Crowded HAB EWS/forecasting field | Yes - sharpen contribution and baseline comparison plan |
| 6 | Small-n/uncertainty/generalizability limits | Medium-High | Overconfident claims likely even with data | Yes - plan descriptive/interval-censored reporting |

## 2. Contradictions between reviews

| Contradiction | Tension | Assessment | Resolution |
|---|---|---|---|
| "Strong process maturity" vs "not competition-ready" | Documentation/readiness is good, but core evidence is missing | Both true | Present as rigorous feasibility/methods work, not confirmatory early-warning result |
| "Original question is good" vs "question may be too broad" | Question is relevant but under-specified operationally | Both true | Keep question unchanged; operationalize definitions only through approved Gate 2/3 process |
| "Negative result could be valuable" vs "may not win high award" | Scientific value and competition impact differ | Both true | Optimize for scientific validity; be honest about competition limits |
| "More analysis now" vs "risk of over-analysis without labels" | Preparation helps, but can create false momentum | Real risk | Restrict to label-free, leakage-aware, reproducible preparation |

## 3. Genuine scientific problems vs presentation/documentation improvements

### Genuine scientific problems
- Missing independent biological event/non-event evidence (W1/W2).
- Interval-censored onset/termination uncertainty (W3).
- Confounding/autocorrelation/common forcing (W4).
- Leakage/evaluation validity (W5).
- Unclear defensible novelty unless empirically demonstrated (W7).

### Presentation/documentation improvements (necessary but insufficient)
- Better report structure, figures, and narrative.
- Clearer competition framing.
- More polished code/docs.
- Explicit limitation statements (already improving).

**Rule:** No presentation improvement can substitute for biological ground truth or valid evaluation design.

## 4. Specific corrections and experiments

| ID | Proposal | Type | Preserves research question? | Scientific value | Feasibility now | Human decision needed? | Notes |
|---|---|---|---|---|---|---|---|
| P1 | **Pre-registered evaluation blueprint (label-free):** define event/non-event schemas, alert accounting, matched-FAR denominator logic, interval-censored lead time, and leakage checklist; test with synthetic fixtures only | Method design | Yes | High | High | Yes for final approval | No real labels; prevents ad-hoc evaluation later |
| P2 | **Confounding/null-control plan:** seasonality-only, shuffled-time, sensor-dropout, and common-trend controls; require relational signal to beat them | Method design | Yes | High | High | Yes for final acceptance | Directly targets strongest methodological attack |
| P3 | **Baseline suite specification:** persistence, univariate thresholds, rolling z-score, simple lagged logistic/regression (when labels exist), all under same splits/alerts | Method design | Yes | High | High | Yes for baseline definitions | Prevents weak-baseline novelty claims |
| P4 | **Candidate biological observation ledger (strict):** convert Painter/BPWTP existing evidence into interval-censored candidate observations with uncertainty fields, no labels | Data structuring | Yes | Medium | High | No for creation; Yes for use | Must be clearly marked candidate-only |
| P5 | **Sensor QA sensitivity matrix:** predefine how M/C/A2-A6/B6/B7 and year-specific sensor gaps affect analyses | Data quality | Yes | Medium | High | Yes for final handling rules | Reduces artifact-driven findings |
| P6 | **Biological-data intake dry run:** validate templates/scripts against synthetic fixtures and schema variations | Technical readiness | Yes | Medium | High | No | Already started in Gate 2G |
| P7 | **Independent biological event reconstruction (if data arrives):** reconstruct candidate intervals only under pre-approved biological-only criteria | Evidence | Yes | Critical | Blocked | Yes | Highest-value path to Option A/B reconsideration |
| P8 | **Matched-FAR confirmatory pilot (if sufficient evidence arrives):** small, pre-registered, event-level, baseline-first evaluation | Confirmatory analysis | Yes | Critical | Blocked | Yes | Only after Gate 2/3 approval |

## 5. Which changes could materially improve scientific quality

**Material now (no new evidence):** P1–P3, P5. They reduce leakage/confounding/baseline risks and make future evaluation defensible.  
**Material only with new evidence:** P7–P8. They address the core blocker (independent biological ground truth and valid confirmatory evaluation).  
**Supportive but not sufficient:** P4, P6, documentation polish.

## 6. Option A recovery prospects (reassessed, not upgraded)

**Assessment:** Option A remains **possible in principle but currently unsupported and uncertain**. Gate 2G/this review improved technical readiness and methodological clarity, but did not add independent biological event/non-event evidence. The binding constraints remain W1–W3. Therefore Gate 2 classification remains **Option C — Exploratory only**.

**What would move prospects materially:** verifiable record-level biological records (Boyer 2017 raw/SI; BPWTP/WSA phytoplankton/biovolume/cell counts/lab chl-a/toxins with metadata), followed by human-approved biological-only event/non-event definitions, interval-censored reconstruction, and matched-FAR evaluation design.

## 7. Independent second-pass review (performed once)

### 7.1 Do proposed corrections actually resolve the weaknesses?

| Weakness | Proposal(s) | Second-pass judgment | Residual gap |
|---|---|---|---|
| W1 No independent biological ground truth | P7 | **Partly resolves only if data arrives and is independently verifiable.** P1-P6 do not resolve it. | No new evidence yet; human approval required |
| W2 No non-bloom exposure/FAR denominator | P1, P7, P8 | **Not resolved now.** Design can be specified, but denominator requires approved biological exposure data. | Exposure evidence missing |
| W3 Interval-censored sampling | P1, P7 | **Partly resolvable.** Can represent uncertainty honestly; cannot create precision that data lacks. | Lead-time claims may remain limited |
| W4 Seasonality/confounding | P2, P5 | **Substantially improvable now** at design level; empirical resolution requires careful future analysis. | Confounding can never be fully eliminated observationally |
| W5 Leakage/evaluation risk | P1, P3, P6 | **Substantially improvable now.** Tests and pre-specification reduce but do not guarantee perfect execution. | Human discipline and code review still needed |
| W7 Originality vulnerability | P1-P3, P8 | **Improvable.** Clear positioning and fair baselines help; true novelty must be demonstrated empirically. | Crowded field remains |

### 7.2 Are any proposals cosmetic?

- Documentation-only polish: **cosmetic unless tied to W1-W5 controls**.
- P4 can become cosmetic/risky if candidate ledger is misused as labels. It must carry hard "candidate-only, not approved" metadata.
- P6 is supportive; valuable for reliability, not a scientific resolution.

### 7.3 Second-pass conclusion

The proposals improve **defensibility and readiness** but do **not** resolve the core confirmatory blocker. The only path to materially resolving W1/W2 is acquisition and human-approved reconstruction of independent biological evidence. After this second pass, no further self-review loop is performed.