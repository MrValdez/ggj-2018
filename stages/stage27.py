# Stop transmission of spam

import pygame
import pyganim
import random
from .stage import Stage, Text, UpdatingText

class Spam:
    def __init__(self):
        self.image = pygame.image.load("images/Spam_can.png")
        self.pos = [random.randint(0, 500), random.randint(50, 400)]
        self.fade = 1.0
        self.destroyed = False
        self.velocity = []

    def change_velocity(self):
        self.velocity = [random.randint(-40, 40), random.randint(-40, 40)]
        self.destroyed = True

    def update(self, input, tick):
        if self.destroyed:
            self.fade -= 0.005
            self.pos[0] += self.velocity[0]
            self.pos[1] += self.velocity[1]

    def draw(self, screen):
        screen.set_alpha(self.fade * 100)
        screen.blit(self.image, self.pos)


class Stage27(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)
        self.dog = pygame.image.load("images/dog.png")
        self.texts = [Text("Overwhelming spam! Close their transmissions", (255, 255, 255), self._center_text)]

        self.reset()
        
    def reset(self):
        self.spams = [Spam()]
        self.deleted = []
        self.images = [self.spams, self.deleted]
        
        self.timer = 100
        self.responses = []

    def update(self, input, tick):
        self._iterate_all(self.images, "update", {"input": input, "tick": tick})

        if len(self.spams) + len(self.deleted) < 20:
            self.timer -= tick
            if self.timer <= 0:
                self.timer = random.randint(100, 400)
                self.spams.append(Spam())

        if len(self.spams) <= 0:
            return True
            
        if input.button:
            delete = random.choice(self.spams)
            delete.change_velocity()
            self.spams.remove(delete)
            self.deleted.append(delete)

    def draw(self, screen):
        screen.fill((100, 200, 30))
        super().draw(screen)      
        
        x, y = 200, 300
        screen.blit(self.dog, (x, y))
                
        self._iterate_all(self.images, "draw", {"screen": screen})