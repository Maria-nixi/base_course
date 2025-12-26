
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10, 0.02)
y = 1 / (x + 0.05)
plt.plot(x, y, label='my parabola')
plt.savefig('fig_dz_2.png')


'''def parabola_plotter(a=1, b=1, c=0):

    

    
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.title('Гипербола')
    plt.legend()

    


if __name__ == '__main__':
    parabola_plotter()'''