"""===========================================================================
Задача 18:
Требуется найти в массиве A[1..N] самый близкий по величине элемент
к заданному числу X.
Пользователь вводит натуральное число N – количество элементов в массиве и число,
которое необходимо проверить - X.
Заполните массив случайными натуральными числами от 1 до N.
Выведите, ближайший к X элемент. Если есть несколько элементов,
которые равноудалены от X, выведите наименьший по величине.

Ввод: 10
Ввод: 7
1 2 1 8 9 6 5 4 3 4
Вывод: 6
==========================================================================="""

"""
Вариант_01 (бинарный поиск ближайших элементов к искомому)
"""
from random import randint

length_list = int(input('Input length array: '))
lst = [randint(0, 100) for i in range(length_list)]
print('List received =', *lst)
lst.sort()
print('Sorted list =', *lst)
number_X = int(input('Input the number to look for: '))


def binarySearch(sort_list, number):
    center = len(sort_list) // 2
    left = 0
    right = len(lst) - 1
    while sort_list[center] != number and left <= right:
        if number > sort_list[center]:
            left = center + 1
        else:
            right = center - 1
        center = (left + right) // 2

    if left > right:
        return sort_list[center], sort_list[center+1]
    else:
        return sort_list[center]


if number_X < lst[0]:
    print(f'near number -> {lst[0]}')
elif number_X > lst[len(lst)-1]:
    print(f'near number -> {lst[len(lst)-1]}')
else:
    near_lst = binarySearch(lst, number_X)
    print(near_lst)
    if near_lst == number_X:
        print(f'near number -> {near_lst}')
    else:
        if number_X - near_lst[0] == near_lst[1] - number_X:
            print(f'numbers {near_lst[0]} and {near_lst[1]} equidistant')
        elif number_X - near_lst[0] < near_lst[1] - number_X:
            print(f'near number -> {near_lst[0]}')
        else:
            print(f'near number -> {near_lst[1]}')


"""
Вариант_02 (линейный поиск)
"""
# from random import randint
#
# length_list = int(input('Input length array: '))
# lst = [randint(0, 100) for i in range(length_list)]
# print('List received =', *lst)
# lst.sort()
# print('Sorted list =', *lst)
# number_X = int(input('Input the number to look for: '))
#
# value = abs(number_X - lst[0])
# near_num = lst[0]
#
# for element in lst:
#     difference = abs(number_X - element)
#     if difference < value and element != number_X:
#         value = difference
#         near_num = element
# print(f'Nearest number to {number_X} is {near_num}')
