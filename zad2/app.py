from zad1.io_.reader import read_wav
from zad1.io_.writer import write_wav
from zad1.signal_analysis import show_stats
from zad1.signal_generators import sinusoidal_signal, gauss_noise, uniform_noise, half_wave_signal, full_wave_signal, \
    rectangular_signal, unit_step_signal, impulse_signal, impulse_noise, rectangular_symmetrical_signal, triangle_wave

from zad1.plot import plot_signals, plot_histogram, plot_signal
from zad2.analytics import analyze_sampling_params
from zad2.quantization import quantization_with_rounding
from zad2.sampling import sample_signal
from zad2.similarity_measures import signal_to_noise_ratio, mean_squared_error, peak_signal_to_noise_ratio, \
    compare_signals


from zad2.upsampling import sinc_resampling

s1 = sinusoidal_signal(amp=-21, t0=12, freq=4, duration=2.1, sampling_rate=100)

s3 = sinc_resampling(s1, 3)

plot_signal(s3)
plot_signal(s1)

plot_signals(s1, s3)
# TODO:
#   1. ENOB
#   2. sinc reconstruction
#
#
