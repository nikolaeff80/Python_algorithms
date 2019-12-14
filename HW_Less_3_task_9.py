# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
arr = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(5)] for _ in range(3)]
print(*arr, sep='\n')

min_val = -1        # Диапазон от 0 до 99, задаем минимальное значение
for j in range(len(arr)):
    max_val = 100       # Диапазон от 0 до 99, задаем максимальное значение
    for i in range(len(arr)):
        if arr[i][j] < max_val:
            max_val = arr[i][j]
    if max_val > min_val:
        min_val = max_val
print('Максимальный элемент среди минимальных элементов столбцов матрицы:  ', min_val)
