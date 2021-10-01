# powers.py, simple plot of powers on same axes
# Author: Ross Downey

import matplotlib.pyplot as plt
import numpy as np

x = np.arange (1.0, 10.0, 0.1)

plt.plot (x, x**2, 'g-', label = "x^2")
plt.plot (x, x**3, 'b-', label = "x^3")
plt.plot (x, x**4, 'r-', label = "x^4")
plt.plot (x, 2 **x, 'y-', label = "2^x")

plt.legend()
plt.show()