import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x = [1, 1, 10, 10, 1]
y = [1, 5, 5, 1, 1]
ax.plot(x, y, '-', linewidth=2, color='k')


x = [1, 5.5, 10]
y = [5, 7, 5]
ax.plot(x, y, '-', linewidth=2, color='k')

x = [5, 5, 6, 6]
y = [1, 3, 3, 1]
ax.plot(x, y, '-', linewidth=2, color='k')

t = np.linspace(0, 2*np.pi, 30)
x = 7.5 + 0.5 * np.cos(t)
y =  3.5 + np.sin(t)
ax.plot(x, y, '-', linewidth=2, color='k')

t = np.linspace(0, 2*np.pi, 30)
x = 3 + 0.6 * np.cos(t)
y =  3.5 + 0.6 * np.sin(t)
ax.plot(x, y, '-', linewidth=2, color='k')



plt.axis('equal')
plt.savefig('home.png')