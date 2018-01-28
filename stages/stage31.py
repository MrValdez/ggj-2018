# Transmit toothpaste to teeth

import pygame
import pyganim
import random
from .stage import Stage, Text, Collidable

class Teeth(Collidable):
    def __init__(self, pos):
        anim = pyganim.PygAnimation([("images/tooth 1.png", 200),
                                     ("images/tooth 2.png", 200)])
        anim.scale([100, 100])
        Collidable.__init__(self, anim, pos)
        self.anim.pause()
        self.dirt = random.randint(100, 200)

class Toothbrush(Collidable):
    def __init__(self, resolution):
        self.resolution = resolution
        
        self.toothbrush_a = pyganim.PygAnimation([("images/toothbrush_a.png", 10),])
        self.toothbrush_b = pyganim.PygAnimation([("images/toothbrush_b.png", 10),])
        self.toothbrush_a.play()
        self.toothbrush_b.play()
        self.toothbrush_a.flip(False, True)
        self.toothbrush_b.flip(False, True)

        self.anim = self.toothbrush_a
        self.speed = 25
        self.pos = [300, 250]
        self.left_move = False

    def update(self, input, tick):
        speed = self.speed
        
        if input.left_hold:
            self.pos[0] -= speed
        if input.right_hold:
            self.pos[0] += speed
        if input.down_hold:
            self.pos[1] += speed
        if input.up_hold:
            self.pos[1] -= speed

    def draw(self, screen):
        self.toothbrush_a.blit(screen, self.pos)
        self.toothbrush_b.blit(screen, [self.pos[0] + self.toothbrush_a.getRect().width, self.pos[1]])


class Stage31(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)

        self.texts = [Text("Transmit toothpaste to teeth", (255, 255, 255), self._center_text)]

        self.reset()
        
    def reset(self):
        self.teeth = [
            Teeth([150, 400]),
            Teeth([250, 400]),
            Teeth([350, 400]),
            Teeth([450, 400]),
            Teeth([550, 400]),
            ]
        self.dirty_teeth = self.teeth[:]
        self.toothbrush = Toothbrush(self.resolution)

    def update(self, input, tick):
        self.toothbrush.update(input, tick)
        
        self.toothbrush.pos[0] = max(0, min(self.resolution[0], self.toothbrush.pos[0]))
        self.toothbrush.pos[1] = max(0, min(self.resolution[1] - 20, self.toothbrush.pos[1]))
        
        #self._iterate_all(self.pastes, "update", {"input": input, "tick": tick})

        for tooth in self.teeth:
            if tooth.has_collide(self.toothbrush):
                tooth.dirt -= 1
                if tooth.dirt <= 0:
                    tooth.anim.nextFrame()       
                    if tooth in self.dirty_teeth:           
                        self.dirty_teeth.remove(tooth)
                    continue

        if len(self.dirty_teeth) <= 0:
            return True

    def draw(self, screen):
        super().draw(screen)

        self._iterate_all(self.teeth, "draw", {"screen": screen})
        self.toothbrush.draw(screen)
        