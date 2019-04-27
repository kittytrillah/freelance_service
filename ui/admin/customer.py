# -*- coding: utf-8 -*-

from flask import flash
from flask_peewee.admin import ModelAdmin


class CustomerAdmin(ModelAdmin):
    columns = ('last_name', 'first_name', 'email', 'is_active',)

    def get_template_overrides(self):
        # override the edit template with a custom one
        return {'index': 'admin/customer_index.html'}

    def get_urls(self):
        url = super(CustomerAdmin, self).get_urls()
        return url + (
            ('/<customer_id>/send_message/', self.send_message),
        )

    def send_message(self, customer_id):

        customer = self._find_customer(customer_id)

        if customer:
            status = customer.send_message(customer_id)
            if status is True:
                flash(f'Successfully sent message by telegram to "{customer}"', 'success')
            else:
                flash(f'Message not sent by telegram to "{customer}"', 'error')

        return self._index_redirect()

    def _find_customer(self, customer_id):
        try:
            customer = self.get_object(customer_id)
        except self.model.DoesNotExist:
            flash('Customer not found', 'warning')
            return None
        else:
            return customer
