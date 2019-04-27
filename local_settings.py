# -*- coding: utf-8 -*-

# Файл с локальными конфигами проекта

# Uncomment on demand

# from settings import *
#
#
# #DB_ENGINE = 'peewee.SqliteDatabase'  # раскомментировать если необходимо работать с SQLite
#
# DATABASE = {'engine': DB_ENGINE,
#             'name': 'kittytrillah', 'user': 'kittytrillah',  # name (имя БД) и user необходимо указать свои
#             'password': 'hci2018hSe',  # password необходимо указать свой
#             'host': 'team2018.piterdata.ninja', 'port': 5432}

# Test version below

from settings import *


DB_ENGINE = 'peewee.SqliteDatabase' # раскомментировать если необходимо работать с SQLite

DATABASE = {'engine': DB_ENGINE,
'name': 'ls.sqlite'}

TELEGRAM_BOT_PROXY = {'https':''}

DOMAIN = '127.0.0.1'
MEDIA_URL = f'//{DOMAIN}/{MEDIA_ROOT}'
