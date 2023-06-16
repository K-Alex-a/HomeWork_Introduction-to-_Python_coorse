"""===================================================================
# Задача 6:
# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу,
# которая проверяет счастливость билета.
Примеры/Тесты:
385916 >>> yes
123456 >>> no
==================================================================="""

"""
Вариант через срезы
"""


def dataInput():
    """
    :return: any value
    """
    value = input('Input a three-digit number: ')
    return value


def checkNumbersForLettersAndLength(number):
    """
    :param number: any value
    :return: valid number between 100000 and 999999
    """
    while not number.isdigit() or len(number) != 6:
        number = input('Wrong. Try again!'
                       '\nInput 6 digit: ')
    return number


def checkLuckyTicket(number):
    """
    :param number: any number
    :return: True or False
    """
    half_length = int(len(number))//2
    sum_left_half = sum_right_half = 0
    total_sum = False
    for element in number[:half_length]:
        sum_left_half += int(element)
    for element in number[half_length:]:
        sum_right_half += int(element)
    if sum_left_half == sum_right_half:
        total_sum = True
    return total_sum


ticket = checkNumbersForLettersAndLength(dataInput())
print(f'Wow! You got {ticket} a lucky ticket!' if checkLuckyTicket(ticket) is True
      else 'Good luck next time.')
