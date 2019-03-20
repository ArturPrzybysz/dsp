import numpy as np
from zad1.Signal import Signal


def sinc_resampling(signal: Signal, k: float):
    duration = signal.time[-1] - signal.time[0]
    new_sr = signal.sampling_rate * k
    interpolated = np.zeros((int(duration * new_sr)))
    time = np.linspace(0, duration, num=interpolated.size)
    time_tick = 1 / signal.sampling_rate

    for v in signal.array:
        added = v * np.sinc(time / time_tick)
        interpolated = interpolated + added
        time = time - time_tick

    return Signal(array=interpolated,
                  sampling_rate=new_sr,
                  name="(sinc_upsampled " + signal.name + ")",
                  time=np.linspace(signal.time[0], signal.time[-1], num=time.size))
