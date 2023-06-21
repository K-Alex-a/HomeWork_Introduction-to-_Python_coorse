"""==================================================
Задача 12:
Петя и Катя – брат и сестра.
Петя – студент, а Катя – школьница.
Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000),
а Катя должна их отгадать.
Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.
Примеры:
4 4 -> 2 2
5 6 -> 2 3
=================================================="""

"""
Вариант_01 (через циклы):
"""


def dataInput(text):
    value = input(f'Input {text} number: ')
    return value


def checkNumbersForLetters(number):
    while not number.isdigit():
        number = input('Wrong! Try Again!\n'
                       'Input only the number: ')
    return int(number)


def guessNums(summa, multiply):
    for i in range(summa // 2 + 1):
        for j in range(multiply // 2 + 1):
            if i + j == summa and \
                    i * j == multiply:
                return i, j
    return 'There is no solution for such numbers'


sum_number = checkNumbersForLetters(dataInput('first'))
multiply_number = checkNumbersForLetters(dataInput('second'))
result = guessNums(sum_number, multiply_number)
print(f'{sum_number} {multiply_number} -> {result}')


"""
Вариант_02 (через дискриминант):
"""
# import math
#
# summa = int(input('Input sum numbers: '))
# multiply = int(input('Input multiply numbers: '))
#
# discriminant = summa ** 2 - multiply * 4
# if discriminant == 0:
#     x = y = summa / 2
#     print(x, y)
# elif discriminant > 0:
#     x = (summa + math.sqrt(discriminant)) / 2
#     y = summa - x
#     print(round(x, 2), round(y, 2))
# else:
#     print('No solutions!')


