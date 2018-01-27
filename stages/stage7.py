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

        self.sad = pyganim.PygAnimation([("images/sad cloud.png", 10)])
        self.sad.play()

        self.yeah = pyganim.PygAnimation([("images/usb ok.jpg", 10)])
        self.yeah.play()

        self.reset()
        
    def reset(self):
        self.texts = [Text("Connect Male and Female ends", (255, 255, 255), self._center_text)]
        self.flips = 0
        self.rotate = 0
        self.victory = 0
        self.sad_visible = 0
        self.distance = 200
        
    def update(self, input, tick):
        if self.victory:
            self.texts = [Text("YEAHHHHHHHHH~!", (255, 128, 100), self._center_text)]
            self.victory += tick
            
            if self.victory > 1500:
                return True
            return

        if input.button or input.up or input.down:
            if self.sad_visible != 0:
                self.rotate += 1
                self.male.flip(False, True)

            self.sad_visible = 0
            self.distance = 200

        if input.right:
            self.distance = 40
            
            if self.rotate < 3:
                self.rotate = 0
                self.sad_visible = 300
            else:
                self.distance = 100
                self.victory = 1

        self.sad_visible -= tick

    def draw(self, screen):
        super().draw(screen)

        male_rect = self.male.getRect()
        female_rect = self.female.getRect()

        male_rect.centerx = (self.resolution[0] / 2) - self.distance
        male_rect.centery = self.resolution[1] / 2
        female_rect.centerx = (self.resolution[0] / 2) + self.distance
        female_rect.centery = self.resolution[1] / 2

        self.male.blit(screen, male_rect)
        self.female.blit(screen, female_rect)

        if not self.victory:
            rect = self.sad.getRect().move(self.resolution[0], 0)
            if self.sad_visible > 0:
                rect.centerx = self.resolution[0] / 2
                rect.centery = self.resolution[1] / 2
            self.sad.blit(screen, rect)
        else:
            rect = self.yeah.getRect()
            rect.centerx = self.resolution[0] / 2
            rect.centery = self.resolution[1] / 2
            self.yeah.blit(screen, rect)
