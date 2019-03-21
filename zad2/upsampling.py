import numpy as np
from zad1.Signal import Signal


def sinc_resampling_ideal(signal: Signal, k: float):
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


def sinc_resampling_kernel(signal: Signal, k: float, kernel_size: int):
    duration = signal.time[-1] - signal.time[0]
    new_sr = signal.sampling_rate * k
    interpolated = np.zeros((int(duration * new_sr)))
    time = np.linspace(0, duration, num=interpolated.size)
    time_tick = 1 / signal.sampling_rate

    k_lower, k_upper = _kernel_boundaries(kernel_size)

    for v in signal.array:
        _k_lower = max(k_lower, 0)
        _k_upper = min(k_upper, time.size)

        added = v * np.sinc(time[_k_lower:_k_upper] / time_tick)
        interpolated[_k_lower:_k_upper] = interpolated[_k_lower:_k_upper] + added
        time = time - time_tick
        k_lower += 1
        k_upper += 1

    return Signal(array=interpolated,
                  sampling_rate=new_sr,
                  name="(sinc_upsampled " + signal.name + ")",
                  time=np.linspace(signal.time[0], signal.time[-1], num=time.size))


def _kernel_boundaries(kernel_size: int):
    if kernel_size == 1:
        return 0, 1

    if kernel_size % 2 == 0:
        return int(1 - kernel_size / 2), int(kernel_size / 2)
    else:
        return int(- kernel_size / 2), int(kernel_size / 2)
