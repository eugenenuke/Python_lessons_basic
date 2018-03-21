#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

from random import shuffle


# Количество колонок
COLS = 9

# Количество рядов у карты
ROWS = 3

# Количество цифр в ряду
NUMS_ON_ROW = 5

# Максимальный номер бочонка
BARRELS_N = 90

# Ширина одного места для цифры
N_WIDTH = len(str(BARRELS_N))


class LottoSack:

    def __init__(self):
        self._barrels = [i for i in range(1, BARRELS_N+1)]
        shuffle(self._barrels)

    def __str__(self):
        return str(self._barrels)

    def __iter__(self):
        return self

    def __next__(self):
        if self._barrels:
            return self._barrels.pop()
        raise StopIteration

    def get_remains(self):
        return len(self._barrels)


class LottoCard:

    def __init__(self):
        pool = [i for i in range(1, BARRELS_N+1)]
        shuffle(pool)
        pool = [
                sorted(pool[:NUMS_ON_ROW]),
                sorted(pool[NUMS_ON_ROW:NUMS_ON_ROW*2]),
                sorted(pool[NUMS_ON_ROW*2:NUMS_ON_ROW*3])]

        self._nums = []
        self._remains = ROWS * NUMS_ON_ROW

        for row in range(0, ROWS):
            # Добавляем ряд
            self._nums.append([])

            # Определяем места для цифр
            places = [i for i in range(0, COLS)]
            shuffle(places)
            places = places[:5]

            # Заполняем ряд
            for col in range(0, COLS):
                if col in places:
                    self._nums[row].append(pool[row].pop(0))
                else:
                    self._nums[row].append('  ')

    def __str__(self):
        card = ''
        for row in self._nums:
            card += " ".join(map(lambda x: str(x).rjust(N_WIDTH), row)) + '\n'
        card = "{0}{1}{0}".format('-' * (COLS * (N_WIDTH + 1) - 1) + '\n', card)
        return card

    def strike_num_out(self, num):
        for row in self._nums:
            if num in row:
                row[row.index(num)] = '-'
                self._remains -= 1
                return True
        return False

    def check_num(self, num):
        return any(num in row for row in self._nums)

    def get_remains(self):
        return self._remains


class LottoPlayer:

    def __init__(self, name):
        self._card = LottoCard()
        self._name = name

    def __str__(self):
        return '\n'.join((self._name, str(self._card)))

    def check_num(self, num):
        return self._card.check_num(num)

    def strike_num_out(self, num):
        return self._card.strike_num_out(num)

    def get_remains(self):
        return self._card.get_remains()


class LottoGame:

    result = {
        'won': 'Вы зачеркнули все номера в карточке. Поздравляем, Вы выиграли!',
        'overlooked': 'Вы проглядели номер, присутсвующий в вашей карточке. Проигрыш!',
        'mistake': 'Невозможно вычеркнуть, у Вас нет такого номера в карточке. Проигрыш!',
        'lose': 'Компьютер зачеркнул все номера в карточке. Вы проиграли!',
        'draw': 'Бочонков больше нет. Ничья!'
        }

    def __init__(self):
        self._player = LottoPlayer('Игрок')
        self._computer = LottoPlayer('Компьютер')
        self._sack = LottoSack()

    def start(self):
        for barrel in self._sack:
            if not self._turn(barrel):
                return
        print(result['draw'])

    def _turn(self, barrel_in_play):
        print('Новый бочонок: {} (осталось {})'.format(
                barrel_in_play, self._sack.get_remains()
                ))
        print(self._player)
        print(self._computer)
        answer = input('Зачеркнуть цифру? (y/n)')
        
        if answer.lower() == 'y':
            if not self._player.strike_num_out(barrel_in_play):
                print(self.result['mistake'])
                return False
        else:
            if self._player.check_num(barrel_in_play):
                print(self.result['overlooked'])
                return False
        
        self._computer.strike_num_out(barrel_in_play)

        if self._player.get_remains() == 0:
            print(self.result['won'])
            return False
        if self._computer.get_remains() == 0:
            print(self.result['lose'])
            return False

        return True


new_game = LottoGame()
new_game.start()
