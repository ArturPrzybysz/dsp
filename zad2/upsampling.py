import numpy as np
from zad1.Signal import Signal
from matplotlib import pyplot as plt


def sinc_resampling(signal: Signal, k: float):
    duration = signal.time[-1] - signal.time[0]
    new_sr = signal.sampling_rate * k
    interpolated = np.zeros((int(duration * new_sr)))
    time = np.linspace(0, duration, num=interpolated.size)
    time_tick = 1 / signal.sampling_rate

    for v in signal.array:
        added = v * np.sinc(time / time_tick)
        # plt.plot(time, added)
        # plt.scatter(signal.time, np.ones_like(signal.time))
        # plt.show()

        interpolated = interpolated + added
        time = time - time_tick

    print("interp max", max(interpolated), "original max", max(signal.array))

    return Signal(array=interpolated,
                  sampling_rate=new_sr,
                  name="(sinc_upsampled " + signal.name + ")",
                  time=np.linspace(signal.time[0], signal.time[0] + duration, num=interpolated.size))
