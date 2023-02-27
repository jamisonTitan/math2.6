import random

numTrials = 10**6

count = 0
for i in range(numTrials):
    x1 = random.random()
    x2 = 1 - x1
    if(x2 > x1):
        count+=1
print("the answer is:", count / numTrials)
