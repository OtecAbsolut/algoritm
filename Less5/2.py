# -*- coding: utf-8 -*-
#
# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import Counter
from collections import defaultdict

ALL_SYMBOL = '123456789abcdef'
COUNT_NUM = 2
chek_set = set(Counter(ALL_SYMBOL).elements())
base_dict = defaultdict(int)
base_value = defaultdict(str)
# Вормируем словарь значений с эквивалентом символа в 10-ой системе исчесления,
# где пара ключ-знач выглядт например так {a:10}
for i, value in enumerate(Counter(ALL_SYMBOL).elements(), start=1):
    base_dict[value] = i
    base_value[i] = value

# получаем от пользователя 2 числа с проверкой на корректность ввода,
# затем переворачиваем его и приводим к структуре: [‘C’, ‘F’, ‘1’]
all_num = []   #сюда пишем числа, добавляем как вложенный список
for i in range(1, COUNT_NUM + 1):
    while True:
        num = input(f'Введите {i} число в 16-ой форме (должно сожержать токалько "{ALL_SYMBOL}"): ')
        each_synb = list((Counter(num).elements()))
        chek_num = set(each_synb)
        if chek_num <= chek_set:
            print('Число принято')
            all_num.append(each_synb)
            break

print(f'Число №1: {all_num[0]} \nЧисло №2: {all_num[1]}')

# Возвращает сумму в 10-м вормате 16-ых чисел
def get_sum(*args):
    ten_sum = 0  # сюда пишем результат сложения в 10-ой системе исчесления
    for num in args:
        each_synb = reversed(num)
        each_synb = list((Counter(each_synb).elements()))
        for index, i in enumerate(each_synb):
            ten_sum += base_dict[i] * (16 ** index)
    return ten_sum

# Возвращает произведение в 10-м формате
def get_multi(*args):
    ten_num = []  # сюда пишем результат сложения в 10-ой системе исчесления
    for num in args:
        one_num = 0
        each_synb = reversed(num)
        each_synb = list((Counter(each_synb).elements()))
        for index, i in enumerate(each_synb):
            one_num += base_dict[i] * (16 ** index)
        ten_num.append(one_num)
    return ten_num[0] * ten_num[1]

# Перевод из 10-го числа в 16-ое
def convert(ten_sum):
    result_sum = []
    while ten_sum > 15:
        i = ten_sum % 16
        ten_sum = ten_sum // 16
        result_sum.append(base_value[i])
        if ten_sum < 16:
            result_sum.append(base_value[ten_sum])
            break
    else:
        result_sum.append(ten_sum)
    return list(reversed(result_sum))


ten_sum = get_sum(*all_num)
ten_multi = get_multi(*all_num)
print('Cумма 2-х чисел равна: ', convert(ten_sum))
print('Произведение 2-х чисел равно: ', convert(ten_multi))
