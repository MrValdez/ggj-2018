# Find the strongest signal

import math
import pygame
import pyganim
import random
from .stage import Stage, Text, Projectile, Collidable, Avatar


class Stage14(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)
        self.texts = [Text("Find the strongest signal and send", (255, 255, 255), self._center_text)]

        self.target_amptitude = 200
        self.reset()
        
    def reset(self):
        size = 20
        self.amptitude_list = [random.randint(0, 300) for i in range(size)]
        self.current = random.choice(range(size))
        self.amptitude_list[self.current] = 10
        self.move_cooldown = 500
        self.check_solution_timer = 0
        self.target_solution_timer = 2000

    def update(self, input, tick):
        self.move_cooldown -= tick
        if self.move_cooldown < 0:
            if input.left_hold:
                self.move_cooldown = 500
                self.current -= 1
                if self.current < 0:
                    self.current = len(self.amptitude_list) - 1
                self.check_solution_timer = 0
                
            if input.right_hold:
                self.move_cooldown = 500
                self.current = (self.current + 1) % len(self.amptitude_list)
                self.check_solution_timer = 0

        self.check_solution_timer += tick
        if self.check_solution_timer > self.target_solution_timer:
            if self.amptitude_list[self.current] >= self.target_amptitude:
                return True

    def draw(self, screen):
        delta = self.check_solution_timer / self.target_solution_timer
        r, g, b = [28 * delta, 145 * delta, 20 * delta]
        screen.fill([min(r, 255), min(g, 255), min(b, 255)])
        super().draw(screen)

        center_y = self.resolution[1] / 2 
        pygame.draw.line(screen, [255, 128, 200], [0, center_y], [self.resolution[0], center_y], 10)
        
        color = [255, 255, 255]
        for x in range(random.randint(0, 20), self.resolution[0], random.randint(1, 20)):
            amptitude = self.amptitude_list[self.current]
            y = math.cos(x) * (amptitude + random.randint(-10, 10))
            pygame.draw.circle(screen, color, [x, int(center_y + y)], 5)