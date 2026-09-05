j = get_component('journal')
be = get_component('bio_exchange_1')
inv = get_component('inventory')

def collect_component(fragment_id: str, count: int) -> None:
    known_frag_locs = {
        cat_frag.fragment_id: cat_frag.coords
        for cat_frag in j.cataloged_fragments('nocturna')
    }
    if not fragment_id in known_frag_locs:
        self.scan()
    for _ in range(count): 
        self.collect(known_frag_locs[fragment_id])
        while self.cargo:
            pass


incomplete_orders = [
    order for order in be.orders() if order.status != 'complete'
]

incomplete_orders.sort(key = lambda o: o.reward, reverse = True)

def main():
    # get active order
    # collect the materials
    # wait for delivery to proceed
    for fragment_id, required_fragment_count in be.active_order().requires.items():
        needed_fragment_count = required_fragment_count - be.active_order().delivered[fragment_id] - inv.get_count(fragment_id)
        collect_component(fragment_id, needed_fragment_count)

main()