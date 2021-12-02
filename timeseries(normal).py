import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace

# This graphs the time series graph of the discrete logistic equation.

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


iterationList = []
i = 0
while i < numPoints:
    iterationList += [logisticEquation(rValues[i], startingX)]        # This while loop keeps calculating the logistic equation and stores the succsessive values to a list so as to be plotted
    for n in range(rValueIterations):
        iterationList += [logisticEquation(rValues[i], iterationList[n])]
    yAxis += iterationList
    xAxis += [rValues[i]] * (rValueIterations - (transients - 1)) # The factor makes sure the lengths of the x and y axes lists are the same, otherwise an error will be thrown when plotting.
    iterationList = []
    i += 1

#plt.scatter(xAxis, yAxis, .001)
#plt.xlim(3.371,  3.701)
#plt.ylim(.329, .590)
#plt.show()

newXAxis = list(range(1,51))       # These lines graph a subsection of the points plotted; otherwise the graph would be too large.
newYAxis = yAxis[901*854:(901*854)+50]

plt.scatter(newXAxis, newYAxis, 4, color = "black")          # these lines graph the time series and connect the points with lines for visualization purposes
plt.plot(newXAxis, newYAxis, linewidth = .5, color = "black")
plt.xlabel("t")
plt.ylabel("x_t")
plt.show()

