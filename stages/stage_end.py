import pygame
import pyganim
from .stage import Stage, Text

class Stage_end(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)

        self.texts = [Text("You won! Press any key to restart", (255, 255, 255), self._center_text)]
        self.bg = pygame.image.load("images/mrvaldez.png")

    def update(self, input, tick):
        if input.button:
            #move to the next stage
            return True

    def draw(self, screen):
        screen.blit(self.bg, [120, 200])
        super().draw(screen)
