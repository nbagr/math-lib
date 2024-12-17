from functools import reduce
import math


def sum(*args):
    return reduce(lambda acc, item: acc + item, args, 0)


def multiply(*args):
    return reduce(lambda acc, item: acc * item, args, 1)


def divide(number, *args):
    if 0 in args:
        return None
    return reduce(lambda acc, item: acc / item, args, number)


def subtraction(*args):
    return reduce(lambda acc, item: acc - item, args[1:], args[0])


def factorial(value):
    if value <= 1:
        return 1
    else:
        return (value * factorial(value - 1))


def pow(number=0, *args):
    result = number
    for item in args:
        result **= item
    return result


def degrees_to_radians(value):
    return round(value * math.pi / 180, 2)


def radians_to_degrees(value):
    return round(value * 180 / math.pi, 2)


def log(value, base=2):
    if base < 2 or value < 1:
        return None

    result = 0

    while base**result <= value:
        result += 1

    return result - 1
