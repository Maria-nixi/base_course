import numpy as np
import task1_module_physic_const as pc


x0 = 1
y0 = 1
v0y = 1
t = 5

x = x0 + x0 * t
y = y0 + v0y * t - (pc.g * t**2 / 2)

a = np.zeros((2, 3))
a[0, 0] = t
a[0, 1] = x
a[0, 2] = y

print(a)

