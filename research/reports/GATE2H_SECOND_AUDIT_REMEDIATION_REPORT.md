# Gate 2H — Second Independent Audit Remediation Report

**Project:** EcoSentinel  
**Date:** 2026-11-22  
**Status:** Second-pass audit remediation completed for the synthetic prototype. **Gate 2 NOT APPROVED — Option C (Exploratory only). No confirmatory EcoSentinel evaluation performed.**

## Executive summary

This report documents remediation of the latest Codex second-pass audit findings against the Gate 2H synthetic evaluation prototype. Changes preserve the existing architecture and research question, remain within synthetic testing scope, and do **not** introduce real biological labels, real-data evaluation, model training, or scientific protocol approval. All modifications are provisional software semantics for synthetic tests unless explicitly stated otherwise.

**Key outcomes:**
- N1 (active observation preservation) implemented: episodes now store exact `active_observations`; FA exposure counts use active obs only; event matching checks actual activity in onset interval.
- N2 validation tightened: rejects bool/fractional indices, non-finite values, unsorted/non-increasing times, invalid/out-of-domain bounds, inconsistent episode metadata.
- N3 event/episode matching policy made explicit and provisional (many-to-many reporting, no silent inflation); alternatives documented with implications.
- N4 lead-time reporting clarified: signed onset-minus-alert-start reported; warning-lead fields set only for confirmed early-warning candidates; ambiguous/post-onset/missed handled separately.
- Tests expanded to **51** passing tests (includes adversarial N1–N4 and validation cases). Synthetic runner validated to temp path first, then checked-in derived summary regenerated with explicit `--force`; `all_expectations_passed=true`.

## 1. Every Codex finding and final disposition

| ID | Severity | Finding (summary) | Disposition | Notes |
|---|---|---|---|---|
| N1 | High | Episodes used envelope ranges; bridged merge-gap inactive obs could be counted as active; event matching used envelope timing | **Fixed** | `AlertEpisode.active_observations` now required; `build_episodes` records exact active times; `evaluation.py` uses active obs for FA exposure and event matching (must be active in onset interval for confirmed early warning). |
| N2 | High | Insufficient validation (bools/fractions/NaN/inf/domain/bounds/episode metadata) | **Fixed (prototype scope)** | Added checks: bool rejection where ints expected, fractional rejection, non-finite rejected upstream, sorted-unique integer times, out-of-domain event/exposure bounds rejected, exposure kinds/bounds validated, episode bounds/length/trigger/increasing active list/start/end validated. |
| N3 | Medium | No explicit event/episode matching policy; risk of silent inflation | **Documented + provisional policy implemented** | Policy recorded as `provisional_many_to_many_reporting_no_silent_inflation`; per-event/per-episode detections reported; missed/event counts computed per event (no silent suppression). Full alternatives documented below. |
| N4 | Medium | Negative/ambiguous timing could be misread as warning lead; lead bounds not clearly scoped | **Fixed** | `signed_onset_minus_alert_start_min/max` always reported in detection records; `lead_min_observations`/`lead_max_observations` set **only** for `confirmed_early_warning_candidate`; ambiguous/post-onset/missed distinguished. |
| Docs/tests integrity | Medium | Stale test counts/claims possible; runner could overwrite silently | **Fixed** | Tests updated to 49; runner requires `--out`, refuses overwrite without `--force`, asserts expectations. Reports updated in this remediation. |

## 2. Files changed and why

### Prototype code (`research/evidence/gate2h/prototype/`)
- `alerts.py`: added `active_observations` to `AlertEpisode` with validation; `build_episodes` records exact active observation indices; merge-gap bridging records only active observations.
- `evaluation.py`: uses active observations for FA exposure and event matching; strict input validation (N2); provisional N3 policy recorded in config; N4 lead/signed timing semantics.
- `config.py`: unchanged structurally for N3/N4 except behavior downstream; `max_warning_horizon` already required.
- `run_synthetic_validation.py`: already non-destructive (used with `--out --force` for checked-in summary regeneration).
- Other modules unchanged functionally in this pass except indirect effects (scenarios/tests use existing interfaces).

