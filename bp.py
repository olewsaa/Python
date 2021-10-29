import sys
import numpy as np
import matplotlib.pyplot as plt

perf=[100,126,111,79]
nodes=[32,64,128,256]

ind = np.arange(4)
plt.figure(figsize=(10, 5))

plt.bar(ind, perf, align='center', color="skyblue",  hatch="\\\\\\")
plt.xticks(ind, nodes)
plt.ylabel("Normalised performance per node [rel %]")
plt.xlabel("Number of nodes")

plt.savefig("bifrost-perf.svg")
plt.show()

