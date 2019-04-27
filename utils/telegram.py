# -*- coding: utf-8 -*-

import requests
from application import APP


class BotHandler(object):

    api_url = None
    proxies = None

    def __init__(self, app):
        self.make_url(app)

    def make_url(self, app):
        if self.api_url is None:
            self.api_url = app.config['TELEGRAM_BOT_URL']
        self.proxies = app.config['TELEGRAM_BOT_PROXY']

    def get_updates(self, offset=None, timeout=30):
        request_params = {'timeout': timeout,
                          'offset': offset}
        try:
            resp = requests.get(self.api_url + 'getUpdates', request_params, proxies=self.proxies)
            result_json = resp.json()['result']
        except Exception as ex:
            raise
        return result_json

    def send_message(self, chat_id, text):
        try:
            request_params = {'chat_id': chat_id,
                              'text': text}
            resp = requests.post(self.api_url + 'sendMessage', request_params, proxies=self.proxies)
        except Exception as ex:
            raise
        return resp

    def get_last_update(self):
        get_result = self.get_updates()
        count = len(get_result)
        if count > 0:
            last_update = get_result[-1]
        else:
            last_update = None
        print(get_result)
        return last_update


telegram_bot = BotHandler(APP.web_app)
