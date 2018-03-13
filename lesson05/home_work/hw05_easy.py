#!/usr/bin/env python3

import os
import sys
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

print('Создаём директории dir_1 - dir_9...')
for i in range(1, 10):
    dir = 'dir_' + str(i)
    try:
        os.mkdir(dir)
    except Exception as e:
        print('Ошибка при создании директории {}: {}'.format(dir, e))

print('Директории созданы, удаляем их...')
for i in range(1, 10):
    dir = 'dir_' + str(i)
    try:
        os.rmdir(dir)
        # shutil.rmtree(dir)
    except Exception as e:
        print('Ошибка при удалении директории {}: {}'.format(dir, e))
print('Директории удалены.\n')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
print('Список папок текущей директории:')
answer = os.listdir()
for item in answer:
    if os.path.isdir(item):
        print(item)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
print('Создаём копию файла: cp {} {}'.format(sys.argv[0], sys.argv[0] + '.copy'))
try:
    res = shutil.copy(sys.argv[0], sys.argv[0] + '.copy')
except Exception as e:
    print('Ошибка при копировании:', e)
else:
    print('Файл успешно скопирован в', res)
