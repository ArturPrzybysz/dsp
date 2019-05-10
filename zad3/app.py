from zad1.plot import plot_signal
from zad1.signal_generators import sinusoidal_signal
from zad3.Filter import Filter
from zad3.convolution import convolve, naive_convolve
from zad3.plot_spectrum import plot_spectra

s1 = sinusoidal_signal(amp=3, freq=300, duration=1, sampling_rate=1000, t0=0.3)
s1 = s1.add(sinusoidal_signal(amp=2, freq=100, duration=1, sampling_rate=1000, t0=0.1))
s1 = s1.add(sinusoidal_signal(amp=1, freq=50, duration=1, sampling_rate=1000, t0=0.2))

plot_spectra(s1.array, mode="real")
# f = Filter(3, "blackman")
#
# s2 = convolve(s1, f)
# s3 = naive_convolve(s1, f)
#
# plot_signal(s1, scatter=True)
# plot_signal(s2, scatter=True)
# plot_signal(s3, scatter=True)
