import matplotlib.pyplot as plt
import numpy as np


def circle_plotter(a,b):

    x = np.arange(-1.1*a, 1.1*a, 0.01)
    y = np.arange(-1.1*a, 1.1*a, 0.01)

    X, Y = np.meshgrid(x, y)

    fxy = X**2 / a**2 + Y**2 / b**2 - 1# Уравнение окружности
    
    plt.contour(x, y, fxy, levels=[0])
    plt.axis('equal')
    plt.title('Эллипсик')
    plt.savefig('Task3.png')


if __name__ == '__main__':
	circle_plotter(1,0.5)