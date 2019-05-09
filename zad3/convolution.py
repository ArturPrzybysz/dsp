import numpy as np

from zad1.Signal import Signal
from zad3.Filter import Filter


def convolve(s: Signal, f: Filter):
    array = np.convolve(s.array, f.array)
    duration = len(array) / s.sampling_rate
    time = np.linspace(s.time[0], s.time[0] + duration, num=len(array))
    return Signal(array=array,
                  time=time,
                  name="convolved(" + s.name + " with " + f.name + ")",
                  sampling_rate=s.sampling_rate,
                  duration=duration)


def naive_convolve(s: Signal, f: Filter):
    convolution_matrix = _convolution_matrix(s.array, f.array)
    array = np.dot(convolution_matrix, s.array)
    duration = len(array) / s.sampling_rate
    time = np.linspace(s.time[0], s.time[0] + duration, num=len(array))
    return Signal(array=array,
                  time=time,
                  name="convolved(" + s.name + " with " + f.name + ")",
                  sampling_rate=s.sampling_rate,
                  duration=duration)


def _convolution_matrix(signal_array: np.array, filter_array: np.array):
    N = len(signal_array)
    M = len(filter_array)
    matrix = np.zeros(( N + M - 1, N))

    flipped_filter = np.flip(filter_array)
    for idx, value in np.ndenumerate(flipped_filter):
        for i in range(N):
            matrix[i + idx[0], i] = value

    return matrix
