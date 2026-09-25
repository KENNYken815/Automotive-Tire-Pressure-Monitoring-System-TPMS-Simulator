import argparse
from scenarios.demo_scenarios import build_simulator,apply_low_pressure,apply_overtemperature,disable_sensor,invalidate_sensor
from src.telemetry import print_status

def run_case(name,setup):
    print('\n'+'='*68+'\n'+name+'\n'+'='*68); sim=build_simulator(); sim.run(1.0); setup(sim); print_status(sim.run(2.0)[-1]); return sim

def main():
    p=argparse.ArgumentParser(description='Automotive TPMS simulator'); p.add_argument('--csv'); a=p.parse_args()
    sims=[run_case('NORMAL DRIVING',lambda s:None),run_case('LOW PRESSURE',apply_low_pressure),run_case('HIGH TEMPERATURE',apply_overtemperature),run_case('SENSOR TIMEOUT',disable_sensor),run_case('INVALID SENSOR DATA',invalidate_sensor)]
    if a.csv: sims[0].export_csv(a.csv); print(f'CSV written to {a.csv}')
if __name__=='__main__': main()
