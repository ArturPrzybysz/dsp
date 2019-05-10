import numpy as np

from zad1.Signal import Signal
from zad1.config import SR
from zad3.Window import Window


def low_pass_filter(length: int, f0: int, sr: int = SR, window_type: str = "blackman"):
    time = np.linspace(0, length / sr, num=length)
    time = time - time[-1] / 2
    ideal_filter = f0 * np.sinc(2 * f0 * time)
    window = Window(length, window_type)

    filter_array = ideal_filter * window.array
    filter_array /= np.max(np.abs(filter_array), axis=0)

    return Signal(array=filter_array,
                  time=np.linspace(0, length / sr, num=length),
                  name="(" + window_type + " filter)",
                  sampling_rate=sr,
                  duration=length / sr)
