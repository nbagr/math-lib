from functools import reduce


def sum(*args):
    return reduce(lambda acc, item: acc + item, args, 0)


def multiply(*args):
    return reduce(lambda acc, item: acc * item, args, 0)


def divide(*args):
    if 0 in args:
        raise ValueError('Can\'t divide by zero')
    return reduce(lambda acc, item: acc / item, args[1:], args[0])


def subtraction(*args):
    return reduce(lambda acc, item: acc - item, args[1:], args[0])
