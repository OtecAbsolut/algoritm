# -*- coding: utf-8 -*-

# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 20
MIN = 1
MAX = 100

test_list = [random.randint(MIN, MAX) for _ in range(SIZE)]
print(test_list)

# сюда будем записывать значения найденные в результате поиска по массиву
result = {'first': MAX, 'second': MAX}

for value in test_list:
    if value < result['first']:
        result['first'] = value
    elif value >= result['first'] and value < result['second']:
        result['second'] = value

print(f'Наименьшие элементы в массиве: {result["first"]}; {result["second"]}')