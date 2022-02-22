def my_f(x, y):
    if x <= 0:
        print('x - положительное действительное число')
    if y >= 0:
        print('у - целое отрицательное число')
    else:
        res = x ** y
        print(res)


my_f(3, -6)


def my_f(x, y):
    if x <= 0:
        print('введите положительное действительное число')
    if y >= 0:
        print('введите целое отрицательное число')
    if y == -1:
        print(1 / x)
    if y < -1:
        n = 1
        res = 1 / x * 1 / x
        while n < abs(y) - 1:
            n = n + 1
            res = res * 1 / x

        print(res)


my_f(3, -6)

