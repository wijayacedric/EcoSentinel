from __future__ import annotations
from dataclasses import dataclass
from typing import Sequence

@dataclass
class LeakageCheckResult:
    ok: bool
    issues: list[str]

def check_no_future_baseline(current_index: int, baseline_indices: Sequence[int]) -> LeakageCheckResult:
    issues = []
    for i in baseline_indices:
        if i >= current_index:
            issues.append(f"baseline index {i} >= current_index {current_index}")
    return LeakageCheckResult(ok=len(issues)==0, issues=issues)

def check_temporal_split(train_end: int, test_start: int) -> LeakageCheckResult:
    issues = []
    if test_start <= train_end:
        issues.append("test_start must be after train_end")
    return LeakageCheckResult(ok=len(issues)==0, issues=issues)

def check_no_random_window_split(is_random_split: bool) -> LeakageCheckResult:
    if is_random_split:
        return LeakageCheckResult(False, ["random window split forbidden for autocorrelated time series"])
    return LeakageCheckResult(True, [])
