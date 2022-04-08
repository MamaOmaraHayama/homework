
from time import sleep


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        n = 0
        while n < 3:
            if n == 0:
                print('Цвет сигнала:', TrafficLight.__color[0])
                sleep(7)
            if n == 1:
                print('Цвет сигнала:', TrafficLight.__color[1])
                sleep(2)
            if n == 2:
                print('Цвет сигнала:', TrafficLight.__color[2])
                sleep(9)
            n += 1


TrafficLight = TrafficLight()
TrafficLight.running()
