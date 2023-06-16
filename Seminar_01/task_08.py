"""============================================================
# Задача 8:
# Требуется определить, можно ли от шоколадки размером
# n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no
==========================================================="""


def dataInput(text):
    """
    :return: any value
    """
    value = input(f'Input the {text}: ')
    return value


def checkFaultChocolate(height, width, segments):
    """
    :param height: object height
    :param width: object width
    :param segments: number to check multiplicity
    :return: True or False
    """
    result = False
    if (segments % height == 0 or segments % width == 0) and segments <= height*width:
        result = True
    return result


height_chocolate = int(dataInput('height chocolate'))
width_chocolate = int(dataInput('width chocolate'))
amount_segment = int(dataInput('number of slices'))
print(f'{amount_segment} pieces can not be broken off from a {height_chocolate}x{width_chocolate} chocolate bar'
      if checkFaultChocolate(height_chocolate, width_chocolate, amount_segment) is False
      else f'Сan be broken off!')
