import matplotlib.pyplot as plt
import numpy as np
def no(A=1,a=1,b=6,B=1):
    t = np.arange(0, 24*np.pi, 0.01)
    x = A * np.sin(a * t + np.pi/2)
    y = B * np.sin(b * t)    

    plt.plot(x,y)
    plt.axis('equal')
    plt.savefig('add_Task_1.png')

