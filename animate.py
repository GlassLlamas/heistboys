import pygame

from buffalo import utils

import entity
import textures

class Animate(entity.Entity):
    def __init__(self,
                 pos,
                 spritePath,
                 speed=0.25,
                 ticksPerSprite=250,
    ):
        self.pos = pos
        self.sprites = textures.loadSprites(spritePath)
        self.spriteKey = "down"
        self.spriteNum = 0
        self.ticks = 0
        self.ticksPerSprite = ticksPerSprite
        super().__init__(self.pos)
        self.render()
        self.movingUp, self.movingDown = False, False
        self.movingLeft, self.movingRight = False, False
        self.speed = speed

    def render(self):
        self.surface = self.sprites[self.spriteKey][self.spriteNum]
        self.size = self.surface.get_size()

    def update(self):
        x, y = self.fpos
        self.xv, self.yv = 0.0, 0.0
        new_v = self.speed * utils.delta

        if self.movingUp:
            self.spriteKey = "up"
            self.yv = -new_v
        elif self.movingDown:
            self.spriteKey = "down"
            self.yv = new_v
        elif self.movingLeft:
            self.spriteKey = "left"
            self.xv = -new_v
        elif self.movingRight:
            self.spriteKey = "right"
            self.xv = new_v
        
        new_ticks = self.ticks + utils.delta
        if new_ticks > self.ticksPerSprite:
            self.spriteNum = (self.spriteNum + 1) % len(self.sprites[self.spriteKey])
        self.ticks = new_ticks % self.ticksPerSprite
        self.render()

        self.fpos = (x + self.xv, y + self.yv)
        self.pos = int(self.fpos[0]), int(self.fpos[1])
