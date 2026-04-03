import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import shapely.geometry as geom

img = plt.imread("crab_nebula.jpg")
fig, ax = plt.subplots()
ax.imshow(img, extent=[0, 640, 0, 640])

def circle(R, x0, y0, starst, stop, step):
    t = np.arange(starst, stop, step)
    x = x0 + R * np.cos(t)
    y = y0 + R * np.sin(t)
    return x, y


x = np.array([])
y = np.array([])


coords = circle(54, 68, 162, np.pi/2+np.pi/7, 3*np.pi/2.2, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

coords = circle(85, 117, 155, np.pi+np.pi/6, 2*np.pi-np.pi/3, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])


coords = circle(70, 220, 115, np.pi+np.pi/6, 2*np.pi-np.pi/3.5, 0.1)
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

coords = circle(70, 522, 310, 2*np.pi-np.pi/3, 2*np.pi+np.pi/4, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

coords = circle(140, 458, 440, 2*np.pi-np.pi/5, 2*np.pi+np.pi/1.4, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

coords = circle(55, 400, 500, np.pi/np.pi+0.05, 2*np.pi-np.pi/1.05, 0.1)
x = np.append(x, coords[0] - 50)
y = np.append(y, coords[1] + 5)

coords = circle(55, 315, 450, np.pi/np.pi+0.05, 2*np.pi-np.pi/1.05, 0.1)
x = np.append(x, coords[0] - 50)
y = np.append(y, coords[1] + 5)


coords = circle(50, 230, 410, np.pi/np.pi+0.01, 2*np.pi-np.pi/1.3, 0.1)
x = np.append(x, coords[0] - 50)
y = np.append(y, coords[1] + 5)

coords = circle(90, 180, 280, np.pi/np.pi+0.5, 2*np.pi-np.pi/1.01, 0.1)
x = np.append(x, coords[0] - 50) 
y = np.append(y, coords[1] + 5)

coords = circle(37, 50, 250, np.pi/3+np.pi/4, 3*np.pi/2, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)

curve_coords = []
for i in range(len(spline_curve[0])):
    curve_coords.append([spline_curve[0][i], spline_curve[1][i]])

polygon = geom.Polygon(curve_coords)
points_numper= 10000
x_pictures_limits = [0, 640]
y_pictures_limits = [0, 640]


def density(x, y, x0=340, y0=300, intensity=[0.00001, 0.000001]):  
        return np.exp(- intensity[0] * (x - x0)**2 - intensity[1] * (y - y0)**2)


def points_generator(x0=0, y0=0, points_numper=10000000, intensity=[0.00001, 0.000001]):
    points_counter = 0

    while points_counter < points_numper:
        x_point_coord = np.random.uniform(0, 640)
        y_point_coord = np.random.uniform(0, 640)
        
        p = geom.Point(x_point_coord, y_point_coord)
        w = np.random.uniform(0.0, 1.0)

        if w <= density(x_point_coord, y_point_coord, x0, y0, intensity) and p.within(polygon):
            points_coords.append(x_point_coord)
            points_coords.append(y_point_coord)
            points_counter += 1


points_coords = []
points_generator(0.8, 0, 5000, [5, 5])
points_generator(0.8, 0.8, 5000, [5, 5])

# Коэффициент отображения координат в расстояние [0, 1] (максимальное расстояние в координатах)
normal_dimention = 2.5 
box_size =  1

# Центрирование объекта
x_p = np.array(points_coords[0::2]) / normal_dimention + box_size / 2
y_p = np.array(points_coords[1::2]) / normal_dimention + box_size / 2

plt.plot(x_p, y_p, 'go', ms=0.5)
plt.axis('equal')
plt.savefig('slide_2_normalize_size.png')
plt.close()

# Учет реальных размеров объекта в парсеках
real_size = 1.7 # Размер туманности Ориона в парсеках

box_size = real_size * box_size
x_p = x_p * real_size
y_p = y_p * real_size

plt.plot(x_p, y_p, 'go', ms=0.5)
plt.axis('equal')
plt.savefig('slide_2_normalize_size.png')
plt.close()