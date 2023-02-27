import numpy as np
from matplotlib import pyplot as plt
import random


numTrials = int(10**4.5)

plt.rcParams["figure.figsize"] = [16, 10]
plt.rcParams["figure.autolayout"] = True

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

x = np.arange(0,1,0.1)

#plot functions as lines
plt.plot(x, f(x), color='red', linewidth=5)
plt.plot(x,g(x),color='blue', linewidth=5)

#generate random points
points = [(random.random(), random.random()) for i in range(numTrials)]

count = 0

#plot points
for point in points:
    def pointColor(isBetween): 
        if isBetween: return "orange"
        else: return "grey"
    #if point i between lines add 1 to count and draw point in orange on graph
    pointIsBetween = pointIsBetweenCurves(point)
    if pointIsBetween:
        count += 1
    plt.plot(point[0],point[1], marker="o", markersize=2, color=pointColor(pointIsBetween))

print("the answer is:", count, "/", numTrials, "=", (count / numTrials)) 

plt.savefig("monte_carlo.png")
plt.show()
