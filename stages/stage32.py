# Transfer knowledge

import pygame
import pyganim
import random
from .stage import Stage, Text, Projectile, Collidable, Avatar


class Ship(Avatar):
    def __init__(self):
        animation_files = [("images/head.png", 200)]

        Avatar.__init__(self, speed=12, pos=[300, 350], facing=[0, -1], animation_files=animation_files)
        self.anim_left = self.anim
        self.anim_right = self.anim.getCopy()
        self.anim_right.flip(True, False)
        self.anim_left.play()
        self.anim_right.play()

    def update(self, input, tick):
        speed = self.speed
        
        if input.left_hold:
            self.pos[0] -= speed
            self.anim = self.anim_left
        if input.right_hold:
            self.pos[0] += speed
            self.anim = self.anim_right
        if input.up_hold:
            self.pos[1] -= speed
            self.anim = self.anim_left
        if input.down_hold:
            self.pos[1] += speed
            self.anim = self.anim_right

class Alien(Collidable):
    def __init__(self, pos):
        alien_anim = pyganim.PygAnimation([("images/book.png", 200),])

        Collidable.__init__(self, alien_anim, pos)
        self.speed = [random.randint(-4, 4),
                      random.randint(-4, 4)]

    def update(self, input, tick):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]

class Stage32(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)
        self.texts = [Text("Transfer knowledge to your brain", (255, 255, 255), self._center_text)]

        self.avatar = Ship()

        self.reset()
        
    def _spawn_book(self):
        x, y = random.randint(0, self.resolution[0]), random.randint(0, self.resolution[1])
        self.book.append(Alien([x, y]))

    def reset(self):
        self.points = 0
        self.target_points = 20
        
        self.book = []
        for i in range(20):
            self._spawn_book()

        self.objects = [self.avatar, self.book]

    def update(self, input, tick):      
        self.avatar.update(input, tick)
        for alien in self.book:
            alien.update(input, tick)

        for alien in self.book:
            if alien.has_collide(self.avatar):
                self.book.remove(alien)
                self._spawn_book()
                self.points += 1
                continue
            if (alien.pos[0] <= 0 or alien.pos[0] >= self.resolution[1] or
                alien.pos[1] <= 0 or alien.pos[1] >= self.resolution[1]):
                self._spawn_book()
                self.book.remove(alien)
                continue
        
        if self.points > self.target_points:
            return True
            
    def draw(self, screen):
        screen.fill([30, 90, 30])
        super().draw(screen)

        self._iterate_all(self.objects, "draw", {"screen": screen})