oxygen_sensor = get_component('oxygen_sensor')

raw_value = oxygen_sensor.get_value()

oxygen_sensor.calibrate(raw_value * 100)