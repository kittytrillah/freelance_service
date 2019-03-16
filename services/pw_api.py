# -*- coding: utf-8 -*-


from flask_peewee.rest import Authentication


def init_api(api):
    from models.category import Category
    from models.customer import Customer
    from models.order import Order, OrderItem
    from models.product import Product
    from models.client import Client
    from models.freelancer import Freelancer
    from models.job import JobAdvertisement
    from models.proposal import Proposal

    api.default_auth = Authentication(protected_methods=[])
    api.register(Category)
    api.register(Product)
    api.register(Customer)
    api.register(Order)
    api.register(OrderItem)
    api.register(Client)
    api.register(Freelancer)
    api.register(JobAdvertisement)
    api.register(Proposal)

    api.setup()
