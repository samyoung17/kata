# coding=utf-8


class Item:

    def __init__(self, name, unit_price, quantity, unit=None, categories=[]):
        self.name = name
        self.unit_price = unit_price
        self.quantity = quantity
        self.unit = unit
        self.categories = categories


def price_items(items):
    return sum(map(lambda item: item.unit_price * item.quantity, items))


def format_item(item):
    if item.unit is None:
        return '{}\t{}:\t\t\t£{:3.2f}'.format(item.quantity, item.name, item.unit_price * item.quantity)
    else:
        return '\t{}:\t{:3.3f}{} @ £{:3.2f}/{}\t£{:3.2f}'\
            .format(item.name, item.quantity, item.unit, item.unit_price, item.unit, item.unit_price * item.quantity)


def itemised_receipt(items):
    return '\n'.join(map(format_item, items)) + '\n'


def format_subtotal(items):
    return 'Subtotal:\t\t\t£{:3.2f}'.format(price_items(items))
