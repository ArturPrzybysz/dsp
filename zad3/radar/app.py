import numpy as np

from zad1.plot import plot_signal
from zad1.signal_generators import gauss_noise, sinusoidal_signal, rectangular_signal
from zad3.convolution import correlate

PROPAGATION_SPEED = 20
OBJECTS_DISTANCE = 1000
duration = 5
# emitted = rectangular_signal(amp=3, duration=duration, k_w=0.9, T=1)
emitted = sinusoidal_signal(amp=2, freq=0.3, t0=30, duration=duration)

received = emitted.delay(2 * OBJECTS_DISTANCE / PROPAGATION_SPEED - duration)
received = received.add(gauss_noise(received.duration, mean=0, variance=4))

correlated = correlate(emitted, received)
max_idx = np.argmax(correlated.array)
t_max = correlated.time[max_idx]

print("o tyle opóźniam: ", 2 * OBJECTS_DISTANCE / PROPAGATION_SPEED)
print("czas maksymalnej korelacji:", t_max)
print("czas trwania korelacji:", correlated.time[-1])
print("dystans przewidywany:", (correlated.time[-1] - t_max) / 2 * PROPAGATION_SPEED)
print("dystans faktyczny:", OBJECTS_DISTANCE)

plot_signal(emitted)
plot_signal(received)
plot_signal(correlated)

# DIST = 13
# PROP_SPEED = 15
# t = 105
#
# v = s/t
# v*t = s
# t = s/v




