import numpy as np
import matplotlib.pyplot as plt

x, y = np.meshgrid(np.linspace(-600, 600, 10), np.linspace(-600, 600, 10))

u = x / np.sqrt(x**2 + y**2)
v = y / np.sqrt(x**2 + y**2)
plt.quiver(x, y, u, v, angles='xy', scale_units='xy')
plt.title('Векторное поле скоростей, v = {y/r, x/r} м/с')
plt.ylabel('Координата Х, м')
plt.xlabel('Координата Y, м')
plt.savefig("ield_2.png")

