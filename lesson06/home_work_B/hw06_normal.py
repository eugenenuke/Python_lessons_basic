#!/usr/bin/env python3
# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

from random import choice

class Person:

    def __init__(self, health, damage, armor):
        self._health = health
        self._damage = damage
        self._armor = armor


    def _get_damage(self, target):
        return round(self._damage / target._armor, 2)


    def _set_damage(self, damage):
        self._health -= damage


    def attack(self, target):
        target._set_damage(self._get_damage(target))


    def get_health(self):
        return self._health


    def get_name(self):
        return self._name


class Player(Person):

    def __init__(self, health, damage, armor):
        super().__init__(health, damage, armor)
        self._name = 'Player'


class Enemy(Person):

    def __init__(self, health, damage, armor):
        super().__init__(health, damage, armor)
        self._name = 'Enemy'


class Game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self._round = 0


    def start(self):
        print("Round\t{}\t{}".format(self.player1.get_name(), self.player2.get_name()))

        while True:
            self._print_scores()
            if not self._turn():
                self._print_scores()
                break

        winner = ''

        if self.player1.get_health() <= 0:
            winner = self.player2.get_name()
        else:
            winner = self.player1.get_name()

        print('\nПобедил', winner)


    def _turn(self):
        attacker = choice((self.player1, self.player2))

        if attacker is self.player1:
            target = self.player2
        else:
            target = self.player1

        attacker.attack(target)

        self._round += 1

        return True if target.get_health() > 0 else False


    def _print_scores(self):
        print("{:3}\t{:.2f}\t{:.2f}".format(
            self._round, self.player1.get_health(), self.player2.get_health())
            )


player = Player(100, 23, 1.3)
enemy = Enemy(120, 26, 1.2)

new_game = Game(player, enemy)
new_game.start()

