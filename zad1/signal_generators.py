import numpy as np

from zad1.Signal import Signal
from zad1.config import SR


def uniform_noise(length: int, low: int, high: int):
    return Signal(array=np.random.uniform(low, high, length),
                  name="uniform_noise")


def gauss_noise(length: int, mean: float, variance: float):
    return Signal(array=np.random.normal(mean, variance, length),
                  name="gaussian_noise")


def sinusoidal_signal(amp, t0, freq, duration, sampling_rate=SR):
    time = np.linspace(t0, duration + t0, num=duration * sampling_rate)
    return Signal(array=amp * np.sin(2 * np.pi * freq * (time - t0)),
                  name="sin(t)",
                  sampling_rate=sampling_rate)


def half_wave_signal(amp, t0, freq, duration, sampling_rate=SR):
    time = np.linspace(0, duration, num=duration * sampling_rate)
    sin_signal = amp * np.sin(2 * np.pi * freq * (time - t0))
    sin_abs = np.abs(sin_signal)
    return Signal(array=sin_signal + sin_abs,
                  name="half_wave(t)",
                  sampling_rate=sampling_rate)


def full_wave_signal(amp, t0, freq, duration, sampling_rate=SR):
    time = np.linspace(0, duration, num=duration * sampling_rate)
    sin_signal = amp * np.sin(2 * np.pi * freq * (time - t0))
    return Signal(array=np.abs(sin_signal),
                  name="half_wave(t)",
                  sampling_rate=sampling_rate)
