# -*- coding: utf-8 -*-

from datetime import datetime
from peewee import *

from application import DB
from models.client import Client
from models.freelancer import Freelancer


STATUSES = [(1, 'Active'),
            (2, 'Taken'),
            (3, 'Completed'),
            (4, 'Cancelled'),
            (5, 'Draft')]

JOBPAYTYPES = [(1, 'Hourly'),
            (2, 'Fixed'),
            (3, 'Monthly')]

JOBTYPES = [(1, 'Coding'),
            (2, 'Design'),
            (3, 'Modelling')]



class JobAdvertisement(DB.Model):

    job_id = PrimaryKeyField()
    client_id = ForeignKeyField(Client, to_field='client_id', null=False)
    job_status = IntegerField(choices=STATUSES, null=False)
    create_time = DateTimeField(default=datetime.now, null=False)
    price = CharField(null=False)
    description = TextField(1200)
    job_name = TextField(300)
    job_hash = TextField(256)
    job_paytype = IntegerField(choices=JOBPAYTYPES, null=False)
    job_type = IntegerField(choices=JOBTYPES, null=False)
    job_fixed_by = ForeignKeyField(Freelancer, to_field='freelancer_id', null=True)
    skills = TextField(300) #скиллы через запятую, чтобы делить regex потом
    job_lock = IntegerField(null=False) #0 - soft lock/ 1 - hard lock
    job_demand = IntegerField(null=False) # 0-100 points

    class Meta:
        table_name = 'jobs'
