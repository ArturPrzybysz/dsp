import numpy as np

from zad1.Signal import Signal
from zad1.plot import plot_signal


def w1(data_set, original_signal):
    walsh_real = Signal(array=np.real(data_set),
                        name="W1 real",
                        sampling_rate=original_signal.sampling_rate,
                        time=original_signal.time,
                        duration=original_signal.time)

    plot_signal(walsh_real)
    walsh_imaginary = Signal(array=np.imag(data_set),
                             name="W1 imaginary",
                             sampling_rate=original_signal.sampling_rate,
                             time=original_signal.time,
                             duration=original_signal.time)
    plot_signal(walsh_imaginary)


def w2(data_set, original_signal):
    walsh_magnitude = Signal(array=np.absolute(data_set),
                             name="W2 magnitude",
                             sampling_rate=original_signal.sampling_rate,
                             time=original_signal.time,
                             duration=original_signal.time)

    plot_signal(walsh_magnitude)

    walsh_magnitude = Signal(array=np.angle(data_set),
                             name="W2 phase",
                             sampling_rate=original_signal.sampling_rate,
                             time=original_signal.time,
                             duration=original_signal.time)
    plot_signal(walsh_magnitude)
