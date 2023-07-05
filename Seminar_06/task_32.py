"""=============================================
Задача 32:
Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше
заданного максимума)
Пример:
Ввод: [-5, 9, 0, 3, -1, -2, 1,
4, -2, 10, 2, 0, -9, 8, 10, -9,
0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]
============================================="""
from random import randint

lst = [randint(-10, 10) for i in range(randint(10, 20))]
print(lst)

range_search = list(map(int, input('Input range from X to Y: ').split()))

max_range = max(range_search)
min_range = min(range_search)
print(f'start = {min_range}, stop = {max_range}')


def index_in_range(lists, start, stop):
    return [(index, lst[index]) for index in range(len(lst)) if start <= lists[index] <= stop]


print(index_in_range(lst, min_range, max_range))
