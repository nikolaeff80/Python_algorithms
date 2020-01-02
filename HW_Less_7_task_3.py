# 3) Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
# называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой — не больше медианы.
import random


def median(lst):
    if len(lst) % 2 == 0:
        middle = []

        for i in lst:
            b = 0

            for j in lst:

                if i < j:
                    b += 1

            if len(lst) == b * 2 + 2 or len(lst) == b * 2:
                middle.append(i)
        return sum(middle) / 2

    else:
        for i in lst:
            num = i
            b = 0

            for j in lst:

                if i < j:
                    b += 1

            if len(lst) == 2 * b + 1:
                return num


if __name__ == '__main__':
    m = random.randint(1, 10)
    size = 2 * m + 1
    arr = [random.randint(1, 50) for i in range(size)]

print(f'Исходный список: \n{(arr)}')
print(f'\nМедиана: {median(arr)}\n')
print(f': \n{sorted(arr)}')
