#!/usr/bin/env python3
# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

class ToyFactory:

    def __init__(self):
        pass


    def buy_raw_stuff(self, toy):
        print('Закупаем материалы для', toy.get_name())


    def sew(self, toy):
        print('Шьём форму/костюм для', toy.get_name())


    def paint(self, toy, color):
        print('Красим {} в {} цвет'.format(toy.get_name(), color))
        toy.set_color(color)


    def build(self, name, color, toy_type):
        #new_toy = Toy(name, toy_type)

        types = {'animal': ToyAnimal, 'car': ToyCar, 'movie character': ToyMovieChar}
        new_toy = types[toy_type](name)

        self.buy_raw_stuff(new_toy)
        self.sew(new_toy)
        self.paint(new_toy, color)
        
        return new_toy


class Toy:

    def __init__(self, name):
        self._name = name


    def get_name(self):
        return self._name


    def set_color(self, color):
        self._color = color


    def get_color(self):
        return self._color


# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный класс, который наследуется от базового - Игрушка

class ToyAnimal(Toy):

    def __init__(self, name):
        super().__init__(name)
        self._type = 'animal'


class ToyCar(Toy):

    def __init__(self, name):
        super().__init__(name)
        self._type = 'car'


class ToyMovieChar(Toy):

    def __init__(self, name):
        super().__init__(name)
        self._type = 'movie character'


factory = ToyFactory()

my_toy1 = factory.build('Тигр', 'рыжий', 'animal')
print('Создана игрушка типа', type(my_toy1))
print()

my_toy2 = factory.build('Ferrari', 'красный', 'car')
print('Создана игрушка типа', type(my_toy2))
print()

my_toy3 = factory.build('Darth Vader', 'чёрный', 'movie character')
print('Создана игрушка типа', type(my_toy3))
