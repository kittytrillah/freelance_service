from application import DB
from datetime import datetime
from peewee import *


class Client(DB.Model):

    client_id = PrimaryKeyField()
    first_name = CharField(50, null=False)
    last_name = CharField(50, null=False)
    email = CharField(unique=True, null=False)
    phone = CharField(21, unique=True, null=False)
    birth_day = DateField(null=True)
    create_time = DateTimeField(default=datetime.now, null=False)
    is_active = BooleanField(default=True)
    companyname = CharField(50)

    class Meta:
        table_name = 'clients'

    def __unicode__(self):
        return '%s %s' % (self.last_name, self.first_name)

    def __str__(self):
        return '%s %s' % (self.last_name, self.first_name)