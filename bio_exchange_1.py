bc = get_component('bio_collector_1')

incomplete_orders = [
    order for order in self.orders() if order.status != 'complete'
]

incomplete_orders.sort(key = lambda o: o.reward, reverse = True)

for order in incomplete_orders:
    self.set_order(order.id)
    while order.status != 'complete':
        self.deliver()

# def collect_components(fragment_id: str, count=1) -> None:
#     bc.coll


# for o in incomplete_orders:
#     # print(o.reward)
#     self.set_order(o.id)
#     print(o)
#     break


# <BioOrder: id='bio_order_10', 
# name='Nocturna Frozen Compendium', 
# biome='frozen', 
# requires={
#     'gw_cranial_plate': 30, 
#     'sd_cranial_crest': 30, 
#     'mh_fruiting_body': 52, 
#     'st_scute_plate': 43
# }, 
# reward=14500, 
# status='available', 
# delivered={
#     'gw_cranial_plate': 0, 
#     'sd_cranial_crest': 0, 
#     'mh_fruiting_body': 0, 
#     'st_scute_plate': 0
# }, 
# percent=0>