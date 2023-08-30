import math
import numpy as np

# Parameters.
amplitude = 300
horiz = 100
colours = ["43B023", "57FC26", "0DFCF0", "FFCC00", "FC2519"]

t_vals = np.linspace(0, 2 * math.pi)

def f(t):
    global amplitude
    x = amplitude * math.cos(t)
    y = amplitude * math.sin(t)
    return (x, y)

for t in t_vals:
    x_1, y_1 = f(t)
    x_2, y_2 = f(t + 2)
    x_1 *= 1.4
    parts = [int(x_1), int(x_2), int(y_1), int(y_2), colours[int(t * horiz) % len(colours)]]
    line = ','.join([str(elt) for elt in parts])
    print(line)
