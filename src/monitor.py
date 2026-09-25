import math
from .models import PressureState,SensorHealth,WheelPosition

class TpmsMonitor:
    def __init__(self,config):
        self.config=config; self.status={w:__import__('src.models',fromlist=['WheelStatus']).WheelStatus(w) for w in WheelPosition}; self.last_reading={}
    def process(self,reading):
        s=self.status[reading.wheel]
        if not reading.valid or not math.isfinite(reading.pressure_psi) or not math.isfinite(reading.temperature_c):
            s.health=SensorHealth.INVALID; s.active_dtcs=['TPMS_202']; return s
        self.last_reading[reading.wheel]=reading
        if not(self.config.minimum_pressure_psi<=reading.pressure_psi<=self.config.maximum_pressure_psi and self.config.minimum_temperature_c<=reading.temperature_c<=self.config.maximum_temperature_c):
            s.health=SensorHealth.INVALID; s.active_dtcs=['TPMS_202']; return s
        if reading.battery_v<self.config.battery_warning_v: s.health=SensorHealth.LOW_BATTERY
        elif reading.signal_quality_pct<40: s.health=SensorHealth.POOR_SIGNAL
        else: s.health=SensorHealth.OK
        if reading.pressure_psi<self.config.low_pressure_psi: s.pressure_state=PressureState.LOW
        elif s.pressure_state==PressureState.LOW and reading.pressure_psi<self.config.low_pressure_clear_psi: s.pressure_state=PressureState.LOW
        elif reading.pressure_psi>self.config.high_pressure_psi: s.pressure_state=PressureState.HIGH
        elif s.pressure_state==PressureState.HIGH and reading.pressure_psi>self.config.high_pressure_clear_psi: s.pressure_state=PressureState.HIGH
        else: s.pressure_state=PressureState.NORMAL
        s.temperature_high=reading.temperature_c>=self.config.high_temperature_c
        dtcs=[]
        if s.pressure_state==PressureState.LOW: dtcs.append('TPMS_101')
        if s.pressure_state==PressureState.HIGH: dtcs.append('TPMS_102')
        if s.temperature_high: dtcs.append('TPMS_103')
        if s.health==SensorHealth.LOW_BATTERY: dtcs.append('TPMS_203')
        if s.health==SensorHealth.POOR_SIGNAL: dtcs.append('TPMS_204')
        s.active_dtcs=dtcs or ['TPMS_000']; return s
    def check_timeouts(self,now_s):
        for w in WheelPosition:
            last=self.last_reading.get(w)
            if last is None or now_s-last.timestamp_s>self.config.sensor_timeout_s:
                self.status[w].health=SensorHealth.TIMEOUT; self.status[w].active_dtcs=['TPMS_201']
    def vehicle_warning(self): return any(s.active_dtcs!=['TPMS_000'] for s in self.status.values())
    def snapshot(self,t):
        from .models import VehicleStatus
        active=sorted({d for s in self.status.values() for d in s.active_dtcs if d!='TPMS_000'})
        return VehicleStatus(t,self.vehicle_warning(),list(self.status.values()),active)
