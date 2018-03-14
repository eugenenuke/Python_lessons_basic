#!/usr/bin/env python3
# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil


def print_help():
    print("""
        help                получение справки
        ls                  отображение полного пути текущей директории
        cd <path>           смена директории на указанную
        rm <file_name>      удаление файла
        cp <file_name>      создание копии указанного файла
        mkdir <dir_name>    создание директории
        ping                тестовый ключ
        """)


def make_dir():
    if not name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(name))
    except FileExistsError:
        print('директория {} уже существует'.format(name))


def ping():
    print("pong")


def cp():
    if not name:
        print("Необходимо указать имя файла вторым параметром")
        return
    
    source_file = os.path.join(os.getcwd(), name)
    if not os.path.isfile(source_file):
        print("Файла не существует, либо была передана директория")
        return

    target_file = os.path.join(os.getcwd(), name + '.copy')
    if os.path.isdir(target_file):
        print('Ошибка. Существует директория, с таким же именем как и у файла назначения.')
        return
    if os.path.isfile(target_file):
        ans = input('Файл назначения существует, переписать? ([Д]/н):')
        if ans != '' and ans.upper() != 'Д' and ans.upper() != 'Y':
            return

    try:
        shutil.copy(source_file, target_file)
        print('файл {0} скопирован в {0}.copy'.format(name))
    except Exception as e:
        print('ошибка копирования файла {}: {}'.format(name, e))


def ls():
    print(os.getcwd())


def rm():
    if not name:
        print("Необходимо указать имя файла вторым параметром")
        return
    
    file_path = os.path.join(os.getcwd(), name)
    if not os.path.isfile(file_path):
        print("Файла не существует, либо была передана директория")
        return

    ans = input('Действительно хотите удалить файл? (д/[Н]):')
    if ans.upper() != 'Д' and ans.upper() != 'Y':
        return

    try:
        os.unlink(file_path)
        print('файл {} удалён'.format(name))
    except Exception as e:
        print('ошибка удаления файла {}: {}'.format(name, e))


def cd():
    if not name or not os.path.isdir(os.path.join(os.getcwd(), name)):
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.chdir(dir_path)
        print('вошли в директорию {}'.format(name))
    except Exception as e:
        print('ошибка входа в директорию {}: {}'.format(name, e))


# _start:

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "ls": ls,
    "cd": cd,
    "rm": rm,
    "cp":cp
}

try:
    name = sys.argv[2]
except IndexError:
    name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key and do.get(key):
    do[key]()
else:
    print("Задан неверный ключ")
    print("Укажите ключ help для получения справки")
