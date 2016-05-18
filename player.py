import os

import pygame

import animate

class Player(animate.Animate):

    DEFAULT_SPRITE_PATH = os.path.join("sprites", "default_player")

    def __init__(self, pos, spritePath=None):
        spritePath = spritePath if spritePath is not None else Player.DEFAULT_SPRITE_PATH
        super().__init__(pos, spritePath)

    def update(self, keys):
        self.movingUp, self.movingLeft, self.movingDown, self.movingRight, shift = (
            keys[pygame.K_w],
            keys[pygame.K_a],
            keys[pygame.K_s],
            keys[pygame.K_d],
            keys[pygame.K_LSHIFT],
        )
        super().update()
