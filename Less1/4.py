# -*- coding: utf-8 -*-

# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

ALPHABET = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

first_letter = input('Введите первую латинску букву: ')
second_letter = input('Введите вторую латинску букву: ')

print(f'\n'
      f'Позиция первой буквы: {ALPHABET.index(first_letter)}\n'
      f'Позиция второй буквы: {ALPHABET.index(second_letter)}\n'
      f'Букв между ними: {ALPHABET.index(second_letter) - ALPHABET.index(first_letter) - 1}')
