# -*- coding: utf-8 -*-

from extensions import InitBaseExtension


class InitRoutes(InitBaseExtension):

    name = 'R'

    def init_app(self, app):  # Инициируем Вьюшки
        self.extension = None

    def configurate_extension(self):
        from ui import get_views
        get_views()
