# -*- coding: utf-8 -*-

from flask import render_template, flash
from application import APP

from models.product import Product


@APP.web_app.route('/')
def all_products():
    # flash('suprice', 'info')
    products = Product.get_available()
    return render_template('product/all.html', title='Главная', products=products)


@APP.web_app.route('/product/<int:product_id>')
def current_product(product_id):
    # flash('suprice', 'info')
    product = Product.get_available(product_id=product_id)
    return render_template('product/current.html', title=product.name, product=product)
