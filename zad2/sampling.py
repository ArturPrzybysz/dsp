from zad1.Signal import Signal


def sample_signal(analog_signal: Signal, sampling_rate: float):
    sr_ratio = analog_signal.sampling_rate // sampling_rate

    array = analog_signal.array[::sr_ratio]
    time = analog_signal.time[::sr_ratio]

    return Signal(array=array,
                  time=time,
                  sampling_rate=sampling_rate,
                  name="(sampled " + analog_signal.name + ")")
