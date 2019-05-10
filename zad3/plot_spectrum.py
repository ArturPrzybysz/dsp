import numpy as np
import matplotlib.pyplot as plt

from zad1.Signal import Signal


def plot_spectra(signal: Signal, mode="real"):
    if mode is "real":
        fft = np.fft.rfft(signal.array)
    elif mode is "full":
        fft = np.fft.fft(signal.array)
    else:
        raise Exception("unsupported value")

    plot_amplitude_spectrum(fft, signal.sampling_rate)
    # plot_phase_spectrum(fft, signal.sampling_rate)


def plot_amplitude_spectrum(fft, sr):
    amplitudes = np.abs(fft)
    plt.plot(np.arange(len(amplitudes)) * sr / (2 * len(amplitudes)), amplitudes)

    plt.xlabel("f [Hz]")
    plt.ylabel("Amplitude")
    plt.show()


def plot_phase_spectrum(fft, sr):
    phases = np.angle(fft)
    # phases = np.unwrap(phases)
    plt.plot(np.arange(len(phases)), phases)
    plt.xlabel("f [Hz]")
    plt.ylabel("Phase [rad]")
    plt.show()
