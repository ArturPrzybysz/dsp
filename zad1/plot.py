import matplotlib.pylab as plt
import numpy as np

from zad1.Signal import Signal


def plot_signal(signal: Signal, scatter=False, title=None):
    plt.title = title
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
        plt.plot(signal.array)
    plt.show()


def plot_histogram(signal: Signal, bins=50, title=None):
    plt.hist(signal.array, bins=bins)
    plt.title = title
    plt.xlabel("value")
    plt.ylabel("occurrences")
    plt.show()
