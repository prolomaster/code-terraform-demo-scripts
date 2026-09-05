clock = get_component('clock')

while True:
    self.set_tilt(clock.get_elevation())