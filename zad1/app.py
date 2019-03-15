from zad1.io_.reader import read_wav
from zad1.io_.writer import write_wav
from zad1.signal_analysis import show_stats
from zad1.signal_generators import sinusoidal_signal, gauss_noise, uniform_noise, half_wave_signal, full_wave_signal, \
    rectangular_signal, unit_step_signal, impulse_signal, impulse_noise, rectangular_symmetrical_signal, triangle_wave

from zad1.plot import plot_signal, plot_histogram

sr = 23215
duration = 2.11

# s1 = uniform_noise(duration=duration, sampling_rate=sr, low=0, high=50)
s1 = impulse_signal(amp=30, sampling_rate=sr, duration=duration, t_s=1)
s2 = gauss_noise(duration=duration, sampling_rate=sr, mean=0, variance=15)

plot_signal(s1, title="sinusoida")
plot_signal(s2, scatter=True, title="gauss")

s3 = s2.append(s1)

# print(s1.time)
print(s1.time.size)
# print(s2.time)
print(s2.time.size)
# print(s3.time)
print(s3.time.size)

plot_signal(s3)

plot_histogram(s3, title="Histogram sumy sygnałów")

filename = s1.name + "+" + s2.name + ".wav"
write_wav(signal=s3, filename=filename)

s4 = read_wav(filename)
plot_signal(s4)

show_stats(s4)
