import numpy as np
from zad1.Signal import Signal


def sinc_resampling(x, s, u):
    if len(x) != len(s):
        raise ValueError('x and s must be the same length')

    # Find the period
    T = s[1] - s[0]

    sincM = np.tile(u, (len(s), 1)) - np.tile(s[:, np.newaxis], (1, len(u)))
    y = np.dot(x, np.sinc(sincM / T))
    return y

    # duration = signal.time[-1] - signal.time[0]
    # new_sr = signal.sampling_rate * k
    # interpolated = np.zeros((int(duration * new_sr)))
    # time = np.linspace(0, duration, num=interpolated.size)
    # time_tick = 1 / signal.sampling_rate
    #
    # for v in signal.array:
    #     interpolated = interpolated + v * np.sinc(time * np.pi)
    #     time = time - time_tick
    #
    # interpolated = duration * np.pi * interpolated / signal.array.size
    #
    # print("interp max", max(interpolated), "original max", max(signal.array))
    #
    # return Signal(array=interpolated,
    #               sampling_rate=new_sr,
    #               name="(sinc_upsampled " + signal.name + ")",
    #               time=np.linspace(signal.time[0], signal.time[0] + duration, num=interpolated.size))
