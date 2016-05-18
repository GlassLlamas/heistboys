import random

import textures

class Item(entity.Entity):
    
    def __init__(self, pos, spritePath, ticksPerSprite=250):
        self.pos = pos
        self.sprites = textures.loadItemSprites(spritePath)
        self.inUse = False
        self.surface = random.choice(self.sprites[self.inUse])
        self.spriteNum = 0
        self.ticks = 0
        self.ticksPerSprite = ticksPerSprite
        super().__init__(self.pos)
        self.render()
        self.velocityGenerators = []

    def render(self):
        if self.inUse:
            self.surface = self.sprites[self.inUse][self.spriteNum]
        else:
            self.surface = random.choice(self.sprites[self.inUse])
        self.size = self.surface.get_size()
    
    def update(self, level):
        if self.inUse:
            new_ticks = self.ticks + utils.delta
            if new_ticks > self.ticksPerSprite:
                self.spriteNum = (self.spriteNum + 1) % len(self.sprites[self.inUse])
                self.ticks = new_ticks % self.ticksPerSprite
            self.render()
        else:
            x, y = self.fpos
            for gen in self.velocityGenerators:
                self.xv, self.yv = gen(self.xv, self.yv)
            # Predict the x and y components separately
            OVERLAP_Y = 0
            pred_fpos = x + self.xv, y
            pred_pos  = int(pred_fpos[0]), int(pred_fpos[1])
            pred_rect = pygame.Rect((pred_pos[0], pred_pos[1] + OVERLAP_Y),
                                    (self.size[0], self.size[1] - OVERLAP_Y))

            if not any(map(lambda w: pygame.Rect(w).colliderect(pred_rect), level.walls)):
                self.fpos = pred_fpos
                self.pos = int(self.fpos[0]), int(self.fpos[1])

            pred_fpos = self.fpos[0], y + self.yv
            pred_pos  = int(pred_fpos[0]), int(pred_fpos[1])
            pred_rect = pygame.Rect((pred_pos[0], pred_pos[1] + OVERLAP_Y),
                                    (self.size[0], self.size[1] - OVERLAP_Y))

            if not any(map(lambda w: pygame.Rect(w).colliderect(pred_rect), level.walls)):
                self.fpos = pred_fpos
                self.pos = int(self.fpos[0]), int(self.fpos[1])
            ##############################################        
