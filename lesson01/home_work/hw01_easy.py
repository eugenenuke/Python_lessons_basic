#!/usr/bin/env python3

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

#number = int(input("Введите число:"))

# v1
number = 234
while number:
    print(number % 10)
    number = number // 10

# v2
#number = str(number)
#for i in number:
#    print(i)

# v3
#for i in range(100):
#    n = (number - number // 10**(i + 1) * 10**(i + 1)) // 10**i
#    if not n:
#        break
#    print(n)


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a = int(input('Введите a: '))
b = int(input('Введите b: '))
print('Меняем местами...')
a = a + b
b = a - b
a = a - b
print('a =', a, 'b =', b)

#v2
#a, b = b, a

#v3
#c = a
#a = b
#b = c

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"
age = int(input('Введите ваш возраст: '))
if age >= 18:
    print("Доступ разрешен")
else:
    print("Извините, пользование данным ресурсом только с 18 лет")
