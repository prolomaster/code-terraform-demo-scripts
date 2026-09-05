archive = self.contract.archive
transmitter = get_component('transmitter')

serialized = [
    [i, j, archive.flip(i, j)]
    for i in range(10)
    for j in range(10)
]

serialized.sort(key=lambda l: l[2])

pairs = [
    [serialized[i][0], serialized[i][1], serialized[i+1][0], serialized[i+1][1]]
    for i in range(0, len(serialized), 2)
]

print(serialized, pairs)

transmitter.connect('earth')
transmitter.transmit(self.contract.id, pairs)