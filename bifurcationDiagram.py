import matplotlib.pyplot as plt  # Importing plotting and numpy libraries
import numpy as np
from numpy import linspace

startingX = 0.0001  # The initial x value for which we start iterating the logistic map.

numPoints = 1000  # Number of r values we wish to calculate for.

rValues = linspace(1, 4, numPoints)  # Gives numPoints evenly spaced values on the interval [1,4]. These will be the r values we iterate through.

rValueIterations = 900  # The number of iterations to run for each r value.

transients = 100 # number of points considered transient, which will ultimately be removed.

xAxis = []
yAxis = []  # creating lists for which we will store calculated values


def logisticEquation(r, val):       # defining a function which computes the logistic map
    output = r * val * (1 - val)
    return output


iterationList = []  # A temporary list to store calculated values of the logistic map
i = 0
while i < numPoints:      # This loop goes through the 1000 r values on the interval. For each r value, the for loop calculates the 900 values of the logistic map we want.
    iterationList += [logisticEquation(rValues[i], startingX)]
    for n in range(rValueIterations):
        iterationList += [logisticEquation(rValues[i], iterationList[n])]
    yAxis += iterationList[transients:]          # This line removes transients and stores the values to the yAxis list.
    xAxis += [rValues[i]] * (rValueIterations - (transients - 1))   # This line adds 900 copies of the r value to the xAxis list. Therefore, a scatter plot can now be generated.
    iterationList = []
    i += 1

plt.scatter(xAxis, yAxis, .001)      # These lines plot the bifurcation diagram.
plt.xlabel("r")
plt.ylabel("x")
plt.xlim(3.371,  3.701)
plt.ylim(.323, .595)
plt.show()
