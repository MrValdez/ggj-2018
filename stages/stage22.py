# Psychic Transmission

import pygame
import pyganim
from .stage import Stage, Text


class Stage22(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)
        self.bg = pygame.image.load("images/Psychic_reading.jpg").convert()
        self.card = pygame.image.load("images/card_back.png").convert()
        self.card_front = pygame.image.load("images/card_front.png").convert()
        self.texts = [Text("Select the correct card using YOUR psychic powers", (255, 255, 255), self._center_text)]

        self.reset()
        
    def reset(self):
        self.current = 0
        self.found = False

    def update(self, input, tick):
        if input.left:
            self.current -= 1
            self.current = max(0, self.current)
        if input.right:
            self.current += 1
            self.current = min(2, self.current)

        if self.found and input.button:
            return True
            
        if input.button:
           self.found = True 

    def draw(self, screen):
        screen.blit(self.bg, (0, 0))
        super().draw(screen)
        
        for i, (x, y) in enumerate([(50, 320), (340, 320), (600, 320)]):
            screen.blit(self.card, (x, y))
            
            if i == self.current:
                color = (255, 255, 0)
                rect = pygame.Rect(x, y, 165, 240)
                pygame.draw.rect(screen, color, rect, 10)            

                if self.found:
                    screen.blit(self.card_front, (x, y))
                    