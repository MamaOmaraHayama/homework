
class Zerodiv(Exception):
    def __init__(self, txt):
        self.txt = txt

try:
    a = int(input('введите делимое: '))
    b = int(input('введите делитель: '))
    if b == 0:
        raise Zerodiv('деление на ноль недопустимо')
except Zerodiv as error:
    print(error)
else:
    res = a / b
    print(res)


