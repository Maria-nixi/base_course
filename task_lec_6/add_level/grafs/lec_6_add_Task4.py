import matplotlib.pyplot as plt
import numpy as np

N = 10

x = np.arange(0, N+1, 0.01)
y = x // 1
    
plt.plot(x,y)
plt.axis('equal')
plt.savefig('add_Task_4.png')

