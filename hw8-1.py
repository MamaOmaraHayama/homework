# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, data):

        self.data = str(data)
        Data.validation(data)

    @classmethod
    def recast(cls, data):
        old_ls = data.split('-')
        new_ls = [int(e) for e in old_ls]

        return new_ls[0], new_ls[1], new_ls[2]

    @staticmethod
    def validation(data):
        old_ls = data.split('-')
        new_ls = [int(e) for e in old_ls]
        d = new_ls[0]
        m = new_ls[1]
        y = new_ls[2]

        if d > 31 or d < 1:
            print('wrong day')
        else:
            print('correct day')
        if m > 12 or m < 1:
            print('wrong month')
        else:
            print('correct month')
        if y > 2022 or y < 1:
            print('wrong year')
        else:
            print('correct year')

    def __str__(self):
        return f'дата {Data.recast(self.data)}'


d1 = Data('3 - 2 - 2020')
print(d1)
d2 = Data('12-32-2023')
print(d2)
Data.validation('4-8-2011')
