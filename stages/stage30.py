# Button mashing

import pygame
import pyganim
import random
from .stage import Stage, Text, Collidable

class Toothpaste(Collidable):
    def __init__(self, pos):
        anim = pyganim.PygAnimation([("images/toothpaste_b.png", 200),])
        anim.play()
        Collidable.__init__(self, anim, pos)
        self.speed = [random.randint(1, 3), random.randint(-4, 4)]

    def update(self, input, tick):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]
        self.speed[1] += 1
        self.anim.rotate(random.randint(1, 2))

class Toothbrush(Collidable):
    def __init__(self, resolution):
        self.resolution = resolution
        
        self.toothbrush_a = pyganim.PygAnimation([("images/toothbrush_a.png", 10),])
        self.toothbrush_b = pyganim.PygAnimation([("images/toothbrush_b.png", 10),])
        self.toothbrush_a.play()
        self.toothbrush_b.play()

        self.anim = self.toothbrush_a
        self.speed = 5
        self.pos = [300, 450]
        self.left_move = False

    def update(self, input, tick):
        speed = self.speed
        if self.left_move:
            self.pos[0] -= speed
        else:
            self.pos[0] += speed
        
        if self.left_move:
            if self.pos[0] < 100:
                self.left_move = not self.left_move
        else:
            if self.pos[0] + 200 >= self.resolution[0]:
                self.left_move = not self.left_move

    def draw(self, screen):
        self.toothbrush_a.blit(screen, self.pos)
        self.toothbrush_b.blit(screen, [self.pos[0] + self.toothbrush_a.getRect().width, self.pos[1]])


class Stage30(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)

        self.texts = [Text("Transmit toothpaste", (255, 255, 255), self._center_text)]

        self.toothpaste = pyganim.PygAnimation([("images/toothpaste.png", 10),])
        self.toothpaste.play()

        self.reset()
        
    def reset(self):
        self.toothbrush = Toothbrush(self.resolution)
        self.toothpaste_pos = [40, 100]
        self.pastes = []
        self.paste_applied = 0

    def update(self, input, tick):
        if input.button:
            pos = self.toothpaste_pos[:]
            pos[0] += 80
            pos[1] += 110
            self.pastes.append(Toothpaste(pos))

        self.toothbrush.update(input, tick)
        self._iterate_all(self.pastes, "update", {"input": input, "tick": tick})
        
        for paste in self.pastes:
            if paste.has_collide(self.toothbrush):
                self.paste_applied += 1
                self.pastes.remove(paste)
                continue
            if paste.pos[1] > self.resolution[1]:
                self.pastes.remove(paste)
                continue
                

        if self.paste_applied > 5:
            return True

    def draw(self, screen):
        super().draw(screen)

        self.toothpaste.blit(screen, self.toothpaste_pos)
        self.toothbrush.draw(screen)
        
        self._iterate_all(self.pastes, "draw", {"screen": screen})