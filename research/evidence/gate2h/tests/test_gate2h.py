import sys, unittest, json, subprocess, tempfile, os
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / 'research/evidence/gate2h'))

from prototype.config import AlertAccountingConfig, EvaluationConfig, RollingCorrelationConfig, RollingZScoreConfig, BaselineThresholdConfig
from prototype.alerts import apply_persistence, build_episodes, AlertEpisode
from prototype.baselines import threshold_alerts, rolling_zscore_alerts
from prototype.multivariate import rolling_correlation_change_alerts
from prototype.evaluation import compute_synthetic_evaluation
from prototype.events import IntervalCensoredEvent, ExposureInterval
from prototype.guards import check_no_future_baseline, check_temporal_split, check_no_random_window_split
from prototype.quality import parse_float, Observation, valid_observation
from prototype.scenarios import (
    genuine_early_warning_scenario, no_warning_scenario, seasonal_false_positive_scenario,
    sensor_artifact_scenario, missing_data_scenario, interval_censored_event_scenario,
    sensor_replacement_scenario, autocorrelated_no_event_scenario
)

def eval_cfg(h=30):
    return EvaluationConfig(max_warning_horizon=h)

class TestAlertAccounting(unittest.TestCase):
    def test_repeated_alerts_one_episode(self):
        times=list(range(10))
        active=[False,True,True,True,False,False,True,True,False,False]
        valid=[True]*10
        eps=build_episodes(times,active,valid,AlertAccountingConfig(merge_gap=0,min_episode_length=1))
        self.assertEqual(len(eps),2)
        self.assertEqual((eps[0].start,eps[0].end),(1,3))
        self.assertEqual((eps[1].start,eps[1].end),(6,7))

    def test_merge_gap(self):
        times=list(range(10))
        active=[False,True,True,False,True,True,False,False,False,False]
        valid=[True]*10
        eps=build_episodes(times,active,valid,AlertAccountingConfig(merge_gap=1,min_episode_length=1))
        self.assertEqual(len(eps),1)
        self.assertEqual((eps[0].start,eps[0].end),(1,5))

    def test_missing_breaks_episode(self):
        times=list(range(6))
        active=[True,True,True,True,True,True]
        valid=[True,True,False,True,True,True]
        eps=build_episodes(times,active,valid,AlertAccountingConfig(merge_gap=5,min_episode_length=1,treat_missing_as_break=True))
        self.assertEqual(len(eps),2)

    def test_persistence_not_backdated(self):
        # M3: should not backdate to raw condition start
        flags=[False,True,True,False,True,True,True]
        out=apply_persistence(flags,3)
        self.assertEqual(out,[False,False,False,False,False,False,True])

class TestGuards(unittest.TestCase):
    def test_no_future_baseline(self):
        self.assertFalse(check_no_future_baseline(10,[8,9,10]).ok)
        self.assertTrue(check_no_future_baseline(10,[8,9]).ok)
    def test_temporal_split(self):
        self.assertFalse(check_temporal_split(10,10).ok)
        self.assertTrue(check_temporal_split(10,11).ok)
    def test_no_random_split(self):
        self.assertFalse(check_no_random_window_split(True).ok)

