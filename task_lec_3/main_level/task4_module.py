import numpy as np

'''Создайте двумерный массив trigonometry_array размером N x M, 
каждый элемент которого вычисляется по формуле trigonometry_array[i, j] = sin(N · i + M · j + 1). 
Если полученный таким образом элемент массива отрицателен, то замените его на 0. Выведите конечный массив на экран.'''

N = 3
M = 4
i = 1
j = 1
trigonometry_array = np.zeros((N, M))
trigonometry_array[i, j] = np.sin(N * i + M * j + 1)

for elem trigonometry_array[i, j]:
    if elem <= 0:
        elem = 0
print(trigonometry_array)
