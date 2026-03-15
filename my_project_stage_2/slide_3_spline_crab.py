import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt


img = plt.imread("my_project_stage_2/crab_nebula.jpg")
fig, ax = plt.subplots()
ax.imshow(img, extent=[0, 640, 0, 640])


def circle(R, x0, y0, starst, stop, step):
    t=np.arange(starst, stop, step)
    x = x0 + R * np.cos(t)
    y = y0 + R * np.sin(t)
    return x, y


x = np.array([])
y = np.array([])


x = np.append(x, [142, 139])
y = np.append(y, [380, 373])


coords = circle(54, 68, 162, np.pi/2+np.pi/7, 3*np.pi/2.2, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

coords = circle(37, 50, 250, np.pi/3+np.pi/4, 3*np.pi/2, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

coords = circle(90, 180, 280, np.pi/np.pi+0.5, 2*np.pi-np.pi/1.01, 0.1)
x = np.append(x, coords[0] - 50)
y = np.append(y, coords[1] + 5)

coords = circle(50, 230, 410, np.pi/np.pi+0.01, 2*np.pi-np.pi/1.3, 0.1)
x = np.append(x, coords[0] - 50)
y = np.append(y, coords[1] + 5)

coords = circle(55, 315, 450, np.pi/np.pi+0.05, 2*np.pi-np.pi/1.05, 0.1)
x = np.append(x, coords[0] - 50)
y = np.append(y, coords[1] + 5)

coords = circle(55, 400, 500, np.pi/np.pi+0.05, 2*np.pi-np.pi/1.05, 0.1)
x = np.append(x, coords[0] - 50)
y = np.append(y, coords[1] + 5)

coords = circle(140, 458, 440, 2*np.pi-np.pi/5, 2*np.pi+np.pi/1.4, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

coords = circle(70, 522, 310, 2*np.pi-np.pi/3, 2*np.pi+np.pi/4, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

coords = circle(70, 220, 115, np.pi+np.pi/6, 2*np.pi-np.pi/3.5, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

coords = circle(85, 117, 155, np.pi+np.pi/6, 2*np.pi-np.pi/3, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

coords = circle(45, 300, 90, np.pi+np.pi/5, 2*np.pi-np.pi/20, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

coords = circle(45, 380, 108, np.pi+np.pi/4.5, 2*np.pi+np.pi/8, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

coords = circle(90, 487, 188, np.pi+np.pi/4.5, 2*np.pi+np.pi/4, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])


spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
spline_curve = interpolate.splev(np.linspace(0, 1, 100), spline_coords) 


plt.plot(x, y, 'bo') 
plt.plot(spline_curve[0], spline_curve[1], 'g') 
plt.savefig('slide_2_spline_crab_nebula.png')

