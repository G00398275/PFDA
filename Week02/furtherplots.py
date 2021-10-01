# Week 02: further plots, two plots on one set of axes, formatting
# Author: Ross Downey

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 10.0, 0.01) # Range 0-10, interval 0.01
y = 3.0 * x + 1.0 # y values
noise = np.random.normal(0.0, 1.0, len(x))# (Centre, Std. Dev, Length of x)

plt.plot (x, y + noise , 'r.')# Noise around straight line in red points
plt.plot (x, y, 'b-') # Blue straight line
plt.show()

plt.plot (x, y + noise , 'r.', label = "Model") # Adding label
plt.plot (x, y, 'b-', label = "Actual")
plt.title ("Simple Plot") # Adding some formatting options
plt.xlabel ("Mass")
plt.ylabel ("Velocity")
plt.legend()
plt.show()