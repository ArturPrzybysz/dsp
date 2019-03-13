import numpy as np

from zad1.Signal import Signal
from zad1.config import SR


def uniform_noise(duration, sampling_rate, low: int, high: int):
    return Signal(array=np.random.uniform(low, high, duration * sampling_rate),
                  name="uniform_noise",
                  sampling_rate=sampling_rate)


def gauss_noise(duration, sampling_rate, mean: float, variance: float):
    return Signal(array=np.random.normal(mean, variance, duration * sampling_rate),
                  name="gaussian_noise",
                  sampling_rate=sampling_rate)


def sinusoidal_signal(amp, freq, duration, t0=0, sampling_rate=SR):
    time = np.linspace(t0, t0 + duration, num=duration * sampling_rate)
    array = amp * np.sin(2 * np.pi * freq * time)
    return Signal(array=array,
                  name="sin(t)",
                  freq=freq,
                  sampling_rate=sampling_rate)


def half_wave_signal(amp, freq, duration, t0=0, sampling_rate=SR):
    time = np.linspace(t0, t0 + duration, num=duration * sampling_rate)
    sin_signal = amp * np.sin(2 * np.pi * freq * time)
    sin_abs = np.abs(sin_signal)
    return Signal(array=sin_signal + sin_abs,
                  name="half wave(t)",
                  freq=freq,
                  sampling_rate=sampling_rate)


def full_wave_signal(amp, freq, duration, t0=0, sampling_rate=SR):
    time = np.linspace(0, duration, num=duration * sampling_rate)
    sin_signal = amp * np.sin(2 * np.pi * freq * (time - t0))
    return Signal(array=np.abs(sin_signal),
                  name="full_wave(t)",
                  freq=freq,
                  sampling_rate=sampling_rate)


def unit_step_signal(amp, duration, t_s, t0=0, sampling_rate=SR):
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
                  name="unit_step_signal(t)",
                  sampling_rate=sampling_rate)


def impulse_signal(amp, t_s, duration, t0=0, sampling_rate=SR):
    signal = np.zeros(int(duration * sampling_rate))
    amp_idx = int((t_s - t0) * sampling_rate)
    assert 0 <= amp_idx <= signal.size
    signal[amp_idx] = amp
    return Signal(array=signal,
                  name="impulse_signal",
                  sampling_rate=sampling_rate)


def impulse_noise(amp, occurrence_probability, duration, t0=0, sampling_rate=SR):
    signal = (np.random.rand(int((duration - t0) * sampling_rate)) < occurrence_probability) * amp
    return Signal(array=signal,
                  name="impulse_noise",
                  sampling_rate=sampling_rate)


def rectangular_signal(amp, T, duration, k_w, t0=0, sampling_rate=SR):
    single_rectangle_signal = np.zeros(int(sampling_rate * T))
    single_rectangle_signal[0:int(T * k_w * sampling_rate)] = amp

    repetition_count = int(duration / T) + 1
    signal = np.tile(single_rectangle_signal, repetition_count)

    t = t0 % T
    signal = signal[int(t * sampling_rate):int((t + duration) * sampling_rate)]

    return Signal(array=signal,
                  name="rectangular_signal(t)",
                  sampling_rate=sampling_rate)


def rectangular_symmetrical_signal(amp, T, duration, k_w, t0=0, sampling_rate=SR):
    single_rectangle_signal = np.ones(int(sampling_rate * T)) * -amp
    single_rectangle_signal[0:int(T * k_w * sampling_rate)] = amp

    repetition_count = int(duration / T) + 1
    signal = np.tile(single_rectangle_signal, repetition_count)

    t = t0 % T
    signal = signal[int(t * sampling_rate):int((t + duration) * sampling_rate)]

    return Signal(array=signal,
                  name="rectangular_symmetrical_signal(t)",
                  sampling_rate=sampling_rate)


def triangle_wave(amp, T, duration, k_w, t0=0, sampling_rate=SR):
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
                  name="triangle_wave_signal(t)",
                  sampling_rate=sampling_rate)
