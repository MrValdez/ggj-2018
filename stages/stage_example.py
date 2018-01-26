import pygame
import pyganim

from .stage import Stage, Text

class StageExample(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)

        # examples
        self.texts = []
        self.texts.append(Text("Hello World", (255, 255, 255), self._center_text))
        example = Text("h", (0, 0, 0), lambda x: x)
        self.texts.append(example)

        self.sprite = pyganim.PygAnimation([("images/spam.png", 10)])
        self.sprite.play()

    def update(self, input):
        if input.left: print("left")
        if input.right: print("right")
        if input.up: print("up")
        if input.down: print("down")
        if input.button1: print("button1")
        if input.button2: print("button2")

    def draw(self, screen):
        super().draw(screen)
        screen.fill([255,128,128])
        self.sprite.blit(screen, (0, 0))