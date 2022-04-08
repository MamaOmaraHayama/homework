
class Depot:
    def __init__(self, storage, occupied):
        self.s = storage
        self.o = occupied

    def vacant(self):
        vacant = self.s - self.o
        if vacant == 0:
            return f'склад заполнен'
        elif vacant < 0:
            return f'неверные данные: количество занятых мест превышает вместимость'
        else:
            return f'свободно {vacant} мест'

    def take(self, *of_equipments):
        n = 0
        for of_equipment in of_equipments:
            self.o = self.o + 1
            n = n + 1
        return f'сохранено объектов: {n} занято мест: {self.o}'

    def transfer(self, *of_equipments):
        n = 0
        for of_equipment in of_equipments:
            self.o = self.o - 1
            n = n + 1
        return f'передано объектов: {n} занято мест: {self.o}'


class Off_equip:
    def __init__(self, name, number, cost):
        self.n = name
        self.num = number
        self.c = cost

    def __str__(self):
        return f'название: {self.n} количество: {self.num} стоимость: {self.c}'


class Printer(Off_equip):
    def __init__(self, name, number, cost, color):
        #цветной,чб
        super().__init__(name, number, cost)
        self.color = color

    def data(self):
        features = {'название': self.n, 'цена': self.c, 'количество': self.num, 'цвет печати': self.color}
        product = tuple([features])
        return product


class Scaner(Off_equip):
    # тип ручной/плншетный
    def __init__(self, name, number, cost, type):
        super().__init__(name, number, cost)
        self.type = type

    def data(self):
        features = {'название': self.n, 'цена': self.c, 'количество': self.num, 'тип': self.type}
        product = tuple([features])
        return product


class Xerox(Off_equip):
    def __init__(self, name, number, cost, color, type):
        super().__init__(name, number, cost)
        self.color = color
        self.type = type

    def data(self):
        features = {'название': self.n, 'цена': self.c, 'количество': self.num, 'цвет печати': self.color, 'тип': self.type}
        product = tuple([features])
        return product


x1 = Xerox('xerox', 1, 54, 'ч/б', 'стац')
p1 = Printer('printer', 1, 7, 'ч.б')
s1 = Scaner('scaner', 1, 66, 'ручной')
print(x1.data())
d1 = Depot(1233, 377)
print(d1.vacant())
print(d1.take(x1, p1))
print(d1.transfer(x1, p1, s1))
print(x1)
