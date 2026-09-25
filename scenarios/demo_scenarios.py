from src.config import TpmsConfig
from src.models import WheelPosition
from src.sensors import VirtualTireSensor
from src.monitor import TpmsMonitor
from src.simulator import TpmsSimulator

def build_simulator():
    sensors={WheelPosition.FL:VirtualTireSensor(WheelPosition.FL,35,32),WheelPosition.FR:VirtualTireSensor(WheelPosition.FR,35.5,33),WheelPosition.RL:VirtualTireSensor(WheelPosition.RL,34.5,31),WheelPosition.RR:VirtualTireSensor(WheelPosition.RR,35,32.5)}
    return TpmsSimulator(TpmsMonitor(TpmsConfig()),sensors)
def apply_low_pressure(sim,wheel=WheelPosition.FL,pressure=27): sim.sensors[wheel].set_pressure(pressure)
def apply_overtemperature(sim,wheel=WheelPosition.RR,temp_c=95): sim.sensors[wheel].set_temperature(temp_c)
def disable_sensor(sim,wheel=WheelPosition.RL): sim.sensors[wheel].enabled=False
def invalidate_sensor(sim,wheel=WheelPosition.FR): sim.sensors[wheel].invalid=True
