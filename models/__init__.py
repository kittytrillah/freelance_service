# -*- coding: utf-8 -*-


def init_models(db):

    # from models.category import Category
    # from models.customer import Customer
    # from models.order import Order, OrderItem
    # from models.product import Product
    from models.client import Client
    from models.freelancer import Freelancer
    from models.job import JobAdvertisement
    from models.proposal import Proposal

    msa = [Client, Freelancer, JobAdvertisement, Proposal]
    #db.database.drop_tables(msa)
    db.database.create_tables(msa)
