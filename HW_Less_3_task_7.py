# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(arr)

if arr[0] > arr[1]:
    min_val1 = 0
    min_val2 = 1
else:
    min_val1 = 1
    min_val2 = 0

for i in range(2, (len(arr))):
    if arr[i] < arr[min_val1]:
        b = min_val1
        min_val1 = i
        if arr[b] < arr[min_val2]:
            min_val2 = b
    elif arr[i] < arr[min_val2]:
        min_val2 = i

print(f'Первый минимальный элемент  {arr[min_val1]}')
print(f'Второй минимальный элемент  {arr[min_val2]}')
