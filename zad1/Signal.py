import numpy as np


class Signal:
    array: np.array
    sampling_rate: int
    name: str
    length: int

    def __init__(self, array: np.array, name: str, sampling_rate=None):
        self.array = array
        self.name = name
        self.length = array.size
        self.sampling_rate = sampling_rate
