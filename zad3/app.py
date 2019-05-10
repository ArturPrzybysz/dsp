import numpy as np

from zad1.signal_generators import sinusoidal_signal, gauss_noise
from zad3.convolution import convolve, naive_convolve
from zad3.filter_generators import low_pass_filter
from zad3.plot_spectrum import plot_spectra

s1 = gauss_noise(duration=1, mean=0, variance=5)

plot_spectra(s1)
f = low_pass_filter(length=101, f0=125)
# plot_signal(f, scatter=False)
plot_spectra(f)

s2 = convolve(s1, f)
plot_spectra(s2)

# s2 = convolve(s1, f)
# s3 = naive_convolve(s1, f)
#
# plot_signal(s1, scatter=True)
# plot_signal(s2, scatter=True)
# plot_signal(s3, scatter=True)
