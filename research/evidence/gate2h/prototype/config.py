from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class BaselineThresholdConfig:
    variable: str
    threshold: float
    direction: str = "above"  # above|below
    min_persistence: int = 1

    def validate(self) -> None:
        if self.direction not in {"above", "below"}:
            raise ValueError("direction must be above|below")
        if self.min_persistence < 1:
            raise ValueError("min_persistence must be >=1")

@dataclass
class RollingZScoreConfig:
    variable: str
    window: int = 24
    z_threshold: float = 3.0
    min_persistence: int = 2

    def validate(self) -> None:
        if self.window < 2: raise ValueError("window must be >=2")
        if self.z_threshold <= 0: raise ValueError("z_threshold must be >0")
        if self.min_persistence < 1: raise ValueError("min_persistence must be >=1")

@dataclass
class RollingCorrelationConfig:
    var_x: str
    var_y: str
    window: int = 24
    baseline_window: int = 72
    delta_threshold: float = 0.5
    min_persistence: int = 3

    def validate(self) -> None:
        if self.window < 3: raise ValueError("window must be >=3")
        if self.baseline_window < 3: raise ValueError("baseline_window must be >=3")
        if self.delta_threshold < 0: raise ValueError("delta_threshold must be >=0")
        if self.min_persistence < 1: raise ValueError("min_persistence must be >=1")

@dataclass
class AlertAccountingConfig:
    merge_gap: int = 0  # merge episodes separated by <= merge_gap valid observations
    min_episode_length: int = 1
    treat_missing_as_break: bool = True

    def validate(self) -> None:
        if self.merge_gap < 0: raise ValueError("merge_gap must be >=0")
        if self.min_episode_length < 1: raise ValueError("min_episode_length must be >=1")

@dataclass
class EvaluationConfig:
    """Configuration for SYNTHETIC evaluation logic only.

    Provisional software semantics - not scientific protocol approval.
    """
    alert_config: AlertAccountingConfig = field(default_factory=AlertAccountingConfig)
    max_warning_horizon: Optional[int] = None  # REQUIRED for evaluation; no scientific default
    allow_unverified_exposure: bool = False  # must be False

    def validate(self, require_horizon: bool = False) -> None:
        self.alert_config.validate()
        if self.allow_unverified_exposure:
            raise ValueError("allow_unverified_exposure must be False; real exposure requires approved biological evidence")
        if require_horizon:
            if self.max_warning_horizon is None:
                raise ValueError("max_warning_horizon is required; no scientifically justified default is provided")
            if self.max_warning_horizon < 0:
                raise ValueError("max_warning_horizon must be >=0")
