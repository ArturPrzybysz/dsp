import matplotlib.pylab as plt
import numpy as np

from zad1.Signal import Signal


def plot_signal(signal: Signal):
    if signal.sampling_rate:
        time = np.linspace(0, signal.length / signal.sampling_rate, num=signal.length)
        plt.xlabel('t [s]')
        plt.ylabel(signal.name)
        plt.tight_layout()
        plt.scatter(time, signal.array)
        plt.show()
    else:
        plt.scatter(signal.array)
        plt.show()
