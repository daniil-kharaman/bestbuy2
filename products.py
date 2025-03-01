class Product:

    def __init__(self, name, price, quantity):
        self.name = Product.validate_name(name)
        self.price = Product.validate_price(price)
        self.quantity = Product.validate_quantity(quantity)
        self.active = ''
        self.activate()


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


    def show(self):

        """Prints full info of product"""

        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")


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
            return quantity * self.price


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 0)


    def buy(self, quantity):
        return quantity * self.price


    def show(self):

        """Prints full info of product"""

        print(f"{self.name}, Price: {self.price}")


    def validate_quantity_in_stock(self, quantity):

        """Validates if it is enough of product in stock"""

        return True


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum


    def buy(self, quantity):
        if quantity > self.maximum:
            return
        if self.validate_quantity_in_stock(quantity):
            self.set_quantity(quantity)
            return quantity * self.price


    def show(self):

        """Prints full info of product"""

        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Maximum: {self.maximum}")
