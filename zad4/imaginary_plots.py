import numpy as np
import matplotlib.pyplot as plt


def plot_rez_to_imz(imaginary_array: np.ndarray):
    assert np.iscomplexobj(imaginary_array) is True
    plt.xlabel("imz")
    plt.ylabel("rez")
    plt.plot(np.real(imaginary_array), np.imag(imaginary_array))
    plt.show()
