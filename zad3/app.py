import numpy as np

from zad1.io_.reader import read_wav
from zad1.io_.writer import write_wav
from zad1.signal_generators import sinusoidal_signal, gauss_noise
from zad2.upsampling import sinc_resampling_ideal
from zad3.convolution import convolve, naive_convolve
from zad3.filter_generators import low_pass_filter
from zad3.plot_spectrum import plot_spectra

song = read_wav("bohemian_rhapsody.wav")
song.array = song.array[:song.sampling_rate * 25]
f0 = 1000
low_pass1 = low_pass_filter(length=1551, f0=f0, sr=song.sampling_rate,window_type="hanning")
# low_pass2 = low_pass_filter(length=151, f0=1000, sr=song.sampling_rate, window_type="hamming")
# low_pass3 = low_pass_filter(length=151, f0=1000, sr=song.sampling_rate, window_type="hanning")

song1 = convolve(song, low_pass1)
# song2 = convolve(song, low_pass2)
# song3 = convolve(song, low_pass3)

plot_spectra(song)
plot_spectra(song1)
# plot_spectra(song2)
# plot_spectra(song3)

song1.array /= np.max(np.abs(song1.array), axis=0)

write_wav(song1, "blackman" + str(f0) + "Hz.wav")
# write_wav(song2, "hamming.wav")
# write_wav(song3, "hanning.wav")

# s2 = convolve(s1, f)
# s3 = naive_convolve(s1, f)
#
# plot_signal(s1, scatter=True)
# plot_signal(s2, scatter=True)
# plot_signal(s3, scatter=True)
