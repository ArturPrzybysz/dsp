import numpy as np


# TODO: consider adding time field?

class Signal:
    array: np.array
    sampling_rate: int
    name: str
    length: int
    freq: float

    def __init__(self, array: np.array, name: str, sampling_rate=None, freq=None):
        self.array = array
        self.name = name
        self.length = array.size
        self.sampling_rate = sampling_rate
        self.freq = freq

    def add(self, s2):
        assert self.length == s2.length
        return Signal(array=self.array + s2.array,
                      name="(" + self.name + " + " + s2.name + ")"
                      )
