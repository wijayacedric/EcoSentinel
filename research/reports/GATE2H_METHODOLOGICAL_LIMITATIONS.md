# Gate 2H — Methodological Limitations

**Project:** EcoSentinel  
**Date:** 2026-11-22  
**Status:** Critical limitation report for Gate 2H prototype. **Gate 2 NOT APPROVED. Option C — Exploratory only.**

## 1. Core limitation statement

Gate 2H produced a **tested synthetic evaluation prototype**, not evidence that EcoSentinel can provide earlier cyanobacterial bloom warning. The prototype improves software readiness; it does not resolve the scientific blockers identified in Gate 2D–2G and the independent devil's advocate review.

## 2. What Gate 2H does NOT establish

- No real biological bloom or non-bloom labels were created.
- No independently reconstructed biological bloom events exist (still 0).
- No defensible independent non-bloom exposure exists.
- No matched-FAR confirmatory EcoSentinel performance was calculated.
- No early-warning lead-time improvement was demonstrated on real data.
- No predictive model was trained/tuned on Buffalo Pound data.
- No Gate 2/3 approval.

## 3. Methodological limitations by component

| Component | Limitation | Why it matters | Human/scientific decision needed |
|---|---|---|---|
| Event definition | Prototype accepts synthetic interval-censored events only | Real events require biological-only criteria and independence checks | Approve event definition (M1/M2/M3/M8) |
| Exposure/non-bloom | FAR requires explicit exposure intervals; real exposure undefined | Any unverified non-bloom assumption invalidates FAR | Approve non-bloom exposure/FAR denominator (M5/M10) |
| Lead time | Bounds computed from interval-censored onset only | Sparse sampling may make few-day claims meaningless | Approve lead-time/censoring interpretation (M12) |
| Alert accounting | Merge gap, persistence, missing-break are configurable | Different settings change episode/FAR counts | Approve alert accounting rules |
| Baselines | Threshold/z-score/correlation demos are transparent but not validated as "conventional monitoring" | Weak/straw-man baselines can inflate perceived novelty | Approve baseline suite (M13) |
| Multivariate indicator | Simple rolling correlation change only | May miss relevant structure or trigger on confounding | Approve indicator family and confounding controls |
| Confounding controls | Synthetic AR(1)/seasonal/artifact controls included, but limited | Real confounding is more complex (hydrology, management, sensor drift) | Approve negative-control/sensitivity protocol |
| Missingness | Missing-as-break supported; real missingness mechanisms more complex | Missing data can create or hide alerts | Approve flag/missingness policy (M14/M15) |
| Spatial alignment | Not implemented for multi-source real data | Intake/buoy/lab location mismatch can invalidate alignment | Approve spatial alignment (M6) |
| Uncertainty | Lead bounds and counts reported; no inferential statistics | Small-n real event counts will limit inference | Approve uncertainty reporting (M16) |

## 4. Specific residual risks

1. **Unknown exposure misclassification:** If future users label ambiguous periods as synthetic_non_event, FAR becomes invalid. Prototype guard refuses missing exposure, but cannot police human mislabeling.
2. **Episode accounting sensitivity:** Merge-gap and persistence choices can inflate/suppress alerts. Sensitivity analysis is required before any real comparison.
3. **Post-artifact lingering alerts:** Sensor artifact scenario showed alerts can persist into recovery/unknown windows; real sensor QA rules must be pre-approved.
4. **Autocorrelation false alarms:** AR(1) control produced false alarms, demonstrating confounding risk for naive relational indicators.
5. **Interval-censored false precision:** Lead-time bounds are better than point estimates but still depend on observation schedule and event definition.

## 5. Readiness assessment

| Dimension | Status | Rationale |
|---|---|---|
| A. Software correctness | **Improved for prototype scope** | 51/51 tests pass after second independent-audit remediation; H1-H4/M1-M6/N1-N4 addressed with provisional semantics; active-observation accounting, stricter validation, explicit matching policy, and lead-time reporting clarified; residual ambiguities documented |
| B. Statistical methodology readiness | **Partial** | Architecture includes FAR/interval-censoring/alert accounting concepts, but definitions, denominators, baselines, and uncertainty rules are unapproved |
| C. Scientific feasibility | **Unchanged / blocked** | No new biological evidence; 0 reconstructed events; no non-bloom exposure; Gate 2 still blocked |
| D. Confirmatory evaluation readiness | **Not ready** | Missing approved biological definitions/data, exposure denominator, splits, baselines, and human Gate 2/3 approval |

## 6. Remediation status

External Codex audit findings H1-H4, M1, M3-M6, L1 were reproduced and remediated in prototype scope (see `GATE2H_REMEDIATION_AUDIT_DISPOSITION.md`). M2 remains partially bounded (integer-index synthetic prototype; irregular real-time semantics unresolved). All semantics are provisional software semantics, not scientific protocol approval.

## 7. Required human decisions before any real-data evaluation

- Approve biological-only event and non-event exposure definitions (M1, M5).
- Approve interval-censoring/anomaly handling (M3, M4).
- Approve alignment and event-separation rules (M6, M7, M8).
- Approve baseline suite and matched-FAR protocol (M10, M13).
- Approve data-quality/flag handling and sensitivity analyses (M14, M15).
- Approve uncertainty/reporting limits for small-n events (M16).