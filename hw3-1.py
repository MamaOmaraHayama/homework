def my_func(a, b):
    try:
        res = a / b
        return res
    except ZeroDivisionError:
        return 'zero division!'


print(my_func(int(input('a:')), int(input('b:'))))
