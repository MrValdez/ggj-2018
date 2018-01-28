# Like Transmission

import pygame
import pyganim
import random
from .stage import Stage, Text


class Stage24(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)
        self.button = pygame.image.load("images/thumb button.png")
        self.thumb = pygame.image.load("images/thumbs.png")
        self.texts = [Text("Transmit your like for my game", (255, 255, 255), self._center_text)]

        self.reset()
        
    def reset(self):
        self.found = False
        self.scale = 0

    def update(self, input, tick):
        if self.found:
            self.scale += 0.05
        if self.found and (input.button or self.scale >= 7):
            return True
        if input.button:
           self.found = True 

    def draw(self, screen):
        screen.fill([128, 10, 10])
        super().draw(screen)      
        
        x, y = self.resolution[0] / 2, self.resolution[1] / 2
        rect = self.button.get_rect()
        rect.center = (x, y)
        screen.blit(self.button, rect)
        
        if self.found:
            thumb = pygame.transform.rotozoom(self.thumb, 1, self.scale)
            rect = thumb.get_rect()
            rect.center = (x, y)
            screen.blit(thumb, rect)