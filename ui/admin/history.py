# -*- coding: utf-8 -*-

from flask_peewee.admin import ModelAdmin


class HistoryAdmin(ModelAdmin):
    columns = ('create_time', 'data',)
