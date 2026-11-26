# Gate 2H — Synthetic Validation Report

**Project:** EcoSentinel  
**Date:** 2026-11-22  
**Status:** Synthetic/software validation only. **NOT empirical EcoSentinel findings. No biological labels. No confirmatory performance.**

## 1. Purpose

Validate that the Gate 2H prototype correctly handles alert accounting, interval-censored events, synthetic FAR logic, missingness, and confounding/negative-control scenarios. All scenarios are deterministic synthetic fixtures.

## 2. Reproducible commands

```bash
PYTHONPATH=research/evidence/gate2h python3 -m unittest discover -s research/evidence/gate2h/tests -p 'test_gate2h.py'
PYTHONPATH=research/evidence/gate2h python3 research/evidence/gate2h/prototype/run_synthetic_validation.py --out research/evidence/gate2h/derived/synthetic_validation_summary.json --force
```

## 3. Automated test results

- **Command:** `PYTHONPATH=research/evidence/gate2h python3 -m unittest discover -s research/evidence/gate2h/tests -p 'test_gate2h.py'`
- **Result:** **Ran 51 tests in ~0.081s — OK**
- **Date run:** 2026-11-22

## 4. Synthetic scenario summary

Source: `research/evidence/gate2h/derived/synthetic_validation_summary.json` (`synthetic_only=true`, `not_empirical_ecosentinel_finding=true`).

| Scenario | Events | Episodes | Confirmed FA episodes | Ambiguous episodes | Alert obs in verified non-event | Verified non-event obs | Obs-level FA fraction | Missed confirmed early warning |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| genuine_synthetic_early_warning | 1 | 2 | 1 | 1 | 1 | 74 | 0.0135 | 0 |
| no_warning | 1 | 0 | 0 | 0 | 0 | 82 | 0.0000 | 1 |
| seasonal_false_positive | 0 | 2 | 2 | 0 | 2 | 240 | 0.0083 | 0 |
| sensor_artifact | 0 | 2 | 0 | 2 | 21 | 129 | 0.1628 | 0 |
| missing_data | 1 | 0 | 0 | 0 | 0 | 90 | 0.0000 | 1 |
| interval_censored | 1 | 2 | 1 | 1 | 20 | 79 | 0.2532 | 1 |
| sensor_replacement | 0 | 0 | 0 | 0 | 0 | 139 | 0.0000 | 0 |
| autocorrelated_no_event | 0 | 11 | 11 | 0 | 131 | 200 | 0.6550 | 0 |

## 5.

## 5. Key validations demonstrated

| Requirement | Evidence |
|---|---|
| Genuine synthetic early-warning scenario | `genuine_synthetic_early_warning` detected with lead bounds |
| No-warning scenario | `no_warning` produced 0 false-alarm episodes |
| Seasonal false-positive/confounding control | `seasonal_false_positive` and `autocorrelated_no_event` included; AR(1) control exposes false alarms |
| Sensor artefact scenario | `sensor_artifact` unknown recovery window prevents miscounting ambiguous period as confirmed non-event false alarm |
| Missing-data scenario | `missing_data` missing block handled; missing-as-break tested |
| Interval-censored event scenario | `interval_censored_event_scenario` and lead-bound test verify min/max lead bounds |
| Unequal FAR comparison | `test_unequal_false_alarm_rates` passes |
| Comparable FAR comparison | `test_comparable_false_alarm_rates` passes |
| Repeated alerts one episode | `test_repeated_alerts_one_episode` passes |
| Missed synthetic event | `test_missed_synthetic_event` and `no_warning`/`missing_data` cases |
| Leakage guards | future-baseline, temporal split, random-split guard tests pass |
| Unverified exposure refusal | `test_refuses_unverified_exposure` passes |

## 6. Interpretation limits

- These results validate **software logic on synthetic fixtures only**. They do not indicate EcoSentinel early-warning performance.
- The AR(1) control producing false alarms is an expected warning signal about confounding, not a real-world performance estimate.
- Real biological evaluation remains blocked by Gate 2 evidence/approval constraints.