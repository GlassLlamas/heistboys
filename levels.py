import os

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

    def __init__(self,
                 width=None, height=None,
                 startX=None, startY=None, # startPosition
                 r=None, g=None, b=None, a=None,
             ):
        self.width = width if width is not None else Level.DEFAULT_WIDTH
        self.height = height if height is not None else Level.DEFAULT_HEIGHT
        self.startX = startX if startX is not None else Level.DEFAULT_START_X
        self.startY = startY if startY is not None else Level.DEFAULT_START_Y
        self.r = r if r is not None else Level.DEFAULT_R
        self.g = g if g is not None else Level.DEFAULT_G
        self.b = b if b is not None else Level.DEFAULT_B
        self.a = a if a is not None else Level.DEFAULT_A
        self.render()

    def blit(self, dest, offset=(0,0)):
        dest.blit(self.surface, (-offset[0], -offset[1]))

    def render(self):
        if not hasattr(self, "surface"):
            self.surface = utils.empty_surface(self.size)
        self.surface.fill(self.color)

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

def load(filename):
    path = os.path.join(BASE_PATH, filename)
    width, height = None, None
    startX, startY = None, None
    r, g, b, a = None, None, None, None
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
                    if r < 0 or r > 255:
                        raise ValueError
                except ValueError:
                    parseError(lineno)
                try:
                    g = int(gString)
                    if g < 0 or g > 255:
                        raise ValueError
                except ValueError:
                    parseError(lineno)
                try:
                    b = int(bString)
                    if b < 0 or b > 255:
                        raise ValueError
                except ValueError:
                    parseError(lineno)
                try:
                    a = int(aString)
                    if a < 0 or a > 255:
                        raise ValueError
                except ValueError:
                    parseError(lineno)
    return Level(width, height, startX, startY, r, g, b, a)
