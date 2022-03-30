 #20 м*5000 м*25 кг/см*м2 *5 см = 12500 т.  - переводить см в м не стала, так как см сокращаются при умножении(масса асфальта изначально задана для квадратного метра
# слоя толщиной 1 см - 25 кг/см*m2)

class Road:
    def __init__(self, lenght, width):
        self._len = lenght
        self._wid = width
        self.mass_m2 = 25
        self.thickness = 5

    def mass(self):
        m = self._len * self._wid * self.mass_m2 * self.thickness / 1000
        print(m)


road1 = Road(20, 5000)
road1.mass()

