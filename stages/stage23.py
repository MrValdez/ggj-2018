# SMS Transmission

import pygame
import pyganim
import random
from .stage import Stage, Text


class Stage23(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)
        self.phone = pygame.image.load("images/phone.png")
        self.phone = pygame.transform.scale2x(self.phone)
        self.mail = pygame.image.load("images/envelope.png")
        self.heart = pygame.image.load("images/heart.png")
        self.texts = [Text("Transmit your message to your crush <3", (255, 255, 255), self._center_text)]

        self.reset()
        
    def reset(self):
        self.current = 0
        self.found = False

    def update(self, input, tick):
        if self.found and input.button:
            return True
            
        if input.button:
           self.found = True 

    def draw(self, screen):
        screen.fill([128, 10, 10])
        super().draw(screen)      
        
        x, y = 200, 190
        if self.found:
            x += random.randint(-2, +2)
            y += random.randint(-2, +2)
        screen.blit(self.phone, (x, y))
        
        x, y = 300, 190
        if not self.found:
            screen.blit(self.mail, (x, y))
        else:
            screen.blit(self.heart, (x, y))