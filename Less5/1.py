# -*- coding: utf-8 -*-

# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести
# наименования предприятий, чья прибыль ниже среднего.

from collections import defaultdict

count = int(input('Введите пож-та количество предприятий: '))

data = defaultdict(int)
for i in range(1, count+1):
    while True:
        key = input(f'Введите название {i} предприятия: ')
        if key != '' and key not in data.keys():
            break
        else:
            print('Введите нормальное название')
    for n in range(1, 5):
        marj = int(input(f'Введите прибыль за {n} квартал для предприятия {key}: '))
        data[key] += marj
    print('----------------------------------')

mid = sum(data.values())/count

for key, value in data.items():
    if value < mid:
        print(f'Ниже среднего - {key}')
    elif value > mid:
        print(f'Выше среднего - {key}')