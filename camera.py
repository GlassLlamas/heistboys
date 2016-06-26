from buffalo import utils

class Camera:
    
    def __init__(self, pos=(0,0), locked=None):
        self.pos = pos
        self.locked = locked
        if self.locked:
            self.pos = [(a - b) for (a, b) in zip(self.locked.pos, utils.SCREEN_M)]
    
    def update(self):
        if self.locked:
            self.pos = [(a - b) for (a, b) in zip(self.locked.pos, utils.SCREEN_M)]
    
    @property
    def pos(self):
        return (self.x, self.y)

    @pos.setter
    def pos(self, value):
        self.x, self.y = value
    
