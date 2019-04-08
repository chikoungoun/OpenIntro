""" Code to compute the percentile from a Z-score using it's general equation
"""

import numpy as np
import math
from scipy import integrate




#Z-score for testing
z=1.25
#The negative infinity
ninf = np.NINF

def fn(x):
    return (1/math.sqrt(2*math.pi)) * math.exp(-x**2/2)

# return a tuple containing the percentile and the error approximate
percentile,err = integrate.quad(fn,ninf,z)

print(percentile)
