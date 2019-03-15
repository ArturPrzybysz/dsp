from zad1.io_.reader import read_wav
from zad1.io_.writer import write_wav
from zad1.signal_analysis import show_stats
from zad1.signal_generators import sinusoidal_signal, gauss_noise, uniform_noise, half_wave_signal, full_wave_signal, \
    rectangular_signal, unit_step_signal, impulse_signal, impulse_noise, rectangular_symmetrical_signal, triangle_wave

from zad1.plot import plot_signals, plot_histogram
from zad2.quantization import quantization_with_rounding
from zad2.sampling import sample_signal
from zad2.similarity_measures import signal_to_noise_ratio, mean_squared_error

s1 = sinusoidal_signal(amp=10, freq=2, duration=1.01, sampling_rate=20000)

s2 = quantization_with_rounding(s1, bins=8)

plot_signals(s1, s2)

print(signal_to_noise_ratio(s1, s2))
print(mean_squared_error(s1, s2))
