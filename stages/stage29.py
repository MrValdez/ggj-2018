# Button mashing

import pygame
import pyganim
import random
from .stage import Stage, Text

class Stage29(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)

        self.texts = [Text("Mash button to transmit with little latency", (255, 255, 255), self._center_text)]

        self.button = pyganim.PygAnimation([("images/button1.png", 10),
                                            ("images/button 2.png", 10)])

        self.button_pos = self.button.getRect()
        self.button_pos.center = (resolution[0] / 2, resolution[1] / 2)

        self.button.play()

        self.reset()
        
    def reset(self):
        self.button_pressed = 0
        self.circles = []

    def update(self, input, tick):
        if input.button:
            color = (255, 128, 128)
            radius = 40
            pos = (self.button_pos.centerx, self.button_pos.centery)
            self.circles.append([color, pos, radius])
            self.button_pressed += 1

        if self.button_pressed > 20:
            return True

    def draw(self, screen):
        super().draw(screen)


        for circle in self.circles:
            color, pos, radius = circle
            circle[2] += len(self.circles)
            pygame.draw.circle(screen, color, pos, radius, random.randint(2, 10))
            
        self.button.blit(screen, self.button_pos)