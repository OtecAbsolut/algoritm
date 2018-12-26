# -*- coding: utf-8 -*-

# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

# диапазон чисел
START = 2
STOP = 99

# генерим словарь для вывода будущих результатов
NUM1 = 2
NUM2 = 9

key = [str(i) for i in range(NUM1, NUM2+1)]
value = [0 for i in range(NUM1, NUM2+1)]
result = dict(zip(key, value))

for i in range(START, STOP+1):
    for j in range(NUM1, NUM2+1):
        if i % j == 0:
           result[str(j)] += 1

for key, value in result.items():
    print(f'Кратны числу {key} => {value}')