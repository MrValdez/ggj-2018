# Dancing

import pygame
import pyganim
import random
from .stage import Stage, Text

class Stage9(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)
        self.texts = [Text("Dance Quickly to transmit!", (255, 255, 255), self._center_text)]

        self.dance = pyganim.PygAnimation([("images/dance1.png", 200),
                                            ("images/dance2.png", 200),
                                            ("images/dance3.png", 200),
                                            ("images/dance4.png", 200)])
        self.dance.rate = 1.0
        self.dance.play()

        self.reset()
        
    def reset(self):
        self.target_dance = 1000
        self.current_dance = self.target_dance

    def update(self, input, tick):
        if input.up or input.left or input.down or input.right:
            self.current_dance -= random.randint(10, 50)

            if self.current_dance <= -500:
                return True
                
            rate = (1 - self.current_dance / self.target_dance) * 2
            self.dance.rate = rate
            self.dance.play()        

    def draw(self, screen):
        super().draw(screen)

        rect = self.dance.getRect()
        rect.centerx = self.resolution[0] / 2
        rect.centery = self.resolution[1] / 2
        self.dance.blit(screen, rect)
