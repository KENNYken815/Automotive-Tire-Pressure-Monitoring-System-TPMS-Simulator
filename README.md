# Automotive Tire Pressure Monitoring System (TPMS) Simulator

A clean, host-runnable automotive TPMS simulator that generates tire pressure and temperature data, evaluates abnormal conditions, tracks sensor health, and produces ECU-style diagnostic/telemetry output.

> **Project status:** Completed reference/simulation project. It demonstrates automotive/embedded software concepts on a PC; it does not claim validation against a real TPMS sensor, RF stack, or vehicle ECU.

## Implemented
- Four virtual wheel sensors: FL, FR, RL, RR
- Pressure and temperature generation
- Sensor battery and signal-quality modelling
- Low/high pressure and high-temperature detection
- Hysteresis to reduce alarm chatter
- Sensor timeout and invalid-data detection
- Per-wheel health/status and DTC-style codes
- Vehicle warning aggregation
- Deterministic fault scenarios
- Console dashboard and CSV telemetry export
- Unit tests with no external Python dependencies

## Reference limits
| Parameter | Value |
|---|---:|
| Low-pressure warning | 30 psi |
| Low-pressure clear | 32 psi |
| High-pressure warning | 44 psi |
| High-pressure clear | 42 psi |
| High-temperature warning | 85 C |
| Sensor timeout | 3 s |
| Low sensor battery | 2.5 V |

These are simulation parameters, not OEM calibration data.

## Repository structure
```text
.
├── src/                    # Core simulator implementation
│   ├── config.py           # Calibration/settings
│   ├── models.py           # Data structures and enums
│   ├── sensors.py          # Virtual tire sensors
│   ├── monitor.py          # Monitoring and fault detection
│   ├── diagnostics.py      # DTC and ECU-style status output
│   ├── telemetry.py        # Console/CSV/JSON support
│   └── simulator.py        # Simulation engine
├── scenarios/              # Demonstration fault scenarios
│   └── demo_scenarios.py
├── tests/                  # Automated tests
│   └── test_tpms.py
├── docs/                   # Design and verification documents
│   ├── ARCHITECTURE.md
│   ├── SIGNALS_AND_DTCS.md
│   └── TEST_PLAN.md
├── output/                 # Generated telemetry (kept out of source code)
├── run_demo.py             # User-facing entry point
├── Makefile                # Convenience commands
└── README.md
```

The folders are separated by responsibility so users can start with `run_demo.py`, inspect behavior in `src/`, try faults in `scenarios/`, and verify logic in `tests/` without mixing generated files with source code.

## Run it
```bash
python3 run_demo.py
python3 -m unittest discover -s tests -v
python3 run_demo.py --csv output/tpms_log.csv
```

Or:
```bash
make run
make test
```

## Scenarios included
- Normal driving
- Low pressure on one wheel
- High temperature on one wheel
- Sensor timeout
- Invalid sensor data

## Diagnostic codes
| Code | Meaning |
|---|---|
| TPMS_000 | No active fault |
| TPMS_101 | Low pressure |
| TPMS_102 | High pressure |
| TPMS_103 | High temperature |
| TPMS_201 | Sensor timeout |
| TPMS_202 | Invalid sensor data |
| TPMS_203 | Low sensor battery |
| TPMS_204 | Poor sensor signal |

These are project-defined diagnostic IDs, not OEM identifiers.

## Portfolio value
Demonstrates sensor modelling, periodic monitoring, threshold/hysteresis logic, fault-state handling, sensor plausibility checks, diagnostic reporting, telemetry and unit testing.

## Extension path
A future MCU version can replace the virtual sensor layer with real ADC/RF/CAN interfaces while keeping the monitoring and diagnostic concepts intact. Real RF timing, sensor accuracy, ECU integration and environmental performance require hardware validation.

## Safety and scope
This is a simulation/reference project, not a certified automotive safety system. Use real vehicle integration only after appropriate hardware, software, safety and validation work.