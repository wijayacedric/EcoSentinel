from __future__ import annotations
from dataclasses import dataclass
from typing import List, Dict, Tuple
import math, random
from .quality import Observation
from .events import IntervalCensoredEvent, ExposureInterval

@dataclass
class SyntheticScenario:
    name: str
    description: str
    times: List[int]
    observations: List[Observation]
    events: List[IntervalCensoredEvent]
    exposure: List[ExposureInterval]
    expected: Dict[str, object]
    max_warning_horizon: int
    synthetic: bool = True

def _obs(t:int, **vals):
    return Observation(t=t, values={k:(float(v) if v is not None else None) for k,v in vals.items()}, flags={k:'' for k in vals})

def genuine_early_warning_scenario() -> SyntheticScenario:
    # x,y stable then relationship breaks down before synthetic event
    times = list(range(120))
    obs=[]
    for t in times:
        seasonal = 10 + 2*math.sin(2*math.pi*t/60)
        x = seasonal + 0.1*(t%5)
        y = 2*x + 0.2  # strong relationship
        if 60 <= t < 80:
            y = 2*x + 0.2 + (t-60)*0.8  # relationship drift before event
        if t >= 80:
            y = 2*x + 8 + math.sin(t)  # changed regime during event
        obs.append(_obs(t, x=x, y=y, temp=seasonal))
    events=[IntervalCensoredEvent('E1', onset_earliest=80, onset_latest=83, termination_earliest=100, termination_latest=105, source='SYNTHETIC_TEST')]
    exposure=[ExposureInterval(0,59,'synthetic_non_event','SYNTHETIC_TEST'), ExposureInterval(60,79,'unknown','SYNTHETIC_TEST'), ExposureInterval(80,105,'synthetic_event','SYNTHETIC_TEST'), ExposureInterval(106,119,'synthetic_non_event','SYNTHETIC_TEST')]
    return SyntheticScenario('genuine_synthetic_early_warning','Relationship changes before synthetic event',times,obs,events,exposure,{'expect_confirmed_early_warning':True}, max_warning_horizon=30)

def no_warning_scenario() -> SyntheticScenario:
    times=list(range(100))
    obs=[]
    for t in times:
        x=10+math.sin(t/10)
        y=2*x+0.1*math.cos(t/8)
        obs.append(_obs(t,x=x,y=y))
    events=[IntervalCensoredEvent('E1', onset_earliest=70,onset_latest=72,termination_earliest=85,termination_latest=87,source='SYNTHETIC_TEST')]
    exposure=[ExposureInterval(0,69,'synthetic_non_event','SYNTHETIC_TEST'),ExposureInterval(70,87,'synthetic_event','SYNTHETIC_TEST'),ExposureInterval(88,99,'synthetic_non_event','SYNTHETIC_TEST')]
    return SyntheticScenario('no_warning','Stable relationship, no early change',times,obs,events,exposure,{'expect_confirmed_early_warning':False,'expect_no_confirmed_false_alarm_episode':True}, max_warning_horizon=30)

def seasonal_false_positive_scenario() -> SyntheticScenario:
    rng=random.Random(42)
    times=list(range(240))
    obs=[]
    for t in times:
        season = math.sin(2*math.pi*t/120)
        x = 20 + 10*season + rng.gauss(0,0.1)
        y = 40 + 20*season + rng.gauss(0,0.1)  # shared seasonality, relationship stable
        obs.append(_obs(t,x=x,y=y))
    events=[]
    exposure=[ExposureInterval(0,239,'synthetic_non_event','SYNTHETIC_TEST')]
    return SyntheticScenario('seasonal_false_positive','Shared seasonality without event',times,obs,events,exposure,{'expect_false_alarm_fraction_reported':True}, max_warning_horizon=30)

