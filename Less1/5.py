# -*- coding: utf-8 -*-

# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

ALPHABET = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

letter_number = int(input('Введите номер буквы: '))
print(f'Введенная буква с номером {letter_number} это : {ALPHABET[letter_number - 1]}')