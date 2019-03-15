from zad1.Signal import Signal
import numpy as np

from zad1.signal_analysis import mean_power


def mean_squared_error(s1: Signal, s2: Signal):
    return np.mean(np.power(s1.array - s2.array, 2))


def signal_to_noise_ratio(pure_signal: Signal, noisy_signal: Signal):
    noise = pure_signal.array - noisy_signal.array

    p1 = mean_power(pure_signal)
    p2 = mean_power(Signal(noise, pure_signal.time, "", pure_signal.sampling_rate))
    return p1 / p2
