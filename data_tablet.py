tablet = self.contract.tablet

print(tablet)
l = [
    [tablet.probe(row, col).char if tablet.probe(row, col).distance == 0 else '' for col in range(30)]
    for row in range(30)
]

for x in l:
    print(''.join(x))

s = ''.join(''.join(x) for x in l)
print(s)


transmitter = get_component("transmitter")
transmitter.connect("earth")
transmitter.transmit(self.contract.id, s)