import matplotlib.pylab as plt
from zad1.Signal import Signal

plt.tight_layout()


def plot_signal(signal: Signal, scatter=False, title=None):
    plt.title = title
    plt.xlabel('t [s]')
    plt.ylabel(signal.name)
    if scatter:
        plt.scatter(signal.time, signal.array, color='r', s=1.2)
    else:
        plt.plot(signal.time, signal.array)

    plt.show()


def plot_histogram(signal: Signal, bins=50, title=None):
    plt.hist(signal.array, bins=bins)
    plt.title = title
    plt.xlabel("value")
    plt.ylabel("occurrences")
    plt.show()


def plot_signals(analog: Signal, digital: Signal, title=None):
    plt.title = title
    plt.xlabel('t [s]')
    plt.ylabel('y(t)')

    plt.plot(digital.time, digital.array, color='r')
    plt.plot(analog.time, analog.array, alpha=0.7)

    plt.show()
