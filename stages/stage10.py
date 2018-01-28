# Ninja Turtle Van

import pygame
import pyganim
import random
from .stage import Stage, Text, Projectile, Collidable, Avatar


class Van(Avatar):
    def __init__(self):
        Avatar.__init__(self, speed=3, pos=[100, 300], facing=[1, 0], animation_files=[("images/car.png", 200),])


class Stage10(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)
        self.texts = [Text("Drive the delivery van to the exit", (255, 255, 255), self._center_text)]

        self.van = Van()

        self.shot_original = pyganim.PygAnimation([("images/wifi signals.png", 200),])
        self.shots = []
        
        self.barrier = pyganim.PygAnimation([("images/car.png", 200),])
        self.barriers = [
            #Collidable(self.barrier, [20, 20])
        ]

        rects = [
                 [64 * 1, 0, 64, 64],
                 [64 * 2, 0, 64, 64],
                 [64 * 3, 0, 64, 64],
                 [64 * 0, 0, 64, 64],
                 ]
        exit = pyganim.getImagesFromSpriteSheet("images/door2.png", rects=rects)
        frames = list(zip(exit, [1000, 400, 400, 400]))
        exit_anim = pyganim.PygAnimation(frames)
        self.exit = Collidable(exit_anim, [700, 100])

        self.reset()
        
    def reset(self):
        pass

    def update(self, input, tick):
        prev_pos = self.van.pos
        self.van.update(input, tick)
        missile_speed = 5

        if input.button:            
            newShot = Projectile(self.shot_original, self.van.pos, self.van.facing, missile_speed, self.resolution)
            self.shots.append(newShot)

        for shot in self.shots:
            if shot.update(input, tick):
                self.shots.remove(shot)

        for barrier in self.barriers:
            for shot in self.shots:
                if shot.has_collide(barrier):
                    self.shots.remove(shot)

        for barrier in self.barriers:
            if barrier.has_collide(self.van):
                self.van.pos = prev_pos
                print(prev_pos)
        
        if self.van.has_collide(self.exit):
            return True

            
    def draw(self, screen):
        super().draw(screen)

        self.exit.draw(screen)
        self.van.draw(screen)
        
        for shot in self.shots:
            shot.draw(screen)
        for barrier in self.barriers:
            barrier.draw(screen)