class TestInputValidation(unittest.TestCase):
    def test_refuses_unverified_exposure(self):
        with self.assertRaises(ValueError):
            compute_synthetic_evaluation('m',[0,1],[True,True],[],[],[],eval_cfg())
    def test_requires_horizon(self):
        with self.assertRaises(ValueError):
            compute_synthetic_evaluation('m',[0,1],[True,True],[],[],[ExposureInterval(0,1,'synthetic_non_event','SYNTHETIC_TEST')],EvaluationConfig())
    def test_mismatched_lengths_rejected(self):
        with self.assertRaises(ValueError):
            compute_synthetic_evaluation('m',[0,1,2],[True,True],[],[],[ExposureInterval(0,2,'synthetic_non_event','SYNTHETIC_TEST')],eval_cfg())
    def test_unsorted_times_rejected(self):
        with self.assertRaises(ValueError):
            compute_synthetic_evaluation('m',[0,2,1],[True,True,True],[],[],[ExposureInterval(0,2,'synthetic_non_event','SYNTHETIC_TEST')],eval_cfg())
    def test_invalid_exposure_kind_rejected(self):
        with self.assertRaises(ValueError):
            compute_synthetic_evaluation('m',[0,1],[True,True],[],[],[ExposureInterval(0,1,'non_event','SYNTHETIC_TEST')],eval_cfg())
    def test_non_finite_rejected(self):
        self.assertIsNone(parse_float('nan'))
        self.assertIsNone(parse_float('inf'))
        obs = Observation(0, {'x': float('inf')}, {'x':''})
        self.assertFalse(valid_observation(obs, ['x']))
    def test_bool_and_fractional_indices_rejected(self):
        with self.assertRaises(ValueError):
            compute_synthetic_evaluation('m',[0,True],[True,True],[],[],[ExposureInterval(0,1,'synthetic_non_event','SYNTHETIC_TEST')],eval_cfg())
        with self.assertRaises(ValueError):
            compute_synthetic_evaluation('m',[0.0,1.0],[True,True],[],[],[ExposureInterval(0,1,'synthetic_non_event','SYNTHETIC_TEST')],eval_cfg())
    def test_out_of_domain_event_bounds_rejected(self):
        with self.assertRaises(ValueError):
            ev=IntervalCensoredEvent('E1',5,6,7,8,'SYNTHETIC_TEST')
            compute_synthetic_evaluation('m',[0,1,2,3],[True]*4,[],[ev],[ExposureInterval(0,3,'synthetic_non_event','SYNTHETIC_TEST')],eval_cfg())

class TestEventMatchingSemantics(unittest.TestCase):
    def setUp(self):
        self.times=list(range(20))
        self.valid=[True]*20
        self.exposure=[ExposureInterval(0,9,'synthetic_non_event','SYNTHETIC_TEST'),ExposureInterval(10,15,'synthetic_event','SYNTHETIC_TEST'),ExposureInterval(16,19,'synthetic_non_event','SYNTHETIC_TEST')]
        self.event=IntervalCensoredEvent('E1',10,12,14,15,'SYNTHETIC_TEST')

    def test_h1_stale_alert_not_counted(self):
        res=compute_synthetic_evaluation('m',self.times,self.valid,[AlertEpisode(0,1,2,2,active_observations=list(range(0,1+1)))],[self.event],self.exposure,eval_cfg(30))
        det=res.event_detections[0]
        self.assertTrue(det['missed_as_confirmed_early_warning'])
        self.assertFalse(det['has_confirmed_early_warning_candidate'])

    def test_warning_must_begin_before_onset_earliest(self):
        res=compute_synthetic_evaluation('m',self.times,self.valid,[AlertEpisode(10,11,2,2,active_observations=list(range(10,11+1)))],[self.event],self.exposure,eval_cfg(30))
        det=res.event_detections[0]['detections'][0]
        self.assertEqual(det['detection_type'],'onset_overlapping_ambiguous')

    def test_post_onset_detection(self):
        res=compute_synthetic_evaluation('m',self.times,self.valid,[AlertEpisode(13,14,2,2,active_observations=list(range(13,14+1)))],[self.event],self.exposure,eval_cfg(30))
        det=res.event_detections[0]['detections'][0]
        self.assertEqual(det['detection_type'],'post_onset_detection')
        self.assertTrue(res.event_detections[0]['missed_as_confirmed_early_warning'])

    def test_confirmed_early_warning_with_horizon(self):
        res=compute_synthetic_evaluation('m',self.times,self.valid,[AlertEpisode(8,11,4,4,active_observations=list(range(8,11+1)))],[self.event],self.exposure,eval_cfg(30))
        det=res.event_detections[0]
        self.assertTrue(det['has_confirmed_early_warning_candidate'])
        self.assertFalse(det['missed_as_confirmed_early_warning'])

    def test_outside_max_horizon_not_confirmed(self):
        res=compute_synthetic_evaluation('m',self.times,self.valid,[AlertEpisode(2,11,10,10,active_observations=list(range(2,11+1)))],[self.event],self.exposure,eval_cfg(5))
        det=res.event_detections[0]['detections'][0]
        self.assertEqual(det['detection_type'],'pre_onset_nonqualifying')
        self.assertTrue(res.event_detections[0]['missed_as_confirmed_early_warning'])

    def test_interval_censored_lead_bounds(self):
        res=compute_synthetic_evaluation('m',self.times,self.valid,[AlertEpisode(8,11,4,4,active_observations=list(range(8,11+1)))],[self.event],self.exposure,eval_cfg(30))
        det=res.event_detections[0]['detections'][0]
        self.assertEqual(det['lead_min_observations'],2)
        self.assertEqual(det['lead_max_observations'],4)

