# -*- coding: utf-8 -*-
# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

def ascii(start, stop, counter=0, len=10):
    counter += 1
    start += 1
    if start < 100:
        space = ' '
    else:
        space = ''
    if start == stop:
        return f'{start} - {chr(start)} ;'
    if counter == len:
        counter = 0
        return f'{space}{start} - {chr(start)};\n' \
               f'{ascii(start, stop, counter)}'
    return f'{space}{start} - {chr(start)} ; {ascii(start, stop, counter)}'


print(ascii(31, 127))
