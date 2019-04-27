# -*- coding: utf-8 -*-

from flask_peewee.admin import Admin, ModelAdmin

from extensions import InitBaseExtension


class InitAdminDashboard(InitBaseExtension):

    name = 'admin'

    def init_app(self, app):  # Инициируем Админку
        web_app = app.web_app
        self.extension = Admin(web_app, app.auth, branding=web_app.config['SITE_NAME'])

    def configurate_extension(self):
        self.make_models_view()
        self.make_panels()
        self.extension.setup()

    def make_models_view(self):
        from ui.admin import get_admin_models

        models = get_admin_models()
        if models:
            for m in models:
                orm_m, adm_m = m if len(m) == 2 else [m[0], ModelAdmin]
                self.extension.register(orm_m, adm_m)

    def make_panels(self):
        from ui.admin import get_admin_panels

        panels = get_admin_panels()
        if panels:
            for title, panel in panels:
                self.extension.register_panel(title, panel)
