#!/usr/bin/python3 -u

""" 
== OpenWeatherMap ==

OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.

Необходимо решить следующие задачи:

== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.
    
    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID, 
    используя дополнительную библиотеку GRAB (pip install grab)

        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up

        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in

        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys
        
        Ключ имеет смысл сохранить в локальный файл, например, "app.id"

        
== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz
    
    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка 
     (воспользоваться модулем gzip 
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)
    
    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}
    
    
== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a

    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a

    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a


    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}    


== Сохранение данных в локальную БД ==    
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):

    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных

2. Выводить список стран из файла и предлагать пользователю выбрать страну 
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))

3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.


При работе с XML-файлами:

Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с пространствами имен удобно пользоваться такими функциями:

    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    tree = ET.parse(f)
    root = tree.getroot()

    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}

    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...

"""

# from datetime import
import datetime
import urllib.request as requests
import urllib.parse as urlparse
import sqlite3
import gzip
import json
import sys
import os

SITIES_URL = 'http://bulk.openweathermap.org/sample/city.list.json.gz'
SITIES_FILE = 'city.list.json.gz'
DB_FILE = 'temp_data.db'


def check_cities_file():
    if not os.path.isfile(SITIES_FILE):
        print('Скачиваем файл с городами...', end='')
        try:
            with requests.urlopen(SITIES_URL) as url:
                if url.getcode() == 200:
                    with open(SITIES_FILE, 'wb') as o_file:
                        o_file.write(url.read())
            print('Ok')
        except Exception as e:
            print(e)
            sys.exit(1)
    else:
        print('Файл с городами уже существует. Пропускаем скачивание.')


def unpack_cities_file():
    print('Загружаем информацию о городах...', end='')
    cities = dict()
    try:
        with gzip.open(SITIES_FILE) as gz_file:
            cities = json.loads(gz_file.read().decode('utf-8'))
        print('Ok')
    except Exception as e:
        print(e)
        sys.exit(1)
    return cities


def find_city(city, cities):
    res = []
    for one_city in cities:
        if one_city['name'].upper().startswith(city.upper()):
            res.append(one_city)
    return res


def select_city(cities):
    while True:
        print(
            'Введите город на латинице',
            '(Пример: Saint Petersburg, Sankt-Peterburg, Moscow, Moskva):'
            )
        city = input('>')
        city = find_city(city, cities)
        if len(city) > 20:
            print('Найдено слишком много совпадений, уточните город.')
            continue
        if len(city) > 1:
            for i, c in enumerate(city):
                print('{} - {} [{}] : {}/{}'.format(
                    i, c['name'], c['country'],
                    c['coord']['lon'], c['coord']['lat']
                    ))
            try:
                sel = int(input('Выберите город:'))
                city = city[sel]
            except Exception as e:
                print('Ошибка ввода:', e)
                continue
        elif len(city) == 1:
            city = city[0]
        else:
            city = None
        break

    return city


def get_data(city_id):
    APP_ID_FILE = 'app.id'
    try:
        with open(APP_ID_FILE) as app_id_file:
            app_id = app_id_file.read().strip()
    except Exception as e:
        print('Невозможно прочитать файл с app_id')
        sys.exit(1)

    url = 'http://api.openweathermap.org/data/2.5/weather'
    data = urlparse.urlencode({
                'id': city_id,
                'units': 'metric',
                'appid': app_id
                })
    url += '?' + data

    try:
        with requests.urlopen(url) as url:
            if url.getcode() == 200:
                data = json.loads(url.read().decode('utf-8'))
            else:
                raise IOError('Ошибка получения данных!')
    except Exception as e:
        print(e)
        sys.exit(1)

    return data


def save_data(city_id, city_name, date, temp, weather_id):
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cur = conn.cursor()

            # Проверяем, существует ли таблица
            cur.execute("SELECT name FROM sqlite_master WHERE type='table'" + \
                    "AND name='temp_data'")
            if not cur.fetchone():
                cur.execute(
                    'CREATE TABLE temp_data (city_id INT NOT NULL PRIMARY KEY,' + \
                    'city_name VARCHAR(255) NOT NULL, `date` DATE NOT NULL,' + \
                    'temp INT NOT NULL, weather_id INT NOT NULL)'
                    )

            date = datetime.datetime.fromtimestamp(date)

            # Проверяем, существует ли запись с таким городом
            cur.execute("SELECT city_id FROM temp_data WHERE city_id=?", (city_id, ))
            if cur.fetchone():
                cur.execute(
                    "UPDATE temp_data SET `date`=?, temp=?, weather_id=? WHERE city_id=?",
                    (date, temp, weather_id, city_id)
                    )
            else:
                cur.execute(
                    'INSERT INTO temp_data (city_id, city_name, `date`, temp, weather_id) ' + \
                    'VALUES (?, ?, ?, ?, ?)', (city_id, city_name, date, temp, weather_id)
                    )

    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == '__main__':
    check_cities_file()
    cities = unpack_cities_file()
    city = select_city(cities)
    if city == None:
        print('Нет такого города. До свидания')
        sys.exit(1)
    data = get_data(city['id'])
    print('Город: {}, температура: {:+.2f}°C'.format(data['name'], data['main']['temp']))
    print('Сохраняем данные в БД')
    save_data(
            data['id'], data['name'], data['dt'],
            data['main']['temp'], data['weather'][0]['id']
            )
    print('Завершение работы программы')
