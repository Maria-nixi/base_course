import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

# Загрузка изображения

img = plt.imread("my_project_stage_2/crab_nebula.jpg")

fig, ax = plt.subplots()

ax.imshow(img, extent=[0, 640, 0, 640])

def circle(R, x0, y0, starst, stop, step):

    """

    Генерирует координаты точек, лежащих на окружности.

    R - радиус окружности

    x0, y0 - координаты центра окружности

    starst - начальный угол

    stop - конечный угол

    step - шаг угла

    """

    t = np.arange(starst, stop, step)

    x = x0 + R * np.cos(t)

    y = y0 + R * np.sin(t)

    return x, y

# Инициализация массивов для координат точек

x = np.array([])

y = np.array([])

# Добавление точек из вашего кода

# Первая линия

x = np.append(x, [41, 10])

y = np.append(y, [210, 180])

# Вторая линия

x = np.append(x, [142, 139])

y = np.append(y, [380, 373])

# Первый круг

coords = circle(40, 35, 150, np.pi/2 + np.pi/4, 3*np.pi/2, 0.1)

x = np.append(x, coords[0])

y = np.append(y, coords[1])

# Второй круг

coords = circle(37, 50, 250, np.pi/3 + np.pi/4, 3*np.pi/2, 0.1)

x = np.append(x, coords[0])

y = np.append(y, coords[1])

# Третий круг (с модификацией)

coords = circle(90, 180, 280, np.pi/np.pi + 0.5, 2*np.pi - np.pi/1.01, 0.1)

x = np.append(x, coords[0] - 50)

y = np.append(y, coords[1] + 5)

# Четвертый круг (с модификацией)

coords = circle(50, 230, 410, np.pi/np.pi + 0.01, 2*np.pi - np.pi/1.3, 0.1)

x = np.append(x, coords[0] - 50)

y = np.append(y, coords[1] + 5)

# Пятый круг (с модификацией)

coords = circle(55, 315, 450, np.pi/np.pi + 0.05, 2*np.pi - np.pi/1.05, 0.1)

x = np.append(x, coords[0] - 50)

y = np.append(y, coords[1] + 5)

# Шестой круг (с модификацией)

coords = circle(55, 400, 500, np.pi/np.pi + 0.05, 2*np.pi - np.pi/1.05, 0.1)

x = np.append(x, coords[0] - 50)

y = np.append(y, coords[1] + 5)

# Седьмой круг

coords = circle(140, 458, 440, 2*np.pi - np.pi/5, 2*np.pi + np.pi/1.4, 0.1)

x = np.append(x, coords[0])

y = np.append(y, coords[1])

# Восьмой круг

coords = circle(70, 522, 310, 2*np.pi - np.pi/3, 2*np.pi + np.pi/4, 0.1)

x = np.append(x, coords[0])

y = np.append(y, coords[1])

# Девятый круг

coords = circle(70, 220, 115, np.pi + np.pi/6, 2*np.pi - np.pi/3.5, 0.1)

x = np.append(x, coords[0])

y = np.append(y, coords[1])

# Десятый круг

coords = circle(82, 108, 149, np.pi + np.pi/6, 2*np.pi - np.pi/3.8, 0.1)

x = np.append(x, coords[0])

y = np.append(y, coords[1])

# Одиннадцатый круг

coords = circle(45, 300, 90, np.pi + np.pi/5, 2*np.pi - np.pi/20, 0.1)

x = np.append(x, coords[0])

y = np.append(y, coords[1])

# Двенадцатый круг

coords = circle(45, 380, 108, np.pi + np.pi/4.5, 2*np.pi + np.pi/8, 0.1)

x = np.append(x, coords[0])

y = np.append(y, coords[1])

# Тринадцатый круг

coords = circle(90, 487, 188, np.pi + np.pi/4.5, 2*np.pi + np.pi/4, 0.1)

x = np.append(x, coords[0])

y = np.append(y, coords[1])

# Интерполяция точек для создания сглаженных кривых

# s=0 означает, что сплайн точно проходит через все точки.

# Если есть повторяющиеся точки, splprep может выдать ошибку.

spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)

spline_curve = interpolate.splev(np.linspace(0, 1, 200), spline_coords) # Создаем 200 точек для гладкой кривой

# Отрисовка точек

ax.plot(x, y, 'o', markersize=2, color='red') # Точки теперь красные

# Отрисовка интерполированных кривых

ax.plot(spline_curve[0], spline_curve[1], lw=2, color='w')

# Сохранение изображения

plt.savefig('slide_2_paint_image.png')

plt.show() # Отобразить график

