import numpy as np

from zad1.Signal import Signal


def convolve(s1: Signal, s2: Signal):
    array = np.convolve(s1.array, s2.array)
    duration = len(array) / s1.sampling_rate
    time = np.linspace(s1.time[0], s1.time[0] + duration, num=len(array))
    return Signal(array=array,
                  time=time,
                  name="convolved(" + s1.name + " with " + s2.name + ")",
                  sampling_rate=s1.sampling_rate,
                  duration=duration)


def naive_convolve(s1: Signal, s2: Signal):
    convolution_matrix = _convolution_matrix(s1.array, s2.array)
    array = np.dot(convolution_matrix, s1.array)
    duration = len(array) / s1.sampling_rate
    time = np.linspace(s1.time[0], s1.time[0] + duration, num=len(array))
    return Signal(array=array,
                  time=time,
                  name="convolved(" + s1.name + " with " + s2.name + ")",
                  sampling_rate=s1.sampling_rate,
                  duration=duration)


def _convolution_matrix(signal_array: np.array, filter_array: np.array):
    N = len(signal_array)
    M = len(filter_array)
    matrix = np.zeros((N + M - 1, N))

    flipped_filter = np.flip(filter_array)
    for idx, value in np.ndenumerate(flipped_filter):
        for i in range(N):
            matrix[i + idx[0], i] = value

    return matrix
