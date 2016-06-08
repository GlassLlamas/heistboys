class Inventory:
    def __init__(self, maxItems=20):
        self.maxItems = maxItems
        self._items = dict() # Item ID -> Quantity

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        raise Exception("Directly modifying Inventory._items is not allowed!")

    def add(self, itemStack):
        if itemStack.item.itemName in self.items:
            self.items[item.itemName] += itemStack.quantity
        elif len(self.items.keys()) < self.maxItems:
            self.items[item.itemName] = itemStack.quantity
