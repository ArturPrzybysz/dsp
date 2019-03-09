from scipy.io.wavfile import write

from zad1.io_.reader import read_wav
from zad1.io_.writer import write_wav
from zad1.signal_analysis import mean_power, variance
from zad1.signal_generators import sinusoidal_signal, gauss_noise, uniform_noise, half_wave_signal, full_wave_signal, \
    rectangular_signal, unit_step_signal, impulse_signal, impulse_noise, rectangular_symmetrical_signal, triangle_wave

from zad1.plot import plot_signal, plot_histogram

# s = gauss_noise(length=3000, mean=10, variance=0.1)
# s = uniform_noise(length=3000, low=-10, high=15)
# s1 = sinusoidal_signal(amp=3000, t0=0, freq=35, duration=5, sampling_rate=10000)

s1 = rectangular_symmetrical_signal(amp=3000, t0=0, T=1 / 440, k_w=0.25, duration=5, sampling_rate=10000)
# s = full_wave_signal(amp=3, t0=0.2, freq=1, duration=3)
# s = unit_step_signal(amp=1, t0=0, t_s=0.2, duration=2)
# s = impulse_signal(amp=1, t0=0, t_s=1.5, duration=2.0, sampling_rate=50)
# s = impulse_noise(amp=1, t0=0, occurrence_probability=0.1, duration=2.0, sampling_rate=10)
# s = rectangular_signal(amp=1, t0=0.1, k_w=0.4, duration=2.43, T=0.2)
# s = rectangular_symmetrical_signal(amp=1, t0=0, k_w=0.1, duration=2.43, T=2.12)
# s = rectangular_symmetrical_signal(amp=1, t0=0, k_w=0.4, duration=2.43, T=2.12)
# s = triangle_wave(amp=1, t0=0.5, k_w=0.9, duration=2, T=1)
plot_signal(s1)
# plot_signal(s1.add(s2))
# plot_signal(s1.multiply(s2))
# plot_signal(s2.divide(s2))
# plot_signal(s1.subtract(s2))
# plot_histogram(s, bins=15)

write_wav(signal=s1, filename="half.wav")
s3 = read_wav("half.wav")
