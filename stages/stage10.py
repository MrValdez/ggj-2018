# Ninja Turtle Van

import pygame
import pyganim
import random
from .stage import Stage, Text, Projectile, Collidable


class Van(Collidable):
    def __init__(self):
        self.van_original = pyganim.PygAnimation([("images/button1.png", 200),
                                                   ("images/button 2.png", 200)])
        self.van_up = self.van_original.getCopy()
        self.van_down = self.van_original.getCopy()
        self.van_down.rotate(180)
        self.van_left = self.van_original.getCopy()
        self.van_left.rotate(90)
        self.van_right = self.van_original.getCopy()
        self.van_right.rotate(-90)
        self.van_up.play()
        self.van_down.play()
        self.van_left.play()
        self.van_right.play()

        self.anim = self.van_right
        self.pos = [100, 300]
        self.facing = [1, 0]
        
    def update(self, input, tick):
        speed = 3
        missile_speed = 5
        
        if input.left_hold:
            self.anim = self.van_left
            self.pos[0] -= speed
            self.facing = [-1, 0]
        if input.right_hold:
            self.anim = self.van_right
            self.pos[0] += speed
            self.facing = [+1, 0]
        if input.down_hold:
            self.anim = self.van_down
            self.pos[1] += speed
            self.facing = [0, +1]
        if input.up_hold:
            self.anim = self.van_up
            self.pos[1] -= speed
            self.facing = [0, -1]


class Stage10(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)
        self.texts = [Text("Drive the turtle van to the exit", (255, 255, 255), self._center_text)]

        self.van = Van()

        self.shot_original = pyganim.PygAnimation([("images/button1.png", 200),
                                                   ("images/button 2.png", 200)])
        self.shots = []
        
        self.barrier = pyganim.PygAnimation([("images/button1.png", 200),
                                                   ("images/button 2.png", 200)])
        self.barriers = [Collidable(self.barrier, [20, 20])]

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
        self.van.update(input, tick)

        if input.button:            
            newShot = Projectile(self.shot_original, self.van.pos, self.van.facing, missile_speed, self.resolution)
            self.shots.append(newShot)

        for shot in self.shots:
            if shot.update(tick):
                self.shots.remove(shot)

        for barrier in self.barriers:
            for shot in self.shots:
                if shot.has_collide(barrier):
                    print("collide")
                    self.shots.remove(shot)
        
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