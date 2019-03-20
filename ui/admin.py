# -*- coding: utf-8 -*-

from flask_peewee.admin import Admin, ModelAdmin
from flask_peewee.auth import Auth


class CustomerAdmin(ModelAdmin):
    columns = ('last_name', 'first_name', 'email', 'is_active',)


def init_admin(app, db):

    auth_admin = Auth(app, db)

    User = auth_admin.User
    User.create_table(fail_silently=True)

    if not User.select().where(User.username == 'admin').exists():
        admin = User(username='admin', email='', admin=True, active=True)
        admin.set_password('admin')
        admin.save()

    admin = Admin(app, auth_admin)

    from models.client import Client
    from models.freelancer import Freelancer
    from models.job import JobAdvertisement
    from models.proposal import Proposal

    admin.register(Client)
    admin.register(Freelancer)
    admin.register(JobAdvertisement)
    admin.register(Proposal)
    admin.setup()

    return admin
