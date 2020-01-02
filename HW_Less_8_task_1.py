# 1) Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.

import hashlib


def sub_str_count(s):
    sub_str = set()

    for i in range(len(s) + 1):
        for j in range(i + 1, len(s) + 1):
            sub_s = hashlib.sha1(s[i:j].encode('utf-8')).hexdigest()
            sub_str.add(sub_s)
    return len(sub_str)


s = input(' Введите строку : ')

print(f' В строке "{s}" {sub_str_count(s)} подстрок ')
