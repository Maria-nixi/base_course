import numpy as np
import task1_module_physic_const as pc


x0 = 1
y0 = 1
v0y = 1

t = np.arange(0, 5, 0.1)
x = x0 + x0 * t
y = y0 + v0y * t - (pc.g * t**2 / 2)

a = np.zeros((2, 3))

print(x)

