#!/usr/bin/env python3
# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class Car:

    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = False

    def go(self):
        print("Машина {} поехала.".format(self.name))

    def stop(self):
        print("Машина {} остановилась.".format(self.name))

    def turn(self, direction):
        print("Машина {} повернула {}.".format(self.name, direction))

    def get_police(self):
        return self.is_police

    def get_name(self):
        return self.name


class PoliceCar(Car):

    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)
        self.is_police = True


class TownCar(Car):
    pass


class WorkCar(Car):
    pass


class SportCar(Car):
    pass


spider = SportCar('Ferrary Spider', 'Красный', '150')
logan = WorkCar('Renault Logan', 'Чёрный', '90')
matiz = TownCar('DaeWoo Matiz', 'Серебристый', 60)
polizia = PoliceCar('ВАЗ 2109', 'Спецокрас', 92)

spider.go()
polizia.go()

spider.turn('направо')
polizia.turn('налево')

spider.stop()
polizia.stop()

for car in (polizia, spider, matiz, logan):
    if car.get_police():
        print('{} является полицейской машиной'.format(car.get_name()))
    else:
        print('{} не является полицейской машиной'.format(car.get_name()))
    print
