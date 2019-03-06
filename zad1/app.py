from zad1.signal_generators import sinusoidal_signal, gauss_noise, uniform_noise, half_wave_signal, full_wave_signal

from zad1.plot import plot_signal

s = gauss_noise(length=1500, mean=10, variance=0.1)
# s = uniform_noise(length=15, low=-10, high=15)
s = sinusoidal_signal(amp=3, t0=0, freq=1, duration=1)
# s = half_wave_signal(amp=3, t0=0, freq=1, duration=3)
s = full_wave_signal(amp=3, t0=0, freq=1, duration=3)

plot_signal(s)
