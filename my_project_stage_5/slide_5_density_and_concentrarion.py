import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import shapely.geometry as geom

# Загрузка изображения
img = plt.imread("crab_nebula.jpg")
fig, ax = plt.subplots()
ax.imshow(img, extent=[0, 640, 0, 640])

def circle(R, x0, y0, start, stop, step):
    t = np.arange(start, stop, step)
    x = x0 + R * np.cos(t)
    y = y0 + R * np.sin(t)
    return x, y

x = np.array([])
y = np.array([])


# Генерация начальных координат для кривых контура туманности
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

# Определение границ области внутри кривой
curve_coords = []
for i in range(len(spline_curve[0])):
    curve_coords.append([spline_curve[0][i], spline_curve[1][i]])

polygon = geom.Polygon(curve_coords)
points_numper_per_side = 100  # Плотность точек для анализа внутри туманности
x_pictures_limits = [0, 640]  # Границы изображения по оси X (в пикселях)
y_pictures_limits = [0, 640]  # Границы изображения по оси Y (в пикселях)

points_coords = []

for x_point_coord in np.linspace(*x_pictures_limits, points_numper_per_side):
    for y_point_coord in np.linspace(*y_pictures_limits, points_numper_per_side):
        p = geom.Point(x_point_coord, y_point_coord)
        if p.within(polygon):
            points_coords.append(x_point_coord)
            points_coords.append(y_point_coord)

x_p = np.array(points_coords[0::2]) + 0.5 # Центрирование объекта на графике по оси Х
y_p = np.array(points_coords[1::2]) + 1 # Центрирование объекта на графике по оси Y


# --- ПЕРЕСЧЁТ К РЕАЛЬНЫМ ЕДИНИЦАМ (ПАРСЕКАМ) ---
# Коэффициенты пересчёта: 1 пиксель = X парсек
x_unit_length = 5 / 640  # пк/пиксель (по оси OX: 5 пк на 640 пикселей)
y_unit_length = 6 / 640  # пк/пиксель (по оси OY: 6 пк на 640 пикселей)

# Реальные координаты в парсеках
x_real_pc = x_p * x_unit_length
y_real_pc = y_p * y_unit_length

fig2, ax2 = plt.subplots(figsize=(8, 8))
sc_plot = ax2.scatter(x_real_pc, y_real_pc, s=1, alpha=0.7)
ax2.set_ylabel('Координата Y, пк')
ax2.set_xlabel('Координата X, пк')
ax2.set_title('Распределение точек внутри туманности «Краб» (в реальных координатах)')
plt.axis('equal')
plt.savefig('slide_5_real_coordinates.png', dpi=150, bbox_inches='tight')
plt.close()


# --- ДАННЫЕ АСТРОНОМИЧЕСКИХ НАБЛЮДЕНИЙ ---
m = 2 * 1.6735575 * 10**(-27)  # масса молекулы водорода в кг
n = 1 * 10**7  # характерная концентрация частиц в туманности «Краб», см⁻³ (≈10⁷ см⁻³)
n_m3 = n * 10**6  # перевод в м⁻³ (1 см⁻³ = 10⁶ м⁻³)
len_unit = 3.0856776 * 10**16  # 1 парсек в метрах

rho_v_in_m = m * n_m3 # плотность водорода в кг/м^3
print('rho_v_in_m: ', rho_v_in_m)

rho_v_in_pc = m * n_m3 * len_unit**3 # плотность водорода в кг/пк^3
print('rho_v_in_pc: ', rho_v_in_pc)

scale = 0.1 * len_unit ** 3 # характерная толщина туманности (10% от объёма туманности), которую можно варьировать
rho_s_in_pc = m * n_m3 * scale # плотность водорода в кг/пк^2

# --- ФУНКЦИЯ ДЛЯ МОДЕЛИРОВАНИЯ РАСПРЕДЕЛЕНИЯ ПЛОТНОСТИ ---
def density_dist(x, y, x0=0, y0=0, intensity=1, dec_rate=[0.5, 0.5]):
    scalar_func = intensity / np.exp(-dec_rate[0] * (x - x0)**2 - dec_rate[1] * (y - y0)**2)
    return scalar_func

# Центр туманности в реальных координатах (пк)
center_x_pc = (5 / 2)  # 2.5 пк (центр по OX)
center_y_pc = (6 / 2)  # 3 пк (центр по OY)

# Расчёт распределения плотности
density_values = density_dist(
    x_real_pc, y_real_pc,
    center_x_pc, center_y_pc,
    intensity=rho_s_in_pc,
    dec_rate=[0.8, 0.8]  # Коэффициенты затухания (подбираются эмпирически)
)

# Визуализация распределения плотности
fig3, ax3 = plt.subplots(figsize=(10, 8))
scatter_plot = ax3.scatter(
    x_real_pc, y_real_pc,
    c=density_values,
    cmap='plasma',      # Цветовая схема (можно заменить на 'viridis', 'hot' и т. д.)
    s=15,           # Размер точек
    alpha=0.8       # Прозрачность
)
ax3.set_ylabel('Координата Y, пк')
ax3.set_xlabel('Координата X, пк')
ax3.set_title('Распределение плотности вещества в туманности «Краб»')

# Добавление цветовой шкалы
cbar = fig3.colorbar(scatter_plot)
cbar.set_label("Поверхностная плотность, кг/пк²")

# Установка равных масштабов осей для корректного отображения формы туманности
plt.axis('equal')

# Сохранение результата
plt.savefig('slide_5_density_field.png', dpi=150, bbox_inches='tight')
plt.close()

fig, ax = plt.subplots()
sc_plot = ax.scatter(x_p, y_p, c=density_dist(x_p, y_p, 340, 300, rho_s_in_pc, [0.000001, 0.000001]))
ax.set_ylabel('Координата Х, м')
ax.set_xlabel('Координата Y, м')

cbar = fig.colorbar(sc_plot)
cbar.set_label("Поле плотности, кг/пк^2")

plt.axis('equal')
plt.savefig('slide_5_conentration_field.png')

