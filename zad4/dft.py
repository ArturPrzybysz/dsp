import numpy as np


def dft_naive(x: np.ndarray):
    N = x.size
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)


def FFT(x: np.ndarray):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]

    if N & (N - 1) != 0:
        raise ValueError("size of x must be a power of 2")
    elif N <= 32:
        return dft_naive(x)
    else:
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate([X_even + factor[:N // 2] * X_odd,
                               X_even + factor[N // 2:] * X_odd])
