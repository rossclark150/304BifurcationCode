import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace

# This program is also identical to the original bifurcation diagram program, except for differences in the while loop on line 29.

startingX = 0.0001

numPoints = 1000

rValues = linspace(1, 4, numPoints)

rValueIterations = 900

transients = 100

xAxis = []
yAxis = []


def logisticEquation(r, val):
    output = r * val * (1 - val)
    return output


iterationList = []  # stores values of iterations of logistic formula
i = 0
k = 0
while i < numPoints:   # Similar to the program which adds constants, the if/elif statements simply multiply r by a constant each iteration. The multiple elif statements are just to get several different intervals of changing r.
    iterationList += [logisticEquation(rValues[i], startingX)]
    for n in range(rValueIterations):
        iterationList += [logisticEquation(k*rValues[i], iterationList[n])]
        if rValues[i] < 1.88: # 1.569 where secondary chaos appears
            k = 1.9
        elif 2.7 > rValues[i] > 1.88:
            k = 1.2
        elif rValues[i] > 3.5:
            k = .9 # "dampen down" chaos
        else:
            k = 1
    yAxis += iterationList[transients:]
    xAxis += [rValues[i]] * (rValueIterations - (transients - 1))
    iterationList = []
    i += 1

plt.scatter(xAxis, yAxis, .001)
plt.xlabel("r")
plt.ylabel("x")
#plt.xlim(3.371,  3.701)
#plt.ylim(.329, .590)
plt.show()