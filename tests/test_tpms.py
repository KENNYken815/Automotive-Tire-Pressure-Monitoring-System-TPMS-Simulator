import unittest
from src.config import TpmsConfig
from src.models import WheelPosition,PressureState,SensorHealth
from src.sensors import VirtualTireSensor
from src.monitor import TpmsMonitor
class TestTpms(unittest.TestCase):
 def setUp(self): self.m=TpmsMonitor(TpmsConfig()); self.s=VirtualTireSensor(WheelPosition.FL,35,30)
 def test_normal(self): self.m.process(self.s.update(.2,.2)); self.assertEqual(self.m.status[WheelPosition.FL].pressure_state,PressureState.NORMAL)
 def test_low(self): self.s.set_pressure(28); self.m.process(self.s.update(.2,.2)); self.assertEqual(self.m.status[WheelPosition.FL].active_dtcs,['TPMS_101'])
 def test_high_temp(self): self.s.set_temperature(90); self.m.process(self.s.update(.2,.2)); self.assertIn('TPMS_103',self.m.status[WheelPosition.FL].active_dtcs)
 def test_invalid(self): self.s.invalid=True; self.m.process(self.s.update(.2,.2)); self.assertEqual(self.m.status[WheelPosition.FL].health,SensorHealth.INVALID)
 def test_timeout(self): self.m.check_timeouts(4); self.assertEqual(self.m.status[WheelPosition.FL].health,SensorHealth.TIMEOUT)
if __name__=='__main__': unittest.main()
