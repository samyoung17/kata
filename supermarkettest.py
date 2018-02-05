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


class TestHalfPrice(unittest.TestCase):

    def test_half_price_toys(self):
        items = [Item('ball', 1.0, 1, categories=['toys'])]
        discounts = [Discount('50% off', 'toys', half_price)]
        discount = total_discount(discounts, items)
        self.assertAlmostEquals(discount, -0.5)

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


class TestTwoForOne(unittest.TestCase):

    def test_two_for_one_pens(self):
        items = [Item('lamy', 12.0, 2, categories=['pens'])]
        discounts = [Discount('2 for 1', 'pens', two_for_one)]
        discount = total_discount(discounts, items)
        self.assertAlmostEquals(discount, -12.0)

    def test_cheapest_pen_is_free(self):
        items = [Item('lamy', 12.0, 1, categories=['pens']), Item('parker', 11.0, 1, categories=['pens'])]
        discounts = [Discount('2 for 1', 'pens', two_for_one)]
        discount = total_discount(discounts, items)
        self.assertAlmostEquals(discount, -11.0)

    def test_odd_number_of_items(self):
        items = [Item('lamy', 12.0, 2, categories=['pens']), Item('parker', 11.0, 1, categories=['pens'])]
        discounts = [Discount('2 for 1', 'pens', two_for_one)]
        discount = total_discount(discounts, items)
        self.assertAlmostEquals(discount, -11.0)

    def test_formatting(self):
        items = [Item('lamy', 12.0, 2, categories=['pens'])]
        discounts = [Discount('2 for 1', 'pens', two_for_one)]
        receipt = itemised_discounts(discounts, items)
        self.assertEquals(receipt, '2 for 1 pens:\t\t\t£-12.00\n')

    def test_pens_offer_doesnt_apply_to_toys(self):
        items = [Item('lamy', 12.0, 2, categories=['pens']), Item('ball', 1.0, 2, categories=['toys'])]
        discounts = [Discount('3 for 2', 'pens', two_for_one)]
        discount = total_discount(discounts, items)
        self.assertAlmostEquals(discount, -12.0)


class TestThreeForTwo(unittest.TestCase):

    def test_three_for_two_pens(self):
        items = [Item('lamy', 12.0, 3, categories=['pens'])]
        discounts = [Discount('3 for 2', 'pens', three_for_two)]
        discount = total_discount(discounts, items)
        self.assertAlmostEquals(discount, -12.0)

    def test_cheapest_pen_is_free(self):
        items = [Item('lamy', 12.0, 2, categories=['pens']), Item('parker', 11.0, 1, categories=['pens'])]
        discounts = [Discount('3 for 2', 'pens', three_for_two)]
        discount = total_discount(discounts, items)
        self.assertAlmostEquals(discount, -11.0)

    def test_four_items(self):
        items = [Item('lamy', 12.0, 2, categories=['pens']), Item('parker', 11.0, 2, categories=['pens'])]
        discounts = [Discount('3 for 2', 'pens', three_for_two)]
        discount = total_discount(discounts, items)
        self.assertAlmostEquals(discount, -11.0)

    def test_six_items(self):
        items = [Item('lamy', 12.0, 3, categories=['pens']), Item('parker', 11.0, 3, categories=['pens'])]
        discounts = [Discount('3 for 2', 'pens', three_for_two)]
        discount = total_discount(discounts, items)
        self.assertAlmostEquals(discount, -22.0)

    def test_formatting(self):
        items = [Item('lamy', 12.0, 3, categories=['pens'])]
        discounts = [Discount('3 for 2', 'pens', three_for_two)]
        receipt = itemised_discounts(discounts, items)
        self.assertEquals(receipt, '3 for 2 pens:\t\t\t£-12.00\n')

    def test_pens_offer_doesnt_apply_to_toys(self):
        items = [Item('lamy', 12.0, 3, categories=['pens']), Item('ball', 1.0, 3, categories=['toys'])]
        discounts = [Discount('3 for 2', 'pens', three_for_two)]
        discount = total_discount(discounts, items)
        self.assertAlmostEquals(discount, -12.0)


class TestThreeForSixQuid(unittest.TestCase):

    def test_three_for_six_quid_ales(self):
        items = [Item('bath', 2.5, 3, categories=['ales'])]
        discounts = [Discount('3 for £6', 'ales', three_for_six_quid)]
        discount = total_discount(discounts, items)
        self.assertAlmostEquals(discount, -1.5)

    def test_different_ales(self):
        items = [Item('bath', 2.5, 2, categories=['ales']), Item('speckled', 2.8, 1, categories=['ales'])]
        discounts = [Discount('3 for £6', 'ales', three_for_six_quid)]
        discount = total_discount(discounts, items)
        self.assertAlmostEquals(discount, -1.8)

    def test_four_items(self):
        items = [Item('bath', 2.5, 2, categories=['ales']), Item('speckled', 2.8, 2, categories=['ales'])]
        discounts = [Discount('3 for £6', 'ales', three_for_six_quid)]
        discount = total_discount(discounts, items)
        self.assertAlmostEquals(discount, -2.1)

    def test_six_items(self):
        items = [Item('bath', 2.5, 3, categories=['ales']), Item('speckled', 2.8, 3, categories=['ales'])]
        discounts = [Discount('3 for £6', 'ales', three_for_six_quid)]
        discount = total_discount(discounts, items)
        self.assertAlmostEquals(discount, -3.9)

    def test_cheap_ales(self):
        items = [Item('john_smith', 1.5, 3, categories=['ales'])]
        discounts = [Discount('3 for £6', 'ales', three_for_six_quid)]
        discount = total_discount(discounts, items)
        self.assertAlmostEquals(discount, 0)

    def test_formatting(self):
        items = [Item('bath', 2.5, 3, categories=['ales'])]
        discounts = [Discount('3 for £6', 'ales', three_for_six_quid)]
        receipt = itemised_discounts(discounts, items)
        self.assertEquals(receipt, '3 for £6 ales:\t\t\t£-1.50\n')

if __name__ == '__main__':
    unittest.main()