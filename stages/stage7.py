# Connect USB

import pyganim
import random
from .stage import Stage, Text

class Stage7(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)

        self.male = pyganim.PygAnimation([("images/usb male.png", 10)])
        self.male.flip(False, True)
        self.male.play()

        self.female = pyganim.PygAnimation([("images/usb female.png", 10)])
        self.female.play()

        self.yeah = pyganim.PygAnimation([("images/spam.png", 10)])
        self.yeah.play()

        self.reset()
        
    def reset(self):
        self.texts = [Text("Connect Male and Female ends", (255, 255, 255), self._center_text)]
        self.flips = 0
        self.rotate = 0
        self.victory = False

    def update(self, input, tick):
        #self.victory = True
        if self.victory:
            self.texts = [Text("YEAHHHHHHHHH~!", (255, 128, 100), self._center_text)]
            self.shake += tick

        #if self.shake > self.target_shake + 1000:
        #    return True
        if input.button or input.up or input.down:
            self.male.flip(False, True)

    def draw(self, screen):
        super().draw(screen)

        if not self.victory:
            male_rect = self.male.getRect()
            female_rect = self.female.getRect()

            male_rect.centerx = (self.resolution[0] / 2) - 100
            male_rect.centery = self.resolution[1] / 2
            female_rect.centerx = (self.resolution[0] / 2) + 100
            female_rect.centery = self.resolution[1] / 2

            self.male.blit(screen, male_rect)
            self.female.blit(screen, female_rect)
        else:
            rect = self.yeah.getRect()
            rect.centerx = self.resolution[0] / 2
            rect.bottom = self.resolution[1]
            self.yeah.blit(screen, rect)