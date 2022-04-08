# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определённое
# название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть
# обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике
# работу декоратора @property.
from abc import ABC, abstractmethod


class Close(ABC):
    def __init__(self, name):
        self.name = name
        print('name:', name)

    @abstractmethod
    def cloth(self):
        print('m2')

    def __add__(self, other):
        result = self.cloth() + other.cloth()
        print(result)


class Coat(Close):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def cloth(self):
        cloth = self.size / 6.5 + 0.5
        return cloth


class Costume(Close):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    def cloth(self):
        cloth = 2 * self.height + 0.3
        return cloth


a = Coat('coat', 54)
print(a.cloth())
b = Costume('costume', 6)
print(b.cloth())
print(a + b)
