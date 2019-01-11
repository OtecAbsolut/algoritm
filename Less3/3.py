# -*- coding: utf-8 -*-

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN = 1
MAX = 10000

test_list = [random.randint(MIN, MAX) for _ in range(SIZE)]

print(f'Исходный массив:\n'
      f'{test_list}')

max_num = 0
index_max = 0
index_min = 0
min_num = MAX

for index, value in enumerate(test_list):
    if value > max_num:
        max_num = value
        index_max = index
    if value < min_num:
        min_num = value
        index_min = index

test_list[index_max] = min_num
test_list[index_min] = max_num
print(f'Результат:\n'
      f'{test_list}')
print(f'max => {max_num}, min => {min_num}')
