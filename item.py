from enum import Enum, unique
import random

import entity
import textures

class Item(entity.Entity):
    
    def __init__(self, pos, inInventory=False):
        super().__init__(pos)
        self.inInventory = inInventory
        self.velocityGenerators = []
    
    @property
    def inInventory(self):
        return self._inInventory

    @inInventory.setter
    def inInventory(self, value):
        self._inInventory = value

    def update(self, level, **kwargs):
        if not self.inInventory:
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

class UsableItem(Item):
    def __init__(self, pos, spritePath, ticksPerSprite):
        super().__init__(pos)
        self.sprites = textures.loadUsableItemSprites(spritePath)
        self.inUse = False
        self.surface = random.choice(self.sprites[self.inUse])
        self.spriteNum = 0
        self.ticks = 0
        self.ticksPerSprite = ticksPerSprite
        self.render()

    def render(self):
        if self.inUse:
            self.surface = self.sprites[self.inUse][self.spriteNum]
        else:
            self.surface = random.choice(self.sprites[self.inUse])
        self.size = self.surface.get_size()
    
    def inUseCallback(self, **kwargs):
        pass

    def update(self, level, **kwargs):
        if self.inUse:
            new_ticks = self.ticks + utils.delta
            if new_ticks > self.ticksPerSprite:
                self.spriteNum = (self.spriteNum + 1) % len(self.sprites[self.inUse])
                self.ticks = new_ticks % self.ticksPerSprite
            self.render()
            return self.inUseCallback(kwargs)
        else:
            super().update(level)
        return None

class UnusableItem(Item):
    def __init__(self, pos, spritePath):
        super().__init__(pos)
        self.sprites = textures.loadUnusableItemSprites(spritePath)
        self.inUse = False
        self.surface = random.choice(self.sprites[self.inUse])
        self.size = self.surface.get_size()

class ConsumableItem(UsableItem):
    def __init__(self, pos, spritePath, ticksPerSprite=250, effects):
        super().__init__(pos, spritePath, ticksPerSprite)
        self.effects = effects

    def inUseCallback(self, **kwargs):
        return self.effects

class Equippable(UsableItem):
    def __init__(self, pos, spritePath, ticksPerSprite, equipped, effects):
        super().__init__(pos, spritePath, ticksPerSprite)
        self.equipped = equipped
        self.effects = effects

    @property
    def equipped(self):
        return self._equipped

    @equipped.setter
    def equipped(self, value):
        self._equipped = value
        if value is True:
            self.inInventory = True

class Weapon(Equippable):
    def __init__(self, pos, spritePath, ticksPerSprite=250,
                 equipped=False, effects=[]):
        super().__init__(pos, spritePath, ticksPerSprite, equipped, effects)

    def attack(self, **kwargs):
        raise NotImplementedError

@unique
class ApparelPosition(Enum):
    helm = 1
    earings = 2
    torso = 3
    leftShoulder = 4
    rightShoulder = 5
    leftHand = 6
    rightHand = 7
    legs = 8
    boots = 9

class Apparel(Equippable):
    def __init__(self, pos, spritePath, ticksPerSprite=250,
                 equipped=False, effects=[],
                 apparelPositions=[]):
        super().__init__(pos, spritePath, ticksPerSprite, equipped, effects)
        self.apparelPositions = apparelPositions
