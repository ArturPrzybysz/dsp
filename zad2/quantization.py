import numpy as np

from zad1.Signal import Signal


def quantization_with_rounding(signal: Signal, bins: int = 8):
    _min = np.min(signal.array)
    _max = np.max(signal.array)

    quant_set = np.linspace(_min, _max, num=bins)

    def find_nearest(value):
        idx = np.searchsorted(quant_set, value, side="left")
        if idx > 0 and (idx == len(quant_set) or np.math.fabs(value - quant_set[idx - 1]) < np.math.fabs(
                value - quant_set[idx])):
            return quant_set[idx - 1]
        else:
            return quant_set[idx]

    quantize = np.vectorize(find_nearest)
    return Signal(array=quantize(signal.array),
                  time=signal.time,
                  name="(quantized " + signal.name + ")",
                  sampling_rate=signal.sampling_rate)
