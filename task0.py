import numpy as np
a = [2, 5, 3, 6]
print(a)
slice = a[0:3:1, 0:2:1]
slice = a[1:3:1, 3:5:1]
slice = a[0:3:1, 5]
slice = a[::, 0:2:1]
slice = a[3::1, 2:4:1]
slice = a[3:4:1, 5::1]