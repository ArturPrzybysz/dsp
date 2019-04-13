import numpy as np
from zad1.Signal import Signal


def sinc_resampling_ideal(signal: Signal, k: float):
    new_sr = signal.sampling_rate * k
    interpolated = np.zeros((int(signal.duration * new_sr)))
    time = np.linspace(0, signal.duration, num=interpolated.size) * signal.sampling_rate

    for v in signal.array:
        added = v * np.sinc(time)
        interpolated = interpolated + added
        time = time - 1

    return Signal(array=interpolated,
                  sampling_rate=new_sr,
                  name="(sinc_upsampled " + signal.name + ")",
                  time=np.linspace(signal.time[0], signal.time[-1], num=time.size),
                  duration=signal.duration)


def sinc_resampling_kernel(signal: Signal, k: float, kernel_size: int):
    k_lower, k_upper = _kernel_boundaries(kernel_size)
    new_sr = signal.sampling_rate * k
    interpolated = np.zeros((int(signal.duration * new_sr)))
    time = np.linspace(0, signal.duration, num=interpolated.size) * signal.sampling_rate

    for v in signal.array:
        _k_lower = max(k_lower, 0)
        _k_upper = min(k_upper, time.size)

        added = v * np.sinc(time)
        interpolated[_k_lower: _k_upper] += added[_k_lower: _k_upper]

        time = time - 1
        k_lower += 1
        k_upper += 1

    return Signal(array=interpolated,
                  sampling_rate=new_sr,
                  name="(sinc_upsampled " + signal.name + ")",
                  time=np.linspace(signal.time[0], signal.time[-1], num=interpolated.size),
                  duration=signal.duration)


def _kernel_boundaries(kernel_size: int):
    if kernel_size % 2 == 0:
        return int(1 - kernel_size / 2), int(kernel_size / 2) + 1
    else:
        return int(- kernel_size / 2), int(kernel_size / 2) + 1
