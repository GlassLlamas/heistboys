import os

import pygame

import animate
import inventory

class Player(animate.Animate):

    DEFAULT_SPRITE_PATH = os.path.join("sprites", "animate", "default_player")

    def __init__(self, pos, spritePath=None, inv=None):
        spritePath = spritePath if spritePath is not None else Player.DEFAULT_SPRITE_PATH
        super().__init__(pos, spritePath)
        if inv is None:
            inv = inventory.Inventory()
        self.inventory = inv

    def update(self, keys, level):
        self.movingUp, self.movingLeft, self.movingDown, self.movingRight, self.running = (
            keys[pygame.K_w],
            keys[pygame.K_a],
            keys[pygame.K_s],
            keys[pygame.K_d],
            keys[pygame.K_LSHIFT],
        )
        super().update(level)

    def pickup(self, itemStack):
        self.inventory.add(itemStack)

    def blit(self, dest, offset):
        super().blit(dest, offset)
        self.inventory.blit(dest)
