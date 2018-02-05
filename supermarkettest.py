# coding=utf-8

import unittest
from supermarket import *


class TestBasicPricing(unittest.TestCase):

    def test_price_one_item(self):
        items = [Item('onion', 0.75, 0.8)]
        price = price_items(items)
        self.assertAlmostEquals(price, 0.6)

    def test_price_two_items(self):
        items = [Item('onion', 0.75, 0.8), Item('strawberries', 1.2, 1)]
        price = price_items(items)
        self.assertAlmostEquals(price, 1.8)


class TestItemisedReceipt(unittest.TestCase):

    def test_itemise_one_item(self):
        items = [Item('ball', 1.0, 1)]
        receipt = itemised_receipt(items)
        self.assertEquals(receipt, '1\tball:\t\t\t£1.00\n')

    def test_itemise_two_items(self):
        items = [Item('ball', 1.0, 1), Item('pen', 12.0, 2)]
        receipt = itemised_receipt(items)
        self.assertEquals(receipt, '1\tball:\t\t\t£1.00\n2\tpen:\t\t\t£24.00\n')

    def test_itemise_onions(self):
        items = [Item('onions', 0.75, 0.8, unit='kg')]
        receipt = itemised_receipt(items)
        self.assertEquals(receipt, '\tonions:\t0.800kg @ £0.75/kg\t£0.60\n')

    def test_mixed_list(self):
        items = [Item('ball', 1.0, 1), Item('pen', 12.0, 2), Item('onions', 0.75, 0.8, unit='kg')]
        receipt = itemised_receipt(items)
        self.assertEquals(receipt, '1\tball:\t\t\t£1.00\n2\tpen:\t\t\t£24.00\n\tonions:\t0.800kg @ £0.75/kg\t£0.60\n')


if __name__ == '__main__':
    unittest.main()