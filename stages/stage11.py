# Space Invaders

import pygame
import pyganim
import random
from .stage import Stage, Text, Projectile, Collidable, Avatar


class Ship(Avatar):
    def __init__(self):
        Avatar.__init__(self, speed=12, pos=[300, 550], facing=[0, -1])

    def update(self, input, tick):
        speed = self.speed
        
        if input.left_hold:
            self.pos[0] -= speed
        if input.right_hold:
            self.pos[0] += speed

class Alien(Collidable):
    def __init__(self, pos):
        alien_anim = pyganim.PygAnimation([("images/button1.png", 200),
                                           ("images/button 2.png", 200)])

        Collidable.__init__(self, alien_anim, pos)
        self.speed = random.randint(1, 3)

    def update(self, input, tick):
        self.pos[1] += self.speed

class Stage11(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)
        self.texts = [Text("Defend Package from Space Invaders", (255, 255, 255), self._center_text)]

        self.avatar = Ship()

        self.shot_original = pyganim.PygAnimation([("images/button1.png", 200),
                                                   ("images/button 2.png", 200)])

        self.bg = pygame.image.load("images/space background.png")
        self.reset()
        
    def reset(self):
        self.shots = []
        self.aliens = []
        for i in range(20):
            x, y = random.randint(20, 500), random.randint(-500, 0)
            self.aliens.append(Alien([x, y]))

        self.objects = [self.avatar, self.shots, self.aliens]


    def update(self, input, tick):      
        missile_speed = 25
        self.avatar.update(input, tick)
        for alien in self.aliens:
            alien.update(input, tick)
            if alien.pos[1] > self.avatar.pos[1]:
                self.reset()

        if input.button:
            newShot = Projectile(self.shot_original, self.avatar.pos, self.avatar.facing, missile_speed, self.resolution)
            self.shots.append(newShot)

        for shot in self.shots:
            if shot.update(input, tick):
                self.shots.remove(shot)
                continue
            if shot.pos[1] <= 0:
                self.shots.remove(shot)
                continue

        for shot in self.shots:
            for alien in self.aliens:
                if shot.has_collide(alien):
                    self.shots.remove(shot)
                    self.aliens.remove(alien)
                    break
        
        if len(self.aliens) <= 0:
            return True
            
    def draw(self, screen):
        screen.blit(self.bg, [0, -100])
        super().draw(screen)

        self._iterate_all(self.objects, "draw", {"screen": screen})