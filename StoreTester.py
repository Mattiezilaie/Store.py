# Author: Mahtab Zilaie
# Date: January 15, 2020
# Description: Testing for Store module. Tests for same product title, different
# names, equal price, equal member status, and almost equal price(float number).

import unittest
import Store

class Testing(unittest.TestCase):

    """Defines unit tests for the Store module"""

    def test_1(self):
        products = Store.Product(1,"eggs","dairy", 1.99, 4)
        self.assertEqual(products.get_title(), "eggs")

    def test_2(self):
        customer = Store.Customer("Sam", "FRW", False)
        self.assertNotEqual(customer.get_name(), "Samantha")

    def test_3(self):
        products = Store.Product(2, "shampoo", "haircare", 2.55, 3)
        self.assertEqual(products.get_price(),2.55)

    def test_4(self):
        products = Store.Product(3,"notebook", "school supplies", 3.50, 6)
        self.assertAlmostEqual(products.get_price(), 3.500000000000001)

    def test_5(self):
        customer = Store.Customer("Ben", "GGF", True)
        self.assertEqual(customer.is_premium_member(),True)


if __name__ == '__main__':
    unittest.main()
