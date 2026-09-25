import csv,json
from dataclasses import asdict
from pathlib import Path

def print_status(status):
    from .diagnostics import format_diagnostics; print(format_diagnostics(status))
def save_csv(rows,filename):
    p=Path(filename); p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f); w.writerow(['time_s','warning','wheel','pressure_state','temperature_high','health','dtcs']); w.writerows(rows)
def save_json(status,filename):
    p=Path(filename); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(asdict(status),indent=2,default=str),encoding='utf-8')
