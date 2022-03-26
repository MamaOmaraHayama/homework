

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.police = is_police
        print('название:', name, 'цвет:',  color, 'является полицейской:',  is_police)

    def go(self):
        print('машина поехала')

    def stop(self):
        print('машина сотановилась')

    def turn_right(self):
        print("машина повернула направо")

    def turn_left(self):
        print("машина повернула налево")

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('скорость:', self.speed, 'превышение!')
        else:
            print('скорость:', self.speed)


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('скорость:', self.speed, 'превышение!')
        else:
            print('скорость:', self.speed)


class SportCar(Car):
    def drag_racing(self):
        print('участвую в гонке')


class PoliceCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)


car1 = Car(45, 'blue', 'fiat idea')
car1.go()
car1.turn_left()

car2 = TownCar(65, 'black', 'lincoln')
car2.stop()
car2.turn_right()
car2.show_speed()

car3 = SportCar(160, 'red', 'ferrari')
car3.drag_racing()
car3.show_speed()

car4 = PoliceCar(46, 'dark blue', 'ford crown victoria')
car4.go()
car4.stop()

car5 = WorkCar(41, 'green', 'caterpillar')
car5.go()
car5.show_speed()
