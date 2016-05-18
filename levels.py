import os

import pygame

from buffalo import utils

BASE_PATH = os.path.join("levels")

class Level:

    DEFAULT_WIDTH = 500
    DEFAULT_HEIGHT = 500
    DEFAULT_START_X = 100
    DEFAULT_START_Y = 100
    DEFAULT_R = 50
    DEFAULT_G = 50
    DEFAULT_B = 50
    DEFAULT_A = 255
    DEFAULT_WALL_R = 50
    DEFAULT_WALL_G = 50
    DEFAULT_WALL_B = 50
    DEFAULT_WALL_A = 255
    DEFAULT_WALLS = []

    def __init__(self,
                 width=None, height=None,
                 startX=None, startY=None, # startPosition
                 r=None, g=None, b=None, a=None,
                 wall_r=None, wall_g=None, wall_b=None, wall_a=None,
                 walls=None,
             ):
        self.width = width if width is not None else Level.DEFAULT_WIDTH
        self.height = height if height is not None else Level.DEFAULT_HEIGHT
        self.startX = startX if startX is not None else Level.DEFAULT_START_X
        self.startY = startY if startY is not None else Level.DEFAULT_START_Y
        self.r = r if r is not None else Level.DEFAULT_R
        self.g = g if g is not None else Level.DEFAULT_G
        self.b = b if b is not None else Level.DEFAULT_B
        self.a = a if a is not None else Level.DEFAULT_A
        self.wall_r = wall_r if wall_r is not None else Level.DEFAULT_WALL_R
        self.wall_g = wall_g if wall_g is not None else Level.DEFAULT_WALL_G
        self.wall_b = wall_b if wall_b is not None else Level.DEFAULT_WALL_B
        self.wall_a = wall_a if wall_a is not None else Level.DEFAULT_WALL_A
        self.walls = walls if walls is not None else Level.DEFAULT_WALLS
        self.walls.append((-10, -10, self.width, 10))
        self.walls.append((-10, -10, 10, self.height))
        self.walls.append((self.width, -10, 10, self.height + 20))
        self.walls.append((-10, self.height, self.width + 20, 10))
        self.render()

    def blit(self, dest, offset=(0,0)):
        dest.blit(self.surface, (-offset[0], -offset[1]))

    def render(self):
        if not hasattr(self, "surface"):
            self.surface = utils.empty_surface(self.size)
        self.surface.fill(self.color)
        for wall in self.walls:
            self.surface.fill(self.wallColor, pygame.Rect(wall))

    @property
    def size(self):
        return (self.width, self.height)

    @size.setter
    def size(self, value):
        self.width, self.height = value

    @property
    def startPosition(self):
        return (self.startX, self.startY)

    @startPosition.setter
    def startPosition(self, value):
        self.startX, self.startY = value
    
    @property
    def color(self):
        return (self.r, self.g, self.b, self.a)
    
    @color.setter
    def color(self, value):
        self.r, self.g, self.b, self.a = value
    
    @property
    def wallColor(self):
        return (self.wall_r, self.wall_g, self.wall_b, self.wall_a)
    
    @wallColor.setter
    def wallColor(self, value):
        self.wall_r, self.wall_g, self.wall_b, self.wall_a = value

def load(filename):
    path = os.path.join(BASE_PATH, filename)
    width, height = None, None
    startX, startY = None, None
    r, g, b, a = None, None, None, None
    walls = []
    with open(path, "r") as levelFile:
        def parseError(lineno):
            print("Could not parse line {}".format(lineno))
        for lineno, line in [(k + 1, v.strip()) for k, v in enumerate(levelFile)]:
            if line.startswith("width:"):
                _, widthString = line.split()
                try:
                    width = int(widthString)
                except ValueError:
                    parseError(lineno)
            elif line.startswith("height:"):
                _, heightString = line.split()
                try:
                    height = int(heightString)
                except ValueError:
                    parseError(lineno)
            elif line.startswith("startPosition:"):
                _, startXString, startYString = line.split()
                try:
                    startX = int(startXString)
                except ValueError:
                    parseError(lineno)
                try:
                    startY = int(startYString)
                except ValueError:
                    parseError(lineno)
            elif line.startswith("color:"):
                _, rString, gString, bString, aString = line.split()
                try:
                    r = int(rString)
                    g = int(gString)
                    b = int(bString)
                    a = int(aString)
                    if r < 0 or r > 255:
                        raise ValueError
                    if g < 0 or g > 255:
                        raise ValueError
                    if b < 0 or b > 255:
                        raise ValueError
                    if a < 0 or a > 255:
                        raise ValueError
                except ValueError:
                    parseError(lineno)
            elif line.startswith("wallColor:"):
                _, rString, gString, bString, aString = line.split()
                try:
                    wall_r = int(rString)
                    wall_g = int(gString)
                    wall_b = int(bString)
                    wall_a = int(aString)
                    if wall_r < 0 or wall_r > 255:
                        raise ValueError
                    if wall_g < 0 or wall_g > 255:
                        raise ValueError
                    if wall_b < 0 or wall_b > 255:
                        raise ValueError
                    if wall_a < 0 or wall_a > 255:
                        raise ValueError
                except ValueError:
                    parseError(lineno)
            elif line.startswith("wall:"):
                _, xs, ys, ws, hs = line.split()
                try:
                    x = int(xs)
                    y = int(ys)
                    w = int(ws)
                    h = int(hs)
                except ValueError:
                    parseError(lineno)
                walls.append((x, y, w, h))
    return Level(width, height,
                 startX, startY,
                 r, g, b, a,
                 wall_r, wall_g, wall_b, wall_a,
                 walls)
