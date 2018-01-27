# Tune TV signal

import pygame
import pyganim
import random
from .stage import Stage, Text, UpdatingText, Avatar

class Icon(Avatar):
    def __init__(self, pos, animation_files):
        Avatar.__init__(self, speed=0, pos=pos, facing=[1, 0],
                        animation_files=animation_files)
        self.default_pos = pos[:]
        self.default_anim = self.anim.getCopy()
        self.alpha = 100

    def update(self, input, tick):
        self.pos = self.default_pos[:]
        self.anim = self.default_anim.getCopy()
        self.anim.set_alpha(self.alpha)
        self.anim.play()

class Stage21(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)
        self.texts = [Text("Fix the TV or you'll miss the show", (0, 0, 0), self._center_text)]

        self.reset()
        
    def reset(self):
        self.fix_needed = 3
        self.hit_tv = False
        self.fist = Icon([500, 200], [("images/fist.png", 200),])
        self.tv = Icon([100, 50], [("images/tv.png", 200),])
        self.tv.default_anim.scale2x()#[200, 200])
        self.image = Icon([180, 240], [("images/RickRoll.png", 200),])
        self.image.default_anim.scale([200, 170])
        self.image.alpha = 10

    def update(self, input, tick):
        if self.fix_needed < 0:
            return True

        self.fist.update(input, tick)
        self.tv.update(input, tick)
        self.image.update(input, tick)
        
        if input.button:
            self.fix_needed -= 1
            self.image.alpha += 60

        self.hit_tv = input.button_hold
        

    def draw(self, screen):
        screen.fill([255, 255, 255])
        super().draw(screen)
        
        if self.hit_tv:
            self.fist.pos[0] -= 60
            self.tv.pos[0] -= 40
            self.tv.pos[1] -= 10
            self.tv.anim.rotate(10)
            self.image.anim.rotate(10)

        self.image.draw(screen)
        self.tv.draw(screen)
        self.fist.draw(screen)