from zad1.plot import plot_signal
from zad1.signal_generators import sinusoidal_signal
from zad3.Filter import Filter
from zad3.convolution import convolve, naive_convolve

s1 = sinusoidal_signal(amp=1, freq=3, duration=1, sampling_rate=1000)
f = Filter(3, "blackman")

s2 = convolve(s1, f)
s3 = naive_convolve(s1, f)

plot_signal(s1, scatter=True)
plot_signal(s2, scatter=True)
plot_signal(s3, scatter=True)
