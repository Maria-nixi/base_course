import numpy as np
import matplotlib.pyplot as plt

V_KM_H = 150000  # км/с
V_S_KM_H = 300000000  # км/с (приблизительно)
V_S_PRO = 0.005  # 0.5% от скорости света
R_S_Y = 5.5  # световых лет
PS_S_Y = 0.306601  # парсек на световой год

V_D_S = V_KM_H / V_S_KM_H
print(f"Скорость расширения туманности: {V_KM_H} км/с ({V_D_S:.4f} от скорости света)")

S_Y_PIX = 100
R_PIX = R_S_Y * S_Y_PIX
print(f"Радиус туманности в пикселях (при масштабе {S_Y_PIX} пикселей/световой год): {R_PIX} пикселей")

x_coords = np.linspace(-R_PIX, R_PIX, 20)
y_coords = np.linspace(-R_PIX, R_PIX, 20)
x, y = np.meshgrid(x_coords, y_coords)

r = np.sqrt(x**2 + y**2)
r[r == 0] = 1e-6

max_v_pix = 5
u = x / r * (max_v_pix * (r / R_PIX))
v = y / r * (max_v_pix * (r / R_PIX))

plt.figure(figsize=(8, 8))
plt.quiver(x, y, u, v, angles='xy', scale_units='xy', scale=1, color='blue')

circle = plt.Circle((0, 0), R_PIX, color='red', fill=False, linestyle='--', linewidth=1)
plt.gca().add_patch(circle)

plt.xlim([-R_PIX * 1.1, R_PIX * 1.1])
plt.ylim([-R_PIX * 1.1, R_PIX * 1.1])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.savefig("crab_nebula_velocity_field.png")