class TestFalseAlarmAccounting(unittest.TestCase):
    def test_h2_unknown_overlap_does_not_erase_verified_non_event_obs(self):
        times=list(range(10)); valid=[True]*10
        exposure=[ExposureInterval(0,3,'synthetic_non_event','SYNTHETIC_TEST'),ExposureInterval(4,5,'unknown','SYNTHETIC_TEST'),ExposureInterval(6,9,'synthetic_non_event','SYNTHETIC_TEST')]
        res=compute_synthetic_evaluation('m',times,valid,[AlertEpisode(0,7,8,8,active_observations=list(range(0,7+1)))],[],exposure,eval_cfg(30))
        # verified non-event obs are 0-3,6-9 = 8 obs; alert covers 0-3,6,7 in those sets = 6 obs
        self.assertEqual(res.verified_non_event_observation_count,8)
        self.assertEqual(res.alert_observations_in_verified_non_event,6)
        self.assertAlmostEqual(res.observation_level_false_alarm_fraction,6/8)
        self.assertEqual(res.confirmed_false_alarm_episode_count,0)
        self.assertEqual(res.ambiguous_episode_count,1)

    def test_h3_no_misleading_episode_rate_field(self):
        times=list(range(10)); valid=[True]*10
        exposure=[ExposureInterval(0,9,'synthetic_non_event','SYNTHETIC_TEST')]
        res=compute_synthetic_evaluation('m',times,valid,[AlertEpisode(0,1,2,2,active_observations=list(range(0,1+1)))],[],exposure,eval_cfg(30))
        self.assertFalse(hasattr(res,'far_per_episode'))
        self.assertTrue(hasattr(res,'confirmed_false_alarm_episode_count'))
        self.assertTrue(hasattr(res,'observation_level_false_alarm_fraction'))

    def test_confirmed_false_alarm_episode(self):
        times=list(range(10)); valid=[True]*10
        exposure=[ExposureInterval(0,9,'synthetic_non_event','SYNTHETIC_TEST')]
        res=compute_synthetic_evaluation('m',times,valid,[AlertEpisode(2,3,2,2,active_observations=list(range(2,3+1)))],[],exposure,eval_cfg(30))
        self.assertEqual(res.confirmed_false_alarm_episode_count,1)
        self.assertEqual(res.ambiguous_episode_count,0)

    def test_ambiguous_episode_crossing_event_boundary(self):
        times=list(range(20)); valid=[True]*20
        exposure=[ExposureInterval(0,9,'synthetic_non_event','SYNTHETIC_TEST'),ExposureInterval(10,15,'synthetic_event','SYNTHETIC_TEST'),ExposureInterval(16,19,'synthetic_non_event','SYNTHETIC_TEST')]
        res=compute_synthetic_evaluation('m',times,valid,[AlertEpisode(8,12,5,5,active_observations=list(range(8,12+1)))],[],exposure,eval_cfg(30))
        # has verified non-event obs (8,9, part? 10-12 are event obs) and overlaps event window
        self.assertEqual(res.confirmed_false_alarm_episode_count,0)
        self.assertEqual(res.ambiguous_episode_count,1)
        self.assertEqual(res.alert_observations_in_verified_non_event,2) # t=8,9

