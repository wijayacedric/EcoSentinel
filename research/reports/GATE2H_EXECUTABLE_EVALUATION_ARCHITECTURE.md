# Gate 2H — Executable Evaluation Architecture

**Project:** EcoSentinel  
**Date:** 2026-11-22  
**Status:** Prototype architecture implemented for **synthetic/software testing only**. **Gate 2 NOT APPROVED. Option C — Exploratory only. No real biological labels. No confirmatory EcoSentinel performance.**

## 1. Objective

Provide a modular, tested evaluation engine that can later accept human-approved biological evidence without rewriting core alert/accounting logic. This prototype validates software logic with deterministic synthetic fixtures only.

## 2. Module layout

Location: `research/evidence/gate2h/prototype/`

| Module | Responsibility | Key safeguards |
|---|---|---|
| `config.py` | Typed configs for baselines, multivariate indicators, alert accounting, evaluation | `EvaluationConfig.allow_unverified_exposure` forced False |
| `quality.py` | Observation parsing, missing/flag validity | M/C/bad-flag validity checks; missing values explicit |
| `baselines.py` | Transparent baseline alerts (threshold, rolling z-score) | Backward-looking windows only |
| `multivariate.py` | Rolling correlation-change indicator | Backward-looking baseline/correlation windows; no future data |
| `alerts.py` | Persistence, episode construction, merge-gap, missing-break handling | Prevents repeated triggers from becoming independent episodes by accounting rules |
| `events.py` | Interval-censored synthetic event and exposure interval representations | Explicit bounds validation; source labels |
| `evaluation.py` | Synthetic evaluation accounting: FAR, episodes, missed events, lead-time bounds | Refuses missing exposure; counts only explicit synthetic non-event exposure; unknown exposure excluded from confirmed false alarms |
| `guards.py` | Leakage/split checks | No future baseline, temporal split, no random window split |
| `scenarios.py` | Deterministic synthetic fixtures | All scenarios/events/exposure labeled `SYNTHETIC_TEST` |
| `run_synthetic_validation.py` | Reproducible synthetic summary JSON | Writes `synthetic_only=true` output |

## 3. Data flow

1. **Ingest observations** -> `Observation(t, values, flags, is_missing)`.
2. **Quality filter** -> valid/invalid per required variables and flags.
3. **Generate raw alert flags** -> baseline or multivariate indicator.
4. **Apply persistence** -> `apply_persistence`.
5. **Build episodes** -> `build_episodes` with merge-gap/missing-break/min-length.
6. **Evaluate on synthetic fixtures only** -> `compute_synthetic_evaluation` with explicit `ExposureInterval`s and `IntervalCensoredEvent`s.
7. **Report** -> synthetic JSON summary with provenance and `not_empirical_ecosentinel_finding=true`.

## 4. Alert accounting rules (configurable)

- **Alert active:** raw indicator true after persistence rule (no activation backdating).
- **Episode envelope:** `start` = first active valid observation in episode, `end` = last active valid observation in episode.
- **Active observations:** exact active observation indices stored in `active_observations`; inactive observations bridged by `merge_gap` are inside envelope but **not** active.
- **Merge gap:** inactive valid gap <= `merge_gap` can merge episodes.
- **Missing as break:** if `treat_missing_as_break=True`, missing/invalid observation breaks episode.
- **Min episode length:** episodes shorter than `min_episode_length` filtered.
- **Evaluation rule:** FA observation counts and event-boundary matching use actual active observations, not envelope membership.

Unresolved scientific decisions (human approval required): operational merge gap, minimum persistence, missing-break policy for real deployment, alert severity weighting.

## 5. Matched-FAR logic (synthetic prototype, provisional semantics)

The prototype computes (provisional software semantics only):
- `observation_level_false_alarm_fraction`: alert observations within verified non-event exposure / all valid verified non-event observations.
- `confirmed_false_alarm_episode_count`: episodes with verified non-event alert observations and no event/unknown overlap.
- `ambiguous_episode_count`: episodes crossing event/unknown boundaries or otherwise ambiguous.

**Option (a) unknown handling:** alert observations count only within verified non-event exposure; event/unknown observations excluded from denominator; valid non-event observations are not discarded because an episode overlaps unknown/event elsewhere. Episodes crossing boundaries are reported separately as ambiguous.

**Hard guards:** `compute_synthetic_evaluation` raises if exposure intervals are missing and `allow_unverified_exposure` is False (default). `max_warning_horizon` is required (no scientific default). No period is treated as non-bloom unless explicitly declared in synthetic fixtures or, in future, by human-approved biological evidence.

## 6. Interval-censored event handling and matching (provisional semantics)

`IntervalCensoredEvent` stores `onset_earliest/latest`, `termination_earliest/latest`. Provisional matching rules:
- Episode ends before `onset_earliest`: cannot count as successful warning.
- Warning begins before `onset_earliest` and is genuinely active in the onset interval: `confirmed_early_warning_candidate` if within explicit `max_warning_horizon`.
- Episode begins inside uncertain onset interval: `onset_overlapping_ambiguous`.
- Episode begins after `onset_latest`: `post_onset_detection`.
- **Lead-time reporting (N4):** `signed_onset_minus_alert_start_min/max` reported for diagnostic timing. `lead_min_observations`/`lead_max_observations` are populated **only** for `confirmed_early_warning_candidate`; ambiguous/post-onset/nonqualifying detections have `null` warning-lead fields.
- **Event/episode matching policy (N3, provisional):** `provisional_many_to_many_reporting_no_silent_inflation`. An episode may be evaluated against multiple events and multiple episodes may be evaluated against one event; detections are reported per event without silent suppression. This is a minimum safe synthetic reporting policy, not scientific approval. Alternatives (one-episode-one-event, distinct warning episodes with overlap rules) are documented in the second-audit remediation report.

No scientifically justified default horizon is invented; scenarios must supply explicit `max_warning_horizon`. Final scientific rules require human approval.

## 7. Leakage safeguards

Implemented/tested:
- Backward-looking baseline windows in baselines/multivariate modules.
- Guard functions: `check_no_future_baseline`, `check_temporal_split`, `check_no_random_window_split`.
- Evaluation refuses unverified exposure.
- Synthetic outputs labeled synthetic.

Not fully enforceable automatically (documented):
- Human could misconfigure thresholds using held-out outcomes.
- Human could label unknown periods as non-event.
- Real biological data provenance/licensing must be human-reviewed.
- Alert semantics for real operational deployment require domain approval.

## 8. Future integration points

When human-approved biological evidence arrives:
1. Ingest via Gate 2G intake templates/validator.
2. Map to approved biological observation schema (candidate vs approved, with provenance).
3. Convert only approved records into event/exposure intervals after Gate 2/3 decisions.
4. Reuse alert accounting and evaluation modules unchanged where possible.
5. Run pre-registered baselines/multivariate methods under approved splits and matched-FAR rules.