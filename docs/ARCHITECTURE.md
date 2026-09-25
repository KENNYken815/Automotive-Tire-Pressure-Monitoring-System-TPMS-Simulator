# Architecture

Sensor generation, monitoring, diagnostics and telemetry are separated into independent modules. The scenario layer changes test conditions without changing the core monitor.

```text
Virtual sensors -> validation -> threshold/hysteresis monitor -> wheel status -> vehicle warning
                                                   |-> DTCs
                                                   `-> telemetry
```
