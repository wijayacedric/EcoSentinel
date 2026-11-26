# Gate 2H — Remediation and Audit Disposition

**Project:** EcoSentinel  
**Date:** 2026-11-22  
**Status:** Remediation completed in synthetic-prototype scope. **Gate 2 NOT APPROVED. Option C — Exploratory only. No confirmatory EcoSentinel performance.**

## 1. Scope

This report records reproduction, remediation, and finding-by-finding disposition of the external Codex audit provided by the user. All fixes are **provisional synthetic software semantics only** (explicitly approved by user for Gate 2H prototype). No scientific protocol approval is implied.

## 2. Reproduced findings (before fix)

| ID | Reproduction | Result |
|---|---|---|
| H1 | Stale episode 0–1 with event onset 5 | `missed_synthetic_events=0`, lead reported as 5 (incorrect) |
| H2 | Episode overlapping unknown but with verified non-event obs | `false_alarm_episode_count=0`, `false_alarm_observations=0` despite 8 verified non-event obs in exposure (incorrect) |
| H3 | 2 FA episodes / 10 non-event obs | `far_per_episode=0.2` (episodes per observation, misleading name) |
| H4 | Runner overwrote checked-in derived summary and did not assert expectations | Confirmed by code inspection; fixed by non-destructive runner |
| M1 | Mismatched times/valid lengths | No error raised (incorrect) |
| M3 | `apply_persistence([F,T,T,F,T,T,T],3)` | Backdated to `[F,T,T,F,T,T,T]` (incorrect) |
| M4 | `parse_float('inf')`, `parse_float('nan')` | Non-finite accepted / inconsistent handling |

## 3. Approved provisional semantics implemented

- **Event matching:** Episodes ending before `onset_earliest` cannot count as successful warnings. Warning must begin before `onset_earliest`. Episode beginning inside uncertain onset interval = `onset_overlapping_ambiguous`, not confirmed early warning. Episode beginning after `onset_latest` = `post_onset_detection`. Episode beginning before `onset_earliest` and remaining active into onset interval can count as warning only if within configured `max_warning_horizon`. `max_warning_horizon` required explicitly (no scientific default) and reported in outputs. Lead bounds preserved; confirmed early warnings distinguished from ambiguous onset-overlapping alerts.
- **FAR accounting:** Report `observation_level_false_alarm_fraction` (alert obs in verified non-event exposure / all valid verified non-event obs), `confirmed_false_alarm_episode_count`, `ambiguous_episode_count`. No episodes-per-observation field reported as episode rate.
- **Unknown exposure (option a):** Count alert obs only within verified non-event exposure; exclude event and unknown from denominator; do not discard valid non-event obs because episode overlaps unknown/event; report boundary-crossing episodes as ambiguous where appropriate; never silently classify unknown as non-event.
- **All semantics labeled provisional synthetic software semantics** in config/output.

## 4. Finding-by-finding disposition

