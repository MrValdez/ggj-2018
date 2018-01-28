# Regrets Transmission

import pygame
import pyganim
import random
from .stage import Stage, Text, UpdatingText


class Angry(UpdatingText):
    def __init__(self):
        text = random.choice([":(", ">:(", "wtf?", "not cool"])
        color = [200, 100, 0, 1.0]
        size = 100
        pos = [random.randint(0, 500), random.randint(100, 400)]
        self.fade = 1.0

        UpdatingText.__init__(self, text, color, pos, size)

    def update(self, input, tick):
        self.pos[1] -= 2
        self.fade -= 0.01
        self.color[3] = max(0, self.fade)

    def draw(self, screen):
        text = self.font.render(self.text, False, self.color)
        text.set_alpha(self.fade * 100)
        screen.blit(text, self.pos)
        return text.get_rect()


class Stage25(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)
        self.phone = pygame.image.load("images/phone.png")
        self.phone = pygame.transform.scale2x(self.phone)
        self.poop = pygame.image.load("images/poop.png")
        self.texts = [Text("Share your regrets on social media", (255, 255, 255), self._center_text)]
        
        self.reset()
        
    def reset(self):
        self.responses = []
        self.sent = 0

    def update(self, input, tick):
        self._iterate_all(self.responses, "update", {"input": input, "tick": tick})

        if self.sent >= 15 and input.button:
            return True
            
        if input.button:
           self.sent += 1 
           self.responses.append(Angry())

    def draw(self, screen):
        screen.fill([10, 200, 10])
        super().draw(screen)      
        
        x, y = 200, 190
        if self.sent:
            x += random.randint(-self.sent * 2, +self.sent * 2)
            y += random.randint(-self.sent * 2, +self.sent * 2)
        screen.blit(self.phone, (x, y))
        
        x, y = 330, 200
        screen.blit(self.poop, (x, y))
        
        self._iterate_all(self.responses, "draw", {"screen": screen})