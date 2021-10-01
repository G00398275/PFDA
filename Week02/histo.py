# histo.py, plotting simple histograms
# Author: Ross Downey

import matplotlib.pyplot as plt
import numpy as np
'''
x = np.random.normal (0.0, 1.0, 1000)

plt.hist (x)
plt.show()

plt.hist (x, bins = 20) # increasing number of bins in histogram
plt.show()
'''
plt.subplot (1, 2, 1) # First plot, 1 row, 2 columns, 1st plot
x = np.random.normal (0.0, 1.0, 10000)
plt.hist (x)
plt.subplot (1, 2, 2) # Adding second plot, 1 row, 2 columns, 2nd plot
x = np.random.uniform (-3.0, 3.0, 10000)
plt.hist (x)
plt.show()

plt.subplot (2, 1, 1) # Changes to two rows, or one on top of the other
x = np.random.normal (0.0, 1.0, 10000)
plt.hist (x)
plt.subplot (2, 1, 2) 
x = np.random.uniform (-3.0, 3.0, 10000)
plt.hist (x)
plt.show()