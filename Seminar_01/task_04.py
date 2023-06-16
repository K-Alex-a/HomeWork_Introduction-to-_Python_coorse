"""===================================
# Задача 4:
# Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза
# больше журавликов, чем Петя и Сережа вместе?
Примеры/Тесты:
6 >>>  1  4  1
24 >>> 4  16  4
60 >>> 10  40  10
==================================="""

"""
Вариант #01 (прямой рассчет с проверкой ввода)
"""


def dataInput():
    """
    :return: any value
    """
    value = input('Input number: ')
    return value


def checkNumbersForLetters(value):
    """
    :param value: any value
    :return: any number
    """
    while not value.isdigit():
        value = input('Try Again!\n Input only number: ')
    return int(value)


def parityCheck(number):
    """
    :param number: any number
    :return: even numbers > 2
    """
    while int(number) % 2 == 1 and total_cranes < 2:
        number = int(input('Try Again!\n Input an even number: '))
    return number


def separationOfCranes(number):
    """
    :param number: even numbers > 2
    :return: text result
    """
    third_kid = number // 2
    first_and_second_kid = third_kid // 2
    print(f'Петя и Сережа сделали по {first_and_second_kid} журавлика(ов) '
          f'\nА Катя сделала  {third_kid} журавлика(ов)')


total_cranes = parityCheck(checkNumbersForLetters(dataInput()))
separationOfCranes(total_cranes)

"""
Вариант #02 (...)
"""
#
# total_cranes = int(input('Input the total number of cranes: '))
# print((f'Петя и Сережа сделали по {total_cranes // 4} журавлика(ов) '
#        f'\nА Катя сделала  {total_cranes // 2} журавлика(ов)')
#       if total_cranes % 2 == 0 and total_cranes > 2 else None)
