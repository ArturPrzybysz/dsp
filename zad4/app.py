import numpy as np
from timeit import default_timer as timer
from datetime import timedelta
from zad1.signal_generators import sinusoidal_signal

from zad4.dft import dft_naive, FFT
from zad4.imaginary_plots import plot_rez_to_imz

from zad1.Signal import Signal
from zad4.plots import w1, w2
from zad4.walshHadamard import walsh_hadamard, fast_walsh_hadamard, reverse_walsh_hadamard

originalSignal = sinusoidal_signal(amp=1, freq=3, duration=8, sampling_rate=128)

# DFT NAIVE PART
# start = timer()
# dft1 = dft_naive(originalSignal.array)
# end = timer()
# print("Naive DFT:", timedelta(seconds=end - start))
# w1(dft1, originalSignal)
# w2(dft1, originalSignal)

# FFT RECURRENT PART
# start = timer()
# fft1 = FFT(originalSignal.array)
# end = timer()
# print("FFT recurrent:", timedelta(seconds=end - start))
# w1(fft1, originalSignal)
# w2(fft1, originalSignal)

# FFT NUMPY PART
start = timer()
fft2 = np.fft.fft(originalSignal.array)
end = timer()
print("Numpy FFT:", timedelta(seconds=end - start))
w1(fft2, originalSignal)
w2(fft2, originalSignal)

# plot_rez_to_imz(x)
# plot_rez_to_imz(xx)
# plot_rez_to_imz(xxx)

# WALSH NORMAL PART
# plot_signal(sinx)
# start = timer()
# w = walsh_hadamard(sinx.array)
# end = timer()
# print("Normal Walsh:", timedelta(seconds=end - start))
# w1(w, sinx)
# w2(w, sinx)
# reversed = Signal(array=reverse_walsh_hadamard(w),
#                         name="reversed",
#                         sampling_rate=sinx.sampling_rate,
#                         time=sinx.time,
#                         duration=sinx.time)
# plot_signal(reversed)

# WALSH fast PART
# plot_signal(sinx)
# start = timer()
# ww = fast_walsh_hadamard(sinx.array)
# end = timer()
# print("Fast Walsh:", timedelta(seconds=end - start))
# w1(ww, sinx)
# w2(ww, sinx)
# reversed = Signal(array=reverse_walsh_hadamard(ww),
#                   name="reversed",
#                   sampling_rate=sinx.sampling_rate,
#                   time=sinx.time,
#                   duration=sinx.time)
# plot_signal(reversed)
# ww = fast_walsh_hadamard (sinx.array)
# plot_rez_to_imz(w.T)
