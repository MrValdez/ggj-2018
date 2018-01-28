# Petting

import pygame
import pyganim
import random
from .stage import Stage, Text, UpdatingText


class Love:
    def __init__(self):
        image = random.choice(["poop.png", "thumbs.png", "heart.png", "wifi signals.png"])
        self.image = pygame.image.load("images/" + image)
        self.pos = [random.randint(0, 500), random.randint(50, 400)]
        self.fade = 1.0

    def update(self, input, tick):
        self.pos[1] += random.randint(-1, 5)
        self.pos[0] += random.randint(-5, 5)
        self.fade -= 0.001

    def draw(self, screen):
        screen.set_alpha(self.fade * 100)
        screen.blit(self.image, self.pos)


class Stage26(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)
        self.dog = pygame.image.load("images/dog.png")
        self.texts = [Text("Pet and transmit the cuteness", (255, 255, 255), self._center_text)]
        
        self.reset()
        
    def reset(self):
        self.responses = []
        self.love = 0

    def update(self, input, tick):
        self._iterate_all(self.responses, "update", {"input": input, "tick": tick})

        if self.love >= 30 and input.button:
            return True
            
        if input.button:
           self.love += 1 
           self.responses.append(Love())

    def draw(self, screen):
        screen.fill((100, 90, 230))
        super().draw(screen)      
        
        x, y = 200, 190
        if self.love:
            x += random.randint(-self.love * 2, +self.love * 2)
            y += random.randint(-self.love * 2, +self.love * 2)
        screen.blit(self.dog, (x, y))
                
        self._iterate_all(self.responses, "draw", {"screen": screen})