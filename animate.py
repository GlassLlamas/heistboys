import pygame

from buffalo import utils

import entity
import textures

class Animate(entity.Entity):
    def __init__(self,
                 pos,
                 spritePath,
                 speed=0.15,
                 runningSpeedMult=1.75,
                 ticksPerSprite=250,
    ):
        self.pos = pos
        self.sprites = textures.loadAnimateSprites(spritePath)
        self.spriteKey = "down"
        self.spriteNum = 0
        self.ticks = 0
        self.ticksPerSprite = ticksPerSprite
        super().__init__(self.pos)
        self.render()
        self.movingUp, self.movingDown = False, False
        self.movingLeft, self.movingRight = False, False
        self.speed = speed
        self.runningSpeedMult = runningSpeedMult
        self.running = False

    def render(self):
        self.surface = self.sprites[self.spriteKey][self.spriteNum]
        self.size = self.surface.get_size()

    def update(self, level):
        x, y = self.fpos
        self.xv, self.yv = 0.0, 0.0
        new_v = self.speed * utils.delta
        if self.running:
            new_v *= self.runningSpeedMult
        if (self.movingUp or self.movingDown) and (self.movingLeft or self.movingRight):
            new_v *= 0.75 # pythagorean theorem (1 / sqrt(2) rounded up a little bit)

        if self.movingUp:
            self.spriteKey = "up"
            self.yv = -new_v
        elif self.movingDown:
            self.spriteKey = "down"
            self.yv = new_v
        if self.movingLeft:
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

        # Predict the x and y components separately
        OVERLAP_Y = 25
        pred_fpos = x + self.xv, y
        pred_pos  = round(pred_fpos[0]), round(pred_fpos[1])
        pred_rect = pygame.Rect((pred_pos[0], pred_pos[1] + OVERLAP_Y),
                                (self.size[0], self.size[1] - OVERLAP_Y))
        self.moveOrCollide(pred_fpos, pred_pos, pred_rect, level)

        pred_fpos = self.fpos[0], y + self.yv
        pred_pos  = round(pred_fpos[0]), round(pred_fpos[1])
        pred_rect = pygame.Rect((pred_pos[0], pred_pos[1] + OVERLAP_Y),
                                (self.size[0], self.size[1] - OVERLAP_Y))
        self.moveOrCollide(pred_fpos, pred_pos, pred_rect, level)

        self.pos = round(self.fpos[0]), round(self.fpos[1])        
        ##############################################

    def moveOrCollide(self, pred_fpos, pred_pos, pred_rect, level):
        if not any(map(lambda w: pygame.Rect(w).colliderect(pred_rect), level.walls)) and \
           not any(map(lambda dO: dO[1].colliderect(pred_rect), level.destructibleObjects)) and \
           not any(map(lambda bO: bO[1].colliderect(pred_rect), level.blockingObjects)):
            self.fpos = pred_fpos
