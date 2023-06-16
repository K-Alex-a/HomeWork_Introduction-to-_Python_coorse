"""===================================
# Задача 2:
# Найдите сумму цифр трехзначного числа.
Примеры/Тесты:
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
==================================="""

"""
# Вариант #01 (прямой рассчет с проверкой ввода):
"""


def dataInput():
    """
    :return: any value
    """
    number = input('Input a three-digit number: ')
    return number


def checkThreeDigitAndText(number):
    """
    :param number: any value
    :return: valid number between 100 and 999
    """
    while not number.isdigit() or not (100 <= int(number) < 1000) or len(number) != 3:
        number = input('Error! Try again!\nInput a number from 100 to 999: ')
    return int(number)


def directCalculationSumDigit(number):
    """
    :param number: numerical value
    :return: sum of digits
    """
    summa = 0
    for element in range(len(str(number))):
        summa += number % 10
        number //= 10
    return summa


any_number = checkThreeDigitAndText(dataInput())
result = directCalculationSumDigit(any_number)
print(f'The sum of the number {any_number} is {result}({"+".join(str(any_number))})')

"""
# Вариант #02 (через строку для любой длины цифр и проверкой на ввод букв):
"""

# def dataInput():
#     number = input('Input a three-digit number: ')
#     return number
#
#
# def checkNumbersForLetters(number):
#     while not number.isdigit():
#         number = input('Error! Try again!\nInput only numbers: ')
#     return number
#
#
# def sumDigit(number):
#     summa = 0
#     for element in number:
#         summa += int(element)
#     return summa
#
#
# any_number = checkNumbersForLetters(dataInput())
# result = sumDigit(any_number)
# print(f'The sum of the number {any_number} is {result} ({"+".join(any_number)})')

"""
# Вариант #03 (функция sum без проверок(comprecetion)):
"""

# number = input('Input a three-digit number: ')
# print(f'The sum of the number {number} is {sum(int(element) for element in number)}({"+".join(number)})')
