#!/usr/bin/env python3
# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, persoтn2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.


from random import choice


def attack(attacker, target):
    target['health'] -= attacker['damage']


print('Задача №1')

player = {'name': input("Введите своё имя: "), 'health': 80, 'damage': 35}
enemy = {'name': input("Введите имя врага: "), 'health': 100, 'damage': 25}

print(player, enemy, sep='\n')

print('Атака!')
attack(player, enemy)

print(player, enemy, sep='\n')


# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

def get_damage(damage, armor):
    return damage / armor


def attack2(attacker, target):
    target['health'] -= get_damage(attacker['damage'], target['armor'])


def dict2str(d):
    return ['{}:{}\n'.format(x, y) for x, y in d.items()]
    # return list(map(lambda x: '{}:{}\n'.format(x[0], x[1]), d.items()))


def str2dict(str):
    d = dict()
    for s in str:
        key, value = s.rstrip().split(':')
        if key != 'name':
            value = float(value)
        d[key] = value
    return d


print('\nЗадача №2')

player = {'name': player['name'], 'health': 80, 'damage': 35, 'armor': 1.2}
enemy = {'name': enemy['name'], 'health': 100, 'damage': 25, 'armor': 1.2}

for entity in (player, enemy):
    with open(entity['name'] + '.txt', 'w') as ef:
        ef.writelines(dict2str(entity))

player['armor'] = 0
with open(player['name'] + '.txt', 'r') as pf:
    player = str2dict(pf.readlines())

enemy['armor'] = 0
with open(enemy['name'] + '.txt', 'r') as ef:
    enemy = str2dict(ef.readlines())

print('Начинаем игру!')
print(player['name'], '\t', enemy['name'])
print(round(player['health'], 2), '\t', round(enemy['health'], 2))

while 0 < player['health'] and 0 < enemy['health']:
    if choice([True, False]):
        attack2(player, enemy)
    else:
        attack2(enemy, player)
    print(round(player['health'], 2), '\t', round(enemy['health'], 2))
print('Победил,', (enemy['name'], player['name'])[player['health'] > 0])
