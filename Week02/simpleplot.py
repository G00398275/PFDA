# Week 02: Simple plots on Matplotlip.pyplot
# Author: Ross Downey

import matplotlib.pyplot as plt
import numpy as np

plt.plot ([1,2,3,4]) # y values only, x values default to 0,1,2,3 in this case
plt.ylabel ("Some Numbers")
plt.show ()

plt.plot ([1,2,3,4], [1,4,9,16]) # x values first, then y values
plt.ylabel ("Some Numbers")
plt.show ()

plt.plot ([1,2,3,4], [1,4,9,16], 'b .') # b for blue, . for points instead of straight line
plt.ylabel ("Some Numbers")
plt.show ()



