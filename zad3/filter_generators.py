import numpy as np
from numpy import convolve

from zad1.Signal import Signal
from zad1.config import SR
from zad3.Window import Window
from zad3.plot_spectrum import plot_spectra


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

    _filter.array[1::2] *= -1
    _filter.name.replace("low", "pass")

    return _filter


def band_pass_filter(length: int, f1: int, f2: int, sr: int = SR, window_type: str = "blackman"):
    _low = low_pass_filter(length, f1, sr, window_type)
    plot_spectra(_low)
    _high = high_pass_filter(length, sr // 2 - f2, sr, window_type)
    plot_spectra(_high)

    band_pass_array = convolve(_low.array, _high.array)

    return Signal(array=band_pass_array,
                  time=np.linspace(0, band_pass_array / sr, num=length),
                  name="(" + window_type + " band pass filter)",
                  sampling_rate=sr,
                  duration=band_pass_array / sr)
