bc = get_component('bio_collector_1')

incomplete_orders = [
    order for order in self.orders() if order.status != 'complete'
]

incomplete_orders.sort(key = lambda o: o.reward, reverse = True)

for order in incomplete_orders:
    self.set_order(order.id)
    while order.status != 'complete':
        self.deliver()

