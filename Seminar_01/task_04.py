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
    :return: even numbers > 6
    """
    while not int(number) % 6 == 0 or number < 6:
        number = int(input('Try Again!\n Input an even number: '))
    return number


def separationOfCranes(number):
    """
    :param number: even numbers > 6
    :return: text result
    """
    first_and_second_kid = number // 6
    third_kid = number - first_and_second_kid * 2
    print(f'Petya and Serezha made  {first_and_second_kid} cranes.'
          f'\nAnd Kate made {third_kid} cranes.')


separationOfCranes(
    parityCheck(
        checkNumbersForLetters(
            dataInput())))

"""
Вариант #02 (...)
"""

# total_cranes = int(input('Input the total number of cranes: '))
# print((f'Petya and Serezha made {total_cranes // 6} cranes.'
#        f'\nAnd Kate made  {total_cranes - ((total_cranes // 6) * 2)} cranes.')
#       if total_cranes % 6 == 0 and total_cranes > 6 else None)
