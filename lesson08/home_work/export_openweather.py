#!/usr/bin/env python3

""" OpenWeatherMap (экспорт)

Сделать скрипт, экспортирующий данные из базы данных погоды, 
созданной скриптом openweather.py. Экспорт происходит в формате CSV или JSON.

Скрипт запускается из командной строки и получает на входе:
    export_openweather.py --csv filename [<город>]
    export_openweather.py --json filename [<город>]
    export_openweather.py --html filename [<город>]
    
При выгрузке в html можно по коду погоды (weather.id) подтянуть 
соответствующие картинки отсюда:  http://openweathermap.org/weather-conditions

Экспорт происходит в файл filename.

Опционально можно задать в командной строке город. В этом случае 
экспортируются только данные по указанному городу. Если города нет в базе -
выводится соответствующее сообщение.

"""

import csv
import json
import sqlite3
import sys
import getopt

DB_FILE = 'temp_data.db'


def export_json(data, filename='out.json'):
    try:
        with open(filename, 'w') as j_out:
            j_out.writelines('\n'.join([json.dumps(row) for row in data]))
    except OSError:
        print('Ошибка записи в файл')
        sys.exit(1)

def export_csv(data, filename='out.csv'):
    try:
        with open(filename, 'w') as csv_out:
            fields = ['city_id', 'city_name', 'date', 'temp', 'weather_id']
            csv_writer = csv.DictWriter(csv_out, fields)
            csv_writer.writeheader()
            for row in data:
                csv_writer.writerow(row)
    except OSError:
        print('Ошибка записи в файл')
        sys.exit(1)

def export_html(data, filename='out.html'):
    print('Экспорт в html не реализован.')

def check_opts(opts):
    for opt in opts:
        if opt[0] in ['--json', '--csv', '--html']:
            return True
    return False

def usage():
    return 'Usage: {} --json | --csv | --html <filename> [city_name]'.format(sys.argv[0])


data = []
try:
    opts, args = getopt.getopt(sys.argv[1:], '', ['json=', 'csv=', 'html='])
except getopt.GetoptError:
    print(usage())
    sys.exit(1)

if len(args) > 1 or not check_opts(opts):
    print(usage())
    sys.exit(1)

try:
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()
        if args:
            cur.execute("SELECT * FROM temp_data WHERE city_name=?", (args[0], ))
        else:
            cur.execute("SELECT * FROM temp_data")
        for row in cur:
            data.append({
                'city_id': row[0],
                'city_name': row[1],
                'date': row[2],
                'temp': row[3],
                'weather_id': row[4]
                })
except Exception as e:
    print(e)

for opt in opts:
    if opt[0] == '--json':
        export_json(data, opt[1])
    if opt[0] == '--csv':
        export_csv(data, opt[1])
    if opt[0] == '--html':
        export_html(data, opt[1])

