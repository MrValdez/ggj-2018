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

class Stage19(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)
        self.bg = pygame.image.load("images/trashy room.png").convert()

        self.reset()
        
    def reset(self):
        self.texts = []
        self.objects = []
        self.trash_names = ["UFO Parts", "Foobars", "Scanners Darkly", "Aluminum Sheets", "Adamantinum", "Statue of Liberty"]
        self.update_text()

    def update_text(self):
        self.trash = [UpdatingText(name, (0, 0, 0), (120, 110 + (32 * i)))
                      for i, name in enumerate(self.trash_names)]

    def update(self, input, tick):
        self._iterate_all(self.objects, "update", {"input": input, "tick": tick})
        self.texts = [Text("Sell trash to boost wifi", (0, 0, 0), self._center_text)]

        if input.button:
            self.trash_names.pop(0)
            self.objects.append(Kaching())
            self.update_text()

        if len(self.trash) <= 0:
            return True

    def draw(self, screen):
        screen.blit(self.bg, (0, 0))
        super().draw(screen)
        

        for trash in self.trash:
            trash.draw(screen)

        color = (128, 255, 128)
        rect = pygame.Rect(100, 100, 600, 200)
        pygame.draw.rect(screen, color, rect, 4)

        self._iterate_all(self.objects, "draw", {"screen": screen})