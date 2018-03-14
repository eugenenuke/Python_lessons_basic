#!/usr/bin/env python3

import os
import sys
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def rmdir(rdir):
    try:
        #os.rmdir(rdir)
        shutil.rmtree(rdir)
    except Exception as e:
        print('Ошибка при удалении директории {}: {}'.format(rdir, e))
        return False
    return True


def mkdir(mdir):
    try:
        os.mkdir(mdir)
    except Exception as e:
        print('Ошибка при создании директории {}: {}'.format(mdir, e))
        return False
    return True


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def lscwd(ftype='a'):
    '''
    ftype:
        a - All
        f - files
        d - dirs
    '''
    contents = os.listdir()
    for item in contents:
        if ftype == 'a' or ftype == 'd' and os.path.isdir(item) or \
           ftype == 'f' and os.path.isfile(item):
            print(item)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def f_copy(source, target):
    try:
        res = shutil.copy(source, target)
        # with open(source) as in_file:
        #     data = in_file.readlines()
        # with open(target, 'w') as out_file:
        #     out_file.writelines(data)
    except Exception as e:
        print('Ошибка при копировании:', e)
    else:
        print('Файл успешно скопирован в', target)


if __name__ == '__main__':
    # Задача-1:
    print('Создаём директории dir_1 - dir_9...')
    for i in range(1, 10):
        mydir = 'dir_' + str(i)
        mkdir(mydir)

    print('Директории созданы, удаляем их...')
    for i in range(1, 10):
        mydir = 'dir_' + str(i)
        rmdir(mydir)
    print('Директории удалены.\n')

    # Задача-2:
    print('Список папок текущей директории:')
    lscwd(ftype='d')

    # Задача-3:
    print('Создаём копию файла: cp {} {}'.format(sys.argv[0], sys.argv[0] + '.copy'))
    f_copy(sys.argv[0], sys.argv[0] + '.copy')
