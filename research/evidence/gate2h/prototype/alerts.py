from __future__ import annotations
from dataclasses import dataclass
from typing import List, Sequence, Optional
from .config import AlertAccountingConfig

@dataclass
class AlertEpisode:
    start: int  # episode envelope start (first active observation index)
    end: int    # episode envelope end (last active observation index)
    length: int # number of active valid observations in episode
    trigger_count: int
    active_observations: Optional[List[int]] = None  # exact active observation indices; required for evaluation
    raw_condition_start: Optional[int] = None  # first index where raw condition became true in this run

    def __post_init__(self) -> None:
        if self.start > self.end:
            raise ValueError("episode start must be <= end")
        if self.length < 1:
            raise ValueError("episode length must be >=1")
        if self.active_observations is not None:
            if not isinstance(self.active_observations, list):
                raise ValueError("active_observations must be a list of ints")
            if len(self.active_observations) != self.length:
                raise ValueError("active_observations length must equal episode length")
            if any(not isinstance(t, int) or isinstance(t, bool) for t in self.active_observations):
                raise ValueError("active_observations must contain integer indices")
            if any(self.active_observations[i] >= self.active_observations[i+1] for i in range(len(self.active_observations)-1)):
                raise ValueError("active_observations must be strictly increasing")
            if self.active_observations[0] != self.start or self.active_observations[-1] != self.end:
                raise ValueError("active_observations must start at episode.start and end at episode.end")
            if self.trigger_count < 1:
                raise ValueError("trigger_count must be >=1")

def apply_persistence(flags: Sequence[bool], min_persistence: int) -> List[bool]:
    """Return alert-active mask. Alert becomes active at persistence-satisfied index (no backdating)."""
    if min_persistence < 1:
        raise ValueError("min_persistence must be >=1")
    out = [False] * len(flags)
    run = 0
    for i, f in enumerate(flags):
        run = run + 1 if f else 0
        if run >= min_persistence:
            out[i] = True
    # once active, keep active while condition remains true? For simplicity, active only where run>=persistence.
    # Better: active from trigger until condition breaks.
    out2 = [False] * len(flags)
    run = 0
    triggered = False
    for i, f in enumerate(flags):
        if f:
            run += 1
            if run >= min_persistence:
                triggered = True
            if triggered:
                out2[i] = True
        else:
            run = 0
            triggered = False
    return out2

def build_episodes(times: Sequence[int], active: Sequence[bool], valid: Sequence[bool], cfg: AlertAccountingConfig) -> List[AlertEpisode]:
    if not (len(times) == len(active) == len(valid)):
        raise ValueError("times/active/valid length mismatch")
    cfg.validate()
    episodes: List[AlertEpisode] = []
    cur_start = None
    cur_end = None
    cur_active: List[int] = []
    cur_triggers = 0
    last_active_valid_t = None
    for t, a, v in zip(times, active, valid):
        if not v:
            if cfg.treat_missing_as_break and cur_start is not None:
                episodes.append(AlertEpisode(cur_start, cur_end, len(cur_active), cur_triggers, active_observations=list(cur_active)))
                cur_start = cur_end = None
                cur_active = []
                cur_triggers = 0
                last_active_valid_t = None
            continue
        if a:
            if cur_start is None:
                cur_start = cur_end = t
                cur_active = [t]
                cur_triggers = 1
                last_active_valid_t = t
            else:
                gap = (t - last_active_valid_t - 1) if last_active_valid_t is not None else 0
                if gap <= cfg.merge_gap:
                    cur_end = t
                    cur_active.append(t)
                    cur_triggers += 1
                    last_active_valid_t = t
                else:
                    episodes.append(AlertEpisode(cur_start, cur_end, len(cur_active), cur_triggers, active_observations=list(cur_active)))
                    cur_start = cur_end = t
                    cur_active = [t]
                    cur_triggers = 1
                    last_active_valid_t = t
        else:
            if cur_start is not None:
                gap = (t - last_active_valid_t - 1) if last_active_valid_t is not None else 0
                if gap > cfg.merge_gap:
                    episodes.append(AlertEpisode(cur_start, cur_end, len(cur_active), cur_triggers, active_observations=list(cur_active)))
                    cur_start = cur_end = None
                    cur_active = []
                    cur_triggers = 0
                    last_active_valid_t = None
        # last_valid_t not needed now
    if cur_start is not None:
        episodes.append(AlertEpisode(cur_start, cur_end, len(cur_active), cur_triggers, active_observations=list(cur_active)))
    episodes = [e for e in episodes if e.length >= cfg.min_episode_length]
    return episodes
