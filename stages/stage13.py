# Send the love letter

import math
import pygame
import pyganim
import random
from .stage import Stage, Text, Projectile, Collidable, Avatar


class Player(Avatar):
    def __init__(self, speed, pos):
        Avatar.__init__(self, speed=speed, pos=pos, facing=[1, 0])

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


class Stage13(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)
        self.texts = [Text("Transmit the love letter", (255, 255, 255), self._center_text)]

        self.reset()
        
    def reset(self):
        pos1 = [100, 350]
        pos2 = [500, 550]
        speed = 10
        self.avatar1 = Player(speed=speed, pos=pos1)
        self.avatar2 = Player(speed=-speed, pos=pos2)
        self.objects = [self.avatar1, self.avatar2]

    def update(self, input, tick):
        self.avatar1.update(input, tick)
        self.avatar2.update(input, tick)
        
        for avatar in [self.avatar1, self.avatar2]:
            avatar.pos[0] = max(10, min(self.resolution[0] - avatar.anim.getRect().width, avatar.pos[0]))
            avatar.pos[1] = max(10, min(self.resolution[1] - avatar.anim.getRect().height, avatar.pos[1]))

        if input.button:
            self.reset()
        if self.avatar1.has_collide(self.avatar2):
            return True

    def draw(self, screen):
        super().draw(screen)

        self._iterate_all(self.objects, "draw", {"screen": screen})