# -*- coding: utf-8 -*-

# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

# функция получения суммы числа
def get_sum(num):
    num_sum = 0
    while num > 0:
        short_number = num // 10
        last_numeral = num - short_number * 10
        num_sum += last_numeral
        num = short_number
    return num_sum


max_sum = 0
found_number = 0
while True:
    number = abs(int(input('Введите натуральное число(выход 0): ')))
    if number == 0:
        break
    else:
        num_sum = get_sum(number)
        if num_sum > max_sum:
            max_sum = num_sum
            found_number = number

print(f'\n'
      f'Число {found_number} имеет наибольшую сумму цифр равную: {max_sum}')
