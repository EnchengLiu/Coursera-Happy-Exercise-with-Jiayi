from sympy import *
from sympy.stats import *
import matplotlib.pyplot as plt

import numpy as np

# Define symbols
t = Symbol('t')
pdf=2*t*exp(-t**2/1000**2)/1000**2
X = ContinuousRV(t, pdf, set=Interval(0, oo))

cdf_X = cdf(X)

cdf_X_func = lambdify(X, cdf_X(X), 'numpy')

samples=[]
for i in range(0,10**6):
    samples.append(sample(X))
print("Mean: ", np.mean(samples))
np.savetxt('samples.txt', samples)