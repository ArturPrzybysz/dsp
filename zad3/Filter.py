import numpy as np
from numpy import cos, pi


class Filter:
    array: np.array
    name: str
    length: int

    def __init__(self, length: int, filter_type: str):
        assert length > 0

        time = np.linspace(0, 1, num=length)

        if filter_type is "blackman":
            self.array = 0.42 - 0.5 * cos(2 * pi * time) + 0.08 * cos(4 * pi * time)
        elif filter_type is "hamming":
            self.array = 0.53836 - 0.46164 * cos(2 * pi * time)
        elif filter_type is "hanning":
            self.array = 0.5 - 0.5 * cos(2 * pi * time)
        else:
            raise Exception("unsupported filter_type")

        self.length = length
        self.name = filter_type
