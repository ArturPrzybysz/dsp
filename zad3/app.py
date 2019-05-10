import numpy as np

from zad1.io_.reader import read_wav
from zad1.io_.writer import write_wav
from zad1.signal_generators import sinusoidal_signal, gauss_noise
from zad2.upsampling import sinc_resampling_ideal
from zad3.convolution import convolve, naive_convolve
from zad3.filter_generators import low_pass_filter, high_pass_filter, band_pass_filter
from zad3.plot_spectrum import plot_spectra

s1 = gauss_noise(duration=5, mean=5, variance=10)
f3 = band_pass_filter(length=101, f1=100, f2=200)
plot_spectra(f3, mode="full")
