from dataclasses import dataclass, field
from enum import Enum
from typing import List

class WheelPosition(str, Enum):
    FL='FL'; FR='FR'; RL='RL'; RR='RR'
class PressureState(str, Enum):
    NORMAL='NORMAL'; LOW='LOW'; HIGH='HIGH'
class SensorHealth(str, Enum):
    OK='OK'; TIMEOUT='TIMEOUT'; INVALID='INVALID'; LOW_BATTERY='LOW_BATTERY'; POOR_SIGNAL='POOR_SIGNAL'
@dataclass
class SensorReading:
    wheel: WheelPosition; timestamp_s: float; pressure_psi: float; temperature_c: float
    battery_v: float=3.0; signal_quality_pct: float=100.0; valid: bool=True
@dataclass
class WheelStatus:
    wheel: WheelPosition; pressure_state: PressureState=PressureState.NORMAL
    temperature_high: bool=False; health: SensorHealth=SensorHealth.OK
    active_dtcs: List[str]=field(default_factory=list)
@dataclass
class VehicleStatus:
    timestamp_s: float; warning_active: bool; wheel_status: List[WheelStatus]; active_dtcs: List[str]
