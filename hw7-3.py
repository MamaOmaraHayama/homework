
class Cell:

    def __init__(self, unit):
        self.unit = int(unit)

    def __str__(self):
        return f'клетка с количеством ячеек {self.unit}'

    def __add__(self, other):
        summa = self.unit + other.unit
        return Cell(summa)

    def __sub__(self, other):
        difference = self.unit - other.unit
        if difference >= 0:
            return Cell(difference)
        else:
            print('разность меньше 0!')

    def __mul__(self, other):
        product = self.unit * other.unit
        return Cell(product)

    def __truediv__(self, other):
        quotient = self.unit / other.unit
        return Cell(quotient)

    def make_order(self, cells_in_row):
        row = int(self.unit / cells_in_row) + 1
        last_row = self.unit - ((row - 1) * cells_in_row)
        print(("*" * cells_in_row + '/n') * (row - 1) + ('*' * last_row))


a = Cell(17)
b = Cell(12)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a.make_order(4))
print(b.make_order(5))
