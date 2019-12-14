# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(arr)

min_val = arr[0]
max_val = 0


for i in range(len(arr)):
    if min_val > arr[i]:
        min_val = arr[i]
    elif max_val < arr[i]:
        max_val = arr[i]

print(max_val, min_val)

arr[arr.index(max_val)], arr[arr.index(min_val)] = arr[arr.index(min_val)], arr[arr.index(max_val)]

print(arr)
