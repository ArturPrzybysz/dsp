from zad1.Signal import Signal
from scipy.io.wavfile import write
from global_config import ROOT
from os.path import join

wav_ext = ".wav"


def write_wav(signal: Signal, filename: str = None):
    if filename is None:
        filename = signal.name
    file_address = join(ROOT, "data", filename)
    if file_address[-4:] != wav_ext:
        file_address += wav_ext
    write(file_address, signal.sampling_rate, signal.array)
