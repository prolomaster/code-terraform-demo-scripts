sensor = get_component('pressure_sensor')
raw_value = sensor.get_value()

sensor.stabilize(
    raw_value if raw_value % 2 == 0 else raw_value + 1
)
