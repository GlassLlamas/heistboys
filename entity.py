class Entity:
    def __init__(self,
                 pos,
                 size=None,
    ):
        self.pos = pos
        self.size = size if size is not None else (0, 0)
        self.fpos = float(self.pos[0]), float(self.pos[1])
        self.xv, self.yv = 0.0, 0.0
        self.surface = None

    def blit(self, dest, offset):
        if self.surface is not None:
            dest.blit(self.surface, [-a + b for (a,b) in zip(offset, self.pos)])

    @property
    def currentSpeed(self):
        return (self.xv ** 2 + self.yv ** 2) ** 0.5

    @property
    def size(self):
        return (self.width, self.height)

    @size.setter
    def size(self, value):
        self.width, self.height = value

    @property
    def pos(self):
        return (self.x, self.y)

    @pos.setter
    def pos(self, value):
        self.x, self.y = value

    @property
    def fpos(self):
        return (self.x, self.y)

    @fpos.setter
    def fpos(self, value):
        self.x, self.y = value

