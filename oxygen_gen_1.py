atmosphere = get_component('atmosphere')

while True:
    co2_level = atmosphere.get_co2()
    self.set_intake(co2_level / 10)
    if self.waste() >= 50:
        self.dump_waste()