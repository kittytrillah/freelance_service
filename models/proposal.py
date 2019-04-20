# -*- coding: utf-8 -*-

from datetime import datetime
from peewee import *
from difflib import SequenceMatcher
from fuzzywuzzy import fuzz
from application import DB
from models.freelancer import Freelancer
from models.job import JobAdvertisement
from models.client import Client


db = DB.database
approved = 0 #1 when is ready to submit
errors = []


STATUSES = [(1, 'Draft'),
            (2, 'Sent'),
            (3, 'Accepted'),
            (4, 'Cancelled'),
            (5, 'Declined')]


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
    skills_fl = TextField(1200)
    skills_job = TextField(1200)
    scores_demand = IntegerField(null=False)

    class Meta:
        table_name = 'proposals'

    @classmethod
    def proposal_create(cls):
        suitability = cls.select().where(cls.skills_fl == cls.skills_job)  # чекаем подходимость, потом добавить разделение на слова с regex
        # if suitability.exists():
        #     cls.update(cls.priority, 0)
        # else:
        #     cls.update(cls.priority, 1)
        pass

    @classmethod
    def proposal_score(cls, job_hash, skills_current_i):
        print("///skills needed: ")
        try:
            j_db = JobAdvertisement.get(JobAdvertisement.job_hash == job_hash)
            skills_demand_i = j_db.skills
            print(j_db.skills)
        except:
            skills_demand_i = ""
            print("Error while getting job skills")
        #skills_demand_i = JobAdvertisement.select(JobAdvertisement.skills).where(JobAdvertisement.job_hash == job_hash)
        print("///////////////")
        a_str = skills_current_i.lower().replace(',', '')
        b_str = skills_demand_i.lower().replace(',', '')
        ratio = 0
        if b_str in a_str: #что если несколько скиллов - поправить
            ratio = 100
        else:
            ratio = fuzz.ratio(skills_current_i.lower().replace(',', ''), skills_demand_i.lower().replace(',', ''))
        print("ratio: ")
        print(ratio)
        return ratio

    @classmethod
    def get_proposal_score(cls, id_job):
        try:
            j_db = JobAdvertisement.get(JobAdvertisement.job_hash == id_job)
            score = j_db.job_demand
        except:
            score = 0
        #score = JobAdvertisement.select(JobAdvertisement.job_demand).where(JobAdvertisement.job_hash == id_job).get()  # выбираем по id
        print("///score is:")
        print("///////////////")
        print(score)
        print("///////////////////")

        return score


    @staticmethod
    def StatusChange(status_a, status_b):
        pass


    @staticmethod
    def ShowError(error_str):
        errors.append(error_str)
        print(errors)
        pass