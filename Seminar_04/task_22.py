"""===========================================================
Задача 22:
Даны два неупорядоченных набора целых чисел (может быть,
с повторениями). Выдать без повторений в порядке
возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа.
n - кол-во элементов первого множества.
m - кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.
Пример:
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12
==========================================================="""

"""Вариант_01 (через перевод в множество и .intersection)"""

lst_1 = [int(input(f'Input {i} element: ')) for i in range(int(input('Input length first list: ')))]
lst_2 = [int(input(f'Input {i} element: ')) for i in range(int(input('Input length second list: ')))]
print(*lst_1)
print(*lst_2)
new_lst = set(lst_1).intersection(set(lst_2))
print(*new_lst)

"""Вариант_02 (циклами с рандомными списками)"""
# from random import randint
#
# lst_1 = [randint(0, 20) for i in range(randint(0, 10))]
# lst_2 = [randint(0, 20) for i in range(randint(0, 10))]
# print(*lst_1)
# print(*lst_2)
#
# new_lst = []
#
# for i in set(lst_1):
#     for j in set(lst_2):
#         if i == j:
#             new_lst.append(i)
#
# print(*new_lst)
