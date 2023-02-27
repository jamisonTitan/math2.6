import numpy as np
import random

numTrials = 10
numPoints = 10**6

def pointIsBetweenCurves(point):
    px = point[0]
    py = point[1]
    #if point > x^2 and less than x then it is inside the functions
    if np.logical_and(py > g(px), py < f(px)).all():
        return True
    return False

def f(x):
   return x

def g(x):
    return x**2

trialOutcomes = [0] * numTrials
for trial in range(numTrials):
    #used to keep track of the number of generated random points inside the two functions f(x) and g(x)
    count = 0
   #generate random points
    points = [(random.random(), random.random()) for i in range(numPoints)]
    for point in points: 
        if pointIsBetweenCurves(point): count += 1
    trialOutcomes[trial] = count / numPoints 
    print("the answer to trial",trial," is:", count / numPoints)
print("avg = total / numTrials:", sum(trialOutcomes) / numTrials)
