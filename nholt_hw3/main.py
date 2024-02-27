'''

Homework 3
Noah Holt
Algorithms

Pseudo code provided in pdf.

'''

from numpy import random
import timeit


# Knapsack Problem Solutions

# exhaustive search
# This looks less like my pseudocode but many changes needed to be made
# for this to properly work.
def Exhaustive(val, weight, max):

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

    # now we have all subsets so lets compare weights and values to get best
    bestSet = []
    for test in allSubSets:
        if len(bestSet) == 0: # if empty
            bestSet = test
        elif AddWeights(weight, test) > max:
            if AddValues(val, test) > AddValues(val, bestSet):
                bestSet = test

    return bestSet


# greedy bugger
def Greedy(val, weight, max):

    grabHighest = []
    for i in range(len(val)):
        grabHighest.append(i)
        if AddWeights(weight, grabHighest) > max:
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
values = random.randint(100, size=3)
weights = random.randint(low=1, high=10000, size=3)

exhaustiveStart = timeit.default_timer()

exhaustiveEnd = timeit.default_timer()
exhaustiveTime = round((exhaustiveEnd - exhaustiveStart) * 10 ** 6, 3)
# returned nano so with difference return seconds

# For greedy, ordering list first
OrderValues(values, weights)

greedyStart = timeit.default_timer()
greedyIndexes = Greedy(values, weights, maxWeigh)
greedyEnd = timeit.default_timer()
greedyTime = round((greedyEnd - greedyStart) * 10 ** 6, 3)

print(f"Greedy Time: {greedyTime} nano secs")

