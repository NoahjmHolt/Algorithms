"""

Homework 3
Noah Holt
Algorithms

Pseudo code provided in pdf.

"""

import numpy
from numpy import random
import timeit
# thanks to https://stackoverflow.com/questions/2512225/matplotlib-plots-not-showing-up-in-mac-osx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


# Knapsack Problem Solutions

# exhaustive search
# This looks less like my pseudocode but many changes needed to be made
# for this to properly work.
def Exhaustive(val, weight, maxW):

    allSubSets = []
    # get all subsets with bit manipulation
    for i in range(1 << len(val)):
        currentSubset = []
        # every element in val
        for j in range(len(val)):
            # check bits in subset
            if (i & (1 << j)) != 0:
                currentSubset.append(j)
        allSubSets.append(currentSubset)

    # now we have all subsets so let's compare weights and values to get best
    bestSet = []
    for test in allSubSets:
        # base case hae not ran yet
        if len(bestSet) == 0:  # if empty
            bestSet = test

        # check weight limit then higher value
        if AddWeights(weight, test) < maxW:
            if AddValues(val, test) > AddValues(val, bestSet):
                bestSet = test

    return bestSet


# greedy bugger
def Greedy(val, weight, maxW):

    grabHighest = []
    for i in range(len(val)):
        grabHighest.append(i)
        if AddWeights(weight, grabHighest) > maxW:
            grabHighest.pop()

    return grabHighest


# Other funcs
# gets total value
def AddValues(val, indexes):
    total = 0

    for i in indexes:
        total += val[i]

    return total


# gets total weight
def AddWeights(weight, indexes):
    total = 0

    for i in indexes:
        total += weight[i]

    return total


# orders from most valuable down
def OrderValues(val, weight):

    for i in range(0, len(val)):
        for j in range(i+1, len(val)):
            if val[i] < val[j]:
                tempVal = val[i]
                tempWeight = weight[i]
                val[i] = val[j]
                weight[i] = weight[j]
                val[j] = tempVal
                weight[j] = tempWeight
    # I looked and saw that this type of algorithm to sort is BigTheta(nlogn)
    # As stated in hw doc, we will ignore when determining other times


# main function
maxWeigh = 10000

exhaustiveTimes = []
exhaustiveWeights = []
exhaustiveValues = []

greedyTimes = []
greedyWeights = []
greedyValues = []

for n in range(3, 16):

    exhaustiveNTimes = []
    exhaustiveNWeights = []
    exhaustiveNValues = []

    greedyNTimes = []
    greedyNWeights = []
    greedyNValues = []

    for x in range(5):
        values = random.randint(100, size=n)
        weights = random.randint(low=1, high=10000, size=n)

        exhaustiveStart = timeit.default_timer()
        exhaustiveIndex = Exhaustive(values, weights, maxWeigh)
        exhaustiveEnd = timeit.default_timer()
        exhaustiveTime = round((exhaustiveEnd - exhaustiveStart) * 10 ** 6, 3)
        # returned nano so with difference return seconds
        exhaustiveNTimes.append(exhaustiveTime)
        exhaustiveNValues.append(AddValues(values, exhaustiveIndex))
        exhaustiveNWeights.append(AddWeights(weights, exhaustiveIndex))

        # For greedy, ordering list first
        OrderValues(values, weights)

        greedyStart = timeit.default_timer()
        greedyIndexes = Greedy(values, weights, maxWeigh)
        greedyEnd = timeit.default_timer()
        greedyTime = round((greedyEnd - greedyStart) * 10 ** 6, 3)

        greedyNTimes.append(greedyTime)
        greedyNValues.append(AddValues(values, greedyIndexes))
        greedyNWeights.append(AddWeights(weights, greedyIndexes))

    exhaustiveTimes.append(exhaustiveNTimes)
    exhaustiveWeights.append(exhaustiveNWeights)
    exhaustiveValues.append(exhaustiveNValues)

    greedyTimes.append(greedyNTimes)
    greedyWeights.append(greedyNWeights)
    greedyValues.append(greedyNValues)


# x = numpy.array(exhaustiveTimes[0])
# y = numpy.array(greedyTimes[0])
plt.xlabel("exhaustive")
plt.ylabel("greedy")

for n in range(len(exhaustiveTimes)):
    plt.scatter(exhaustiveTimes[n], greedyTimes[n])
    plt.title("Time Difference")

plt.show()

for n in range(len(exhaustiveValues)):
    plt.scatter(exhaustiveValues[n], greedyValues[n])
    plt.title("Value Difference")

plt.show()

for n in range(len(exhaustiveWeights)):
    plt.scatter(exhaustiveWeights[n], greedyWeights[n])
    plt.title("Weight Difference")

plt.show()

