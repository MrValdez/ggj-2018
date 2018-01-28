import pygame
import pyganim
from .stage import Stage, Text

class Stage_start(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)

        self.texts = [Text("32 bits of delivery. Controls are arrow keys and Q. You can use joypad", (255, 255, 255), self._center_text)]

    def update(self, input, tick):
        if input.button:
            #move to the next stage
            return True

    def draw(self, screen):
        super().draw(screen)
