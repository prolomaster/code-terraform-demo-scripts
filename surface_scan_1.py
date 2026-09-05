grid = [
    a + str(i) 
    for a in 'ABCDEFGH'
    for i in range(1, 25)
]
for c in grid:
    self.scan(c)

self.get_scanned()