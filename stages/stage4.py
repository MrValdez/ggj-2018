# Punch game

import pygame
import pyganim
from .stage import Stage, Text

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
        self.enemy_anim = pyganim.PygAnimation([("images/button1.png", 10),
                                               ("images/button 2.png", 10)])
        self.stand_anim.play()
        self.left_anim.play()
        self.enemy_anim.play()

        self.center_x = resolution[0] / 2
        self.bottom_y = resolution[1]
        self.reset()
        
    def reset(self):
        self.current_anim = self.stand_anim
        self.enemies = []
        for i in range(4):
            pos = [0, 0]
            enemy = self.enemy_anim.getCopy()
            self.enemies.append((enemy, pos))
        self.punch_cooldown = 0

    def update(self, input, tick):
        for i, enemy in enumerate(self.enemies):
            self.enemies[i][1][1] += 2
        
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

        for anim, pos in self.enemies:
            anim.blit(screen, pos)