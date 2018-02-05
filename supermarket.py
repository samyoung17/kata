# coding=utf-8


class Item:

    def __init__(self, name, unit_price, quantity, unit=None, categories=[]):
        self.name = name
        self.unit_price = unit_price
        self.quantity = quantity
        self.unit = unit
        self.categories = categories


class Discount:

    def __init__(self, name, category, rule):
        self.name = name
        self.category = category
        self.rule = rule


def base_price_items(items):
    return sum(map(lambda item: item.unit_price * item.quantity, items))


def calculate_discount(discount, items):
    eligible_items = filter(lambda item: discount.category in item.categories, items)
    return discount.rule(eligible_items)


def total_discount(discounts, items):
    return sum(map(lambda discount: calculate_discount(discount, items), discounts))


def format_item(item):
    if item.unit is None:
        return '{}\t{}:\t\t\t£{:3.2f}\n'.format(item.quantity, item.name, item.unit_price * item.quantity)
    else:
        return '\t{}:\t{:3.3f}{} @ £{:3.2f}/{}\t£{:3.2f}\n'\
            .format(item.name, item.quantity, item.unit, item.unit_price, item.unit, item.unit_price * item.quantity)


def itemised_receipt(items):
    return ''.join(map(format_item, items))


def format_subtotal(items):
    return 'Subtotal:\t\t\t£{:3.2f}'.format(base_price_items(items))


def format_discount(discount, items):
    return '{} {}:\t\t\t£{:3.2f}\n'.format(discount.name, discount.category, discount.rule(items))


def itemised_discounts(discounts, items):
    return ''.join(map(lambda discount: format_discount(discount, items), discounts))
