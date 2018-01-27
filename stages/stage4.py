# Punch game

import pygame
import pyganim
import random
from .stage import Stage, Text

class Enemy:
    def __init__(self, midscreen):
        self.midscreen = midscreen

        self.anim = pyganim.PygAnimation([("images/button1.png", 10),
                                          ("images/button 2.png", 10)])
        self.anim.play()

        self.rect = self.anim.getRect()
        self.rect.centerx = self.midscreen
        self.rect.top = random.randint(0, 1)
        
        self.speed = [0.3, 1]
        self.dir = random.choice([-1, +1])
        self.scale = 1

    def update(self, tick):
        self.rect.y += self.speed[0]
        if abs(self.midscreen - self.rect.centerx) < 130:
            self.rect.centerx += (self.speed[1] / 2) * self.dir
        self.speed[0] += 0.09
        self.speed[1] += 0.04
        
        self.scale += 0.01
        self.scale = min(self.scale, 2.1)
        self.anim._transformedImages = []        # force reset. inefficient
        self.anim.rotozoom(0, self.scale)

    def draw(self, screen):
        self.anim.blit(screen, (self.rect.x, self.rect.y))

class Stage4(Stage):            
    def __init__(self, resolution):
        super().__init__(resolution)

        self.texts = [Text("PROTECT THE PACKET", (255, 255, 255), self._center_text)]

        self.stand_anim = pyganim.PygAnimation([("images/button1.png", 10),
                                               ("images/button 2.png", 10)])
        self.left_anim = pyganim.PygAnimation([("images/button1.png", 10),
                                               ("images/button 2.png", 10)])
        self.right_anim = pyganim.PygAnimation([("images/button1.png", 10),
                                               ("images/button 2.png", 10)])
        self.stand_anim.play()
        self.left_anim.play()

        self.center_x = resolution[0] / 2
        self.bottom_y = resolution[1]
        self.reset()
        
    def reset(self):
        self.current_anim = self.stand_anim
        self.enemies = []
        for i in range(4):
            self.enemies.append(Enemy(self.center_x))
        self.punch_cooldown = 0

    def update(self, input, tick):
        for enemy in self.enemies:
            enemy.update(tick)
        
        self.punch_cooldown -= tick
        
        cooldown = 1000
        if input.left:
            self.current_anim = self.left_anim
            self.punch_cooldown = cooldown
        elif input.right:
            self.current_anim = self.right_anim
            self.punch_cooldown = cooldown
        elif self.punch_cooldown <= 0:
            self.current_anim = self.stand_anim


    def draw(self, screen):
        super().draw(screen)

        rect = self.current_anim.getRect()
        rect.centerx = self.center_x
        rect.bottom = self.bottom_y - 100

        distance = 200
        if self.current_anim == self.left_anim:
            rect.x -= distance
            rect.y -= 50
        elif self.current_anim == self.right_anim:
            rect.x += distance
            rect.y -= 50
            
        self.stand_anim.blit(screen, (rect.x, rect.y))

        for enemy in self.enemies:
            enemy.draw(screen)