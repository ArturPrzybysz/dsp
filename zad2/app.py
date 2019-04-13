from zad1.signal_generators import sinusoidal_signal, gauss_noise, uniform_noise, half_wave_signal, full_wave_signal, \
    rectangular_signal, unit_step_signal, impulse_signal, impulse_noise, rectangular_symmetrical_signal, triangle_wave

from zad1.plot import plot_signals, plot_histogram, plot_signal
from zad2.analytics import analyze_sampling_params
from zad2.quantization import quantization_with_rounding
from zad2.sampling import sample_signal
from zad2.similarity_measures import compare_signals

from zad2.upsampling import sinc_resampling_ideal, sinc_resampling_kernel

s_perfect = sinusoidal_signal(amp=41, t0=0, freq=1, duration=1, sampling_rate=200)
s_to_be_sampled = sinusoidal_signal(amp=41, t0=0, freq=1, duration=1, sampling_rate=100)

remade = sinc_resampling_kernel(s_to_be_sampled, 2, 90)

plot_signal(s_perfect, scatter=True)
plot_signal(remade, scatter=True)

plot_signals(s_perfect, remade)

compare_signals(s_perfect, remade)

# TODO:
#   1. ENOB
