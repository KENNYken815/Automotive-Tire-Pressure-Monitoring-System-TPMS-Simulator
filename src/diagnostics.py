DTC_TEXT={'TPMS_000':'No fault','TPMS_101':'Low pressure','TPMS_102':'High pressure','TPMS_103':'High temperature','TPMS_201':'Sensor timeout','TPMS_202':'Invalid sensor data','TPMS_203':'Low sensor battery','TPMS_204':'Poor sensor signal'}
def format_diagnostics(status):
    lines=[f'Time: {status.timestamp_s:4.1f}s | WARNING: {"ON" if status.warning_active else "OFF"}']
    for w in status.wheel_status:
        lines.append(f'  {w.wheel.value}: pressure={w.pressure_state.value:<6} temp={"HIGH" if w.temperature_high else "OK":<4} health={w.health.value:<12} DTC={",".join(w.active_dtcs)}')
    if status.active_dtcs: lines.append('  Vehicle DTCs: '+', '.join(f'{d} ({DTC_TEXT.get(d,"Unknown")})' for d in status.active_dtcs))
    return '\n'.join(lines)
def encode_can_status(status):
    return bytes([1 if status.warning_active else 0,min(len(status.active_dtcs),255),len(status.wheel_status),0,0,0,0,0])
