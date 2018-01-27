# Tune TV signal

import pygame
import pyganim
import random
from .stage import Stage, Text, UpdatingText, Avatar

class Signal(Avatar):
    def __init__(self, speed, pos):
        Avatar.__init__(self, speed=speed, pos=pos, facing=[1, 0],
                        animation_files=[("images/knuckles.jpg", 200),])
        self.anim.set_alpha(50)

    def update(self, input, tick):
        speed = self.speed

        if input.left_hold:
            self.pos[0] -= speed
        if input.right_hold:
            self.pos[0] += speed

class Stage20(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)
        self.texts = [Text("Tune the TV to watch your favorite (?) show", (255, 255, 255), self._center_text)]

        self.reset()
        
    def reset(self):
        self.objects = [Signal(+10, [-750, 50]),
                        Signal(-10, [self.resolution[0] + 50, 50]),]

    def update(self, input, tick):
        self._iterate_all(self.objects, "update", {"input": input, "tick": tick})

        if self.objects[0].pos[0] == self.objects[1].pos[0]:
            return True

    def draw(self, screen):
        super().draw(screen)
        
        self._iterate_all(self.objects, "draw", {"screen": screen})