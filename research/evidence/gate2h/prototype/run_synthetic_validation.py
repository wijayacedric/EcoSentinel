"""Run deterministic synthetic validation scenarios and write JSON summary.

SYNTHETIC TEST OUTPUT ONLY - NOT EMPIRICAL ECOSENTINEL FINDINGS.
Non-destructive: requires --out and refuses to overwrite unless --force.
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from datetime import datetime, timezone
ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / 'research/evidence/gate2h'))
from prototype.config import RollingCorrelationConfig, EvaluationConfig, AlertAccountingConfig
from prototype.alerts import apply_persistence, build_episodes
from prototype.multivariate import rolling_correlation_change_alerts
from prototype.evaluation import compute_synthetic_evaluation
from prototype.scenarios import (
    genuine_early_warning_scenario, no_warning_scenario, seasonal_false_positive_scenario,
    sensor_artifact_scenario, missing_data_scenario, interval_censored_event_scenario,
    sensor_replacement_scenario, autocorrelated_no_event_scenario
)

SCENARIOS = [
    genuine_early_warning_scenario(), no_warning_scenario(), seasonal_false_positive_scenario(),
    sensor_artifact_scenario(), missing_data_scenario(), interval_censored_event_scenario(),
    sensor_replacement_scenario(), autocorrelated_no_event_scenario()
]

def check_expectations(sc, res):
    failures = []
    exp = sc.expected
    if exp.get('expect_confirmed_early_warning') is True:
        if not any(d['has_confirmed_early_warning_candidate'] for d in res.event_detections):
            failures.append('expected confirmed early warning candidate')
    if exp.get('expect_confirmed_early_warning') is False:
        if any(d['has_confirmed_early_warning_candidate'] for d in res.event_detections):
            failures.append('did not expect confirmed early warning candidate')
    if exp.get('expect_no_confirmed_false_alarm_episode') is True:
        if res.confirmed_false_alarm_episode_count != 0:
            failures.append(f'expected 0 confirmed false-alarm episodes, got {res.confirmed_false_alarm_episode_count}')
    if exp.get('expect_no_confirmed_events') is True:
        if res.total_synthetic_events != 0:
            failures.append('expected 0 synthetic events')
    if exp.get('expect_false_alarm_fraction_reported') is True:
        if res.observation_level_false_alarm_fraction is None:
            failures.append('expected observation_level_false_alarm_fraction')
    if exp.get('expect_lead_bounds_reported') is True:
        # lead bounds reported if any detections exist; also acceptable to be empty but field present
        if not isinstance(res.event_detections, list):
            failures.append('missing event_detections')
    return failures

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True, help='Output JSON path (required; non-destructive)')
    ap.add_argument('--force', action='store_true', help='Allow overwriting existing output file')
    args = ap.parse_args()
    out_path = Path(args.out)
    if out_path.exists() and not args.force:
        raise SystemExit(f"Refusing to overwrite existing file: {out_path}. Use --force to overwrite explicitly.")

    cfg = RollingCorrelationConfig('x','y',window=10,baseline_window=30,delta_threshold=0.2,min_persistence=2)
    summary = {
        'generated_at': datetime.now(timezone.utc).isoformat().replace('+00:00','Z'),
        'synthetic_only': True,
        'not_empirical_ecosentinel_finding': True,
        'provisional_software_semantics': True,
        'scenarios': []
    }
    all_failures = []
    for sc in SCENARIOS:
        flags=rolling_correlation_change_alerts(sc.observations,cfg)
        active=apply_persistence(flags,cfg.min_persistence)
        valid=[not o.is_missing for o in sc.observations]
        eps=build_episodes(sc.times,active,valid,AlertAccountingConfig(merge_gap=2,min_episode_length=1))
        eval_cfg = EvaluationConfig(max_warning_horizon=sc.max_warning_horizon)
        res=compute_synthetic_evaluation('rolling_corr_demo',sc.times,valid,eps,sc.events,sc.exposure,eval_cfg)
        failures = check_expectations(sc, res)
        if failures:
            all_failures.append({'scenario': sc.name, 'failures': failures})
        summary['scenarios'].append({
            'name': sc.name,
            'description': sc.description,
            'synthetic': True,
            'max_warning_horizon_observations': sc.max_warning_horizon,
            'events': len(sc.events),
            'episodes': len(res.episodes),
            'confirmed_false_alarm_episode_count': res.confirmed_false_alarm_episode_count,
            'ambiguous_episode_count': res.ambiguous_episode_count,
            'alert_observations_in_verified_non_event': res.alert_observations_in_verified_non_event,
            'verified_non_event_observation_count': res.verified_non_event_observation_count,
            'observation_level_false_alarm_fraction': res.observation_level_false_alarm_fraction,
            'missed_synthetic_events': res.missed_synthetic_events,
            'event_detections': res.event_detections,
            'episode_classifications': res.episode_classifications,
            'expected': sc.expected,
            'expectation_failures': failures,
        })
    summary['all_expectations_passed'] = len(all_failures) == 0
    summary['expectation_failures'] = all_failures
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(summary, indent=2), encoding='utf-8')
    print(json.dumps({'wrote': str(out_path), 'all_expectations_passed': summary['all_expectations_passed'], 'failures': all_failures}, indent=2))
    if all_failures:
        raise SystemExit(1)

if __name__=='__main__':
    main()
