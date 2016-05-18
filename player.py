import pygame

import animate

class Player(animate.Animate):
    def __init__(self, pos, spritePath):
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
