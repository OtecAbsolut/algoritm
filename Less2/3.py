# -*- coding: utf-8 -*-

# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number = abs(int(input('Введите натуральное число: ')))


# считаем количество знаков в числе для чисел от 10 до 99 будет 1, для 100 - 999 будет 2
# в дальнейше эту цифры 1 и 2 будем использовать для возведения 10^1 и 10^2 и использовать при реверсе числа
def null_count(number):
    count = 0
    while number >= 10:
        short_number = number // 10
        number = short_number
        count += 1
    return count


def even(num, count):
    if count == 0:
        residue = num % 2
        if residue == 0 or num == 0:
            return num
        else:
            return ''

    first_number = num // 10 ** count
    next_number = num - first_number * (10 ** count)
    count -= 1
    residue = first_number % 2
    if residue == 0 or first_number == 0:
        return f'{first_number} {even(next_number, count)}'
    else:
        return even(next_number, count)


def odd(num, count):
    if count == 0:
        residue = num % 2
        if residue != 0:
            return num
        else:
            return ''

    first_number = num // 10 ** count
    next_number = num - first_number * (10 ** count)
    count -= 1
    residue = first_number % 2
    if residue != 0:
        return f'{first_number} {odd(next_number, count)}'
    else:
        return odd(next_number, count)


count = null_count(number)
print(f'\n'
      f'  Четные: {even(number, count)}\n'
      f'Нечетные: {odd(number, count)}')

