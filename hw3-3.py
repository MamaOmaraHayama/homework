def my_func(a, b, c):
    if a > b > c:
        print(a + b)
    if b > c > a:
        print(b + c)
    if c > a > b:
        print(c + a)


my_func(3, 9, 7)


def my_f(a, b, c):
    ls = [a, b, c]
    max_1 = max(ls)
    ls.remove(max_1)
    max_2 = max(ls)
    res = max_1 + max_2
    print(res)


my_f(3, 9, 7)

