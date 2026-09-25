from .telemetry import save_csv
class TpmsSimulator:
    def __init__(self,monitor,sensors): self.monitor=monitor; self.sensors=sensors; self.time_s=0.0; self.rows=[]
    def step(self,dt_s=0.2):
        self.time_s+=dt_s
        for sensor in self.sensors.values():
            r=sensor.update(self.time_s,dt_s)
            if r is not None: self.monitor.process(r)
        self.monitor.check_timeouts(self.time_s); status=self.monitor.snapshot(self.time_s)
        for w in status.wheel_status: self.rows.append([f'{self.time_s:.1f}',int(status.warning_active),w.wheel.value,w.pressure_state.value,int(w.temperature_high),w.health.value,'|'.join(w.active_dtcs)])
        return status
    def run(self,duration_s,dt_s=0.2): return [self.step(dt_s) for _ in range(int(duration_s/dt_s))]
    def export_csv(self,filename): save_csv(self.rows,filename)
