"""========================================
Задача 14:
Требуется вывести все целые степени двойки
(т.е. числа вида 2k),
не превосходящие числа N.
Пример:
10 -> 1 2 4 8
========================================"""

"""
Вариант_01:
"""
import numpy as np


def dataInput():
    """
    :return: any value
    """
    value = input('Input the numbers of coins: ')
    return value


def checkNumbersForLetters(number):
    """
    :param number: any value
    :return: number
    """
    while not number.isdigit():
        number = input('Wrong! Try Again!\n'
                       'Input only the number: ')
    return int(number)


def allPowersOfTwo(number):
    """
    :param number: max number
    :return: integer powers of two
    """
    all_power = []
    count = 0
    while np.power(2, count) <= number:
        all_power.append(np.power(2, count))
        count += 1
    return all_power


num = checkNumbersForLetters(dataInput())
result = allPowersOfTwo(num)
print(f'{num} -> {str(result)[1:-1]}')


"""
Вариант_02 (comprehensive):
"""
# import numpy as np
# num = int(input("Input the numbers of coins: "))
# print(*[np.power(2, i) for i in range(num) if np.power(2, i) <= num])
