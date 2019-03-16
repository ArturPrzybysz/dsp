import numpy as np
from zad1.Signal import Signal


def sinc_resampling(signal: Signal, k: float):
    duration = signal.time[-1]
    new_sr = signal.sampling_rate * k
    interpolated = np.zeros((int(duration * new_sr)))
    time = np.linspace(0, duration, num=interpolated.size)
    time_tick = 1 / signal.sampling_rate

    for v in signal.array:
        interpolated = interpolated + v * np.sinc(time * np.pi)
        time = time - time_tick
    # TODO: resize interpolated
    return Signal(array=interpolated,
                  sampling_rate=new_sr,
                  name="(sinc_upsampled " + signal.name + ")",
                  time=np.linspace(0, duration, num=interpolated.size))
