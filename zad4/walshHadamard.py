import numpy as np
from scipy.linalg import hadamard


def walsh_hadamard(x: np.ndarray):
    N = x.size
    if N & (N - 1) != 0:
        raise ValueError("size of x must be a power of 2")
    else:
        matrix = generate_matrix(N)
        x = np.array([x]).T
        r = np.dot(matrix, x)
        r[:] = [x / N for x in r]
        reverse_walsh_hadamard(r)
        return r


def reverse_walsh_hadamard(x: np.ndarray):
    N = x.size
    matrix = generate_matrix(N)
    r = np.dot(matrix, x)
    # print("signal after", r)
    return r


def fast_walsh_hadamard(xx: np.ndarray):
    N = xx.size
    if N & (N - 1) != 0:
        raise ValueError("size of x must be a power of 2")
    else:
        a = np.array([xx]).T
        h = 1
        while h < N:
            for i in range(0, N, h * 2):
                for j in range(i, i + h):
                    x = a[j]
                    y = a[j + h]
                    a[j] = x + y
                    a[j + h] = x - y
            h *= 2
    a[:] = [k / N for k in a]
    # print("fast",a)
    return a


def generate_matrix(n):
    return hadamard(n, complex)
