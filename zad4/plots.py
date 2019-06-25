import numpy as np
import matplotlib.pyplot as plt

from zad1.Signal import Signal
from zad1.plot import plot_signal


def w1(dataSet, originalSignal):
    walsh_real = Signal(array=np.real(dataSet),
                        name="W1 real",
                        sampling_rate=originalSignal.sampling_rate,
                        time=originalSignal.time,
                        duration=originalSignal.time)

    plot_signal(walsh_real)
    walsh_imaginary = Signal(array=np.imag(dataSet),
                             name="W1 imaginary",
                             sampling_rate=originalSignal.sampling_rate,
                             time=originalSignal.time,
                             duration=originalSignal.time)
    plot_signal(walsh_imaginary)


def w2(dataSet, originalSignal):
    walsh_magnitude = Signal(array=np.absolute(dataSet),
                             name="W2 magnitude",
                             sampling_rate=originalSignal.sampling_rate,
                             time=originalSignal.time,
                             duration=originalSignal.time)

    plot_signal(walsh_magnitude)

    walsh_magnitude = Signal(array=np.angle(dataSet),
                             name="W2 phase",
                             sampling_rate=originalSignal.sampling_rate,
                             time=originalSignal.time,
                             duration=originalSignal.time)

    plot_signal(walsh_magnitude)
