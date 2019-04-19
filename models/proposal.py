# -*- coding: utf-8 -*-

from datetime import datetime
from peewee import *
from difflib import SequenceMatcher

from application import DB
from models.freelancer import Freelancer
from models.job import JobAdvertisement
from models.client import Client


db = DB.database
approved = 0 #1 when is ready to submit


class BaseModel(DB.Model):

    class Meta:
        database = db


class Proposal(DB.Model):

    proposal_id = PrimaryKeyField()
    freelancer_id = ForeignKeyField(Freelancer, to_field='freelancer_id', null=False)
    client_id = ForeignKeyField(Client, to_field='client_id')
    proposal_time = DateTimeField(default=datetime.now, null=False)
    offeredprice = CharField(null=False)
    proposal_text = TextField(1200)
    jobadv_id = ForeignKeyField(JobAdvertisement, to_field='job_id', null=False)
    priority = IntegerField(null=False) #0 - First priority/ 1 - Second priority
    # skills_fl = ForeignKeyField(Freelancer, to_field='skills', null=False)
    # skills_job = ForeignKeyField(JobAdvertisement, to_field='skills', null=False)
    # scores_demand = ForeignKeyField(JobAdvertisement, to_field='job_demand', null=False)
    skills_fl = TextField(1200)
    skills_job = TextField(1200)
    scores_demand = IntegerField(null=False)

    class Meta:
        table_name = 'proposals'

    @classmethod
    def proposal_create(cls):
        suitability = cls.select().where(cls.skills_fl == cls.skills_job)  # чекаем подходимость, потом добавить разделение на слова с regex
        if suitability.exists():
            cls.update(cls.priority, 0)
        else:
            cls.update(cls.priority, 1)

    @classmethod
    def proposal_score(cls, skills_fl, skills_job):
        percentage = SequenceMatcher(None, skills_fl, skills_job).ratio()
        if percentage >= cls.scores_demand:
            approved = 1
            pass

