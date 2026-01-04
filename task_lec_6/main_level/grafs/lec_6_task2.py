import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10, 0.02)
y = 1 / (x + 0.05)
plt.plot(x, y, label='my parabola')
plt.savefig('Task2.png')
