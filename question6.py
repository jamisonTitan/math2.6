import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

n = 10
p = 0.6
k = np.arange(0,n+1)

binomialPmf = binom.pmf(k, n, p)

plt.plot(k, binomialPmf, color='blue')
plt.title(f"Binomial Distribution (n={n}, p={p})")
plt.show()

print(binomialPmf)
