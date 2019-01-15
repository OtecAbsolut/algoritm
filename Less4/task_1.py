# -*- coding: utf-8 -*-

# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random
import cProfile
import sys

sys.setrecursionlimit(3000)

MIN = -1000
MAX = 1000


# АЛГОРИТМ №1 ----------------------------------------------------------------
def two_min(*args):
    # сюда будем записывать значения найденные в результате поиска по массиву
    result = {'first': float('inf'), 'second': float('inf')}

    for value in args:
        if value < result['first']:
            result['second'] = result['first']
            result['first'] = value
        elif value >= result['first'] and value < result['second']:
            result['second'] = value

    return result["first"], result["second"]


# функция запуска для оценки времени где 'n' это SIZE массива
def start(n):
    test_list = [random.randint(MIN, MAX) for _ in range(n)]
    return two_min(*test_list)


# 100 loops, best of 3: 14.8 usec per loop : n = 10
# 100 loops, best of 3: 141 usec per loop : n = 100
# 100 loops, best of 3: 1.39 msec per loop: n = 1000
# cProfile.run('start(1000)')
# 1    0.000    0.000    0.000    0.000 task_1.py:14(two_min)
# 1    0.000    0.000    0.002    0.002 task_1.py:33(start)
# ----------------------------------------------------------------------

# АЛГОРИТМ №2 --------------------------------------------------------
def two_min2(min1, min2, *args):
    if len(args) == 1:
        value = args[0]
        if value < min1:
            min2 = min1
            min1 = value
        elif value >= min1 and value < min2:
            min2 = value
        return min1, min2

    value = args[0]
    if value < min1:
        min2 = min1
        min1 = value
    elif value >= min1 and value < min2:
        min2 = value
    args = args[1:]
    return two_min2(min1, min2, *args)


def start2(n):
    test_list = [random.randint(MIN, MAX) for _ in range(n)]
    return two_min2(float('inf'), float('inf'), *test_list)


# 100 loops, best of 3: 18.6 usec per loop : n = 10
# 100 loops, best of 3: 357 usec per loop : n = 100
# 100 loops, best of 3: 7.61 msec per loop : n = 1000
# cProfile.run('start2(1000)')
# 1000/1    0.026    0.000    0.027    0.027 task_1.py:46(two_min2)
# 1         0.000    0.000    0.031    0.031 task_1.py:66(start2)
#------------------------------------------------------------------


# Функция тестирования алгоритмов
def test_min(func):
    test_tuples = [[-15, -10, 0, 3, 5, 7],  # min -15, -10
                   [1, 2, 9, 6, 3, 16, 22, 0],  # min 0, 1
                   [2, 9, 6, 3, 16, 22, 0, 1],  # min 0, 1
                   [2, 9, 6, 3, 16, 22, 1, 0],  # min 0, 1
                   [0, 2, 9, 6, 3, 16, 22, 1],  # min 0, 1
                   [10, 2, 9, 6, 3, 16, 22, 11],  # min 2, 3
                   [10, 3, 9, 6, 2, 16, 22, 11],  # min 2, 3
                   [10, 20, 9, 2, 3, 16, 22, 11],  # min 2, 3
                   [10, 20, 9, 3, 2, 16, 22, 11],  # min 2, 3
                   [-10, -20, -9, -39, -29, -16, -22, -11]]  # min -39, -29

    answer = ((-15, -10), (0, 1), (0, 1), (0, 1), (0, 1), (2, 3), (2, 3), (2, 3), (2, 3), (-39, -29))
    for i, tup in enumerate(test_tuples):
        # one, two = func(*tup)     # Тест АЛГОРИТМА №1  test_min
        one, two = func(float('inf'), float('inf'), *tup)  # Тест АЛГОРИТМА №1  test_min
        assert answer[i][0] == one and answer[i][1] == two
        print(f'Test {i + 1} => ОК')

# test_min(two_min2)
# test_min(two_min)
'''
Вывод:
Пример достаточно синтетический, прошу не судить строго, рекурсию пришлось прикрутить дабы был какой то второй вариант
и было с чем сравнивать.

Данные по Алгоритму №1
14.8 usec ; n = 10
141 usec  ; n = 100
1.39 msec ; n = 1000
Явная линейная зависимость O(n)

Данные по алгоритму №2
18.6 usec  : n = 10
357 usec   : n = 100
7.61 msec  : n = 1000
Тут уже видно что сложность растет не линейно O(n**2), похоже на параболу вида y = 8/1000* x^2 
Bывод очевиден первый алгоритм лучше и быстрее.

'''