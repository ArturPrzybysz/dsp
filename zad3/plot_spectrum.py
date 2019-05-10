import numpy as np
import matplotlib.pyplot as plt


def plot_spectra(array: np.array, mode="real"):
    if mode is "real":
        fft = np.fft.rfft(array)
    elif mode is "full":
        fft = np.fft.fft(array)
    else:
        raise Exception("unsupported value")

    plot_amplitude_spectrum(fft)
    plot_phase_spectrum(fft)


def plot_amplitude_spectrum(fft):
    amplitudes = np.abs(fft)
    amplitudes = amplitudes / len(amplitudes)
    plt.plot(np.arange(len(amplitudes)), amplitudes)

    plt.xlabel("f [Hz]")
    plt.ylabel("Amplitude")
    plt.show()


def plot_phase_spectrum(fft):
    phases = np.angle(fft)
    # phases = np.unwrap(phases)
    plt.plot(np.arange(len(phases)), phases)
    plt.xlabel("f [Hz]")
    plt.ylabel("Phase [rad]")
    plt.show()
