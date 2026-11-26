from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List

@dataclass
class IntervalCensoredEvent:
    """Synthetic/approved-event representation with interval-censored bounds.

    All bounds are integer time indices in test fixtures. No real biological labels.
    """
    event_id: str
    onset_earliest: int
    onset_latest: int
    termination_earliest: int
    termination_latest: int
    source: str = "SYNTHETIC"

    def validate(self) -> None:
        def _is_int(v):
            return isinstance(v, int) and not isinstance(v, bool)
        for name, val in [('onset_earliest',self.onset_earliest),('onset_latest',self.onset_latest),('termination_earliest',self.termination_earliest),('termination_latest',self.termination_latest)]:
            if not _is_int(val):
                raise ValueError(f"{name} must be integer")
            if val < 0:
                raise ValueError(f"{name} must be >=0")
        if not (self.onset_earliest <= self.onset_latest <= self.termination_latest):
            raise ValueError("invalid onset bounds")
        if not (self.onset_earliest <= self.termination_earliest <= self.termination_latest):
            raise ValueError("invalid termination bounds")
        if self.termination_earliest < self.onset_latest:
            # allow, but this means uncertain overlap; caller must handle
            pass

@dataclass
class ExposureInterval:
    start: int
    end: int  # inclusive
    kind: str  # synthetic_non_event | unknown | synthetic_event
    source: str = "SYNTHETIC"

    def validate(self) -> None:
        def _is_int(v):
            return isinstance(v, int) and not isinstance(v, bool)
        if not _is_int(self.start) or not _is_int(self.end):
            raise ValueError("exposure bounds must be integers")
        if self.start < 0 or self.end < 0:
            raise ValueError("exposure bounds must be >=0")
        if self.start > self.end:
            raise ValueError("exposure start must be <= end")
        if self.kind not in {"synthetic_non_event","unknown","synthetic_event"}:
            raise ValueError(f"invalid exposure kind: {self.kind}")
