# 1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.


import random


def bubble_sort(arr):
    switched = True
    while switched:
        switched = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                switched = True


if __name__ == '__main__':
    n = 10
    arr = [random.randint(-100, 100) for _ in range(n)]

print(arr)
bubble_sort(arr)
print(arr)
