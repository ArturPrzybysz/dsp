import numpy as np

np.seterr(divide='ignore', invalid='ignore')


class Signal:
    array: np.array
    time: np.array
    sampling_rate: int
    name: str
    length: int
    freq: float

    def __init__(self, array: np.array, time: np.array, name: str, sampling_rate, freq=None):
        self.array = array
        self.name = name
        self.length = array.size
        self.sampling_rate = sampling_rate
        self.freq = freq
        self.time = time

    def add(self, s2):
        assert self.length == s2.length
        return Signal(array=self.array + s2.array,
                      name="(" + self.name + " + " + s2.name + ")",
                      sampling_rate=self.sampling_rate,
                      time=self.time)

    def subtract(self, s2):
        assert self.length == s2.length
        return Signal(array=self.array - s2.array,
                      name="(" + self.name + " - " + s2.name + ")",
                      sampling_rate=self.sampling_rate,
                      time=self.time)

    def multiply(self, s2):
        assert self.length == s2.length
        return Signal(array=self.array * s2.array,
                      name="(" + self.name + " * " + s2.name + ")",
                      sampling_rate=self.sampling_rate,
                      time=self.time)

    def divide(self, s2):
        assert self.length == s2.length
        array = np.divide(self.array, s2.array)
        normalized_array = np.nan_to_num(array)
        return Signal(array=normalized_array,
                      name="(" + self.name + " / " + s2.name + ")",
                      sampling_rate=self.sampling_rate,
                      time=self.time)

    def append(self, s2):
        time2 = s2.time + self.time[-1] + 1 / s2.sampling_rate
        new_time = np.append(self.time, time2)
        return Signal(array=np.append(self.array, s2.array),
                      name="[" + self.name + " then " + s2.name + "]",
                      sampling_rate=self.sampling_rate,
                      time=new_time)
