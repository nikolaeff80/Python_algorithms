# 2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random


def merge_sort(arr):
    s = len(arr)
    if s < 2:
        return arr

    left_arr = merge_sort(arr[:s // 2])
    right_arr = merge_sort(arr[s // 2:s])

    i = j = 0
    sorted_arr = []
    while i < len(left_arr) or j < len(right_arr):
        if not i < len(left_arr):
            sorted_arr.append(right_arr[j])
            j += 1
        elif not j < len(right_arr):
            sorted_arr.append(left_arr[i])
            i += 1
        elif left_arr[i] < right_arr[j]:
            sorted_arr.append(left_arr[i])
            i += 1
        else:
            sorted_arr.append(right_arr[j])
            j += 1
        print(sorted_arr)
    return sorted_arr


if __name__ == '__main__':
    arr = [float(random.randint(0, 50)) for i in range(10)]

    print(arr)
    arr = merge_sort(arr)
    print(arr)
