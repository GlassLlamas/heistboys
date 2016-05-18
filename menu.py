import sys

import pygame

from buffalo import utils
from buffalo.scene import Scene
from buffalo.label import Label
from buffalo.button import Button
from buffalo.option import Option

import debug

class Menu(Scene):

    def on_escape(self):
        sys.exit()

    def update(self):
        pass

    def blit(self):
        pass

    def __init__(self):
        Scene.__init__(self)
        self.BACKGROUND_COLOR = (50, 50, 100, 255)
        Button.DEFAULT_BG_COLOR = (100, 100, 100, 255)
        Button.DEFAULT_FONT = "default18"
        Option.DEFAULT_FONT = "default18"
        heistboysLabel = Label(
            (5, 5),
            "Heistboys V 1.0",
        )
        self.labels.add(heistboysLabel)
        self.buttons.add(
            Button(
                (5, heistboysLabel.pos[1] + heistboysLabel.surface.get_size()[1] + 5),
                "Debug",
                func=self.goToDebug,
            )
        )
        self.buttons.add(
            Button(
                (utils.SCREEN_W / 2, utils.SCREEN_H - 50),
                "Exit",
                x_centered=True,
                y_centered=True,
                func=exit,
            )
        )

    def goToDebug(self):
        utils.set_scene(debug.Debug())