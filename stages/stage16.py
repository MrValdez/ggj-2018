# Use poop to stop WiFi transmissions

import math
import pygame
import pyganim
import random
from .stage import Stage, Text, Projectile, Collidable, Avatar


class Player(Avatar):
    def __init__(self):
        Avatar.__init__(self, speed=20, pos=[400, 350], facing=[1, 0],
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

class Enemy(Collidable):
    def __init__(self, pos):
        anim = pyganim.PygAnimation([("images/button1.png", 200),
                                     ("images/button 2.png", 200)])
        anim.play()
        
        Collidable.__init__(self, anim, pos)

class Stage16(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)
        self.texts = [Text("Use poop to make them stop the WiFi transmission", (255, 255, 255), self._center_text)]

        self.reset()
        
    def reset(self):
        self.avatar = Player()
        
        self.enemies = []
        for i in range(200):
            pos = [random.randint(100, 700),
                   random.randint(100, 500)]
            self.enemies.append(Enemy(pos))

        self.objects = [self.enemies, self.avatar]

    def update(self, input, tick):
        self.avatar.update(input, tick)

        self.avatar.pos[0] = max(0, min(self.resolution[0], self.avatar.pos[0]))
        self.avatar.pos[1] = max(0, min(self.resolution[1] - 20, self.avatar.pos[1]))

        for enemy in self.enemies:
            speed = random.randint(-1, 20)
            if enemy.has_collide(self.avatar):
                for i in [0, 1]:
                    if enemy.pos[i] < self.avatar.pos[i]: enemy.pos[i] -= speed
                    if enemy.pos[i] > self.avatar.pos[i]: enemy.pos[i] += speed
        
                    if (enemy.pos[i] >= (self.resolution[i] - 75) or
                        enemy.pos[i] <= 75):
                        self.enemies.remove(enemy)
                        break

        if len(self.enemies) < 50:
            return True
                
    def draw(self, screen):
        super().draw(screen)

        self._iterate_all(self.objects, "draw", {"screen": screen})