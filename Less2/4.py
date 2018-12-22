# -*- coding: utf-8 -*-

# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

number = abs(int(input('Введите целое число: ')))


# считаем количество знаков в числе для чисел от 10 до 99 будет 1, для 100 - 999 будет 2
# в дальнейше эту цифры 1 и 2 будем использовать для возведения 10^1 и 10^2 и использовать при реверсе числа
def null_count(number):
    count = 0
    while number >= 10:
        short_number = number // 10
        number = short_number
        count += 1
    return count


# цикл самого реверса числа
new_number = 0
count = null_count(number)
while number > 0:
    short_number = number // 10
    last_numeral = number - short_number * 10
    number = short_number
    if count > 0:
        new_number += last_numeral * (10 ** count)
        count -= 1
    else:
        new_number += last_numeral

print(f'\n'
      f'Получилось число: {new_number}')