class TestScenarios(unittest.TestCase):
    def _run(self, sc, cfg=None):
        cfg = cfg or RollingCorrelationConfig('x','y',window=10,baseline_window=30,delta_threshold=0.2,min_persistence=2)
        flags=rolling_correlation_change_alerts(sc.observations,cfg)
        active=apply_persistence(flags,cfg.min_persistence)
        valid=[not o.is_missing for o in sc.observations]
        eps=build_episodes(sc.times,active,valid,AlertAccountingConfig(merge_gap=2,min_episode_length=1))
        return compute_synthetic_evaluation('rolling_corr_demo',sc.times,valid,eps,sc.events,sc.exposure,eval_cfg(sc.max_warning_horizon))

    def test_genuine_early_warning(self):
        res=self._run(genuine_early_warning_scenario())
        self.assertTrue(any(d['has_confirmed_early_warning_candidate'] for d in res.event_detections))
        # demo indicator may produce some post-event false alarms; key property is early warning exists
        self.assertLessEqual(res.confirmed_false_alarm_episode_count,1)

    def test_no_warning(self):
        res=self._run(no_warning_scenario())
        self.assertFalse(any(d['has_confirmed_early_warning_candidate'] for d in res.event_detections))
        self.assertEqual(res.confirmed_false_alarm_episode_count,0)

    def test_seasonal_control(self):
        res=self._run(seasonal_false_positive_scenario())
        # simple demo indicator can emit occasional false alarms; accounting must report them explicitly
        self.assertLessEqual(res.confirmed_false_alarm_episode_count,2)

    def test_sensor_artifact(self):
        res=self._run(sensor_artifact_scenario())
        self.assertEqual(res.confirmed_false_alarm_episode_count,0)

    def test_missing_data(self):
        res=self._run(missing_data_scenario())
        self.assertEqual(res.confirmed_false_alarm_episode_count,0)

    def test_interval_censored(self):
        res=self._run(interval_censored_event_scenario())
        self.assertIsInstance(res.event_detections, list)

    def test_sensor_replacement(self):
        res=self._run(sensor_replacement_scenario())
        self.assertLessEqual(res.confirmed_false_alarm_episode_count,1)

    def test_autocorrelated_control_reports_far(self):
        res=self._run(autocorrelated_no_event_scenario(), RollingCorrelationConfig('x','y',window=12,baseline_window=40,delta_threshold=0.4,min_persistence=3))
        self.assertEqual(res.total_synthetic_events,0)
        self.assertIsNotNone(res.observation_level_false_alarm_fraction)

    def test_synthetic_labels_present(self):
        sc=interval_censored_event_scenario()
        self.assertTrue(all(e.source.startswith('SYNTHETIC') for e in sc.events))
        self.assertTrue(all(x.source.startswith('SYNTHETIC') for x in sc.exposure))

class TestRunnerNonDestructive(unittest.TestCase):
    def test_runner_refuses_overwrite_without_force(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td)/'out.json'
            out.write_text('{}')
            cmd=[sys.executable,'research/evidence/gate2h/prototype/run_synthetic_validation.py','--out',str(out)]
            r=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True)
            self.assertNotEqual(r.returncode,0)
            self.assertIn('Refusing to overwrite', r.stdout + r.stderr)

    def test_runner_writes_new_file_and_checks_expectations(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td)/'summary.json'
            cmd=[sys.executable,'research/evidence/gate2h/prototype/run_synthetic_validation.py','--out',str(out)]
            r=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True)
            self.assertEqual(r.returncode,0, msg=r.stdout+r.stderr)
            data=json.loads(out.read_text())
            self.assertTrue(data['synthetic_only'])
            self.assertTrue(data['provisional_software_semantics'])
            self.assertIn('all_expectations_passed', data)


