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
        # print(f'Память нарастающим итогом: {wrapper.size}')
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


# ---------------------------------------------------------------------------------------
# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

SIZE = 20
MIN = -1000
MAX = 1000

test_list = [random.randint(MIN, MAX) for _ in range(SIZE)]
print(test_list)

# сюда будем записывать значения найденные в результате поиска по массиву
result = {'first': float('inf'), 'second': float('inf')}

for value in test_list:
    if value < result['first']:
        result['first'] = value
    elif value >= result['first'] and value < result['second']:
        result['second'] = value

print(f'Наименьшие элементы в массиве: {result["first"]}; {result["second"]}')

memory = list(locals().items())

# ----------Цикл прокрутки локальных переменных через функцию подсчета памяти-----------
for i in reversed(memory):
    if i[0] == 'show_size':
        break
    print(i[0], show_size(i[1]))
# --------------------------------------------------------------------------------------
# Вывод программы:
# Я написал декоратор для функции show_size  с урока, этот дерокатор считает вызовы фукнкциии, и суммирует размеры объектов,
# которые проходят через функцию show_size.
# Общее использование памяти всеми переменными в данном скрипт: 1341 Кб
