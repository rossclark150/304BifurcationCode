import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace

# This program is identical to the original bifurcation diagram except one change in the while loop on line 29.

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
while i < numPoints:
    iterationList += [logisticEquation(rValues[i], startingX)]
    for n in range(rValueIterations):
        iterationList += [logisticEquation(rValues[i] + k, iterationList[n])]
        if rValues[i] < 3.7:   # This if/else look adds the constant on to the r value after each iteration, as long as r is less that 3.7. This maximum r value can be changed as long as the constant is adjusted accordingly.
            k += .0003333
        else:
            k = 0
    yAxis += iterationList[transients:]
    xAxis += [rValues[i]] * (rValueIterations - (transients - 1))
    iterationList = []
    k = 0
    i += 1

plt.scatter(xAxis, yAxis, .001)
plt.xlabel("r")
plt.ylabel("x")
#plt.xlim(3.371,  3.701)
#plt.ylim(.329, .590)
plt.show()