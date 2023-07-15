"""=======================================================
Задача 36:
Напишите функцию print_operation_table(operation,
num_rows=6, num_columns=6), которая принимает в качестве
аргумента функцию, вычисляющую элемент по номеру строки и
столбца. Аргументы num_rows и num_columns указывают число
строк и столбцов таблицы, которые должны быть распечатаны.
Нумерация строк и столбцов идет с единицы (подумайте,
почему не с нуля). Примечание: бинарной операцией называется
любая операция, у которой ровно два аргумента, как, например,
у операции умножения.

Ввод: print_operation_table(lambda x, y: x * y)
Вывод:
1 2 3 4 5 6
2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36
======================================================="""

"""=======================================
Вариант_01 (лямбда)
======================================="""


def print_operation_table(operation, num_rows, num_columns):
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            print(operation(i, j), end='\t')
        print()


print_operation_table(lambda x, y: x * y, num_rows=6, num_columns=6)

"""=======================================
Вариант_02 (без лямбды и двумерный массив)
======================================="""
# num_rows = 8
# num_columns = 7
#
#
# def fillArr(rows, columns):
#     if rows > columns:
#         length = rows
#     else:
#         length = columns
#
#     array = [k + 1 for k in range(length)]
#     new_array = [[0] * columns for k in range(rows)]
#
#     for a in range(columns):
#         for b in range(rows):
#             new_array[b][a] = array[a] * array[b]
#     return new_array
#
#
# def print_Array(array):
#     for i in array:
#         print()
#         for j in i:
#             print(j, end='\t')
#
#
# print_Array(fillArr(num_rows, num_columns))
