import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

n = 10
p = 0.6
x = np.arange(0,n+1)
x2 = np.arange(0,8)
x3 = np.arange(8,n+1)

plt.plot(x, binom.pmf(x,n,p), color='black')
plt.fill_between(x2, binom.pmf(x2,n,p) , color="blue")
plt.fill_between(x3, binom.pmf(x3,n,p), color="orange")
plt.title("Question 6")
plt.show()

probLessThanEight = 0
probMoreThanEight = 0

for i in x2:
    probMoreThanEight += binom.pmf(i,n,p)

for i in x3:
    probLessThanEight += binom.pmf(i,n,p)

print(probMoreThanEight)
print(probLessThanEight)
