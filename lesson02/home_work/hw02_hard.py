#!/usr/bin/env python3

print("\nЗадание 1\n")

# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y

a, op, b = (equation.split()[2:])
a = float(a[:-1])
b = float(b)

# Вообще, достаточно посчитать y = a * x + b, но, также, рассмотрим
# вариант y = a * x - b
y = a * x
if op == '+':
    y += b
elif op == '-':
    y -= b

print("y = {}".format(y))

print("\nЗадание 2\n")

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '29.02.2000'

# Примеры некорректных дат
#date = '01.22.1001'
#date = '1.12.1001'
#date = '-2.10.3001'
#date = '29.02.1900'

print(date)

# Список месяцев, в которых 31 день
m31 = [1, 3, 5, 7, 8, 10, 12]

answer = 'неверно'
day, month, year = date.split('.')

# Проверяем условие №4 и возможность сконвертировать дату в integer
date = "".join(date.split('.'))
if date.isnumeric() and len(day) == len(month) == 2 and len(year) == 4:
    day, month, year = (int(i) for i in (day, month, year))
    
    # Проверяем, високосный ли год
    vis = bool(not year % 4 and (year % 100 == year % 400 == 0 or year % 100))

    # Определяем, допустимый ли день в феврале
    bad_feb = month == 2 and (day > 29 or day == 29 and not vis)
    
    # Проверяем условия №1-3
    # год можем не проверять - весь диапазон из 4х цифр допустим
    # отрицательные значения не проверяем, они отсеиваюся на этапе isnumeric
    if year > 1 and 0 < month < 13 and 0 < day < 32 and \
      not (day == 31 and month not in m31 or bad_feb):
        answer = 'верно'

print("Дата введена {}.".format(answer))


print("\nЗадание 3\n")

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3


# 1. Вариант математического решения (самый быстрый)

room = int(input("Введите номер комнаты:"))

# Количество комнат Sn в секции n и во всех нижних секциях
# Sn = 1^2 + 2^2 + 3^2 + ... + n^2 => Cумма квадратов натурального ряда
# https://ru.wikipedia.org/wiki/Квадрат_(алгебра)
# Sn = n^3/3 + n^2/2 +n/6 = n(n + 1)(2n + 1)/6
# Зная номер комнаты, можно определить номер секции, в которую входит комната,
# решив кубическое уравнение 2n^3 + 3n^2 + n - 6Sn = 0
# https://ru.wikipedia.org/wiki/Формула_Кардано

# Ищем секцию. Т.к, все коэффициенты, кроме последнего фиксированы,
# можем заранее вычислить некоторые компоненты формулы
# p = -1 / 4
q = -3 * room
Q = (3888 * room * room - 1) / 1728
section = int((-q / 2 + Q**0.5)**(1/3) + (-q / 2 - Q**0.5)**(1/3) - 0.5) + 1

# Определяем этаж и комнату
# 1 + 2 + 3 + 4 + ... = натуральный ряд
# https://ru.wikipedia.org/wiki/Натуральный_ряд
# floor = n * (n-1) / 2
floor = section * (section - 1) // 2 + 1
room -= round((section - 1)**3/3 + (section - 1)**2/2 + (section - 1)/6) + 1
floor += room // section
room = room % section + 1

print(floor, room)


# 2. Вариант решения через цикл (самый понятный)
# room = int(input("Введите номер комнаты:"))
# 
# # Ищем секцию
# floor, section = 1, 1
# rooms_under = 0
# while rooms_under + section**2 < room:
#     rooms_under += section**2
#     floor += section
#     section += 1
# print("Комната {}, секция {}, этаж {}-{}".format(room, section, floor, floor + section - 1))
# 
# 
# # Определяем этаж и комнату
# room -= rooms_under + 1
# floor += room // section
# room = room % section + 1
# 
# print(floor, room)



# 3. Смешанный вариант
# room = int(input("Введите номер комнаты:"))
# 
# # Ищем секцию
# section = 1
# while round((section - 1)**3/3 + (section - 1)**2/2 + (section - 1)/6) < room:
#     section += 1
# 
# # Исключаем самую верхнюю секцию, в которой находится комната
# section -= 1
# 
# # Определяем этаж и комнату
# floor = section * (section - 1) // 2 + 1
# room -= round((section - 1)**3/3 + (section - 1)**2/2 + (section - 1)/6) + 1
# floor += room // section
# room = room % section + 1
# 
# print(floor, room)
# 
