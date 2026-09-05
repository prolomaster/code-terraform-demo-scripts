lock = self.contract.lock
transmitter = get_component('transmitter')

def intercept_multiply(n: int, lock_intercept: list[bool]) -> list[int]:
    return map(lambda b: int(b) * n, lock_intercept)

def test_intercept(n: int) -> list[int]:
    return intercept_multiply(n, lock.intercept([n]*6))

def sum_collapse(matrix: list[list[int]]) -> list[int]:
    return [sum(x) for x in zip(*matrix)]

m = map(
    test_intercept,
    range(1, 101)
)
code = sum_collapse(m)

transmitter.connect('earth')
transmitter.transmit(self.contract.id, code)