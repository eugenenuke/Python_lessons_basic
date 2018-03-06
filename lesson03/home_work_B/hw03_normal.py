#!/usr/bin/env python3
# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.

employes = ['Вася', 'Петя', 'Ваня', 'Гриня']
salaries = [15000, 21101, 25000, 501001]
print('Входные данные:', employes, salaries, sep='\n')

db = dict(zip(employes, salaries))
print('Словарь:', db)

out_data = list(map('{0[0]} - {0[1]}\n'.format,
                    filter(lambda x: x[1] < 500000, db.items())))

with open('salary.txt', 'w', encoding='utf-8') as out_file:
    out_file.writelines(out_data)

with open('salary.txt', encoding='utf-8') as in_file:
    in_data = dict(
        map(lambda y: (y[0], round(float(y[1])*.87, 2)),
            map(lambda x: x.rstrip().split(' - '), in_file.readlines())
            ))
    print('\n'.join(map('{0[0]}: {0[1]}'.format, in_data.items())).upper())
