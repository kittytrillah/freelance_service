# -*- coding: utf-8 -*-


def get_admin_models():
    from models.client import Client
    from models.freelancer import Freelancer
    from models.job import JobAdvertisement
    from models.proposal import Proposal

    from ui.admin.customer import CustomerAdmin
    from ui.admin.history import HistoryAdmin
    from ui.admin.order import OrderAdmin
    from ui.admin.product import ProductAdmin

    return [
        (Client, CustomerAdmin),
        (Freelancer, OrderAdmin),
        (JobAdvertisement, HistoryAdmin),
        (ProductAdmin, ProductAdmin),
    ]


def get_admin_panels():
    from ui.admin.telegram_panel import TelegramPanel
    # return [
    #     ('Telegram', TelegramPanel)
    # ]
    return None
