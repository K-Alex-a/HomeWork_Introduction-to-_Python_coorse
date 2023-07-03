"""
Задача 28:
Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
*Пример:*
2 2
4
"""

first_number = int(input('Input first number: '))
second_number = int(input('Input second number: '))


def sumNumber(number_1, number_2):
    if number_2 < 1:
        return number_1
    else:
        return sumNumber(number_1 + 1, number_2 - 1)


print(sumNumber(first_number, second_number))
