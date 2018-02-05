# coding=utf-8

import unittest
from supermarket import *


class TestBasicPricing(unittest.TestCase):

    def test_price_one_item(self):
        items = [Item('onion', 0.75, 0.8)]
        price = base_price_items(items)
        self.assertAlmostEquals(price, 0.6)

    def test_price_two_items(self):
        items = [Item('onion', 0.75, 0.8), Item('strawberries', 1.2, 1)]
        price = base_price_items(items)
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


class TestSubtotal(unittest.TestCase):

    def test_itemise_one_item(self):
        items = [Item('ball', 1.0, 1), Item('pen', 12.0, 2), Item('onions', 0.75, 0.8, unit='kg')]
        subtotal = format_subtotal(items)
        self.assertEquals(subtotal, 'Subtotal:\t\t\t£25.60')


def half_price(items):
    return -0.5 * sum(map(lambda item: item.unit_price * item.quantity, items))


class TestHalfPrice(unittest.TestCase):

    def test_half_price_toys(self):
        items = [Item('ball', 1.0, 1, categories=['toys'])]
        discounts = [Discount('50% off', 'toys', half_price)]
        discount = total_discount(discounts, items)
        self.assertEquals(discount, -0.5)

    def test_half_price_toys_formatting(self):
        items = [Item('ball', 1.0, 1, categories=['toys'])]
        discounts = [Discount('50% off', 'toys', half_price)]
        receipt = itemised_discounts(discounts, items)
        self.assertEquals(receipt, '50% off toys:\t\t\t£-0.50\n')

    def test_half_price_toys_doesnt_apply_to_pens(self):
        items = [Item('ball', 1.0, 1, categories=['toys']), Item('pen', 12.0, 2, categories=['stationary'])]
        discounts = [Discount('50% off', 'toys', half_price)]
        discount = total_discount(discounts, items)
        self.assertAlmostEquals(discount, -0.5)


if __name__ == '__main__':
    unittest.main()