class TestN1ActiveObservations(unittest.TestCase):
    def test_merge_gap_inactive_obs_not_counted_in_verified_non_event(self):
        # active at 0,1,3,4 with merge_gap=1; index 2 inactive inside verified non-event exposure
        times=list(range(6)); valid=[True]*6
        exposure=[ExposureInterval(0,5,'synthetic_non_event','SYNTHETIC_TEST')]
        ep=AlertEpisode(0,4,4,4,active_observations=[0,1,3,4])
        res=compute_synthetic_evaluation('m',times,valid,[ep],[],exposure,eval_cfg(10))
        self.assertEqual(res.alert_observations_in_verified_non_event,4)
        self.assertAlmostEqual(res.observation_level_false_alarm_fraction,4/6)

    def test_max_merge_gap_boundary(self):
        times=list(range(8)); valid=[True]*8
        active=[True,False,False,True,False,False,False,False]
        # merge_gap=2 should bridge gap of 2 inactive valid obs between 0 and 3? gap = t-last_active_valid_t-1 = 3-0-1=2
        eps=build_episodes(times,active,valid,AlertAccountingConfig(merge_gap=2))
        self.assertEqual(len(eps),1)
        self.assertEqual(eps[0].active_observations,[0,3])

    def test_inactive_merge_gap_at_onset_earliest_not_active(self):
        times=list(range(10)); valid=[True]*10
        exposure=[ExposureInterval(0,4,'synthetic_non_event','SYNTHETIC_TEST'),ExposureInterval(5,9,'synthetic_event','SYNTHETIC_TEST')]
        event=IntervalCensoredEvent('E1',5,6,8,9,'SYNTHETIC_TEST')
        # inactive at onset_earliest=5 but active at 6 (inside onset interval) - merged episode
        ep=AlertEpisode(4,6,2,2,active_observations=[4,6])
        res=compute_synthetic_evaluation('m',times,valid,[ep],[event],exposure,eval_cfg(10))
        det=res.event_detections[0]['detections'][0]
        self.assertTrue(det['active_in_onset_interval'])  # active at 6
        self.assertEqual(det['detection_type'],'confirmed_early_warning_candidate')

    def test_envelope_extends_across_onset_but_not_active(self):
        times=list(range(10)); valid=[True]*10
        exposure=[ExposureInterval(0,4,'synthetic_non_event','SYNTHETIC_TEST'),ExposureInterval(5,9,'synthetic_event','SYNTHETIC_TEST')]
        event=IntervalCensoredEvent('E1',5,6,8,9,'SYNTHETIC_TEST')
        ep=AlertEpisode(3,7,2,2,active_observations=[3,7]) # envelope spans onset, but no active in onset interval [5,6]
        res=compute_synthetic_evaluation('m',times,valid,[ep],[event],exposure,eval_cfg(10))
        det=res.event_detections[0]['detections'][0]
        self.assertEqual(det['detection_type'],'pre_onset_nonqualifying')
        self.assertTrue(det['active_at_or_after_onset_earliest'])
        self.assertFalse(det['active_in_onset_interval'])

    def test_genuinely_active_at_onset(self):
        times=list(range(10)); valid=[True]*10
        exposure=[ExposureInterval(0,4,'synthetic_non_event','SYNTHETIC_TEST'),ExposureInterval(5,9,'synthetic_event','SYNTHETIC_TEST')]
        event=IntervalCensoredEvent('E1',5,6,8,9,'SYNTHETIC_TEST')
        ep=AlertEpisode(3,6,3,3,active_observations=[3,4,6]) # active at 6 (inside onset interval)
        res=compute_synthetic_evaluation('m',times,valid,[ep],[event],exposure,eval_cfg(10))
        det=res.event_detections[0]['detections'][0]
        self.assertEqual(det['detection_type'],'confirmed_early_warning_candidate')
        self.assertTrue(det['active_at_or_after_onset_earliest'])

    def test_false_alarm_fraction_ignores_merged_gap_obs(self):
        times=list(range(6)); valid=[True]*6
        exposure=[ExposureInterval(0,5,'synthetic_non_event','SYNTHETIC_TEST')]
        ep=AlertEpisode(0,5,4,4,active_observations=[0,1,4,5]) # gaps at 2,3
        res=compute_synthetic_evaluation('m',times,valid,[ep],[],exposure,eval_cfg(10))
        self.assertEqual(res.alert_observations_in_verified_non_event,4)
        self.assertAlmostEqual(res.observation_level_false_alarm_fraction,4/6)

    def test_merged_episode_crossing_event_unknown_non_event(self):
        times=list(range(12)); valid=[True]*12
        exposure=[ExposureInterval(0,3,'synthetic_non_event','SYNTHETIC_TEST'),ExposureInterval(4,5,'unknown','SYNTHETIC_TEST'),ExposureInterval(6,8,'synthetic_event','SYNTHETIC_TEST'),ExposureInterval(9,11,'synthetic_non_event','SYNTHETIC_TEST')]
        event=IntervalCensoredEvent('E1',6,7,8,8,'SYNTHETIC_TEST')
        ep=AlertEpisode(1,10,5,5,active_observations=[1,3,5,7,10]) # active in non-event, unknown, event, non-event
        res=compute_synthetic_evaluation('m',times,valid,[ep],[event],exposure,eval_cfg(10))
        self.assertEqual(res.alert_observations_in_verified_non_event,3) # 1,3,10
        self.assertEqual(res.ambiguous_episode_count,1)

