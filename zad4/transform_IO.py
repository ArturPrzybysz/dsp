import numpy as np


def save_transform(data_set, file_name):
    np.savetxt(file_name, data_set, fmt='%.4e')


def read_transform(file_name):
    return np.loadtxt(file_name, dtype=complex)
