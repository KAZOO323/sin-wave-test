import numpy as npy
import matplotlib.pyplot as plt

x = npy.arange(0, 5*npy.pi, 0.1)
y = npy.sin(x)
plt.plot(x, y)
plt.show()