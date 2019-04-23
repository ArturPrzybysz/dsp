from zad1.Signal import Signal
import numpy as np

from zad1.signal_analysis import mean_power


def compare_signals(pure_signal: Signal, noisy_signal: Signal):
    print("Mean squared error:", np.round(mean_squared_error(pure_signal, noisy_signal), 3))
    print("Signal to noise ratio:", np.round(signal_to_noise_ratio(pure_signal, noisy_signal), 3))
    print("Peak signal to noise ratio:", np.round(peak_signal_to_noise_ratio(pure_signal, noisy_signal), 3))
    print("Max difference:", np.round(max_difference(pure_signal, noisy_signal), 3))


def mean_squared_error(s1: Signal, s2: Signal):
    return np.mean(np.power(s1.array - s2.array, 2))


def signal_to_noise_ratio(pure_signal: Signal, noisy_signal: Signal):
    noise = pure_signal.array - noisy_signal.array

    p1 = mean_power(pure_signal)
    p2 = mean_power(Signal(noise, pure_signal.time, "", pure_signal.sampling_rate, duration=pure_signal.duration))
    return p1 / p2


def effective_number_of_bytes(pure_signal: Signal, noisy_signal: Signal):
    snr = signal_to_noise_ratio(pure_signal, noisy_signal)
    decibel_to_bits = 6.02
    quantization_error = 1.76
    return (snr - quantization_error) / decibel_to_bits


def peak_signal_to_noise_ratio(pure_signal: Signal, noisy_signal: Signal):
    mse = mean_squared_error(pure_signal, noisy_signal)
    psnr = 10 * np.log10((np.max(pure_signal.array) ** 2) / mse)
    return psnr


def max_difference(s1: Signal, s2: Signal):
    return np.max(np.abs(s1.array - s2.array))
