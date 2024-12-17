import math


def circle_perimeter(value):
    if value <= 0:
        return None
    return round(value * 2 * math.pi, 2)


def circle_area(value):
    if value <= 0:
        return None
    return round(value * value * math.pi, 2)


def square_perimeter(value):
    if value <= 0:
        return None
    return round(value * 4, 2)


def square_area(value):
    if value <= 0:
        return None
    return round(value * value, 2)


def triangle_perimeter(side1=0, side2=0, side3=0):
    sides = [side1, side2, side3]
    if 0 in sides:
        return None
    return round(sum(sides))


def rectangle_area(value1, value2):
    sides = [value1, value2]
    if 0 in sides:
        return None
    return round(value1 * value2, 2)


def rectangle_perimeter(value1, value2):
    sides = [value1, value2]
    if 0 in sides:
        return None
    return round((value1 + value2) * 2, 2)
