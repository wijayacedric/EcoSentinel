from __future__ import annotations
from dataclasses import dataclass
from typing import List, Sequence, Dict, Any, Optional
from .config import EvaluationConfig
from .events import IntervalCensoredEvent, ExposureInterval
from .alerts import AlertEpisode

@dataclass
class MethodResult:
    method: str
    config: Dict[str, Any]
    episodes: List[AlertEpisode]
    valid_observation_count: int
    verified_non_event_observation_count: int
    alert_observations_in_verified_non_event: int
    observation_level_false_alarm_fraction: Optional[float]
    confirmed_false_alarm_episode_count: int
    ambiguous_episode_count: int
    missed_synthetic_events: int
    total_synthetic_events: int
    event_detections: List[Dict[str, Any]]
    episode_classifications: List[Dict[str, Any]]
    synthetic_only: bool = True

def _is_int(v: Any) -> bool:
    return isinstance(v, int) and not isinstance(v, bool)

def _overlaps(a_start: int, a_end: int, b_start: int, b_end: int) -> bool:
    return a_start <= b_end and b_start <= a_end

def _validate_inputs(times: Sequence[int], valid: Sequence[bool], episodes: Sequence[AlertEpisode], events: Sequence[IntervalCensoredEvent], exposure_intervals: Sequence[ExposureInterval]) -> None:
    if len(times) != len(valid):
        raise ValueError("times and valid must have same length")
    if len(times) == 0:
        pass
    for i, t in enumerate(times):
        if not _is_int(t):
            raise ValueError("times must be integer indices in synthetic prototype")
        if i > 0 and times[i] <= times[i-1]:
            raise ValueError("times must be strictly increasing")
    for i, v in enumerate(valid):
        if not isinstance(v, bool):
            raise ValueError("valid flags must be booleans")
    time_set = set(times)

    seen_ids = set()
    for e in events:
        e.validate()
        if not isinstance(e.event_id, str) or not e.event_id:
            raise ValueError("event_id must be a non-empty string")
        if e.event_id in seen_ids:
            raise ValueError(f"duplicate event_id: {e.event_id}")
        seen_ids.add(e.event_id)
        for name, val in [('onset_earliest',e.onset_earliest),('onset_latest',e.onset_latest),('termination_earliest',e.termination_earliest),('termination_latest',e.termination_latest)]:
            if not _is_int(val):
                raise ValueError(f"{name} must be integer")
            if val not in time_set:
                raise ValueError(f"event {e.event_id} {name} outside observation domain")

    allowed_kinds = {"synthetic_non_event", "unknown", "synthetic_event"}
    for x in exposure_intervals:
        x.validate()
        if x.start not in time_set or x.end not in time_set:
            raise ValueError("exposure interval bounds outside observation domain")

    for ep in episodes:
        if not _is_int(ep.start) or not _is_int(ep.end) or not _is_int(ep.length) or not _is_int(ep.trigger_count):
            raise ValueError("episode numeric fields must be integers")
        if ep.start > ep.end:
            raise ValueError("episode start must be <= end")
        if ep.start not in time_set or ep.end not in time_set:
            raise ValueError("episode bounds must correspond to observation times")
        if ep.length < 1:
            raise ValueError("episode length must be >=1")
        if ep.trigger_count < 1:
            raise ValueError("episode trigger_count must be >=1")
        if ep.active_observations is None:
            raise ValueError("episode.active_observations is required for evaluation (exact active observation indices)")
        if len(ep.active_observations) != ep.length:
            raise ValueError("episode active_observations length must equal length")
        if any(not _is_int(t) for t in ep.active_observations):
            raise ValueError("episode active_observations must be integers")
        if any(ep.active_observations[i] >= ep.active_observations[i+1] for i in range(len(ep.active_observations)-1)):
            raise ValueError("episode active_observations must be strictly increasing")
        if ep.active_observations[0] != ep.start or ep.active_observations[-1] != ep.end:
            raise ValueError("episode active_observations must match envelope start/end")
        if any(t not in time_set for t in ep.active_observations):
            raise ValueError("episode active_observations must be within observation domain")

