# Order for WiFi

import pygame
import pyganim
from .stage import Stage, Text, Avatar


class Player(Avatar):
    def __init__(self):
        Avatar.__init__(self, speed=10, pos=[400, 350], facing=[1, 0],
                        animation_files=[("images/poop.png", 200),])

    def update(self, input, tick):
        speed = self.speed

        if input.left_hold:
            self.pos[0] -= speed
        if input.right_hold:
            self.pos[0] += speed
        if input.up_hold:
            self.pos[1] -= speed
        if input.down_hold:
            self.pos[1] += speed

class Stage17(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)
        self.bg = pygame.image.load("images/coffee shop.png").convert()

        self.cost = [0.5, 1.3, 0.9, 1.10, 2.5]
        self.reset()
        
    def reset(self):
        self.texts = []
        self.objects = []
        self.total = 0
        self.current = 0

    def update(self, input, tick):
        self.texts = [Text("$ {:.2f}".format(self.total), (0, 0, 0), lambda x: (550, 300))]

        if input.up:
            self.current -= 1
            self.current = max(0, self.current)
        if input.down:
            self.current += 1
            self.current = min(4, self.current)
        if input.button:
            self.total += self.cost[self.current]
        if self.total >= 10:
            return True

    def draw(self, screen):
        screen.blit(self.bg, (0, 0))
        super().draw(screen)
        
        color = (0, 255, 0)
        rect = pygame.Rect(100, 210 + (self.current * 38), 240, 40)
        pygame.draw.rect(screen, color, rect, 1)

        self._iterate_all(self.objects, "draw", {"screen": screen})