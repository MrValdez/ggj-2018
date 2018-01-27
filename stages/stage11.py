# Space Invaders

import pygame
import pyganim
import random
from .stage import Stage, Text, Projectile, Collidable, Avatar


class Ship(Avatar):
    def __init__(self):
        Avatar.__init__(self, speed=6, pos=[100, 600], facing=[0, 1])

class Stage11(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)
        self.texts = [Text("Defend Package from Space Invaders", (255, 255, 255), self._center_text)]

        self.avatar = Ship()

        self.shot_original = pyganim.PygAnimation([("images/button1.png", 200),
                                                   ("images/button 2.png", 200)])
        self.shots = []
        
        self.alien_anim = pyganim.PygAnimation([("images/button1.png", 200),
                                                ("images/button 2.png", 200)])
        self.aliens = [Collidable(self.alien_anim, [20, 20])]

        self.objects = [self.avatar, self.shots, self.aliens]

        self.reset()
        
    def reset(self):
        pass

    def update(self, input, tick):      
        missile_speed = 10
        self.avatar.update(input, tick)

        if input.button:            
            newShot = Projectile(self.shot_original, self.avatar.pos, self.avatar.facing, missile_speed, self.resolution)
            self.shots.append(newShot)

        for shot in self.shots:
            if shot.update(input, tick):
                self.shots.remove(shot)
            
    def draw(self, screen):
        super().draw(screen)

        self._iterate_all(self.objects, "draw", {"screen": screen})