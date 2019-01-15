# -*- coding: utf-8 -*-

# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»

# Примечание ко всему домашнему заданию:
# Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.

import cProfile
import math


# ---------------------------------------------------------------------------------------------------------
# Алгоритм №1 (handmade без решета) будем пользоваться тем, что простое число делится на цело только на 1 и на само себя.
# Алгоритм жутковатый конечно...
def simple(n):
    i = 1  # перебор простых чисел, начинается с 2-х
    counter = 0
    num = int(2 * n * math.log1p(2 * n))
    k = int(math.log(num))

    exept = set()
    while counter < n:
        i += 1
        count = 0
        for i_2 in range(1, i + 1):
            if i % i_2 == 0:
                count += 1
            if count == 2 and i_2 != i:
                count += 1
                break
        if count == 2:
            counter += 1
    return i


# 100 loops, best of 3: 21.6 usec per loop ; n = 10
# 100 loops, best of 3: 72.8 usec per loop ; n = 20
# 100 loops, best of 3: 155 usec per loop  ; n = 30
# 100 loops, best of 3: 424 usec per loop  ; n = 50
# 100 loops, best of 3: 1.86 msec per loop ; n = 100
# 100 loops, best of 3: 295 msec per loop ; n = 1000
# 100 loops, best of 3: 2.11 sec per loop ; n = 2500
# 1 loops, best of 3: 39.8 sec per loop ; n = 10 000
# cProfile.run('simple(100)')
# 1    0.002    0.002    0.002    0.002 task_2.py:15(simple)
# --------------------------------------------------------------------

# АЛГОРИТМ №2 (с решетом)
def sieve(n):
    num = int(2 * n * math.log1p(2 * n))
    lst = [i for i in range(num + 1)]
    lst[1] = 0
    for i in range(2, num):
        if lst[i] * 2 > num:
            break
        if lst[i] != 0:
            j = i + i
            while j <= num:
                lst[j] = 0
                j += i
    result = [i for i in lst if i != 0]
    return result[n - 1]


# 100 loops, best of 3: 12.3 usec per loop ; n = 10
# 100 loops, best of 3: 30.3 usec per loop; n = 20
# 100 loops, best of 3: 50 usec per loop ; n = 30
# 100 loops, best of 3: 107 usec per loop ; n = 50
# 100 loops, best of 3: 266 usec per loop ; n = 100
# 100 loops, best of 3: 4.5 msec per loop ; n = 1000
# 100 loops, best of 3: 13.7 msec per loop; n = 2500
# 100 loops, best of 3: 73.2 msec per loop; n = 10 000
# 1 loops, best of 3: 1.16 sec per loop ; n = 100 000
# 1 loops, best of 3: 14.6 sec per loop ; n = 1 000 000

# cProfile.run('sieve(10000)')
# 1    0.005    0.005    0.095    0.095 <string>:1(<module>)
# 1    0.075    0.075    0.090    0.090 task_2.py:49(sieve)
# 1    0.009    0.009    0.009    0.009 task_2.py:51(<listcomp>)
# 1    0.006    0.006    0.006    0.006 task_2.py:61(<listcomp>)
# 1    0.000    0.000    0.095    0.095 {built-in method builtins.exec}
# ------------------------------------------------------------------------

# Функция тестирования
def test(func):
    lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for index, i in enumerate(lst, start=1):
        assert func(index) == i
        print(f'Test {index} => OK')

# print(simple(1000))
print(sieve(2500))
# test(simple)
# test(sieve)
