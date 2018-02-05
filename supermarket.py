class Item:

    def __init__(self, name, unit_price, quantity, categories=[]):
        self.name = name
        self.unit_price = unit_price
        self.quantity = quantity
        self.categories = categories


def price_items(items):
    return sum(map(lambda item: item.unit_price * item.quantity, items))