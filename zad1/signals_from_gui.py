from zad1.signal_analysis import show_stats
from zad1.signal_generators import sinusoidal_signal, gauss_noise, uniform_noise, half_wave_signal, full_wave_signal, \
    rectangular_signal, unit_step_signal, impulse_signal, impulse_noise, rectangular_symmetrical_signal, triangle_wave

from zad1.plot import plot_signal, plot_histogram


def create_signals(values):
    first = values[0]
    operation = values[1]
    second = values[2]

    sampling_rate = int(values[3])
    duration = int(values[4])

    low1 = values[5]
    low2 = values[6]
    high1 = values[7]
    high2 = values[8]
    mean1 = values[9]
    mean2 = values[10]
    variance1 = values[11]
    variance2 = values[12]
    amp1 = values[13]
    amp2 = values[14]
    T1 = values[15]
    T2 = values[16]
    t01 = values[17]
    t02 = values[18]
    kw1 = values[19]
    kw2 = values[20]
    ts1 = values[21]
    ts2 = values[22]
    occurrence_probability1 = values[23]
    occurrence_probability2 = values[24]
    histogram_interval = values[25]
    print_first = values[26]
    print_second = values[27]
    print_result = values[28]

    if print_first:
        s1 = _create_signal(first, sampling_rate, duration, low1, high1, mean1, variance1, amp1, T1, t01, kw1, ts1,
                            occurrence_probability1)
        plot_signal(s1)
        plot_histogram(s1, int(histogram_interval))
        show_stats(s1)
    if print_second:
        s2 = _create_signal(second, sampling_rate, duration, low2, high2, mean2, variance2, amp2, T2, t02, kw2, ts2,
                            occurrence_probability2)
        plot_signal(s2)
        plot_histogram(s2, int(histogram_interval))
        show_stats(s2)
    if print_result:
        s1 = _create_signal(first, sampling_rate, duration, low1, high1, mean1, variance1, amp1, T1, t01, kw1, ts1,
                            occurrence_probability1)
        s2 = _create_signal(second, sampling_rate, duration, low2, high2, mean2, variance2, amp2, T2, t02, kw2, ts2,
                            occurrence_probability2)
        s3 = _execute_operation(operation, s1, s2)
        plot_signal(s3)
        plot_histogram(s3, int(histogram_interval))
        show_stats(s3)


def _create_signal(type, sampling_rate, duration, low, high, mean, variance, amp, T, t0, kw, ts,
                   occurrence_probability):
    if type == 'S1':
        return uniform_noise(int(duration) * int(sampling_rate), int(low), int(high))
    if type == 'S2':
        return gauss_noise(int(duration) * int(sampling_rate), float(mean), float(variance))
    if type == 'S3':
        return sinusoidal_signal(float(amp), 1 / float(T), int(duration), 0 if t0 == "" else int(t0),
                                 int(sampling_rate))
    if type == 'S4':
        return half_wave_signal(float(amp), 1 / float(T), int(duration), 0 if t0 == "" else int(t0), int(sampling_rate))
    if type == 'S5':
        return full_wave_signal(float(amp), 1 / float(T), int(duration), 0 if t0 == "" else int(t0), int(sampling_rate))
    if type == 'S6':
        return rectangular_signal(float(amp), float(T), int(duration), float(kw), 0 if t0 == "" else int(t0),
                                  int(sampling_rate))
    if type == 'S7':
        return rectangular_symmetrical_signal(float(amp), float(T), int(duration), float(kw),
                                              0 if t0 == "" else int(t0), int(sampling_rate))
    if type == 'S8':
        return triangle_wave(float(amp), float(T), int(duration), float(kw), 0 if t0 == "" else int(t0),
                             int(sampling_rate))
    if type == 'S9':
        return unit_step_signal(float(amp), int(duration), int(ts), 0 if t0 == "" else int(t0), int(sampling_rate))
    if type == 'S10':
        return impulse_signal(float(amp), int(ts), int(duration), 0 if t0 == "" else int(t0), int(sampling_rate))
    if type == 'S11':
        return impulse_noise(float(amp), float(occurrence_probability), int(duration), 0 if t0 == "" else int(t0),
                             int(sampling_rate))


def _execute_operation(operation, s1, s2):
    if operation == '+':
        return s1.add(s2)
    if operation == '-':
        return s1.subtract(s2)
    if operation == '/':
        return s1.divide(s2)
    if operation == '*':
        return s1.multiply(s2)