def compute_synthetic_evaluation(
    method: str,
    times: Sequence[int],
    valid: Sequence[bool],
    episodes: Sequence[AlertEpisode],
    events: Sequence[IntervalCensoredEvent],
    exposure_intervals: Sequence[ExposureInterval],
    cfg: EvaluationConfig,
) -> MethodResult:
    cfg.validate(require_horizon=True)
    _validate_inputs(times, valid, episodes, events, exposure_intervals)

    if not exposure_intervals and not cfg.allow_unverified_exposure:
        raise ValueError("No exposure intervals provided; cannot compute FAR without explicit synthetic exposure")

    max_h = cfg.max_warning_horizon
    assert max_h is not None

    valid_count = sum(1 for v in valid if v)
    verified_non_event = set()
    unknown_obs = set()
    event_obs = set()
    for t, v in zip(times, valid):
        if not v:
            continue
        is_non = any(x.kind == 'synthetic_non_event' and x.start <= t <= x.end for x in exposure_intervals)
        is_unk = any(x.kind == 'unknown' and x.start <= t <= x.end for x in exposure_intervals)
        is_evt = any(x.kind == 'synthetic_event' and x.start <= t <= x.end for x in exposure_intervals)
        if is_non and not is_unk and not is_evt:
            verified_non_event.add(t)
        if is_unk:
            unknown_obs.add(t)
        if is_evt:
            event_obs.add(t)

    alert_obs_verified_non_event = set()
    episode_classes = []
    confirmed_fa_eps = 0
    ambiguous_eps = 0

    for ep in episodes:
        ep_active = list(ep.active_observations or [])
        ep_verified_non_event_obs = [t for t in ep_active if t in verified_non_event]
        ep_unknown_obs = [t for t in ep_active if t in unknown_obs]
        ep_event_obs = [t for t in ep_active if t in event_obs]
        ep_overlaps_event_window = any(_overlaps(ep.start, ep.end, ev.onset_earliest, ev.termination_latest) for ev in events)
        ep_overlaps_event_exposure = len(ep_event_obs) > 0
        ep_overlaps_event = ep_overlaps_event_window or ep_overlaps_event_exposure
        ep_overlaps_unknown = len(ep_unknown_obs) > 0
        ep_has_verified_non_event = len(ep_verified_non_event_obs) > 0

        for t in ep_verified_non_event_obs:
            alert_obs_verified_non_event.add(t)

        if ep_has_verified_non_event and not ep_overlaps_event and not ep_overlaps_unknown:
            cls = 'confirmed_false_alarm_episode'
            confirmed_fa_eps += 1
        elif ep_has_verified_non_event and (ep_overlaps_event or ep_overlaps_unknown):
            cls = 'ambiguous_episode'
            ambiguous_eps += 1
        elif ep_overlaps_event or ep_overlaps_unknown:
            cls = 'ambiguous_episode'
            ambiguous_eps += 1
        else:
            cls = 'no_verified_non_event_exposure'
        episode_classes.append({
            'episode_start': ep.start,
            'episode_end': ep.end,
            'active_observation_count': len(ep_active),
            'classification': cls,
            'verified_non_event_observation_count': len(ep_verified_non_event_obs),
            'unknown_observation_count': len(ep_unknown_obs),
            'event_observation_count': len(ep_event_obs),
            'overlaps_event_window': ep_overlaps_event_window,
            'overlaps_event_exposure': ep_overlaps_event_exposure,
            'overlaps_unknown_exposure': ep_overlaps_unknown,
            'synthetic_only': True,
        })

    obs_far = (len(alert_obs_verified_non_event) / len(verified_non_event)) if verified_non_event else None

    detections = []
    missed = 0
    for ev in events:
        ev_dets = []
        for ep in episodes:
            ep_active = list(ep.active_observations or [])
            if not ep_active:
                continue
            if ep.end < ev.onset_earliest:
                continue
            active_at_or_after_onset_earliest = any(t >= ev.onset_earliest for t in ep_active)
            active_in_onset_interval = any(ev.onset_earliest <= t <= ev.onset_latest for t in ep_active)
            if ep.start > ev.onset_latest:
                det_type = 'post_onset_detection'
            elif ev.onset_earliest <= ep.start <= ev.onset_latest:
                det_type = 'onset_overlapping_ambiguous'
            elif ep.start < ev.onset_earliest:
                within_horizon = (ev.onset_earliest - ep.start) <= max_h
                # Must be genuinely active in the onset interval (relevant boundary) to qualify
                if active_in_onset_interval and within_horizon:
                    det_type = 'confirmed_early_warning_candidate'
                else:
                    det_type = 'pre_onset_nonqualifying'
            else:
                det_type = 'unclassified'
            lead_min = ev.onset_earliest - ep.start
            lead_max = ev.onset_latest - ep.start
            ev_dets.append({
                'event_id': ev.event_id,
                'episode_start': ep.start,
                'episode_end': ep.end,
                'episode_active_observation_count': len(ep_active),
                'detection_type': det_type,
                'onset_earliest': ev.onset_earliest,
                'onset_latest': ev.onset_latest,
                'signed_onset_minus_alert_start_min': lead_min,
                'signed_onset_minus_alert_start_max': lead_max,
                'lead_min_observations': lead_min if det_type == 'confirmed_early_warning_candidate' else None,
                'lead_max_observations': lead_max if det_type == 'confirmed_early_warning_candidate' else None,
                'active_at_or_after_onset_earliest': active_at_or_after_onset_earliest,
                'active_in_onset_interval': active_in_onset_interval,
                'within_max_warning_horizon': (ev.onset_earliest - ep.start) <= max_h,
                'max_warning_horizon_observations': max_h,
                'synthetic_only': True,
            })
        has_success = any(d['detection_type'] == 'confirmed_early_warning_candidate' for d in ev_dets)
        has_ambiguous = any(d['detection_type'] == 'onset_overlapping_ambiguous' for d in ev_dets)
        has_post = any(d['detection_type'] == 'post_onset_detection' for d in ev_dets)
        if not has_success:
            missed += 1
        detections.append({
            'event_id': ev.event_id,
            'missed_as_confirmed_early_warning': not has_success,
            'has_confirmed_early_warning_candidate': has_success,
            'has_onset_overlapping_ambiguous': has_ambiguous,
            'has_post_onset_detection': has_post,
            'detections': ev_dets,
            'synthetic_only': True,
        })

    return MethodResult(
        method=method,
        config={
            'max_warning_horizon_observations': max_h,
            'merge_gap': cfg.alert_config.merge_gap,
            'min_episode_length': cfg.alert_config.min_episode_length,
            'treat_missing_as_break': cfg.alert_config.treat_missing_as_break,
            'synthetic_only': True,
            'provisional_software_semantics': True,
            'event_episode_matching_policy': 'provisional_many_to_many_reporting_no_silent_inflation',
        },
        episodes=list(episodes),
        valid_observation_count=valid_count,
        verified_non_event_observation_count=len(verified_non_event),
        alert_observations_in_verified_non_event=len(alert_obs_verified_non_event),
        observation_level_false_alarm_fraction=obs_far,
        confirmed_false_alarm_episode_count=confirmed_fa_eps,
        ambiguous_episode_count=ambiguous_eps,
        missed_synthetic_events=missed,
        total_synthetic_events=len(events),
        event_detections=detections,
        episode_classifications=episode_classes,
    )
