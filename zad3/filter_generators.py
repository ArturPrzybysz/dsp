import numpy as np

from zad1.Signal import Signal
from config import SR
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
                  name="(" + window_type + " low pass filter)",
                  sampling_rate=sr,
                  duration=length / sr)


def high_pass_filter(length: int, f0: int, sr: int = SR, window_type: str = "blackman"):
    _filter = low_pass_filter(length, sr // 2 - f0, sr, window_type)

    _filter.array[::2] *= -1
    _filter.name.replace("low", "pass")

    return _filter


def band_pass_filter(length: int, f1: int, f2: int, sr: int = SR, window_type: str = "blackman"):
    assert f1 <= f2

    low_filter = low_pass_filter(length=length // 2 + 1, f0=f2, sr=sr, window_type="none")
    high_filter = high_pass_filter(length=length // 2 + 1, f0=f1, sr=sr, window_type="none")

    band_filter = np.convolve(low_filter.array, high_filter.array)
    window = Window(length=len(band_filter), window_type=window_type)

    return Signal(array=band_filter * window.array,
                  time=np.linspace(0, length / sr, num=length),
                  name="(" + window_type + " band pass filter)",
                  sampling_rate=sr,
                  duration=length / sr)
