"""==========================================================
Задача 26:
Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
=========================================================="""
import math


def powerNumber(number, degree):
    if degree == 1:
        return number
    else:
        return number * powerNumber(number, degree - 1)


first_number = int(input('Input first number: '))
second_number = int(input('Input second number: '))
print(powerNumber(first_number, second_number))
