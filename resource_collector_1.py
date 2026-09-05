s = get_component('scanner')
inv = get_component("inventory")

def to_coord(sector: str) -> list[int, int]:
    return [
        int(sector[1:]),
        'ABCDEFGH'.index(sector[0])
    ]

def to_sector(coord: list[int, int]) -> str:
    return 'ABCDEFGH'[coord[1]] + str(coord[0])

def sign(i: int) -> int:
    return (i > 0) - (i < 0)

def heat_check():
    if self.get_heat() >= 90:
        print('Harvester overheated; sleeping for 60s')
        sleep(120)


def move_collect(sector: str) -> None:
    target_coord = to_coord(sector)
    current_coord = to_coord(self.get_position())
    
    x_delta = target_coord[0] - current_coord[0]
    y_delta = target_coord[1] - current_coord[1]

    print(f'Moving {abs(x_delta) + abs(y_delta)} cells from {to_sector(current_coord)} to {to_sector(target_coord)}')
    # Move in x axis
    for _ in range(abs(x_delta)):
        current_coord = to_coord(self.get_position())
        step = to_sector([current_coord[0] + sign(x_delta), current_coord[1]])
        self.move(step)
        heat_check()

    # Move in y axis
    for _ in range(abs(y_delta)):
        current_coord = to_coord(self.get_position())
        step = to_sector([current_coord[0], current_coord[1] + sign(y_delta)])
        self.move(step)
        heat_check()

    pickup = self.collect()
    if pickup.ok:
        stored = inv.store()
        print("stored " + pickup.name)

scanned = [
    {'sector': k, 'result': v}
    for k, v in s.get_scanned().items()
    if v.value != 0
]
scanned.sort(key=lambda d: d['result'].value, reverse=True)

inv.store()
# Rares
for s in (
    'B14'
):
    move_collect(s)
