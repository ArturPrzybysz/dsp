import numpy as np

from zad1.io_.reader import read_wav
from zad1.io_.writer import write_wav
from zad1.plot import plot_signal
from zad3.convolution import convolve, naive_convolve
from zad3.filter_generators import low_pass_filter, high_pass_filter, band_pass_filter
from zad1.signal_generators import *
from zad3.plot_spectrum import plot_spectra

# s1 = read_wav("bohemian_rhapsody.wav")
# s1.array = s1.array[:10 * s1.sampling_rate]
# s1.array /= np.max(np.abs(s1.array), axis=0)
#
# f3 = band_pass_filter(length=3111, f1=500, f2=2000, sr=s1.sampling_rate)
# plot_spectra(f3, mode="real")
# plot_signal(f3)
#
#
# s2 = convolve(s1, f3)
# s2.array /= np.max(np.abs(s2.array), axis=0)
# write_wav(s2)
#
# plot_spectra(s1, mode="real")
# plot_spectra(s2, mode="real")


s1 = sinusoidal_signal(amp=1, freq=40, duration=3)
s1 = s1.add(sinusoidal_signal(amp=1, freq=42, duration=3))
s1 = s1.add(sinusoidal_signal(amp=3, freq=54, duration=3))
s1 = s1.add(sinusoidal_signal(amp=1, freq=65, duration=3))
s1 = s1.add(sinusoidal_signal(amp=4, freq=43, duration=3))
s1 = s1.add(sinusoidal_signal(amp=6, freq=10, duration=3))
s1 = s1.add(sinusoidal_signal(amp=1, freq=12, duration=3))
s1 = s1.add(sinusoidal_signal(amp=0.1, freq=13, duration=3))
s1 = s1.add(sinusoidal_signal(amp=1, freq=14, duration=3))

# plot_spectra(s)

f = high_pass_filter(length=41, f0=20)

s3 = convolve(s1, f)
plot_signal(s1)
plot_signal(s3)
# plot_spectra(s1)
# plot_spectra(s3)
