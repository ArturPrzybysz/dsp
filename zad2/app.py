from zad1.signal_generators import sinusoidal_signal, gauss_noise, uniform_noise, half_wave_signal, full_wave_signal, \
    rectangular_signal, unit_step_signal, impulse_signal, impulse_noise, rectangular_symmetrical_signal, triangle_wave

from zad1.plot import plot_signals, plot_histogram, plot_signal
from zad2.analytics import analyze_sampling_params
from zad2.quantization import quantization_with_rounding
from zad2.sampling import sample_signal
from zad2.similarity_measures import compare_signals

from zad2.upsampling import sinc_resampling_ideal, sinc_resampling_kernel

target_sr = 250
s_perfect = triangle_wave(amp=41, t0=0, duration=1, sampling_rate=target_sr, T=1, k_w=0.8)
s_to_be_sampled = triangle_wave(amp=41, t0=0, duration=1, sampling_rate=target_sr // 3, T=1, k_w=0.8)

remade = sinc_resampling_kernel(s_to_be_sampled, 2.1, kernel_size=30)

plot_signal(s_perfect, scatter=True)
plot_signal(remade, scatter=True)

plot_signals(s_perfect, remade)

# compare_signals(s_perfect, remade)
