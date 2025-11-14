import numpy as np
g = 9.8
t = [0, 1, 2, 3, 4, 5]
v_0 = 8
x_0 = 5
y_0 = 2
y = x_0 + v_0 * t 
x = y_0 + v_0 * t - (g * t ** 2 / 2)
a = np.zeros((1, 3))
a[0, 0] = t
a[0, 1] = x
a[0, 2] = y
print(a)
