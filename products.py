from promotions import Promotion

class Product:

    def __init__(self, name, price, quantity):
        self.name = Product.validate_name(name)
        self.price = Product.validate_price(price)
        self.quantity = Product.validate_quantity(quantity)
        self.active = ''
        self.activate()
        self._promotion = None


    def validate_name(name: str):

        """Validates name of product"""

        try:
            if False in [i.isalnum() for i in name.split()] or name.isspace() or len(name) == 0:
                raise ValueError('Only literals and numbers are allowed.')
            return name
        except AttributeError:
            print('Only literals and numbers are allowed.')
        except ValueError and Exception as e:
            print(f"Such error occurred: {e}")


    def validate_price(price: float):

        """Validates price of product"""

        try:
            if not isinstance(price, (int, float)) or price < 0:
                raise ValueError('Only positive integers are allowed.')
            return price
        except ValueError and Exception as e:
            print(f"Such error occurred: {e}")


    def validate_quantity(quantity: int):

        """Validates quantity of product"""

        try:
            if not str(quantity).isdigit():
                raise ValueError('Only positive integers are allowed.')
            return quantity
        except ValueError and Exception as e:
            print(f"Such error occurred: {e}")


    def get_quantity(self) -> int:

        """Returns quantity of product"""

        return self.quantity


    def set_quantity(self, quantity):

        """Decreases the quantity of product"""

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()


    def is_active(self):

        """Checks if product is active"""

        return self.active


    def activate(self):

        """Activates product"""

        self.active = True


    def deactivate(self):

        """Deactivates product"""

        self.active = False


    def _get_print_info(self):

        """Return the information about thr product"""

        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def show(self):

        """Prints full info of product"""

        print_info = self._get_print_info()
        if self.promotion is not None:
            print_info += f", Promotion: {self.promotion}"
        print(print_info)


    def validate_quantity_in_stock(self, quantity):

        """Validates if it is enough of product in stock"""

        try:
            if self.quantity - quantity < 0:
                raise Exception(f"Oops! There are only {self.quantity} of the {self.name} left.")
            return True
        except Exception as e:
            print(f"Such error occurred: {e}")


    def buy(self, quantity) -> float:

        """
        According to entered quantity decreases the quantity of the product.
        Returns the price of the bought product.
        """

        if self.validate_quantity_in_stock(quantity):
            self.set_quantity(quantity)
            if self._promotion is not None:
                price_with_promotion = self.promotion.apply_promotion(product=self, quantity=quantity)
                return round(price_with_promotion, 1)
            return quantity * self.price


    @property
    def promotion(self):

        """Returns the promotion"""

        return self._promotion


    @promotion.setter
    def promotion(self, new_promotion):

        """Changes the promotion"""

        if not isinstance(new_promotion, Promotion):
            raise ValueError('The promotion must be an instance of the Promotion class')
        else:
            self._promotion = new_promotion


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 0)


    def buy(self, quantity):
        if self._promotion is not None:
            price_with_promotion = self.promotion.apply_promotion(product=self, quantity=quantity)
            return round(price_with_promotion, 1)
        return quantity * self.price


    def _get_print_info(self):
        return f"{self.name}, Price: {self.price}"


    def validate_quantity_in_stock(self, quantity):
        return True


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum


    def buy(self, quantity):
        if quantity > self.maximum:
            quantity = self.maximum
            self.set_quantity(quantity)
            return self.price * quantity, 'Maximum quantity was exceeded'
        return super().buy(quantity)


    def _get_print_info(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Maximum: {self.maximum}"
