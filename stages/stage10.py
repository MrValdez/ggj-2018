# Ninja Turtle Van

import pygame
import pyganim
import random
from .stage import Stage, Text

class Stage10(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)
        self.texts = [Text("Drive the turtle van to the exit", (255, 255, 255), self._center_text)]

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

        self.van = self.van_right
        self.pos = [100, 300]
        self.facing = [1, 0]

        self.shot_original = pyganim.PygAnimation([("images/button1.png", 200),
                                                   ("images/button 2.png", 200)])
        self.shots = []

        rects = [
                 [64 * 1, 0, 64, 64],
                 [64 * 2, 0, 64, 64],
                 [64 * 3, 0, 64, 64],
                 [64 * 0, 0, 64, 64],
                 ]
        exit = pyganim.getImagesFromSpriteSheet("images/door2.png", rects=rects)
        frames = list(zip(exit, [1000, 400, 400, 400]))
        self.exit = pyganim.PygAnimation(frames)
        self.exit.play()
        self.exit_rect = self.exit.getRect()
        self.exit_rect.move_ip(700, 100)

        self.reset()
        
    def reset(self):
        pass

    def update(self, input, tick):
        speed = 3
        missile_speed = 5
        
        if input.up_hold:
            self.van = self.van_up
            self.pos[1] -= speed
            self.facing = [0, -1]
        if input.down_hold:
            self.van = self.van_down
            self.pos[1] += speed
            self.facing = [0, +1]
        if input.left_hold:
            self.van = self.van_left
            self.pos[0] -= speed
            self.facing = [-1, 0]
        if input.right_hold:
            self.van = self.van_right
            self.pos[0] += speed
            self.facing = [+1, 0]
        if input.button:
            newShot = self.shot_original.getCopy()
            newShot.play()
            if self.facing == [+1, 0]:
                newShot.rotate(-90)
            elif self.facing == [-1, 0]:
                newShot.rotate(90)
            elif self.facing == [0, 1]:
                newShot.rotate(180)
            pos = self.pos[:]
            facing = self.facing[:]
            
            self.shots.append([newShot, pos, facing, missile_speed])

        for i, (shot, pos, facing, missile_speed) in enumerate(self.shots):
            self.shots[i][1][0] += self.shots[i][2][0] * missile_speed
            self.shots[i][1][1] += self.shots[i][2][1] * missile_speed
            
    def draw(self, screen):
        super().draw(screen)

        self.exit.blit(screen, self.exit_rect)
        self.van.blit(screen, self.pos)
        
        for shot, pos, facing, missile_speed in self.shots:
            shot.blit(screen, pos)