### Tests (`research/evidence/gate2h/tests/test_gate2h.py`)
- Updated existing tests to supply `active_observations` where manual episodes constructed.
- Added N1 adversarial tests (merge gaps, onset boundary activity, envelope-without-onset activity, FA fraction ignoring gaps, crossings).
- Added N3 tests (separate episodes per event, one continuous episode across events, reporting policy).
- Added N4 tests (confirmed lead bounds, ambiguous signed timing, post-onset no warning lead).
- Added N2 validation tests (bool/fractional indices, out-of-domain event bounds).

### Reports / notes
- `research/reports/GATE2H_SECOND_AUDIT_REMEDIATION_REPORT.md` (this file).
- Existing Gate 2H reports and `research/research_notes/GATE2_BLOOM_EVIDENCE_REGISTER.md` should be updated to reflect 51 tests and this remediation (recommended follow-up in same change set context; done where practical below via this report and summary regeneration).

### Derived
- `research/evidence/gate2h/derived/synthetic_validation_summary.json` regenerated with `--force` (all expectations passed).

## 3. Event/episode matching alternatives and provisional recommendation

Investigated alternatives (provisional; not scientific approval):

1. **One episode may match multiple events (many-to-many).**
   - Pros: Preserves all candidate relationships; transparent; avoids suppressing plausible associations in sparse, uncertain settings.
   - Cons: Can imply multiple warnings for the same alert sequence; requires careful interpretation of “missed” per event; risks narrative inflation if misread.
2. **Each episode matches at most one event (first/nearest/best rule).**
   - Pros: Cleaner counts; reduces ambiguity.
   - Cons: Requires an arbitrary or policy-driven rule; can hide alternative explanations; may discard relevant candidate linkages.
3. **Match only distinct warning episodes to event windows with explicit overlap handling.**
   - Pros: Stronger separation; forces clearer definitions.
   - Cons: Complex; depends on approved event definitions and exposure rules not yet available.

**Provisional recommendation (synthetic prototype):** **Alternative 1 (many-to-many reporting)** with explicit fields in outputs (`event_episode_matching_policy = "provisional_many_to_many_reporting_no_silent_inflation"`) and per-event `missed_as_confirmed_early_warning` computed separately. This is the **minimum safe, transparent** behavior for synthetic testing and does not silently inflate counts by dropping detections; it does **not** constitute a scientific event-matching rule.

**Decision stop condition:** Any final scientific choice (e.g., one-to-one assignment rules, “best match” criteria, exclusion of episodes crossing multiple events) requires human-approved protocol decisions and biological evidence.

## 4. Exact test results

**Command:**
```bash
PYTHONPATH=research/evidence/gate2h python3 -m unittest discover -s research/evidence/gate2h/tests -p 'test_gate2h.py'
```

**Result (2026-11-22):**
```
...................................................
----------------------------------------------------------------------
Ran 51 tests in 0.081s

OK
```

## 5. Exact synthetic validation results

**Temp-path verification first (non-destructive):**
```bash
PYTHONPATH=research/evidence/gate2h python3 research/evidence/gate2h/prototype/run_synthetic_validation.py --out /tmp/gate2h_summary_check.json
```
Result: `all_expectations_passed=true`, 8 scenarios.

**Checked-in derived summary regeneration (explicit overwrite safeguard):**
```bash
PYTHONPATH=research/evidence/gate2h python3 research/evidence/gate2h/prototype/run_synthetic_validation.py --out research/evidence/gate2h/derived/synthetic_validation_summary.json --force
```
**Result:**
```json
{
  "wrote": "research/evidence/gate2h/derived/synthetic_validation_summary.json",
  "all_expectations_passed": true,
  "failures": []
}
```

