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
import levels
import player

class Debug(Scene):

    def on_escape(self):
        sys.exit()

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update(keys, self.level)
        for a in self.animates:
            a.update(self.level)
        self.camera.update()

    def blit(self):
        self.level.blit(utils.screen, self.camera.pos)
        for a in self.animates:
            a.blit(utils.screen, self.camera.pos)
        self.player.blit(utils.screen, self.camera.pos)

    def __init__(self):
        Scene.__init__(self)
        self.BACKGROUND_COLOR = (0, 0, 0, 255)
        self.level = levels.load("basic.lvl")
        self.player = player.Player(self.level.startPosition)
        self.camera = camera.Camera(locked=self.player)
        self.animates = []

    def goToDebug(self):
        utils.set_scene(debug.Debug())
