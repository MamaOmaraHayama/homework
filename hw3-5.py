def my_f():
    a = 0
    try:
        while True:
            ls = input('введите числа, для завершения введите любую букву:').split()
            digits = map(int, ls)
            for e in digits:
                a += e

            print(a)
    except ValueError:
        print(a)
        return


my_f()
