import matplotlib.pylab as plt

from zad1.Signal import Signal
from zad2.quantization import quantization_with_rounding
from zad2.similarity_measures import signal_to_noise_ratio, mean_squared_error, peak_signal_to_noise_ratio, \
    max_difference

plt.tight_layout()


def analyze_sampling_params(bins, pure_signal: Signal):
    mse_values = []
    stn_values = []
    pstn_values = []
    md_values = []
    for b in bins:
        quantized_signal = quantization_with_rounding(pure_signal, bins=b)
        
        mse_values.append(mean_squared_error(pure_signal, quantized_signal))
        stn_values.append(signal_to_noise_ratio(pure_signal, quantized_signal))
        pstn_values.append(peak_signal_to_noise_ratio(pure_signal, quantized_signal))
        md_values.append(max_difference(pure_signal, quantized_signal))

    plt.plot(bins, mse_values)
    plt.xlabel("bin")
    plt.ylabel("MSE(bin)")
    plt.show()

    plt.plot(bins, stn_values)
    plt.xlabel("bin")
    plt.ylabel("STN(bin)")
    plt.show()

    plt.plot(bins, pstn_values)
    plt.xlabel("bin")
    plt.ylabel("PSTN(bin)")
    plt.show()

    plt.plot(bins, md_values)
    plt.xlabel("bin")
    plt.ylabel("MD(bin)")
    plt.show()
