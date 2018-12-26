# -*- coding: utf-8 -*-
'''
2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6
(или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
'''
import random

SIZE = 10
MIN = 1
MAX = 18000

test_list = [random.randint(MIN, MAX) for _ in range(SIZE)]

result = []

for index, value in enumerate(test_list):
    if value % 2 == 0:
        result.append(index)

print(f'Исходный массив:\n'
      f'{test_list}\n'
      f'\n'
      f'Результат:\n'
      f'{result}')
