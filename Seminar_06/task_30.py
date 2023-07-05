"""====================================================
Задача 30:
Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно
ввести с клавиатуры. Формула для получения n-го члена
прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
Пример:
Ввод: 7 2 5
Вывод: 7 9 11 13 15
===================================================="""
number = int(input('Input number: '))
dif_and_length = list(map(int, input('Input difference number and length: ').split()))
print(number, *dif_and_length)


def arifProgress(first_number, step, length):
    return [first_number + (i-1) * step for i in range(1, length + 1)]


print(*arifProgress(number, dif_and_length[0], dif_and_length[1]))

