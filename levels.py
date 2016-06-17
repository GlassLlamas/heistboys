import os

import pygame

from buffalo import utils

import textures

BASE_PATH = os.path.join("levels")

class Level:

    def __init__(self,
                 backgroundImage=None,
                 startX=None, startY=None,
                 walls=[],
                 destructibleObjects=[],
                 blockingObjects=[],
                 nonblockingObjects=[],
             ):
        if backgroundImage is None:
            print("No background image specified.")
            raise Exception
        self.backgroundImage = backgroundImage
        self.startX = startX
        self.startY = startY
        self.walls = walls
        self.destructibleObjects = destructibleObjects
        self.blockingObjects = blockingObjects
        self.nonblockingObjects = nonblockingObjects
        self.render()

    def blit(self, dest, offset=(0,0)):
        dest.blit(self.surface, (-offset[0], -offset[1]))

    def render(self):
        if not hasattr(self, "surface"):
            self.surface = utils.empty_surface(self.backgroundImage.get_size())
            self.surface.blit(self.backgroundImage, (0, 0))
        for (pos, surface) in self.nonblockingObjects:
            self.surface.blit(surface, pos)
        for (pos, rect, surface, drops) in self.destructibleObjects:
            self.surface.blit(surface, pos)
        for (pos, rect, surface) in self.blockingObjects:
            self.surface.blit(surface, pos)

    @property
    def startPosition(self):
        return (self.startX, self.startY)

    @startPosition.setter
    def startPosition(self, value):
        self.startX, self.startY = value

def load(filename):
    path = os.path.join(BASE_PATH, filename)
    backgroundImage = None
    startX, startY = None, None
    walls = []
    destructibleObjects = []
    blockingObjects = []
    nonblockingObjects = []
    with open(path, "r") as levelFile:
        def parseError(lineno, e):
            print("Could not parse line {} of {} => in levels.py: {}".format(lineno, path, e))
        for lineno, line in [(k + 1, v.strip()) for k, v in enumerate(levelFile)]:
            try:
                if line.startswith("backgroundImage:"):
                    _, filename = line.split()
                    backgroundImage = textures.getSprite(os.path.join("sprites", "rooms", filename))
                elif line.startswith("startPosition:"):
                    _, startXString, startYString = line.split()
                    startX = int(startXString)
                    startY = int(startYString)
                elif line.startswith("wall:"):
                    _, xs, ys, ws, hs = line.split()
                    x = int(xs)
                    y = int(ys)
                    w = int(ws)
                    h = int(hs)
                    walls.append((x, y, w, h))
                elif line.startswith("destructibleObject:"):
                    elems = line.split()
                    filename, xs, ys = elems[1:4]
                    x = int(xs)
                    y = int(ys)
                    drops = []
                    if len(elems) > 4:
                        if len(elems[4:]) % 2 == 1:
                            raise ValueError
                        drops = [(itemName, float(chance)) for itemName, chance in zip(elems[4::2], elems[5::2])]
                    sprite = textures.getSprite(os.path.join("sprites","misc","destructible", filename))
                    OVERLAP_Y = 0
                    sprite_size = sprite.get_size()
                    destructibleObjects.append((
                        (x, y),
                        pygame.Rect((x, y + OVERLAP_Y), (sprite_size[0], sprite_size[1] - OVERLAP_Y)),
                        sprite,
                        drops
                    ))
                elif line.startswith("blockingObject:"):
                    _, filename, xs, ys = line.split()
                    x = int(xs)
                    y = int(ys)
                    sprite = textures.getSprite(os.path.join("sprites","misc","blocking", filename))
                    OVERLAP_Y = 0
                    sprite_size = sprite.get_size()
                    blockingObjects.append((
                        (x, y),
                        pygame.Rect((x, y + OVERLAP_Y), (sprite_size[0], sprite_size[1] - OVERLAP_Y)),
                        sprite
                    ))
                elif line.startswith("nonblockingObject:"):
                    _, filename, xs, ys = line.split()
                    x = int(xs)
                    y = int(ys)
                    nonblockingObjects.append((
                        (x, y),
                        textures.getSprite(os.path.join("sprites","misc","nonblocking", filename))
                    ))
            except Exception as e:
                parseError(lineno, e)
    return Level(
        backgroundImage,
        startX, startY,
        walls,
        destructibleObjects,
        blockingObjects,
        nonblockingObjects,
    )
