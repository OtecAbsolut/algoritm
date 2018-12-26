# -*- coding: utf-8 -*-

# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

MAX = 100
MIN = 1
COLUMNS = 5
ROWS = 5

test_matrix = [[random.randint(MIN, MAX) for _ in range(COLUMNS)] for _ in range(ROWS)]

# генерим список будущих миниальных элементов
min_num =[MAX for _ in range(COLUMNS)]
max_min = 0
print('Исходная матрица:\n'
      '-------------------')
for row in test_matrix:
    print(row)
    for index, number in enumerate(row):
        if number < min_num[index]:
            min_num[index] = number
print('-------------------\n')
print(min_num)

for i in min_num:
    if i > max_min:
        max_min = i
print(f'Максимальное среди минимальных: {max_min}')

