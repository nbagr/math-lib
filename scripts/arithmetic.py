from functools import reduce


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
