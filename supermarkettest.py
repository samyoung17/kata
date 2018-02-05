import unittest
from supermarket import *


class TestBasicPricing(unittest.TestCase):

    def test_price_single_item(self):
        items = [Item('onion', 1, 3.2)]
        price = price_items(items)
        self.assertEquals(price, 3.2)

if __name__ == '__main__':
    unittest.main()