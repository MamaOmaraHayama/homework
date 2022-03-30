from functools import reduce


def func(a, b):
    return a * b


print(reduce(func, [e for e in range(100, 1001) if e % 2 == 0]))
