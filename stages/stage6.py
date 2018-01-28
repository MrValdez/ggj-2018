#energize

import pyganim
import random
from .stage import Stage, Text

class Stage6(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)

        self.drink = pyganim.PygAnimation([("images/spam_can.png", 10)])
        self.drink.rotate(90)
        self.drink.play()

        self.avatar = pyganim.PygAnimation([("images/g&w1.png", 10)])
        self.avatar.play()

        self.yeah = pyganim.PygAnimation([("images/thumbs.png", 10)])
        self.yeah.play()

        self.reset()
        
    def reset(self):
        self.texts = [Text("Shake and energize", (255, 255, 255), self._center_text)]

        self.shake = 0
        self.pos = [500, 100]
        self.victory = False
        self.target_shake = 1000

    def update(self, input, tick):
        if self.shake < self.target_shake:
            if input.left_hold or input.right_hold or input.button_hold:  
                self.pos[0] += random.randint(-10, 10)
                self.pos[1] += random.randint(-5, 5)
                self.shake += random.randint(1, 30)

        if self.shake >= self.target_shake:
            self.victory = True
            self.texts = [Text("YEAHHHHHHHHH~!", (255, 128, 100), self._center_text)]
            self.shake += tick

        if self.shake > self.target_shake + 1000:
            return True

    def draw(self, screen):
        screen.fill([128, 128, 128])
        super().draw(screen)

        if self.shake < self.target_shake:
            self.drink.blit(screen, self.pos)
            self.avatar.blit(screen, [200, 200])
        else:
            rect = self.yeah.getRect()
            rect.centerx = self.resolution[0] / 2
            rect.bottom = self.resolution[1] - 100
            self.yeah.blit(screen, rect)
        