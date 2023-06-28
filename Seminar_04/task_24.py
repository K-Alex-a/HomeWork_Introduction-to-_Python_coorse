"""========================================================================
Задача 24:
В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.
Пример:
4 -> 1 2 3 4
9
========================================================================"""

"""Вариант_01 (через увеличение списка и срезы для любого количества кустов рядом)"""
from random import randint

lst = [randint(1, 10) for i in range(randint(6, 15))]
print(len(lst), "->", *lst)
bushes_per_turn = 3
lst = lst[:] + lst[:bushes_per_turn - 1]
max_sum = sum(lst[:bushes_per_turn])
bush = 0

for i in range(len(lst) - bushes_per_turn):
    max_sum_current = sum(lst[i + 1:i + 1 + bushes_per_turn])
    if max_sum < max_sum_current:
        max_sum = max_sum_current
        bush = i + bushes_per_turn
print(f'Max amount of berries {max_sum} (around the bush -> {bush})\n'
      f'*bushes start counting from 1')


"""Вариант_02 (для трех кустов рядом)"""
# from random import randint
#
# lst = [randint(1, 10) for i in range(randint(3, 15))]
# print(len(lst), ' -> ', *lst)
#
# max_sum = 0
# central_bush = 0
#
# for index in range(-1, len(lst) - 1):
#     current_sum = lst[index - 1] + lst[index] + lst[index + 1]
#     if max_sum < current_sum:
#         max_sum = current_sum
#         central_bush = index
#
# if central_bush < 0:
#     central_bush += len(lst)
#
# print(f'Max amount of berries {max_sum} (around the bush -> {central_bush + 1})\n'
#       f'*bushes start counting from 1')
