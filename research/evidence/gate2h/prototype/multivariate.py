from __future__ import annotations
from typing import List, Sequence, Optional
import math
from .quality import Observation, valid_observation
from .config import RollingCorrelationConfig

def _corr(a: List[float], b: List[float]) -> Optional[float]:
    n = len(a)
    if n < 3:
        return None
    ma = sum(a)/n; mb=sum(b)/n
    va = sum((x-ma)**2 for x in a)
    vb = sum((x-mb)**2 for x in b)
    if va <= 0 or vb <= 0:
        return None
    cov = sum((x-ma)*(y-mb) for x,y in zip(a,b))
    return cov / math.sqrt(va*vb)

def rolling_correlation_change_alerts(obs: Sequence[Observation], cfg: RollingCorrelationConfig) -> List[bool]:
    """Return raw condition flags; persistence applied by caller."""
    cfg.validate()
    out = [False] * len(obs)
    # compute rolling correlation series
    corrs: List[Optional[float]] = [None] * len(obs)
    xs: List[Optional[float]] = []
    ys: List[Optional[float]] = []
    for o in obs:
        ok = valid_observation(o, [cfg.var_x, cfg.var_y])
        xs.append(o.values.get(cfg.var_x) if ok else None)
        ys.append(o.values.get(cfg.var_y) if ok else None)
    for i in range(len(obs)):
        start = max(0, i - cfg.window + 1)
        ax, ay = [], []
        for j in range(start, i+1):
            if xs[j] is not None and ys[j] is not None:
                ax.append(xs[j]); ay.append(ys[j])
        corrs[i] = _corr(ax, ay)
    # alert when recent correlation deviates from baseline window
    for i in range(len(obs)):
        cur = corrs[i]
        if cur is None:
            continue
        bstart = max(0, i - cfg.baseline_window)
        base = [c for c in corrs[bstart:i] if c is not None]
        if len(base) < max(5, cfg.baseline_window // 4):
            continue
        bmean = sum(base)/len(base)
        if abs(cur - bmean) >= cfg.delta_threshold:
            out[i] = True
    return out
