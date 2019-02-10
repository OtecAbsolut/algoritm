# -*- coding: utf-8 -*-

# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# то используйте метод сортировки, который не рассматривался на уроках

import random
import timeit
from Less7.task_1 import bubble
import copy

SIZE = 11
MIN = -100
MAX = 100

array = [random.randint(MIN, MAX) for _ in range(SIZE)]
print(f'Было:  {array}')

# Медиана это средний элемент отсортированного массива, в функции ниже считаю количество элементов которые <=

def mid_element(array):
    m = int((len(array) - 1) / 2)
    for ind, num in enumerate(array):
        spam = copy.copy(array)
        count = 0
        spam.pop(ind)
        for index, value in enumerate(spam):
            if value <= num:
                count += 1
            if count > m:
                break
            if index == (len(spam)-1) and count == m:
                return f'"Медиана - {num}'



print(f'Стало: {mid_element(array)}')
# Для удобства проверки печатаем отсортированный массив
print(f'Стало: {bubble(array)}')

