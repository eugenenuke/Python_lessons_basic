#!/usr/bin/env python3
# Задача: используя цикл запрашивайте у пользователя число пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степерь 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число не верное,
# и сообщаете об диапазоне допустимых. И просите ввести заного.
# Допустим пользователь ввел 2, оно подходит, возводим в степень 2, и выводим 4
a_min = 0
a_max = 10
print('Попади в диапазон')
while True:
    ans = int(input('Твоё число: '))
    if a_min < ans < a_max:
        print('Попал!', str(ans)+'^2 =', ans ** 2)
        break
    print('Неверно, допустимый диапазон:', a_min, '-', a_max)
    print('Попробуй ещё раз')


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;

a = int(input('Введи первое число:'))
b = int(input('Введи второё число:'))
print('a =', a, 'b =', b)
print('Меняем числа местами...')
a = a + b
b = a - b
a = a - b
# a, b = b, a
print('a =', a, 'b =', b)
