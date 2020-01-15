# Author: Mahtab Zilaie
# Date: January 15 2019
# Description: Program with three classes: Product, Customer, and Store. The Product class initializes five data
# members:id_code, title, description, price, quantity_available. All five data members are initialized and have get
# methods. The Customer class has three data members:name, account_id, and premium member. All three data members are
# initializedand have get methods. The Customer class is used to get all the data for the customer and their cart.
# Finally, thenStore class has no data members but two parameters are initialized which are members and inventory. In
# this class products and members are added to the inventory and members list. This is where customers checkout and get
# their total price for all products in their cart and where members are verified.



class InvalidCheckoutError(Exception):
    pass





class Product:

    """Class named Product contains five data members: id_codes, title, description, price, and quantity_available"""

    def __init__(self, id_code, title, description, price, quantity_available):

        """Initializes five parameters: id_code, title, description, price, and quantity_available"""

        self._id_code = id_code
        self._title = title
        self._description = description
        self._price = price
        self._quantity_available = quantity_available
        # all data members in class- Product are private



    def get_id_code(self):

        """The function returns id_code"""

        return self._id_code



    def get_title(self):

        """The function returns the title"""
        return self._title



    def get_description(self):

        """The function returns the description"""

        return self._description



    def get_price(self):

        """Function returns the price"""

        return self._price



    def get_quantity_available(self):

        """Function returns the quantity available"""

        return self._quantity_available



    def decrease_quantity(self):

        """Function reduces the quantity available by 1"""

        self._quantity_available = self._quantity_available - 1
        return self._quantity_available




class Customer:

    """Class named Customer has three data members:name, account_id, and premium member"""

    def __init__(self, name, account_id, premium_member):

        """Initializes parameters: name, account_id, and premium_member"""

        self._name = name
        self._account_id = account_id
        self._premium_member = premium_member
        self.customer_cart = []



    def get_customer_cart(self):

        """Function returns customer's cart"""

        return self.customer_cart



    def get_name(self):

        """function returns customer's name"""

        return self._name



    def get_account_id(self):

        """function returns customer's account id"""

        return self._account_id



    def is_premium_member(self):

        """Function returns if customer is premium member"""

        return self._premium_member



    def add_product_to_cart(self, product_id):

        """Function adds product to cart with product id"""

        self.customer_cart.append(product_id)
        # adds product_id to customer_cart



    def empty_cart(self):

        """function empties customer's cart"""

        self.customer_cart.clear()
        # customer_cart will go to empty



class Store:

    """Class named Store with no data members"""


    def __init__(self):

        """Initializes parameters: inventory and members """

        self._inventory = []
        self._members = []



    def add_product(self, product):

        """function adds products to store inventory"""

        self._inventory.append(product)
        # adds products to inventory list



    def add_member(self, member):

        """function adds members to members list"""

        self._members.append(member)
        # adds member to members list



    def get_product_from_id(self, id_code):

        """function iterates through inventory list with id_code"""

        for product in self._inventory:
            if id_code == product.get_id_code():
                return product
            else:
                return None
            # goes through inventory list to get products and find their id codes or returns special value None



    def get_member_from_ID(self, account_id):

        """function iterates through members list to check if account id matches customer id"""

        for customer in self._members:
            if account_id == customer.get_account_id():
                return customer
            return None
        # iterates through members list to see if account id matches customer if yes returns the customer w/ id if not returns special val None



    def product_search(self, key):

        """function iterates through inventory list to check for id_codes and add to list"""

        id_codes = []  # id_codes into a list
        first = key[:1]
        new = first.lower()  # lowercase
        for product in self._inventory:
            if product.get_title().find(key) > -1 or product.get_description().find(key) > -1:
                id_codes.append(product)  # adds products to list
                id_codes.sort()  # sort id_codes list
        return id_codes  # returns id_codes



    def add_product_to_member_cart(self, product_id, member_id):

        """function adds products to cart for valid member id's"""

        product = self.get_product_from_id(product_id)
        customer = self.get_member_from_ID(member_id)
        if product is None:
            return "product ID not found"
        elif customer is None:
            return "member ID not found"
        else:
            if product.get_quantity_available() > 0:
                customer.add_product_to_cart(product.get_id_code())
                return "product added to cart"
            else:
                return "product out of stock"


    def check_out_member(self, member_id):

        """function makes sure product is available and adds prices of products from customers cart. function also figues out if customer is a premium member
         or not and figures out total price """

        total_price_of_products = 0.00
        total_price = 0.00
        shipping = 0.00
        member = self.get_member_from_ID(member_id)
        if member is None:
            raise InvalidCheckoutError
        else:
            if member.get_customer_cart() == 0:
                print("No items in cart")
            for i in member.get_customer_cart():
                product = self.get_product_from_id(i)
                if product.get_quantity_available() <= 0:
                    print('Sorry, product' + product.get_id_code + ',' + product.get_title())
                else:
                    total_price_of_products = total_price_of_products + product.get_price()
                    product.decrease_quantity()
            if member.is_premium_member() is True:
                total_price = total_price_of_products
            else:
                shipping = .07 * total_price_of_products
                total_price = shipping + total_price_of_products
        print("Subtotal: $" + str(total_price_of_products))
        print("Shipping: $" + str(shipping))
        print("Total: $" + str(total_price))
        member.empty_cart()
        return total_price



def main():
    try:
        check_out_member = None
    except InvalidCheckoutError:
        print("Sorry invalid checkout, which is not allowed")



if __name__ == '__main__':
    store = Store()


