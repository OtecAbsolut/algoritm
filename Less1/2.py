# -*- coding: utf-8 -*-

# 3. По введенным пользователем координатам двух точек вывести уравнение прямой, проходящей через эти точки.

x1 = int(input('Введите координату x1: '))
y1 = int(input('Введите координату y1: '))
x2 = int(input('Введите координату x2: '))
y2 = int(input('Введите координату y2: '))

k = (y2 - y1) / (x2 - x1)
b = y1 - ((y2 - y1) / (x2 - x1)) * x1

if b > 0:
    print(f'Результат: y = {k}*x + {b}')
elif b < 0:
    print(f'Результат: y = {k}*x {b}')
else:
    print(f'Результат: y = {k}*x')
