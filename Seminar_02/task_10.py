"""====================================
Задача 10:
На столе лежат n монеток.
Некоторые из них лежат вверх решкой,
а некоторые – гербом.
Определите минимальное число монеток,
которые нужно перевернуть,
чтобы все монетки были повернуты
вверх одной и той же стороной.
Выведите минимальное количество монет,
которые нужно перевернуть.
Пример:
5 -> 1 0 1 1 0
2
===================================="""
from random import randint

"""
Вариант (прямое решение через список и линейный подсчет)
"""


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
        number = input('Wrong! Try again!\n'
                       'Input only the number:')
    return int(number)


def randomList(number: int):
    """
    :param number: length list
    :return: random list
    """
    random_list = [0] * number
    for element in range(number - 1):
        random_list[element] = randint(0, 1)
    return random_list


def repetitionCount(random_list):
    """
    :param random_list: list of values
    :return: number of duplicate values
    """
    null = 0
    one = 0
    for element in range(len(random_list)):
        null += 1 if random_list[element] == 0 else 0
        one += 1 if random_list[element] == 1 else 0
    return null, one


def compareValues(number_first, number_second):
    """
    :param number_first: any number
    :param number_second: number
    :return: more number
    """
    if number_second == number_first:
        return f'any {number_first} eagle or {number_second} tails'
    elif number_first < number_second:
        return f'{number_first} eagle'
    else:
        return f'{number_second} tails'


total_coins = checkNumbersForLetters(dataInput())
random_binary_list = randomList(total_coins)
number_eagle_and_tails = repetitionCount(random_binary_list)
result = compareValues(number_eagle_and_tails[0], number_eagle_and_tails[1])
print(f'Total coins => {total_coins}\n'
      f'Here they are: {str(random_binary_list)[1:-1]}.\n'
      f'Where 0 -> is eagle, and 1 -> is tails\n\n'
      f'Profitable to flip {result}')
