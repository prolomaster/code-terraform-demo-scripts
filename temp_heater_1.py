lookup = {
    'clear': 5,
    'dust_storm': 3,
    'heat_bleed': 9,
    'dust_veil': 2
}

while True:
    self.set_power(lookup[self.thermal_state()])