class TestN3EventEpisodeMatching(unittest.TestCase):
    def test_two_events_separate_warning_episodes(self):
        times=list(range(20)); valid=[True]*20
        exposure=[ExposureInterval(0,19,'synthetic_non_event','SYNTHETIC_TEST')]
        # events with synthetic_event exposure? keep simple
        exposure=[ExposureInterval(0,4,'synthetic_non_event','SYNTHETIC_TEST'),ExposureInterval(5,7,'synthetic_event','SYNTHETIC_TEST'),ExposureInterval(8,11,'synthetic_non_event','SYNTHETIC_TEST'),ExposureInterval(12,14,'synthetic_event','SYNTHETIC_TEST'),ExposureInterval(15,19,'synthetic_non_event','SYNTHETIC_TEST')]
        e1=IntervalCensoredEvent('E1',5,6,7,7,'SYNTHETIC_TEST')
        e2=IntervalCensoredEvent('E2',12,13,14,14,'SYNTHETIC_TEST')
        eps=[AlertEpisode(3,5,2,2,active_observations=[3,5]), AlertEpisode(10,12,2,2,active_observations=[10,12])]
        res=compute_synthetic_evaluation('m',times,valid,eps,[e1,e2],exposure,eval_cfg(10))
        self.assertTrue(res.event_detections[0]['has_confirmed_early_warning_candidate'])
        self.assertTrue(res.event_detections[1]['has_confirmed_early_warning_candidate'])

    def test_two_events_one_continuous_warning_episode(self):
        times=list(range(20)); valid=[True]*20
        exposure=[ExposureInterval(0,4,'synthetic_non_event','SYNTHETIC_TEST'),ExposureInterval(5,7,'synthetic_event','SYNTHETIC_TEST'),ExposureInterval(8,11,'synthetic_non_event','SYNTHETIC_TEST'),ExposureInterval(12,14,'synthetic_event','SYNTHETIC_TEST'),ExposureInterval(15,19,'synthetic_non_event','SYNTHETIC_TEST')]
        e1=IntervalCensoredEvent('E1',5,6,7,7,'SYNTHETIC_TEST')
        e2=IntervalCensoredEvent('E2',12,13,14,14,'SYNTHETIC_TEST')
        ep=AlertEpisode(3,13,9,9,active_observations=[3,4,5,6,7,8,10,11,13])
        res=compute_synthetic_evaluation('m',times,valid,[ep],[e1,e2],exposure,eval_cfg(20))
        # provisional policy: many-to-many reporting, no silent inflation; both events see the episode
        self.assertTrue(res.event_detections[0]['has_confirmed_early_warning_candidate'])
        self.assertTrue(res.event_detections[1]['has_confirmed_early_warning_candidate'])
        self.assertIn('provisional_many_to_many_reporting_no_silent_inflation', res.config['event_episode_matching_policy'])

    def test_one_episode_eligible_multiple_events_flagged(self):
        times=list(range(15)); valid=[True]*15
        exposure=[ExposureInterval(0,4,'synthetic_non_event','SYNTHETIC_TEST'),ExposureInterval(5,6,'synthetic_event','SYNTHETIC_TEST'),ExposureInterval(7,8,'synthetic_event','SYNTHETIC_TEST'),ExposureInterval(9,14,'synthetic_non_event','SYNTHETIC_TEST')]
        e1=IntervalCensoredEvent('E1',5,5,6,6,'SYNTHETIC_TEST')
        e2=IntervalCensoredEvent('E2',7,7,8,8,'SYNTHETIC_TEST')
        ep=AlertEpisode(3,7,4,4,active_observations=[3,4,5,7])
        res=compute_synthetic_evaluation('m',times,valid,[ep],[e1,e2],exposure,eval_cfg(10))
        self.assertEqual(len(res.event_detections),2)
        self.assertTrue(res.event_detections[0]['has_confirmed_early_warning_candidate'])
        self.assertTrue(res.event_detections[1]['has_confirmed_early_warning_candidate'])

    def test_overlapping_event_onset_intervals(self):
        times=list(range(12)); valid=[True]*12
        exposure=[ExposureInterval(0,3,'synthetic_non_event','SYNTHETIC_TEST'),ExposureInterval(4,8,'synthetic_event','SYNTHETIC_TEST'),ExposureInterval(9,11,'synthetic_non_event','SYNTHETIC_TEST')]
        e1=IntervalCensoredEvent('E1',4,6,7,8,'SYNTHETIC_TEST')
        e2=IntervalCensoredEvent('E2',5,7,7,8,'SYNTHETIC_TEST')
        ep=AlertEpisode(2,5,3,3,active_observations=[2,3,5])
        res=compute_synthetic_evaluation('m',times,valid,[ep],[e1,e2],exposure,eval_cfg(10))
        self.assertEqual(len(res.event_detections),2)
        # Both events should be evaluated; no silent suppression
        self.assertTrue(all('missed_as_confirmed_early_warning' in d for d in res.event_detections))

    def test_multiple_episodes_eligible_for_one_event(self):
        times=list(range(15)); valid=[True]*15
        exposure=[ExposureInterval(0,9,'synthetic_non_event','SYNTHETIC_TEST'),ExposureInterval(10,12,'synthetic_event','SYNTHETIC_TEST'),ExposureInterval(13,14,'synthetic_non_event','SYNTHETIC_TEST')]
        e1=IntervalCensoredEvent('E1',10,11,12,12,'SYNTHETIC_TEST')
        eps=[AlertEpisode(6,10,2,2,active_observations=[6,10]), AlertEpisode(7,11,2,2,active_observations=[7,11])]
        res=compute_synthetic_evaluation('m',times,valid,eps,[e1],exposure,eval_cfg(10))
        det=res.event_detections[0]
        self.assertTrue(det['has_confirmed_early_warning_candidate'])
        self.assertEqual(len(det['detections']),2)

