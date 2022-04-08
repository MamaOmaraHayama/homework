
class Numerr(Exception):
    def __init__(self, txt):
        self.txt = txt


def my_ls():
    ls = []
    while True:
        n = input('введите число, для завршения работы введите "stop": ')
        if n == 'stop':
            print('вы вышли')
            break

        else:
            try:
                if n.isdigit() == True:
                    ls.append(n)
                    print(ls)

                else:
                    raise Numerr('недопустимое значение, введите число')
            except Numerr as err:
                print(err)


my_ls()
