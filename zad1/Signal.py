import numpy as np

np.seterr(divide='ignore', invalid='ignore')


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
                      name="(" + self.name + " + " + s2.name + ")",
                      sampling_rate=self.sampling_rate)

    def subtract(self, s2):
        assert self.length == s2.length
        return Signal(array=self.array - s2.array,
                      name="(" + self.name + " - " + s2.name + ")",
                      sampling_rate=self.sampling_rate)

    def multiply(self, s2):
        assert self.length == s2.length
        return Signal(array=self.array * s2.array,
                      name="(" + self.name + " * " + s2.name + ")",
                      sampling_rate=self.sampling_rate)

    def divide(self, s2):
        assert self.length == s2.length
        array = np.divide(self.array, s2.array)
        normalized_array = np.nan_to_num(array)
        return Signal(array=normalized_array,
                      name="(" + self.name + " / " + s2.name + ")",
                      sampling_rate=self.sampling_rate)

    def append(self, s2):
        return Signal(array=np.append(self.array, s2.array),
                      name="[" + self.name + " then " + s2.name + "]",
                      sampling_rate=self.sampling_rate)
