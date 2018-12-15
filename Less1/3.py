# -*- coding: utf-8 -*-

# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ. Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random
ALPHABET = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

int_number1 = int(input('Введите певрое число диапазона: '))
int_number2 = int(input('Введите второе число диапазона: '))

print(f'Случайное целое число диапазона от {int_number1} до {int_number2}: {random.randint(int_number1, int_number2)}')

float_number1 = float(input('Введите певрое вещественное (2 знака после запятой) число диапазона: '))
float_number2 = float(input('Введите второе вещественное (2 знака после запятой) число диапазона: '))

float_result = random.randint(int(float_number1 * 100), int(float_number2 * 100)) / 100

print(f'Случайное вещественное число диапазона от {float_number1} до {float_number2}: {float_result}')

letter1 = input('Введите певую латинскую букву диапазона: ')
letter2 = input('Введите вторую латинскую букву диапазона: ')

letter_result = ALPHABET[random.randint(ALPHABET.index(letter1), ALPHABET.index(letter2))]

print(f'Случайное буква диапазона от {letter1} до {letter2}: {letter_result}')
