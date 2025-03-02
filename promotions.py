from abc import ABC, abstractmethod

class Promotion(ABC):
    @property
    @abstractmethod
    def name(self):

        """Returns name of the promotion"""

        pass


    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:

        """Returns the discounted price after promotion was applied"""

        pass


    def __str__(self):
        return self.name


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        self._name = name
        self._percent = percent


    @property
    def name(self):
        return self._name


    @property
    def percent(self):

        """Returns the discount's percent"""

        return self._percent


    def apply_promotion(self, product, quantity) -> float:
        percent = self.percent / 100
        discount = product.price * percent
        price_with_discount = product.price - discount
        return price_with_discount * quantity


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        self._name = name.title()


    @property
    def name(self):
        return self._name


    def apply_promotion(self, product, quantity) -> float:
        quantity_every_second_item = quantity // 2
        second_item_price = product.price / 2
        items_with_full_price = quantity - quantity_every_second_item
        return items_with_full_price * product.price + quantity_every_second_item * second_item_price


class ThirdOneFree(Promotion):
    def __init__(self, name):
        self._name = name


    @property
    def name(self):
        return self._name


    def apply_promotion(self, product, quantity) -> float:
        quantity_every_third_item = quantity // 3
        third_item_price = 0
        items_with_full_price = quantity - quantity_every_third_item
        return items_with_full_price * product.price + quantity_every_third_item * third_item_price
