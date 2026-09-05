thermometer = get_component('thermometer')
transmitter = get_component('transmitter')

temp = thermometer.get_value()

transmitter.connect('earth')
transmitter.transmit('current_temperature', temp)
