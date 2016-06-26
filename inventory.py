import os

from buffalo import utils

import textures

class Inventory:
    def __init__(self, maxItems=20):
        self.maxItems = maxItems
        self._items = dict() # item name -> itemstack
        Inventory.loadSprites()
        self.render()

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        raise Exception("Directly modifying Inventory._items is not allowed!")

    def add(self, itemStack):
        if itemStack.item.itemName in self.items:
            self.items[itemStack.item.itemName].quantity += itemStack.quantity
        elif len(self.items.keys()) < self.maxItems:
            self.items[itemStack.item.itemName] = itemStack
        self.render()

    def render(self):
        if not hasattr(Inventory, "backgroundSprite"):
            Inventory.loadSprites()
        self.surface = utils.empty_surface((88, 408))
        self.surface.blit(Inventory.backgroundSprite, (0, 0))
        for index, element in enumerate(self.items.items()):
            itemName, itemStack = element
            itemStack.render()
            pos = (8 + (index % 2) * 40, 8 + (index // 2) * 40)
            itemStack.blit(self.surface, pos)

    def blit(self, dest):
        if self.surface is not None:
            dest.blit(
                self.surface,
                (utils.SCREEN_W - 88, int(utils.SCREEN_H / 2 - 204))
            )

    def loadSprites():
        bgPath = os.path.join("sprites", "misc", "inventory", "background.png")
        Inventory.backgroundSprite = textures.getSprite(bgPath)
