from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Optional, Sequence
import math

MISSING_TOKENS = {"", "NA", "NaN", "nan", "null", "None", "N/A", "na"}

@dataclass
class Observation:
    t: int  # integer time index for deterministic synthetic tests
    values: Dict[str, Optional[float]]
    flags: Dict[str, str]
    is_missing: bool = False

def is_missing_value(v) -> bool:
    if v is None:
        return True
    if isinstance(v, str) and v.strip() in MISSING_TOKENS:
        return True
    return False

def parse_float(v) -> Optional[float]:
    if is_missing_value(v):
        return None
    try:
        x = float(v)
    except Exception:
        return None
    if not math.isfinite(x):
        return None
    return x

def normalize_flag(flag: Optional[str]) -> str:
    if flag is None:
        return ""
    return str(flag).strip().upper()

def valid_observation(obs: Observation, required_vars: Sequence[str], bad_flags: Sequence[str]=("M","C")) -> bool:
    if obs.is_missing:
        return False
    bad = {normalize_flag(f) for f in bad_flags}
    for var in required_vars:
        if var not in obs.values or obs.values[var] is None:
            return False
        val = obs.values[var]
        if isinstance(val, float) and not math.isfinite(val):
            return False
        flag = normalize_flag(obs.flags.get(var, ""))
        if flag in bad:
            return False
    return True
