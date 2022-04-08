
# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        sum1 = self.a + other.a
        sum2 = self.b + other.b
        return f'{sum1} + {sum2}i'

    def __mul__(self, other):
        num1 = self.a * other.a - self.b * other.b
        num2 = self.a * other.b + self.b * other.a
        return f'{num1} + {num2}i'


c1 = Complex(3, 4)
c2 = Complex(1, 2)
print(c1 + c2)
print(c1 * c2)
