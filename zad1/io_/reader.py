import numpy as np

from zad1.Signal import Signal
from scipy.io.wavfile import read
from global_config import ROOT
from os.path import join

wav_ext = ".wav"


def read_wav(filename: str, directory: str = None):
    if directory is None:
        directory = join(ROOT, "data")
    file_address = join(directory, filename)

    sampling_rate, array = read(file_address)

    name = filename
    if name[-4:] == wav_ext:
        name = name[:-4]

    return Signal(array=array,
                  sampling_rate=sampling_rate,
                  name=name,
                  time=np.linspace(0, array.size / sampling_rate, array.size))
