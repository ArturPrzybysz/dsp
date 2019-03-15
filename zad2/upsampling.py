import numpy as np

from zad1.Signal import Signal


def sinc_upsampling(signal: Signal, k: float):
    assert k >= 1
    interpolated = np.zeros(int(signal.length * k))
