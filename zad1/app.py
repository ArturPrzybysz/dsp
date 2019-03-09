from zad1.signal_analysis import mean_power, variance
from zad1.signal_generators import sinusoidal_signal, gauss_noise, uniform_noise, half_wave_signal, full_wave_signal, \
    rectangular_signal, unit_step_signal, impulse_signal, impulse_noise, rectangular_symmetrical_signal, triangle_wave

from zad1.plot import plot_signal, plot_histogram

# s = gauss_noise(length=3000, mean=10, variance=0.1)
# s = uniform_noise(length=3000, low=-10, high=15)
s = sinusoidal_signal(amp=3, t0=0.3, freq=3.1, duration=1.1)
# s = half_wave_signal(amp=3, t0=0.1, freq=1, duration=3)
# s = full_wave_signal(amp=3, t0=0.2, freq=1, duration=3)
# s = unit_step_signal(amp=1, t0=0, t_s=0.2, duration=2)
# s = impulse_signal(amp=1, t0=0, t_s=1.5, duration=2.0, sampling_rate=50)
# s = impulse_noise(amp=1, t0=0, occurrence_probability=0.1, duration=2.0, sampling_rate=10)
# s = rectangular_signal(amp=1, t0=0.1, k_w=0.4, duration=2.43, T=0.2)
# s = rectangular_symmetrical_signal(amp=1, t0=0, k_w=0.1, duration=2.43, T=2.12)
# s = rectangular_symmetrical_signal(amp=1, t0=0, k_w=0.4, duration=2.43, T=2.12)
# s = triangle_wave(amp=1, t0=0.5, k_w=0.9, duration=2, T=1)
plot_signal(s)
# plot_histogram(s, bins=15)

print(mean_power(s))
print(variance(s))
