import matplotlib.pyplot as plt
import numpy as np

img = plt.imread("crab_nebula.jpg")
fig, ax = plt.subplots()
ax.imshow(img, extent=[0, 640, 0, 640])


def circle(R, x0, y0, starst, stop, step):
    t=np.arange(starst, stop, step)
    x = x0 + R * np.cos(t)
    y = y0 + R * np.sin(t)
    return x, y


plt.plot([142, 139], [380, 373], lw=2, color='w')
plt.savefig('slide_1_paint_image.png')


coords = circle(54, 68, 162, np.pi/2+np.pi/7, 3*np.pi/2.2, 0.1)
plt.plot(coords[0], coords[1], lw=2, color='w')
plt.savefig('slide_1_paint_image.png')

coords = circle(37, 50, 250, np.pi/3+np.pi/4, 3*np.pi/2, 0.1)
plt.plot(coords[0], coords[1], lw=2, color='w')
plt.savefig('slide_1_paint_image.png')

coords = circle(90, 180, 280, np.pi/np.pi+0.5, 2*np.pi-np.pi/1.01, 0.1)
plt.plot(coords[0] - 50, coords[1] + 5, lw=2, color='w')
plt.savefig('slide_1_paint_image.png')

coords = circle(50, 230, 410, np.pi/np.pi+0.01, 2*np.pi-np.pi/1.3, 0.1)
plt.plot(coords[0] - 50, coords[1] + 5, lw=2, color='w')
plt.savefig('slide_1_paint_image.png')


coords = circle(55, 315, 450, np.pi/np.pi+0.05, 2*np.pi-np.pi/1.05, 0.1)
plt.plot(coords[0] - 50, coords[1] + 5, lw=2, color='w')
plt.savefig('slide_1_paint_image.png')

coords = circle(55, 400, 500, np.pi/np.pi+0.05, 2*np.pi-np.pi/1.05, 0.1)
plt.plot(coords[0] - 50, coords[1] + 5, lw=2, color='w')
plt.savefig('slide_1_paint_image.png')


coords = circle(140, 458, 440, 2*np.pi-np.pi/5, 2*np.pi+np.pi/1.4, 0.1)
plt.plot(coords[0], coords[1], lw=2, color='w')
plt.savefig('slide_1_paint_image.png')

coords = circle(70, 522, 310, 2*np.pi-np.pi/3, 2*np.pi+np.pi/4, 0.1)
plt.plot(coords[0], coords[1], lw=2, color='w')
plt.savefig('slide_1_paint_image.png')


coords = circle(70, 220, 115, np.pi+np.pi/6, 2*np.pi-np.pi/3.5, 0.1)
plt.plot(coords[0], coords[1], lw=2, color='w')
plt.savefig('slide_1_paint_image.png')

coords = circle(85, 117, 155, np.pi+np.pi/6, 2*np.pi-np.pi/3, 0.1)
plt.plot(coords[0], coords[1], lw=2, color='w')
plt.savefig('slide_1_paint_image.png')

coords = circle(45, 300, 90, np.pi+np.pi/5, 2*np.pi-np.pi/20, 0.1)
plt.plot(coords[0], coords[1], lw=2, color='w')
plt.savefig('slide_1_paint_image.png')

coords = circle(45, 380, 108, np.pi+np.pi/4.5, 2*np.pi+np.pi/8, 0.1)
plt.plot(coords[0], coords[1], lw=2, color='w')
plt.savefig('slide_1_paint_image.png')

coords = circle(90, 487, 188, np.pi+np.pi/4.5, 2*np.pi+np.pi/4, 0.1)
plt.plot(coords[0], coords[1], lw=2, color='w')
plt.savefig('slide_1_paint_image.png')

#----------------------------------------------------
# это то что внутри

# coords = circle(90, 413, 410, np.pi+np.pi/1.4, 2*np.pi+np.pi/1.5, 0.1)
# plt.plot(coords[0], coords[1], lw=2, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(160, 443, 328, np.pi/np.pi+0.7, 2*np.pi-np.pi, 0.1)
# plt.plot(coords[0] - 50, coords[1] + 5, lw=2, color='w')
# plt.savefig('slide_2_paint_image.png')

# plt.plot([233, 247], [336, 325], lw=2, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(30, 220, 310, 2*np.pi-np.pi/1.5, 2*np.pi+np.pi/6, 0.1)
# plt.plot(coords[0], coords[1], lw=2, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(20, 242, 263, np.pi/np.pi+0.08, 2*np.pi-np.pi/1.08, 0.1)
# plt.plot(coords[0] - 50, coords[1] + 5, lw=2, color='w')
# plt.savefig('slide_2_paint_image.png')

# plt.plot([170, 130], [265, 300], lw=2, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(37, 138, 262, np.pi/3+np.pi/4, 3*np.pi/2, 0.1)
# plt.plot(coords[0], coords[1], lw=2, color='w')
# plt.savefig('slide_2_paint_image.png')


# coords = circle(30, 158, 200, 2*np.pi-np.pi/5, 2*np.pi+np.pi/1.4, 0.1)
# plt.plot(coords[0], coords[1], lw=2, color='w')
# plt.savefig('slide_2_paint_image.png')


# coords = circle(30, 210, 190, np.pi+np.pi/8, 2*np.pi-np.pi/5, 0.1)
# plt.plot(coords[0], coords[1], lw=2, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(30, 315, 165, np.pi/np.pi-1, 2*np.pi-np.pi/1, 0.1)
# plt.plot(coords[0] - 50, coords[1] + 5, lw=2, color='w')
# plt.savefig('slide_2_paint_image.png')


# coords = circle(35, 320, 198, np.pi+np.pi/4.5, 2*np.pi+np.pi/8, 0.1)
# plt.plot(coords[0], coords[1], lw=2, color='w')
# plt.savefig('slide_2_paint_image.png')


# coords = circle(30, 430, 210, np.pi+np.pi/4.5, 2*np.pi+np.pi/8, 0.1)
# plt.plot(coords[0], coords[1], lw=2, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(45, 475, 295, np.pi/3+np.pi/4.5, 3*np.pi/2.2, 0.1)
# plt.plot(coords[0], coords[1], lw=2, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(20, 423, 200, np.pi/np.pi-0.4, 2*np.pi-np.pi/1, 0.1)
# plt.plot(coords[0] - 50, coords[1] + 5, lw=2, color='w')
# plt.savefig('slide_2_paint_image.png')

# plt.plot([393, 410], [213, 190], lw=2, color='w')
# plt.savefig('slide_2_paint_image.png')

# plt.plot([455, 459], [254, 210], lw=2, color='w')
# plt.savefig('slide_2_paint_image.png')