| ID | Severity | Disposition | Fix | Verification |
|---|---|---|---|---|
| H1 | High | **Fixed** | Event matching excludes episodes ending before `onset_earliest`; requires warning start before `onset_earliest`; classifies onset-overlapping/post-onset; requires active into onset interval and `max_warning_horizon` | `test_h1_stale_alert_not_counted`, `test_warning_must_begin_before_onset_earliest`, `test_post_onset_detection`, `test_confirmed_early_warning_with_horizon`, `test_outside_max_horizon_not_confirmed` |
| H2 | High | **Fixed** | Observation-level accounting counts verified non-event alert obs regardless of episode overlap; episode classified ambiguous when crossing event/unknown boundaries; no whole-episode discard | `test_h2_unknown_overlap_does_not_erase_verified_non_event_obs`, `test_ambiguous_episode_crossing_event_boundary` |
| H3 | High | **Fixed** | Removed `far_per_episode`; added explicit `observation_level_false_alarm_fraction`, `confirmed_false_alarm_episode_count`, `ambiguous_episode_count` | `test_h3_no_misleading_episode_rate_field` |
| H4 | High | **Fixed** | Runner requires `--out`, refuses overwrite without `--force`, asserts scenario expectations, writes `all_expectations_passed` | `test_runner_refuses_overwrite_without_force`, `test_runner_writes_new_file_and_checks_expectations` |
| M1 | Medium | **Fixed (prototype scope)** | Input validation for lengths, sorted unique integer times, exposure kinds/bounds, duplicate event IDs, episode bounds | `test_mismatched_lengths_rejected`, `test_unsorted_times_rejected`, `test_invalid_exposure_kind_rejected` |
| M2 | Medium | **Partially fixed / explicitly bounded** | Still integer-index synthetic prototype; times validated as strictly increasing ints; irregular real-time semantics remain unresolved and documented | Validation tests; limitations report updated |
| M3 | Medium | **Fixed** | `apply_persistence` no longer backdates; alert active from persistence-satisfied index onward | `test_persistence_not_backdated` |
| M4 | Medium | **Fixed** | `parse_float` rejects non-finite values; `valid_observation` normalizes flags and rejects non-finite | `test_non_finite_rejected` |
| M5 | Medium | **Fixed (prototype scope)** | Config `validate()` added for all configs; baselines/multivariate call validate; EvaluationConfig requires horizon when evaluating | Validation tests; config validation |
| M6 | Medium | **Fixed** | Weak scenario tests replaced with specific expectation assertions in runner and stronger unittest assertions | Scenario tests + runner expectation checks |
| L1 | Low | **Documented / not scientifically resolved** | Rolling correlation remains simple descriptive demo; AR(1)/seasonal controls included; no inferential claim | Limitations report; scenario controls |

## 5. Verification

- **Unit/scenario tests:** `PYTHONPATH=research/evidence/gate2h python3 -m unittest discover -s research/evidence/gate2h/tests -p 'test_gate2h.py'` → **Ran 51 tests, OK** (2026-11-22).
- **Synthetic runner:** `PYTHONPATH=research/evidence/gate2h python3 research/evidence/gate2h/prototype/run_synthetic_validation.py --out research/evidence/gate2h/derived/synthetic_validation_summary.json --force` → `all_expectations_passed=true`.
- **No raw data modified. No commits/pushes.**

## 6. Residual unresolved ambiguities (not hidden by defaults)

- **Irregular real-time semantics:** prototype uses integer indices; real-time gap/persistence rules unresolved.
- **Max warning horizon value:** required config; no scientifically justified value selected.
- **Episode rate denominator:** not reported; if needed later, requires explicit defensible unit/denominator.
- **Ambiguous episode policy:** episodes crossing unknown/event boundaries reported as ambiguous; whether they are excluded/included in specific future analyses requires human protocol decision.
- **Post-onset detection utility:** reported separately; scientific value depends on approved event definition.
- **Exposure interval precedence/overlaps:** current precedence treats any unknown/event as excluding verified non-event at observation level; complex overlapping exposure maps require explicit policy.
- **Autocorrelation/confounding:** simple demo indicator can false-alarm on AR(1); not a validated detector.

## 7. Status after remediation

- **Software correctness (prototype scope):** Improved; major audit defects addressed and regression-tested.
- **Statistical methodology readiness:** Partial; provisional semantics explicit, but scientific decisions remain human-approved.
- **Scientific feasibility:** Unchanged/blocked (Gate 2 NOT APPROVED, Option C).
- **Confirmatory evaluation readiness:** Not ready.

## 8. Second independent audit remediation

See `research/reports/GATE2H_SECOND_AUDIT_REMEDIATION_REPORT.md` for N1-N4 remediation (active observation preservation, stricter validation, explicit provisional event/episode matching policy, lead-time reporting clarification), 51/51 tests, and adversarial review.
