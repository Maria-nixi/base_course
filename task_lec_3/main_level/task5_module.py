'''В числовой массив из предыдущей задачи поменять местами два столбца, 
т. е. все элементы одного столбца поставить на соответствующие им позиции другого,
 а элементы второго переместить в первый.'''

import numpy as np


N = 3
M = 4
i = 1
j = 1
trigonometry_array = np.zeros((N, M))
trigonometry_array[i, j] = np.sin(N * i + M * j + 1)

a = [1, 5, 3, 6]
d = [1, 6, 3, 6]


b = np.array([a, np.array(a)*3, d])
print(b)
print(trigonometry_array)

slice1 = trigonometry_array[::, 0]
print(slice1)

slice2 = trigonometry_array[::, 1]
print(slice2)

trigonometry_array[::, 0] = slice2
trigonometry_array[::, 1] = slice1

print(trigonometry_array)



