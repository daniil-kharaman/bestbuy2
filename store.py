from products import Product, LimitedProduct


class Store:

    def __init__(self, store_products: list):
        self.store_products = Store.validate_products(store_products)


    def validate_products(store_products):

        """Validates the entered store products"""

        try:
            if not isinstance(store_products, list):
                raise TypeError('Products must be a list')
            if len(store_products) == 0:
                raise ValueError('List is empty')
            for product in store_products:
                if not isinstance(product, Product):
                    raise TypeError('Wrong format of the product. Only Product type is allowed.')
            return store_products
        #I didn't get why I should just return here None, because anyway None will be returned.
        except TypeError and ValueError and Exception as e:
            print(f"Such error occurred: {e}")


    def validate_product(product):

        """Validates the entered store product"""

        try:
            if not isinstance(product, Product):
                raise TypeError('Only Product type is allowed')
            return product
        except TypeError and Exception as e:
            print(f"Such error occurred: {e}")


    def add_product(self, product: Product):

        """Adds store product"""
        checked_product = Store.validate_product(product)
        if checked_product is not None:
            self.store_products.append(checked_product)


    def remove_product(self, product: Product):

        """Removes store product"""

        if product in self.store_products:
            self.store_products.remove(product)
        else:
            print('There is no such product in the store.')


    def get_total_quantity(self):

        """Returns amount of products in the store"""

        return len(self.store_products)


    def get_all_products(self):

        """Returns the list of products in the store if they are active"""

        return [product for product in self.store_products if product.is_active()]


    def list_all_products(product_list):

        """Prints full info about entered products"""

        print('_' * 10)
        for number, product in enumerate(product_list, 1):
            print(f"{number}.", end=' '), product.show()


    def show_total_amount_in_store(product_list):

        """Prints total quantity of the all products in the store"""

        total_amount = 0
        for product in product_list:
            total_amount += product.quantity
        print(f"Total of {total_amount} items in store")


    def validate_shopping_list(shopping_list):

        """Validates list of products, which is necessary to make the order"""

        try:
            if not isinstance(shopping_list, list):
                raise TypeError('Invalid format of the shopping list.')
            return shopping_list
        except TypeError and Exception as e:
            print(f"Such error occurred: {e}")


    def order(self, shopping_list: list):

        """
        According to the entered list of products decreases their amount in the store
        and returns the total price of the order.
        """

        shopping_list = Store.validate_shopping_list(shopping_list)
        if shopping_list is None:
            return 'Impossible to make the order.'
        total_price = 0
        for order_item in shopping_list:
            product, quantity = order_item
            item_price = product.buy(quantity)
            if isinstance(product, LimitedProduct) and item_price is None:
                return f"Order was partially made. Only 1 item is allowed for the {product.name}"
            if item_price is None:
                return 'Order was partially made.'
            total_price += item_price
        return total_price
