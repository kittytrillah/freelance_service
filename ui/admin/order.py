# -*- coding: utf-8 -*-

from flask import flash
from flask_peewee.admin import ModelAdmin


class OrderAdmin(ModelAdmin):

    # foreign_key_lookups = {'user': 'username'}
    # filter_fields = ('user', 'content', 'pub_date', 'user__username')

    def get_template_overrides(self):
        # override the edit template with a custom one
        return {'index': 'admin/order_index.html'}

    def get_urls(self):
        url = super(OrderAdmin, self).get_urls()
        return url + (
            ('/set_status/<status>/<order_id>/', self.set_status),
        )

    def set_status(self, status, order_id):
        order = self._find_order(order_id)
        if order is None:
            flash(f'Order #{order_id} not found', 'error')

        else:
            if status not in order.get_statuses():
                flash(f'Status "{status}" is incorrect', 'error')
            else:
                if order.order_status != status:
                    if order.order_items.count() > 0:
                        if order and status in order.get_statuses():
                            result = order.set_status(status)
                            if result is not None:
                                flash(f'Successfully "{status}" order #{order_id}', 'success')
                            else:
                                flash(f'Order #{order_id} did not change status to "{status}"', 'error')
                    else:
                        flash(f'Order #{order_id} is empty', 'error')
                else:
                    flash(f'Order #{order_id} already has status "{status}"', 'error')
        return self._index_redirect()

    def _find_order(self, order_id):
        try:
            order = self.get_object(order_id)
        except self.model.DoesNotExist:
            flash(f'Order #{order_id} not found', 'warning')
            return None
        else:
            return order
