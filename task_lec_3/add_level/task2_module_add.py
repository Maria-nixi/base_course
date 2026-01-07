import numpy as np
n, b, z = int(input()), int(input()), int(input())
c, s, g = int(input()), int(input()), int(input())

a = [n, b, z]
b = [c, s, g]
a1 = np.array(a) * 3
b1 = np.array(b) * 3
f = np.array([a, b, a1, b1])
print(f)
x = int(input())
st, sf = int(input()), int(input())
f[st, sf] = x
print(f)

# slice = a[0:2:1]
# print(slice)

# slice = a[3:0:-1]
# print(slice)

# slice = a[::-1]
# print(slice)

# b = np.array([a, np.array(a) * 3, np.array(a) * 5])
# print(b)

# slice = b[::, 1]
# print(slice)

# slice = b[1, 2:3:1]
# print(slice)

# slice = b[1, 2::1]
# print(slice)