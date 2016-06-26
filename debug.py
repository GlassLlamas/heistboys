import os
import sys

import pygame

from buffalo import utils
from buffalo.scene import Scene
from buffalo.label import Label
from buffalo.button import Button
from buffalo.option import Option

import animate
import camera
import item
import levels

class Debug(Scene):

    def on_escape(self):
        sys.exit()

    def update(self):
        self.level.update(self.camera.pos, pygame.key.get_pressed())
        self.camera.update()

    def blit(self):
        self.level.blit(utils.screen, self.camera.pos)

    def __init__(self, levelName="basic.lvl"):
        Scene.__init__(self)
        self.BACKGROUND_COLOR = (0, 0, 0, 255)
        item.loadItems()
        self.level = levels.load(levelName)
        self.camera = camera.Camera(locked=self.level.player)

    def goToDebug(self):
        utils.set_scene(debug.Debug())
