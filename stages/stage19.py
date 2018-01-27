# Sell Trash

import pygame
import pyganim
import random
from .stage import Stage, Text, UpdatingText, Avatar


class Kaching(UpdatingText):
    def __init__(self):
        text = "$$$"
        color = [0, 190, 0, 1.0]
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

class Player(Avatar):
    def __init__(self):
        Avatar.__init__(self, speed=10, pos=[400, 350], facing=[1, 0],
                        animation_files=[("images/poop.png", 200),])

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

class Stage19(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)
        self.bg = pygame.image.load("images/trashy room.png").convert()

        self.reset()
        
    def reset(self):
        self.texts = []
        self.objects = []
        self.trash = ["UFO Parts", "Foobars"]

    def update(self, input, tick):
        self._iterate_all(self.objects, "update", {"input": input, "tick": tick})
        self.texts = [Text("Sell trash to boost wifi", (0, 0, 0), self._center_text)]

        if input.button:
            self.trash.pop(0)
            self.objects.append(Kaching())

        if len(self.trash) <= 0:
            return True

    def draw(self, screen):
        screen.blit(self.bg, (0, 0))
        super().draw(screen)

        
        color = (128, 255, 128)
        rect = pygame.Rect(100, 100, 600, 200)
        pygame.draw.rect(screen, color, rect, 4)

        self._iterate_all(self.objects, "draw", {"screen": screen})