import matplotlib.pyplot as plt
import numpy as np


b = 0.3

phi = np.arange(0, 8*np.pi, 0.1)
r = np.e ** (b * phi)

x = r * np.cos(phi)
y = r * np.sin(phi)

plt.plot(x, y)
plt.axis('equal')
plt.savefig('Task_4.1.png')

plt.close()
k = 0.4

phi = np.arange(0, 8*np.pi, 0.1)
r = k * phi

x = r * np.cos(phi)
y = r * np.sin(phi)

plt.plot(x, y)
plt.axis('equal')
plt.savefig('Task4_.2.png')

plt.close()

alfa = 5

phi = np.arange(0.01, 8*np.pi, 0.1)
r = alfa / np.sqrt(phi)

x = r * np.cos(phi)
y = r * np.sin(phi)

plt.plot(x, y)
plt.axis('equal')
plt.savefig('Task_4.3.png')

plt.close()


k = 8

phi = np.arange(0, 8*np.pi, 0.1)
r = np.sin(phi * k)

x = r * np.cos(phi)
y = r * np.sin(phi)

plt.plot(x, y)
plt.axis('equal')
plt.savefig('Task_4.4.png')