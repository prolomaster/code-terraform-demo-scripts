c = get_component('bio_collector_1')
inv = get_component('inventory')
shop = get_component('shop')

while True:
    while not c.cargo:
        sleep(1)
    self.take_from(c)
    a = self.analyze()
    for reagent, quantity in a.required_recipe.items():
        while quantity > inv.get_count(reagent):
            shop.buy(reagent)
        self.load(reagent, quantity)
    self.extract()