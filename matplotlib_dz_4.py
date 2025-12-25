import matplotlib.pyplot as plt
import numpy as np

b = 0.3

phi = np.arange(0, 8*np.pi, 0.1)
r = np.e ** (b * phi)

x = r * np.cos(phi)
y = r * np.sin(phi)

plt.plot(x, y, label='my parabola')
plt.savefig('fig_dz_4.png')