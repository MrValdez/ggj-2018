# Chrome game

import pygame
import pyganim
from .stage import Stage, Text

class Stage3(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)

        self.texts = [Text("JUMP", (255, 255, 255), self._center_text)]

        self.run_anim = pyganim.PygAnimation([("images/button1.png", 10),
                                              ("images/button 2.png", 10)])
        self.jump_anim = pyganim.PygAnimation([("images/button1.png", 10),
                                               ("images/button 2.png", 10)])

        self.run_anim.play()
        self.jump_anim.play()

        self.obstacle = pyganim.PygAnimation([("images/button1.png", 10),
                                               ("images/button 2.png", 10)])
        self.obstacle.play()

        self.reset()
        
    def reset(self):
        self.ground_y = 200
        self.state = "run"
        self.jump_power = 0
        self.jump_tick = 0
        self.obstacle_pos = [1000, self.ground_y]

    def update(self, input, tick):
        if input.button:
            if self.state == "run":
                self.state = "jump"
                self.jump_power = 350

        self.jump_tick += tick
        if self.jump_tick > 100:
            self.jump_power -= 10

            if self.jump_power < 0:
                self.jump_power = 0
                self.state = "run"
                
            self.obstacle_pos[0] -= 13

    def draw(self, screen):
        super().draw(screen)

        if self.state == "run":
            self.run_anim.blit(screen, [20, self.ground_y])
        else:
            y = self.ground_y - min(self.jump_power, 100)
            self.run_anim.blit(screen, [20, y])

        self.obstacle.blit(screen, self.obstacle_pos)