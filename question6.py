import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

n = 10
p = 0.6
k = np.arange(0,n+1)

binomialPmf = binom.pmf(k, n, p)

plt.plot(k, binomialPmf, color='blue')
plt.plot(8, 0.12, marker="o", markersize=20, markeredgecolor="black", markerfacecolor="green")
plt.title(f"Question 6")
plt.savefig("question6.1_graph.png")

print(binomialPmf[8])
