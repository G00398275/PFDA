# sin.py, simple sin and cos plots
# Author: Ross Downey

import matplotlib.pyplot as plt
import numpy as np

x = np.arange (-2.0 * np.pi, 2.0 * np.pi, 0.1) # ensure arange as arrange

plt.plot (x, np.sin (x), 'g.') # Plotting between -2 pi and +2 pi for sin and cos
plt.plot (x, np.cos (x), 'b.')
plt.show()