import matplotlib.pylab as plt
import numpy as np

from zad1.Signal import Signal


def plot_signal(signal: Signal, scatter=False):
    if signal.sampling_rate:
        time = np.linspace(0, signal.length / signal.sampling_rate, num=signal.length)
        plt.xlabel('t [s]')
        plt.ylabel(signal.name)
        plt.tight_layout()
        if scatter:
            plt.scatter(time, signal.array)
        else:
            plt.plot(time, signal.array)
        plt.show()
    else:
        if scatter:
            plt.scatter(signal.array)
        else:
            plt.plot(signal.array)
        plt.show()


def plot_histogram(signal: Signal, bins=50):
    plt.hist(signal.array, bins=bins)
    plt.xlabel('t [s]')
    plt.ylabel(signal.name)
    plt.show()
