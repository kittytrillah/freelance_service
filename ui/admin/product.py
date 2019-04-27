# -*- coding: utf-8 -*-

from flask import request
from flask_peewee.admin import ModelAdmin

from ui.forms import ImageField


class ProductAdmin(ModelAdmin):

    columns = ('name', 'price', 'preview_description', 'available_quantity', )
    exclude = ('image', )

    def get_template_overrides(self):
        return {'edit': 'admin/product.html'}

    def get_form(self, adding=False, is_edit=False):
        form = super(ProductAdmin, self).get_form(adding)
        if is_edit is False:
            setattr(form, 'image', ImageField())
        return form

    def get_edit_form(self, instance):
        return self.get_form(is_edit=request.method == 'POST')

    def save_model(self, instance, form, adding=False):
        if 'image' in request.files:
            file = request.files['image']
            instance.save_image(file)
        return super(ProductAdmin, self).save_model(instance, form, adding)