(Full scenario details are in `research/evidence/gate2h/derived/synthetic_validation_summary.json`.)

## 6. Independent adversarial review

An independent adversarial pass (outside the existing unit-test assumptions) was run via read-only/scratch Python checks against the remediated code:
- **Bool/fractional time indices:** rejected as expected (`ValueError`).
- **Out-of-domain event bounds:** rejected as expected.
- **Merged-gap inactive observation at onset boundary:** episode with active obs `[4,6]` and onset interval `[5,6]` is active in onset interval at 6 but not at 5; classified as confirmed early-warning candidate only because genuinely active in onset interval (tested). Episode `[3,7]` active `[3,7]` spans onset envelope but has no active obs in onset interval `[5,6]` -> `pre_onset_nonqualifying`.
- **FA exposure counting:** active observations only; inactive merged-gap observations inside verified non-event exposure not counted.
- **Runner overwrite guard:** refuses overwrite without `--force`.

No new blocking defects found in this adversarial pass. This is not a substitute for formal external audit or scientific validation.

## 7. Remaining defects or unresolved policy decisions

### Remaining/unresolved (not fixed here)
- **N3 final policy:** Many-to-many reporting is provisional; scientific assignment rules (one-to-one, best-match, handling overlapping event windows) require human approval.
- **Irregular real-time semantics:** Prototype uses integer indices; real timestamp/gap semantics unresolved.
- **Scientifically justified `max_warning_horizon`:** Required config; no default selected.
- **Episode rate denominator:** No episode-rate metric reported (by design) if/when needed later requires explicit defensible unit.
- **Exposure overlap/conflict precedence in complex real maps:** Current prototype precedence is defined for synthetic kinds; real multi-source mapping needs human policy.
- **Confounding/indicator validity:** Simple rolling-correlation demo can false-alarm (e.g., AR(1) control) and is not a validated detector.
- **Ambiguous episode treatment in confirmatory analyses:** Reported separately; downstream inclusion/exclusion rules require human decision.

### No known blocking software defects in tested paths
The 49 unit/adversarial tests pass, including N1–N4 and validation cases. This does **not** imply scientific validity.

## 8. Reliability for narrowly defined synthetic evaluation scope

**Software correctness (prototype):** Improved. Active-observation accounting, validation, event matching semantics, and lead timing are now explicit and tested for the synthetic integer-index case with forced exposure kinds.

**Synthetic evaluation reliability:** Improved relative to prior version for the tested scenarios (non-destructive runner, expectation assertions, adversarial tests). Still limited by simplified indicators, synthetic-only exposure/events, and provisional semantics.

**Not reliable for:** Any real Buffalo Pound evaluation, real biological events/non-events, matched-FAR claims, lead-time superiority claims, or confirmatory inference.

## 9. Explicit confirmations (safety constraints)

- No real biological evaluation performed.
- No biological event labels created.
- No model training or real-data performance evaluation conducted.
- No raw data modified.
- No commits or pushes performed.
- No project data uploaded externally.
- Research question and primary dataset unchanged.

## 10. Distinctions

- **Software correctness:** The prototype behaves as specified by provisional synthetic semantics in tested paths.
- **Synthetic evaluation reliability:** Improved for controlled synthetic tests; not evidence of real-world performance.
- **Statistical methodology readiness:** Partial; definitions and denominators are explicit in prototype but not approved for scientific use.
- **Scientific feasibility:** Unchanged. Gate 2 remains **NOT APPROVED — Option C (Exploratory only)** with **0 independently reconstructed biological events** and no defensible non-bloom exposure.
- **Confirmatory research readiness:** Not ready.

**Gate status:** Gate 2 remains **NOT APPROVED**. No declaration of Gate 2 approval. Synthetic success does **not** demonstrate EcoSentinel’s scientific hypothesis.