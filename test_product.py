import pytest
from products import Product

def test_create_product():
    product_instance = Product('iPhone', 1000, 50)
    assert product_instance.name and product_instance.price and product_instance.price is not None


def test_negative_create_product_name():
    product_instance = Product(1, 1000, 50)
    assert product_instance.name is None


def test_negative_create_product_price():
    product_instance = Product('iPhone', 'asda#$151', 50)
    assert product_instance.price is None


def test_negative_create_product_quantity():
    product_instance = Product('iPhone', 1000, 'ada12$#')
    assert product_instance.quantity is None


def test_product_inactive():
    product_instance = Product('iPhone', 1000, 50)
    product_instance.buy(50)
    assert not product_instance.active


def test_buy_product_quantity_positive():
    product_instance = Product('iPhone', 1000, 50)
    product_instance.buy(20)
    assert product_instance.quantity == 30


def test_buy_product_quantity_negative():
    product_instance = Product('iPhone', 1000, 50)
    assert not product_instance.buy(51)
