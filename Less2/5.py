# -*- coding: utf-8 -*-
# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

n = abs(int(input('Введите количество элементов: ')))
found_sum = 1
start_num = 1

for i in range(n):
    reside = i % 2
    if reside == 0:
        found_sum -= start_num/2
        print(f'-{start_num/2}')
    else:
        found_sum += start_num/2
        print(f'+{start_num/2}')
    start_num = start_num/2

print(f'Сумма последовательности: {found_sum}')