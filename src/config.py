from dataclasses import dataclass

@dataclass(frozen=True)
class TpmsConfig:
    low_pressure_psi: float = 30.0
    low_pressure_clear_psi: float = 32.0
    high_pressure_psi: float = 44.0
    high_pressure_clear_psi: float = 42.0
    high_temperature_c: float = 85.0
    sensor_timeout_s: float = 3.0
    battery_warning_v: float = 2.5
    minimum_pressure_psi: float = 5.0
    maximum_pressure_psi: float = 80.0
    minimum_temperature_c: float = -40.0
    maximum_temperature_c: float = 125.0
