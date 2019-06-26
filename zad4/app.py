import numpy as np
from timeit import default_timer as timer
from datetime import timedelta

from zad1.plot import plot_signal
from zad1.signal_generators import sinusoidal_signal

from zad4.dft import dft_naive, FFT
from zad4.imaginary_plots import plot_rez_to_imz

from zad1.Signal import Signal
from zad4.plots import w1, w2
from zad4.transform_IO import save_transform, read_transform
from zad4.walsh_hadamard import walsh_hadamard, fast_walsh_hadamard, reverse_walsh_hadamard

sr = 512
# originalSignal = sinusoidal_signal(amp=1, freq=3, duration=8, sampling_rate=128)
original_signal = sinusoidal_signal(amp=2, freq=0.5, duration=8, sampling_rate=sr)
original_signal = original_signal.add(sinusoidal_signal(amp=1, freq=1, duration=8, sampling_rate=sr))
original_signal = original_signal.add(sinusoidal_signal(amp=5, freq=2, duration=8, sampling_rate=sr))

# DFT NAIVE PART
# start = timer()
# dft1 = dft_naive(original_signal.array)
# end = timer()
# print("Naive DFT:", timedelta(seconds=end - start))
# w1(dft1, original_signal)
# w2(dft1, original_signal)

# FFT RECURRENT PART
# start = timer()
# fft1 = FFT(original_signal.array)
# end = timer()
# print("FFT recurrent:", timedelta(seconds=end - start))
# w1(fft1, original_signal)
# w2(fft1, original_signal)

# FFT NUMPY PART
# start = timer()
# fft2 = np.fft.fft(original_signal.array)
# end = timer()
# print("Numpy FFT:", timedelta(seconds=end - start))
# w1(fft2, original_signal)
# w2(fft2, original_signal)

# plot_rez_to_imz(x)
# plot_rez_to_imz(xx)
# plot_rez_to_imz(xxx)

# WALSH NORMAL PART
plot_signal(original_signal)
start = timer()
w = walsh_hadamard(original_signal.array)
end = timer()
print("Normal Walsh:", timedelta(seconds=end - start))
# w1(w, original_signal)
# w2(w, original_signal)
save_transform(w, "array.txt")
w_out = read_transform("array.txt")
reversed = Signal(array=reverse_walsh_hadamard(w_out),
                  name="reversed",
                  sampling_rate=original_signal.sampling_rate,
                  time=original_signal.time,
                  duration=original_signal.time)
plot_signal(reversed)

# WALSH fast PART
# plot_signal(original_signal)
# start = timer()
# ww = fast_walsh_hadamard(original_signal.array)
# end = timer()
# print("Fast Walsh:", timedelta(seconds=end - start))
# w1(ww, original_signal)
# w2(ww, original_signal)
# reversed = Signal(array=reverse_walsh_hadamard(ww),
#                   name="reversed",
#                   sampling_rate=original_signal.sampling_rate,
#                   time=original_signal.time,
#                   duration=original_signal.time)
# plot_signal(reversed)
# ww = fast_walsh_hadamard (original_signal.array)
# plot_rez_to_imz(w.T)
