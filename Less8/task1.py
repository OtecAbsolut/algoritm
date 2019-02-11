# -*- coding: utf-8 -*-

# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
from binarytree import bst, Node, tree
from collections import Counter
from collections import defaultdict
import uuid
import datetime
import copy

# !!!!!!!!!!!!!! Начало скрипта ввод исходной строки!!!!!!!!!!!!!!!!!!!!!!
start_string = input('Введите вашу строку(которую мы потом закодируем!): ')
# start_string = 'beep boop beer!'

print(f'Начальная строка => {start_string}', '\n')
each_element_count = Counter(start_string)  # считаем околичество каждого символа


# print(each_element_count)

# Функция сортировка словаря по значению
def sort_dict(each_element_count):
    sort_key = sorted(each_element_count,
                      key=each_element_count.get)  # получаем список ключей от словаря отсортированных по значени.
    result = defaultdict()
    for i in sort_key:
        result[i] = each_element_count[i]

    return result


sorted_dict = sort_dict(each_element_count)
print(f'Отсрортированный словарь значений:\n{sorted_dict}')

# Приводим словарь с списук для удобства последующей сортировки
list_ = []
for key, value in sorted_dict.items():
    list_.append([key, value])

copy_list = copy.deepcopy(list_)


def main_sort(lis):
    copy_ = copy.deepcopy(lis)
    if len(copy_) == 2:
        new_key = copy_[0][0] + copy_[1][0]
        new_value = copy_[0][1] + copy_[1][1]
        for index, value in enumerate(list_):
            if new_value <= value[1]:
                list_.insert(index, [new_key, new_value])
                break
            elif new_value > value[1] and index == (len(list_) - 1):
                list_.append([new_key, new_value])
                break
            elif new_value < value[1] and new_value > list_[index - 1][1]:
                list_.insert(index, [new_key, new_value])
                break
        return 'finish'

    elif len(copy_) == 1:
        new_key = copy_[0][0]
        new_value = copy_[0][1]
        last_key = list_[-1][0]
        last_value = list_[-1][1]
        if new_value > last_value:
            list_.append([new_key + last_key, new_value + last_value])
        else:
            list_.append([last_key + new_key, new_value + last_value])
        return 'finish'

    lis1, lis2 = copy_.pop(0), copy_.pop(0)
    # print(copy_)
    new_key = lis1[0] + lis2[0]
    new_value = lis1[1] + lis2[1]
    for index, value in enumerate(list_):
        if new_value <= value[1]:
            list_.insert(index, [new_key, new_value])
            break
        elif new_value > value[1] and index == (len(list_) - 1):
            list_.append([new_key, new_value])
            break
        elif new_value < value[1] and new_value > list_[index - 1][1]:
            list_.insert(index, [new_key, new_value])
            break
    for index, value in enumerate(copy_):
        if new_value <= value[1]:
            copy_.insert(index, [new_key, new_value])
            break
        elif new_value > value[1] and index == (len(copy_) - 1):
            copy_.append([new_key, new_value])
            break
        elif new_value < value[1] and new_value > list_[index - 1][1]:
            copy_.insert(index, [new_key, new_value])
            break

    return main_sort(copy_)


main_sort(copy_list)
print('*********************Печатаем все дерево в строчку***************************')
print(list_)

branches = []
for ind, value in enumerate(list_):
    dict_branch = []
    if len(value[0]) == 1:
        for value2 in list_:
            if value[0] in value2[0]:
                dict_branch.append(value2)
        branches.append(dict_branch)

print('**********************Ветки нашего дерева*********************************')
for i in branches:
    print(i)


# Функция которая проверяет слев или справа листочек дерева и соответвенно возвращает либо 0 либо 1
# first_node в нашем случае это большая строка напрмиер 'b or!pe', next_node это 'r!pe', функция вернет соответвенно 1
def right_or_left(first_node, next_node):
    for i, symbol in enumerate(first_node):
        if next_node[0] == symbol:
            if i == 0:
                return '0'
            else:
                return '1'


# Тут создаем таблицу символов прогоняю каждую ветку по циклу проверок
result_dict = defaultdict()
for branch in branches:
    rev_branch = list(reversed(branch))
    num_code = ''
    for i, node in enumerate(rev_branch):
        if (i + 1) == (len(rev_branch) - 1):
            first_node = node[0]
            next_node = rev_branch[i + 1][0]
            num_code += right_or_left(first_node, next_node)
            result_dict[next_node] = num_code
            break

        first_node = node[0]
        next_node = rev_branch[i + 1][0]
        num_code += right_or_left(first_node, next_node)

# Выводим на печать таблицу символов:
print('\n', 'Таблица символов\n',
      '***************')
for key, value in result_dict.items():
    print(f'     {key} => {value}')
print('***************')

# Печатаем нашу строку в закодированном виде
result_string = ''
for i in start_string:
    result_string += result_dict[i] + ' '

print('\n', '********Закодированная строка****************')
print(result_string)
print('*******************************************')


# Функция раскодирования обратно с троку
def decode_string(string, result_dict):
    string = string.split(' ')
    result = ''
    for i in string:
        for key, value in result_dict.items():
            if value == i:
                result += key
    return result

print(f'\nОбратное кодирование символов в строку:\n{decode_string(result_string, result_dict)}')