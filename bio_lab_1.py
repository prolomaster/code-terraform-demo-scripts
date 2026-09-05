c = get_component('bio_collector_1')

while True:
    while not c.cargo:
        sleep(1)
    self.take_from(c)
    a = self.analyze()
    for reagent, quantity in a.required_recipe.items():
        self.load(reagent, quantity)
    self.extract()