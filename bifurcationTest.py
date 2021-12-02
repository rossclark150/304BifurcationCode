import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace

# This program calculates r values at which bifurcations occur.

numPoints = 1000

rValues = linspace(1, 4, numPoints)

interval = linspace(0,1, numPoints) # Since we will be calculating intersections of the n-th iterative map with the 45 degree line, we need this interval too.

def logisticEquation(r, val):
    output = r * val * (1 - val)
    return output

def funcNester(r, n, x):  # I have to thank the solution found at https://stackoverflow.com/questions/58850623/how-to-compose-a-function-n-times-in-python for this function. Basically, this just iterates the logistic map n times using a for loop which updates the value of x after each calculation.
    for l in range(n):
        x = logisticEquation(r, x)
    return x

cycle = int(input("What cycle bifurcation? ")) # This takes in which cycle bifurcation the user wants

outputList = [] # empty lists that will be added too later in the program

bifurcationPoints = []

count = 0

for r in rValues: # Here is where the program calculates the bifurcation points. First, the outer for loop loops through all r values in the set rValues.
    for i in interval: # This loop loops through all values on the  interval [0,1]. For each value it calculates the n-th iterative map, as given by the cycle inputted. It then stores this to outputList.
        outputList += [funcNester(r, cycle, i)]
    for k in range(len(outputList)-2): # This loop will go through the output list to check if the desired number of bifurcation points has been found.
        if k == 0: # skip k = 0 since this throws a list index error
            continue
        elif outputList[k] - interval[k] > 0 > outputList[k + 1] - interval[k + 1]: # This line checks if the n-th iterative map crosses the 45 degree line and is decreasing while doing so. As explained in the paper, this indicates a fixed point of period n.
            count += 1
    if count >= cycle:  # If for this r value, the number of fixed points of period n equals the cycle the user wanted, then we store this r value to print to the user.
        bifurcationPoints += [rValues[np.where(rValues==r)]]
    count = 0
    outputList = []

print(bifurcationPoints[0]) # Prints the found r value. We only print the first value of the list, since r values greater than this found value will also satisfy the conditions, but are not desired.
