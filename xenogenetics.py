transmitter = get_component('transmitter')

transmitter.connect('earth')

transmitter.transmit(
    self.contract.id,
    [x for x in self.contract.samples if x not in self.contract.earth_ref]
)