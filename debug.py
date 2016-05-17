import sys

import pygame

from buffalo import utils
from buffalo.scene import Scene
from buffalo.label import Label
from buffalo.button import Button
from buffalo.option import Option

class Debug(Scene):

    def on_escape(self):
        sys.exit()

    def update(self):
        pass

    def blit(self):
        pass

    def __init__(self):
        Scene.__init__(self)
        self.BACKGROUND_COLOR = (0, 0, 0, 255)

    def goToDebug(self):
        utils.set_scene(debug.Debug())
