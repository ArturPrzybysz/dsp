import numpy as np

from zad1.Signal import Signal


def _t2_from_freq(signal):
    T = 1 / signal.freq
    samples_in_period = T * signal.sampling_rate
    return int(signal.length - signal.length % samples_in_period)


def _interval(signal, t1, t2, use_freq):
    if use_freq:
        assert signal.freq is not None
        return 0, _t2_from_freq(signal)
    elif t2 is not None:
        return t1, t2
    else:
        return t1, signal.length


def mean(signal: Signal, t1=0, t2=None, use_freq=False):
    t1, t2 = _interval(signal, t1, t2, use_freq)
    return np.mean(signal.array[t1:t2])


def mean_abs(signal: Signal, t1=0, t2=None, use_freq=False):
    t1, t2 = _interval(signal, t1, t2, use_freq)
    return np.mean(np.abs(signal.array[t1:t2]))


def mean_power(signal: Signal, t1=0, t2=None, use_freq=False):
    t1, t2 = _interval(signal, t1, t2, use_freq)
    return np.mean(signal.array[t1:t2] ** 2)


def variance(signal: Signal, t1=0, t2=None, use_freq=False):
    t1, t2 = _interval(signal, t1, t2, use_freq)
    return np.var(signal.array[t1:t2])


# wartość skuteczna
def root_mean_square(signal: Signal, t1=0, t2=None, use_freq=False):
    t1, t2 = _interval(signal, t1, t2, use_freq)
    return np.sqrt(mean_power(signal, t1, t2))