def sensor_artifact_scenario() -> SyntheticScenario:
    times=list(range(150))
    obs=[]
    for t in times:
        x=10 + 0.01*t
        y=20 + 0.02*t
        if 70 <= t <= 75:  # sensor spike/fouling artifact
            x = x + 50
        obs.append(_obs(t,x=x,y=y))
    events=[]
    # recovery period after artifact treated as unknown for this synthetic control; alerts there are ambiguous, not confirmed non-event false alarms
    exposure=[ExposureInterval(0,69,'synthetic_non_event','SYNTHETIC_TEST'),ExposureInterval(70,90,'unknown','SYNTHETIC_TEST'),ExposureInterval(91,149,'synthetic_non_event','SYNTHETIC_TEST')]
    return SyntheticScenario('sensor_artifact','Sensor spike without biological event; recovery window marked unknown',times,obs,events,exposure,{'expect_no_confirmed_false_alarm_episode':True,'artifact_window':[70,75],'recovery_unknown':[76,90]}, max_warning_horizon=30)

def missing_data_scenario() -> SyntheticScenario:
    times=list(range(120))
    obs=[]
    for t in times:
        if 40 <= t <= 50:
            obs.append(Observation(t=t, values={'x':None,'y':None}, flags={'x':'M','y':'M'}, is_missing=True))
        else:
            x=10+math.sin(t/12)
            y=2*x
            obs.append(_obs(t,x=x,y=y))
    events=[IntervalCensoredEvent('E1',90,92,105,108,'SYNTHETIC_TEST')]
    exposure=[ExposureInterval(0,39,'synthetic_non_event','SYNTHETIC_TEST'),ExposureInterval(51,89,'synthetic_non_event','SYNTHETIC_TEST'),ExposureInterval(90,108,'synthetic_event','SYNTHETIC_TEST'),ExposureInterval(109,119,'synthetic_non_event','SYNTHETIC_TEST')]
    return SyntheticScenario('missing_data','Missing block should not create fake alerts',times,obs,events,exposure,{'expect_no_confirmed_false_alarm_episode':True}, max_warning_horizon=30)

def interval_censored_event_scenario() -> SyntheticScenario:
    times=list(range(100))
    obs=[]
    for t in times:
        x=10+0.05*t
        y=2*x + (5 if 45 <= t < 70 else 0)
        obs.append(_obs(t,x=x,y=y))
    events=[IntervalCensoredEvent('E1', onset_earliest=60, onset_latest=65, termination_earliest=75, termination_latest=80, source='SYNTHETIC_TEST')]
    exposure=[ExposureInterval(0,59,'synthetic_non_event','SYNTHETIC_TEST'),ExposureInterval(60,80,'synthetic_event','SYNTHETIC_TEST'),ExposureInterval(81,99,'synthetic_non_event','SYNTHETIC_TEST')]
    return SyntheticScenario('interval_censored','Event bounds uncertain',times,obs,events,exposure,{'expect_lead_bounds_reported':True}, max_warning_horizon=30)

def sensor_replacement_scenario() -> SyntheticScenario:
    times=list(range(160))
    obs=[]
    for t in times:
        x=10+math.sin(t/15)
        y=2*x
        if t>=80:  # sensor replacement/recalibration shifts baseline
            x = x + 3
            y = 2*(x-3) + 1.5  # relationship slightly changed due to replacement artifact
        obs.append(_obs(t,x=x,y=y))
    events=[]
    exposure=[ExposureInterval(0,79,'synthetic_non_event','SYNTHETIC_TEST'),ExposureInterval(80,100,'unknown','SYNTHETIC_TEST'),ExposureInterval(101,159,'synthetic_non_event','SYNTHETIC_TEST')]
    return SyntheticScenario('sensor_replacement','Abrupt sensor replacement causes structural change',times,obs,events,exposure,{'expect_no_confirmed_false_alarm_episode':True,'replacement_t':80}, max_warning_horizon=30)

def autocorrelated_no_event_scenario() -> SyntheticScenario:
    rng=random.Random(7)
    times=list(range(200))
    obs=[]
    x=0.0; y=0.0
    for t in times:
        x = 0.95*x + rng.gauss(0,1)
        y = 0.95*y + rng.gauss(0,1)  # independent AR(1), no true relationship
        obs.append(_obs(t,x=x,y=y))
    events=[]
    exposure=[ExposureInterval(0,199,'synthetic_non_event','SYNTHETIC_TEST')]
    return SyntheticScenario('autocorrelated_no_event','Independent autocorrelated variables',times,obs,events,exposure,{'expect_no_confirmed_events':True,'expect_false_alarm_fraction_reported':True}, max_warning_horizon=30)
