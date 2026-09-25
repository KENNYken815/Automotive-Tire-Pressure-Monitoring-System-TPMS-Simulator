# Test Plan

1. Normal pressure remains NORMAL.
2. Low pressure creates TPMS_101.
3. High pressure creates TPMS_102.
4. High temperature creates TPMS_103.
5. Invalid sensor data creates TPMS_202.
6. Sensor silence beyond 3 s creates TPMS_201.
7. Low battery creates TPMS_203.
8. Poor signal creates TPMS_204.
9. Multiple wheel faults raise the vehicle warning.

The included unit tests cover representative software behavior. RF performance, physical sensor accuracy and real ECU integration require hardware validation.
