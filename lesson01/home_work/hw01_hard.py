#!/usr/bin/env python3
__author__ = 'Ваши Ф.И.О.'

# Задание-1:
# Ваня набрал несколько операций в интерпретаторе и получал результаты:
# 	Код: a == a**2
# 	Результат: True
# 	Код: a == a*2
# 	Результат: True
# 	Код: a > 999999
# 	Результат: True

# Вопрос: Чему была равна переменная a,
# если точно известно, что её значение не изменялось?

# Подсказка: это значение точно есть ;)

a = float('Inf')

print('a =', a)
print('a == a*2:', a == a*2)
print('a == a**2:', a == a**2)
print('a > 999999:', a > 999999)


print()


# Вариант 2
# hack the int
from random import randint

class mad_int(int):
    def __eq__(self, x):
        return True
    def __gt__(self, x):
        return True

a = mad_int(randint(0, 1000000))

print('a =', a)
print('a == a*2:', a == a*2)
print('a == a**2:', a == a**2)
print('a > 999999:', a > 999999)
