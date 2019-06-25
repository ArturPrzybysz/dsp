import numpy as np
from timeit import default_timer as timer
from datetime import timedelta
from zad1.signal_generators import sinusoidal_signal
from zad4.dft import dft_naive, FFT
from zad4.imaginary_plots import plot_rez_to_imz

sinx = sinusoidal_signal(amp=1, freq=42, duration=1, sampling_rate=1024)

start = timer()
x = dft_naive(sinx.array)
end = timer()
print("Naive DFT:", timedelta(seconds=end - start))
start = timer()
xxx = FFT(sinx.array)
end = timer()
print("FFT recurrent:", timedelta(seconds=end - start))
start = timer()
xx = np.fft.fft(sinx.array)
end = timer()
print("Numpy FFT:", timedelta(seconds=end - start))

plot_rez_to_imz(x)
plot_rez_to_imz(xx)
plot_rez_to_imz(xxx)
