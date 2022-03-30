# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationery:
    def __init__(self, title):
        self.tit = title
        print('название:', title)

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('запуск отрисовки ручкой')


class Pencil(Stationery):
    def draw(self):
        print('запуск отрисовки карандашом')


class Handle(Stationery):
    def draw(self):
        print('запуск отрисовки маркером')


s1 = Pen('Ручка')
s1.draw()

s2 = Pencil('Карандаш')
s2.draw()

s3 = Handle('Маркер')
s3.draw()
