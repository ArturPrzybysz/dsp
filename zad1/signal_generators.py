import numpy as np

from zad1.Signal import Signal
from zad1.config import SR


def uniform_noise(length: int, low: int, high: int):
    return Signal(array=np.random.uniform(low, high, length),
                  name="uniform_noise")


def gauss_noise(length: int, mean: float, variance: float):
    return Signal(array=np.random.normal(mean, variance, length),
                  name="gaussian_noise")


def sinusoidal_signal(amp, t0, freq, duration, sampling_rate=SR):
    time = np.linspace(t0, duration + t0, num=duration * sampling_rate)
    return Signal(array=amp * np.sin(2 * np.pi * freq * (time - t0)),
                  name="sin(t)",
                  sampling_rate=sampling_rate)


def half_wave_signal(amp, t0, freq, duration, sampling_rate=SR):
    time = np.linspace(0, duration, num=duration * sampling_rate)
    sin_signal = amp * np.sin(2 * np.pi * freq * (time - t0))
    sin_abs = np.abs(sin_signal)
    return Signal(array=sin_signal + sin_abs,
                  name="half_wave(t)",
                  sampling_rate=sampling_rate)


def full_wave_signal(amp, t0, freq, duration, sampling_rate=SR):
    time = np.linspace(0, duration, num=duration * sampling_rate)
    sin_signal = amp * np.sin(2 * np.pi * freq * (time - t0))
    return Signal(array=np.abs(sin_signal),
                  name="half_wave(t)",
                  sampling_rate=sampling_rate)


def unit_step_signal(amp, t0, duration, t_s, sampling_rate=SR):
    time = np.linspace(t0, duration + t0, num=duration * sampling_rate)

    def step_function(t):
        if t > t_s:
            return amp
        elif t == t_s:
            return amp / 2
        else:
            return 0

    step_function_vectorized = np.vectorize(step_function)
    return Signal(array=step_function_vectorized(time),
                  name="unit step signal(t)",
                  sampling_rate=sampling_rate)


def impulse_signal(amp, t0, t_s, duration, sampling_rate=SR):
    signal = np.zeros(int(duration * sampling_rate))
    amp_idx = int((t_s - t0) * sampling_rate)
    assert 0 <= amp_idx <= signal.size
    signal[amp_idx] = amp
    return Signal(array=signal,
                  name="impulse signal",
                  sampling_rate=sampling_rate)


def impulse_noise(amp, t0, occurrence_probability, duration, sampling_rate=SR):
    signal = (np.random.rand(int((duration - t0) * sampling_rate)) < occurrence_probability) * amp
    return Signal(array=signal,
                  name="impulse noise",
                  sampling_rate=sampling_rate)


def rectangular_signal(amp, T, t0, duration, k_w, sampling_rate=SR):
    single_rectangle_signal = np.zeros(int(sampling_rate * T))
    single_rectangle_signal[0:int(T * k_w * sampling_rate)] = amp

    repetition_count = int(duration / T) + 1
    signal = np.tile(single_rectangle_signal, repetition_count)

    t = t0 % T
    signal = signal[int(t * sampling_rate):int((t + duration) * sampling_rate)]

    return Signal(array=signal,
                  name="rectangular signal(t)",
                  sampling_rate=sampling_rate)


def rectangular_symmetrical_signal(amp, T, t0, duration, k_w, sampling_rate=SR):
    single_rectangle_signal = np.ones(int(sampling_rate * T)) * -amp
    single_rectangle_signal[0:int(T * k_w * sampling_rate)] = amp

    repetition_count = int(duration / T) + 1
    signal = np.tile(single_rectangle_signal, repetition_count)

    t = t0 % T
    signal = signal[int(t * sampling_rate):int((t + duration) * sampling_rate)]

    return Signal(array=signal,
                  name="rectangular symmetrical signal(t)",
                  sampling_rate=sampling_rate)


def triangle_wave(amp, T, t0, duration, k_w, sampling_rate=SR):
    time = np.linspace(0, T, num=T * sampling_rate)

    def triangle_signal(t):
        if t < T * k_w:
            return t * amp / (T * k_w)
        else:
            return t * amp / ((k_w - 1) * T) - amp / (k_w - 1)

    vectorized_tr_signal = np.vectorize(triangle_signal)
    single_triangle_wave = vectorized_tr_signal(time)
    repetition_count = int(duration / T) + 1
    signal = np.tile(single_triangle_wave, repetition_count)

    t = t0 % T
    signal = signal[int(t * sampling_rate):int((t + duration) * sampling_rate)]

    return Signal(array=signal,
                  name="triangle wave signal(t)",
                  sampling_rate=sampling_rate)

# y = ax + b

# 0 = a*T + b
# amp = a * T*k_w + b
# b = -a*T
# a = (amp - b) / (T * k_w)
# a = (amp -a*T) / T * k_w
# a
#
#
