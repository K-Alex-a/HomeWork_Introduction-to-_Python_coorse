"""=================================================================
Задача 16:
Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1.N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai.
Последняя строка содержит число X.
Пример:
5
1 2 3 4 5
3
-> 1
================================================================="""
import random


def binarySearch(sort_list, number):
    center = len(lst) // 2
    left = 0
    right = len(lst) - 1
    while sort_list[center] != number and left <= right:
        if number > sort_list[center]:
            left = center + 1
        else:
            right = center - 1
        center = (left + right) // 2

    if left > right:
        return 'No value'
    else:
        return center


def elementCount(sort_list, number, search_num):
    count = 0
    initial_number = number
    if search_num == sort_list[-1]:
        count += 1
    while sort_list[number] == search_num and number < len(sort_list) - 1:
        count += 1
        number += 1
    while sort_list[initial_number] == search_num:
        count += 1
        initial_number -= 1
    return count - 1


number_N = int(input('Input length array: '))
lst = [random.randint(0, 5) for i in range(number_N)]
print('List received =', *lst)
lst.sort()
print('Sorted list =', *lst)
number_X = int(input('Input the number to look for: '))

found_index = binarySearch(lst, number_X)
found_numbers_element = elementCount(lst, found_index, number_X)
print(f'-> {found_numbers_element}')

