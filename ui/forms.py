# -*- coding: utf-8 -*-

import os
from wtforms.fields import FileField
from wtforms.widgets import FileInput
from wtforms.widgets.core import HTMLString

from application import APP


class ImageFileInput(FileInput):

    def __call__(self, field, **kwargs):
        html = super(FileInput, self).__call__(field, **kwargs)
        tag = ''
        if field.data:
            image_url = os.path.join(APP.web_app.config['MEDIA_URL'], field.data)
            tag = f'<img src="{image_url}" style="height:150px;object-fit:cover;float:left" alt="{field.name}" />'

        return HTMLString(f'{tag}{html}')


class ImageField(FileField):
    widget = ImageFileInput()

    def __init__(self, *args, **kwargs):
        super(ImageField, self).__init__(*args, **kwargs)
        pass
