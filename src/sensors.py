import math
from typing import Optional
from .models import SensorReading, WheelPosition

class VirtualTireSensor:
    def __init__(self,wheel,pressure_psi,temperature_c,battery_v=3.0,signal_quality_pct=100.0):
        self.wheel=wheel; self.pressure_psi=pressure_psi; self.temperature_c=temperature_c
        self.battery_v=battery_v; self.signal_quality_pct=signal_quality_pct
        self.enabled=True; self.invalid=False; self.phase=0.0
    def update(self,timestamp_s,dt_s=0.2)->Optional[SensorReading]:
        self.phase += dt_s
        if not self.enabled: return None
        if self.invalid:
            return SensorReading(self.wheel,timestamp_s,float('nan'),float('nan'),self.battery_v,self.signal_quality_pct,False)
        return SensorReading(self.wheel,timestamp_s,self.pressure_psi+0.08*math.sin(self.phase),self.temperature_c+0.25*math.sin(self.phase/3),self.battery_v,self.signal_quality_pct,True)
    def set_pressure(self,psi): self.pressure_psi=psi
    def set_temperature(self,temp_c): self.temperature_c=temp_c
