# -*- coding: utf-8 -*-

from flask_peewee.admin import AdminPanel
from utils.telegram import telegram_bot


class TelegramPanel(AdminPanel):
    template_name = 'admin/telegram_panel.html'

    def get_urls(self):
        return (
            ('/messages/', self.get_messages),
        )

    def get_messages(self):
        return {}

    def get_context(self):
        return {'messages': telegram_bot.get_updates() }
