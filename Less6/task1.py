# -*- coding: utf-8 -*-

# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.


import sys
import random


# -------Функция подсчета объема выделяемой памяти------------
def wrapper(func):
    wrapper.size = 0

    def counter(x, level=0):
        wrapper.size += sys.getsizeof(x)
        func(x, level=0)
        return wrapper.size

    return counter


@wrapper
def show_size(x, level=0):
    print('\t' * level, f'type = {type(x)}, size = {sys.getsizeof(x)}, obj = {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                show_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)


# -----------------------------------------------------------------------
# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
MAX = 100
MIN = -100
COLUMNS = 10
ROWS = 10

test_matrix = [[random.randint(MIN, MAX) for _ in range(COLUMNS)] for _ in range(ROWS)]

# генерим список будущих миниальных элементов
min_num =[float('inf') for _ in range(len(test_matrix))]
max_min = float('-inf')
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

print(f'Максимальное среди минимальных: {max_min}\n')


# ----------Цикл прокрутки локальных переменных через функцию подсчета памяти-----------
memory = list(locals().items())
for i in reversed(memory):
    if i[0] == 'show_size':
        break
    print(i[0], show_size(i[1]))
# --------------------------------------------------------------------------------------
# Вывод программы:
# Я написал декоратор для функции show_size  с урока, этот дерокатор считает вызовы фукнкциии, и суммирует размеры объектов,
# которые проходят через функцию.
# Общее использование памяти всеми переменными в данном скрипте: 6080 Кб
