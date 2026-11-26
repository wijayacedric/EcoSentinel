from __future__ import annotations
from typing import List, Sequence, Optional, Dict
import math
from .quality import Observation, valid_observation
from .config import BaselineThresholdConfig, RollingZScoreConfig

def threshold_alerts(obs: Sequence[Observation], cfg: BaselineThresholdConfig) -> List[bool]:
    """Return raw condition flags; persistence applied by caller."""
    cfg.validate()
    out = []
    for o in obs:
        if not valid_observation(o, [cfg.variable]):
            out.append(False)
            continue
        v = o.values[cfg.variable]
        if v is None:
            out.append(False)
        elif cfg.direction == 'above':
            out.append(v >= cfg.threshold)
        elif cfg.direction == 'below':
            out.append(v <= cfg.threshold)
        else:
            raise ValueError('bad direction')
    return out

def rolling_zscore_alerts(obs: Sequence[Observation], cfg: RollingZScoreConfig) -> List[bool]:
    """Return raw condition flags; persistence applied by caller."""
    cfg.validate()
    vals: List[Optional[float]] = []
    for o in obs:
        vals.append(o.values.get(cfg.variable) if valid_observation(o, [cfg.variable]) else None)
    out = [False] * len(obs)
    for i in range(len(obs)):
        start = max(0, i - cfg.window)
        window = [v for v in vals[start:i] if v is not None]
        cur = vals[i]
        if cur is None or len(window) < max(5, cfg.window // 3):
            out[i] = False
            continue
        mean = sum(window) / len(window)
        var = sum((x - mean) ** 2 for x in window) / len(window)
        sd = math.sqrt(var)
        if sd == 0:
            out[i] = False
        else:
            out[i] = abs((cur - mean) / sd) >= cfg.z_threshold
    return out
