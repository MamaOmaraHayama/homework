# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
        self.wage = wage
        self.bonus = bonus


class Position(Worker):
    def get_full_name(self):
        full_name = self.name + ' ' + self.surname
        print(full_name)

    def get_total_income(self):
        total_income = self.wage + self.bonus
        print(total_income)


w1 = Position('Екатерина', 'Шиманович', 'врач-анестезиолог', 1470, 3100)
w1.get_full_name()
w1.get_total_income()
print(w1._income)
print(w1.position)
