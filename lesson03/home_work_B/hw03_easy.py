#!/usr/bin/env python3
# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"
def pers_info(name, age, city):
    data = (name, str(age), city)
    form = (', ', ' год(а), проживает в городе ', '')
    return ''.join(map(''.join, zip(data, form)))
    # return name + ', ' + str(age) + ' год(а), проживает в городе ' + city

test_list = ['Василий', 21, 'Москва']
print('Входные данные:', test_list)
print('pers_info =', pers_info(*test_list))

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них
def new_max(one, two, three):
    return max(one, two, three)

test_list = [10, 34, 20]
print('Ищем максимальное число из:', test_list)
print('max =', new_max(*test_list))

# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов
def max_len(*strings):
    return max(map(len, strings))

test_list = ['cat', 'snake', 'parrot', 'dog']
print('Ищем максимальную длинну слова из списка:', test_list)
print('max_len =', max_len(*test_list))
