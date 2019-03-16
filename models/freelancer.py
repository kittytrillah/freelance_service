from application import DB
from datetime import datetime
from peewee import *


class Freelancer(DB.Model):

    freelancer_id = PrimaryKeyField()
    first_name = CharField(50, null=False)
    last_name = CharField(50, null=False)
    email = CharField(unique=True, null=False)
    phone = CharField(21, unique=True, null=False)
    birth_day = DateField(null=True)
    create_time = DateTimeField(default=datetime.now, null=False)
    is_active = BooleanField(default=True)
    skills = CharField(unique=False, null=False)
    expyears = CharField(3, null=False)

    class Meta:
        table_name = 'freelancers'

    def __unicode__(self):
        return '%s %s' % (self.last_name, self.first_name)

    def __str__(self):
        return '%s %s' % (self.last_name, self.first_name)