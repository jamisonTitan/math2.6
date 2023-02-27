import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0,8)
y = np.full(8, 1/7)
ax = plt.axes()
plt.axis([0,10,0,0.5])

ax.set_xticks(range(0,11))
ax.set_yticks(np.arange(0,0.5,0.142))

plt.title("Probability Distribution")
plt.plot(x, y, color ="green")
plt.axvline(x = 7, ymin = 0, ymax = (2/7), color = 'green',)
ax.axvspan(0,2,color="red",ymax=(2/7), alpha=0.5)
ax.axvspan(2,6,color="yellow",ymax=(2/7), alpha=0.5)
ax.axvspan(6,7,color="blue",ymax=(2/7), alpha=0.5)

plt.savefig("question2.3.png")
plt.show()
