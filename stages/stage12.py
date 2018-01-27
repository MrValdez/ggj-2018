# Charge to end

import math
import pygame
import pyganim
import random
from .stage import Stage, Text, Projectile, Collidable, Avatar


class Player(Avatar):
    def __init__(self):
        Avatar.__init__(self, speed=0.4, pos=[400, 350], facing=[1, 0])

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
    def __init__(self, pos, avatar):
        anim = pyganim.PygAnimation([("images/button1.png", 200),
                                     ("images/button 2.png", 200)])
        anim.play()

        Collidable.__init__(self, anim, pos)
        self.speed = 0.3
        self.avatar = avatar

    def update(self, input, tick):
        if self.avatar.pos[0] - self.pos[0] < 0:
            self.pos[0] -= self.speed
        if self.avatar.pos[0] - self.pos[0] > 0:
            self.pos[0] += self.speed

        self.pos[1] -= 0.5

class Stage12(Stage):
    def _next_line_text(self, pos):
        pos.x = (self.resolution[0] / 2) - 100
        pos.y = 80

        pos.move_ip(0, 18)
        return pos

    def __init__(self, resolution):
        super().__init__(resolution)
        self.title = Text("Charge to the end without getting caught", (255, 255, 255), self._center_text)
        self.texts = [self.title]

        self.reset()
        
    def reset(self):
        self.avatar = Player()
        self.target_y = -5000
        
        self.enemies = []
        self.enemy_spawn_time = 100

        self.objects = [self.avatar, self.enemies]

    def update(self, input, tick):
        self.texts = [self.title,
                      Text("Target: {} meters".format(max(0, -self.target_y)), (255, 255, 255), self._next_line_text)
                        ]

        if input.button and self.target_y < 0:
            self.target_y += random.randint(40, 80)
            self.avatar.anim.nextFrame()
        else:
            self.target_y += random.randint(3, 6)

        self.enemy_spawn_time -= tick
        if self.enemy_spawn_time <= 0:
            self.enemy_spawn_time = random.randint(20, 100)
            if random.randint(0, 1):
                x = random.randint(20, 300)
            else:
                x = self.resolution[0] - random.randint(20, 100)
            
            y = self.resolution[1]
            self.enemies.append(Enemy([x, y], self.avatar))

        self.avatar.update(input, tick)
        for enemy in self.enemies:
            enemy.update(input, tick)

            if enemy.has_collide(self.avatar):
                self.reset()
                
        if self.avatar.pos[1] <= self.target_y:
            return True

    def draw(self, screen):
        super().draw(screen)

        pygame.draw.line(screen, [255, 128, 200], [0, self.target_y], [self.resolution[1] * 2, self.target_y], 10)

        self._iterate_all(self.objects, "draw", {"screen": screen})