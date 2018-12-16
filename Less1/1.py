# -*- coding: utf-8 -*-

# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = str(input('Введите 3-х значное число: '))
first = int(number[0])
second = int(number[1])
third = int(number[2])
sum = first + second +  third
print(f'Сумма цифр введенного числа равна: {sum}')
multiply = first * second * third
print(f'Произведение цифр введенного числа: {multiply}')