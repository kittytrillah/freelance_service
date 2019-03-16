# -*- coding: utf-8 -*-

from datetime import datetime
from peewee import *

from application import DB
from models.freelancer import Freelancer
from models.job import JobAdvertisement


class Proposal(DB.Model):

    proposal_id = PrimaryKeyField()
    freelancer_id = ForeignKeyField(Freelancer, to_field='freelancer_id', null=False)
    proposal_time = DateTimeField(default=datetime.now, null=False)
    offeredprice = CharField(null=False)
    proposal_text = TextField(1200)
    jobadv_id = ForeignKeyField(JobAdvertisement, to_field='job_id', null=False)

    class Meta:
        table_name = 'proposals'
