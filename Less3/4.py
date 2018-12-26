# -*- coding: utf-8 -*-

# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10
MIN = 1
MAX = 100

test_list = [random.randint(MIN, MAX) for _ in range(SIZE)]
print(test_list)

# сюда будем записывать значения найденные в результате поиска по массиву
max_num = 0
index_max = 0
min_num = MAX
index_min = 0
# сюда будем приплюсовывать сумму элементов
found_sum = 0

for index, value in enumerate(test_list):
    if value > max_num:
        max_num = value
        index_max = index
    if value < min_num:
        min_num = value
        index_min = index

if abs(index_min - index_max) == 1:
    print(f'{max_num} => {index_max} ; {min_num} => {index_min}\n'
          f'Нет элементов между MAX и MIN')
elif index_min - index_max == 0:
    print('В массиве только один элемент')
elif index_min > index_max:
    for i in range(index_max+1, index_min):
        found_sum += test_list[i]
    print(f'{max_num} => {index_max} ; {min_num} => {index_min}\n'
          f'Cумма элементов между Мин и Макс {found_sum}')
elif index_min < index_max:
    for i in range(index_min+1, index_max):
        found_sum += test_list[i]
    print(f'{max_num} => {index_max} ; {min_num} => {index_min}\n'
          f'Cумма элементов между Мин и Макс {found_sum}')

