# -*- coding: utf-8 -*-

# https://drive.google.com/file/d/1BdkG3aGYL45TRy1jnYTMde5fggkiaGQW/view?usp=sharing

# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

# функция с рекурсией которая считает количество цифр встречающиеся в числе
def get_quantity(number, numeral, counter=0):
    num = number // 10
    if num == 0 and number == numeral:
        counter += 1
        return counter
    elif num == 0:
        return counter

    if (number - num * 10) == numeral:
        counter += 1
    return get_quantity(num, numeral, counter)


quantity = int(input('Укажите кол-во чисел которые вы собираетесь ввести: '))
numeral = int(input('Укажите ОДНУ цифру которую будем считать в последовательности чисел: '))

counter = 0
for i in range(quantity):
    number = int(input(f'Введите число № {i+1}: '))
    counter += get_quantity(number, numeral)
print(f'\n'
      f'Ваше число {numeral}, встретилось в числах {counter} раз(а)')
