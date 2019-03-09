import numpy

from zad1.io_.reader import read_wav
from zad1.io_.writer import write_wav
from zad1.signal_analysis import show_stats
from zad1.signal_generators import sinusoidal_signal, gauss_noise, uniform_noise, half_wave_signal, full_wave_signal, \
    rectangular_signal, unit_step_signal, impulse_signal, impulse_noise, rectangular_symmetrical_signal, triangle_wave

from zad1.plot import plot_signal, plot_histogram

sr = 22000
duration = 2

s1 = sinusoidal_signal(amp=3000, freq=440, sampling_rate=sr, duration=duration)
s2 = gauss_noise(length=duration * sr, mean=0, variance=100)

plot_signal(s1, title="sinusoida")
plot_signal(s2, scatter=True, title="gauss")

s3 = s1.add(s2).append(s1).append(s2)

plot_signal(s3)
plot_signal(s3.append(s3))

plot_histogram(s3, title="Histogram sumy sygnałów")

filename = s1.name + "+" + s2.name + ".wav"
write_wav(signal=s3, filename=filename)

s4 = read_wav(filename)
plot_signal(s4)

show_stats(s4)
