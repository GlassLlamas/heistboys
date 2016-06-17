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
import player

class Debug(Scene):

    def on_escape(self):
        sys.exit()

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update(keys, self.level)
        self.camera.update()
        self.level.update(self.camera.pos)

    def blit(self):
        self.level.blit(utils.screen, self.camera.pos)
        self.player.blit(utils.screen, self.camera.pos)

    def __init__(self, levelName="basic.lvl"):
        Scene.__init__(self)
        self.BACKGROUND_COLOR = (0, 0, 0, 255)
        item.loadItems()
        self.level = levels.load(levelName)
        self.player = player.Player(self.level.startPosition)
        self.camera = camera.Camera(locked=self.player)

    def goToDebug(self):
        utils.set_scene(debug.Debug())
