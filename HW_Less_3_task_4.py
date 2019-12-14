# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(arr)

num = arr[0]
max_freq = 1
for i in range(len(arr)):
    freq = 1
    for k in range(i + 1, (len(arr))):
        if arr[i] == arr[k]:
            freq += 1
    if freq > max_freq:
        max_freq = freq
        num = arr[i]

if max_freq > 1:
    print(f'Число {num} встречается {max_freq} раз(а)')
else:
    print('Нет повторов')