class TestN4LeadTimeReporting(unittest.TestCase):
    def test_confirmed_early_warning_has_lead_bounds(self):
        times=list(range(20)); valid=[True]*20
        exposure=[ExposureInterval(0,9,'synthetic_non_event','SYNTHETIC_TEST'),ExposureInterval(10,15,'synthetic_event','SYNTHETIC_TEST'),ExposureInterval(16,19,'synthetic_non_event','SYNTHETIC_TEST')]
        event=IntervalCensoredEvent('E1',10,12,14,15,'SYNTHETIC_TEST')
        res=compute_synthetic_evaluation('m',times,valid,[AlertEpisode(8,11,4,4,active_observations=[8,9,10,11])],[event],exposure,eval_cfg(30))
        det=res.event_detections[0]['detections'][0]
        self.assertEqual(det['detection_type'],'confirmed_early_warning_candidate')
        self.assertEqual(det['lead_min_observations'],2)
        self.assertEqual(det['lead_max_observations'],4)
        self.assertEqual(det['signed_onset_minus_alert_start_min'],2)

    def test_ambiguous_onset_no_warning_lead_label(self):
        times=list(range(20)); valid=[True]*20
        exposure=[ExposureInterval(0,9,'synthetic_non_event','SYNTHETIC_TEST'),ExposureInterval(10,15,'synthetic_event','SYNTHETIC_TEST'),ExposureInterval(16,19,'synthetic_non_event','SYNTHETIC_TEST')]
        event=IntervalCensoredEvent('E1',10,12,14,15,'SYNTHETIC_TEST')
        res=compute_synthetic_evaluation('m',times,valid,[AlertEpisode(11,13,3,3,active_observations=[11,12,13])],[event],exposure,eval_cfg(30))
        det=res.event_detections[0]['detections'][0]
        self.assertEqual(det['detection_type'],'onset_overlapping_ambiguous')
        self.assertIsNone(det['lead_min_observations'])
        self.assertIsNone(det['lead_max_observations'])
        self.assertEqual(det['signed_onset_minus_alert_start_min'],-1)

    def test_post_onset_no_warning_lead(self):
        times=list(range(20)); valid=[True]*20
        exposure=[ExposureInterval(0,9,'synthetic_non_event','SYNTHETIC_TEST'),ExposureInterval(10,15,'synthetic_event','SYNTHETIC_TEST'),ExposureInterval(16,19,'synthetic_non_event','SYNTHETIC_TEST')]
        event=IntervalCensoredEvent('E1',10,12,14,15,'SYNTHETIC_TEST')
        res=compute_synthetic_evaluation('m',times,valid,[AlertEpisode(13,14,2,2,active_observations=[13,14])],[event],exposure,eval_cfg(30))
        det=res.event_detections[0]['detections'][0]
        self.assertEqual(det['detection_type'],'post_onset_detection')
        self.assertIsNone(det['lead_min_observations'])

if __name__ == '__main__':
    unittest.main()
