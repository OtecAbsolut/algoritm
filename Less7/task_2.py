# -*- coding: utf-8 -*-

# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random
import timeit

SIZE = 11
MIN = 0
MAX = 50

array = [random.randint(MIN, MAX) for _ in range(SIZE)]
print(f'Было:  {array}')

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            first_l = left.pop(0)
            result.append(first_l)
        else:
            first_r = right.pop(0)
            result.append(first_r)
    while len(left) > 0:
        result.append(left.pop(0))
    while len(right) > 0:
        result.append(right.pop(0))
    return result

def merge_sort(array):
    if len(array) <= 1:
        return array
    else:
        middle = int(len(array) / 2)
        left = array[0: middle]
        right = array[middle: len(array)]
        left = merge_sort(left)
        right = merge_sort(right)
        result = merge(left, right)
        print(result)
    return result

print(f'Стало: {merge_sort(array)}')

