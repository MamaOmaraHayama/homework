from itertools import count
from math import factorial

n = int(input('введите целое число:'))


def fact():
    for el in count(1):
        yield factorial(el)


i = 0
for e in fact():
    if i < n:
        print(e)
        i += 1
    else:
        break
