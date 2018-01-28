# Game & Watch

import pygame
import pyganim
import random
from .stage import Stage, Text


class LED:
    def __init__(self, image, pos, flip=False, convert=True, alt=None):
        self.image = pygame.image.load(image)
        self.image2 = pygame.image.load(alt)

        self.pos = pos
        self.active = False
        if flip:
            self.image = pygame.transform.flip(self.image, True, False)
            self.image2 = pygame.transform.flip(self.image2, True, False)

    def update(self, input, tick):
#        self.active = not self.active
        pass

    def draw(self, screen):
        if self.active:
            screen.blit(self.image2, self.pos) 
        else:
            screen.blit(self.image, self.pos) 
            

class Stage28(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)
        self.texts = [Text("Help Mister Game And Watch find signal", (255, 255, 255), self._center_text)]
        gw1 = "images/g&w1b.png"
        gw1b = "images/g&w1.png"
        gw2 = "images/g&w2b.png"
        gw2b = "images/g&w2.png"
        wifi = "images/wifi signals 3.png"
        wifi2 = "images/wifi signals 2.png"

        self.gwLEDs = [
            LED(gw1, [-50, 300], alt=gw1b),
            LED(gw2, [200, 340], alt=gw2b),
            LED(gw2, [400, 340], flip=True, alt=gw2b),
            LED(gw1, [650, 300], flip=True, alt=gw1b),
            ]
        center = (resolution[0] / 2) - 40
        self.wifiLEDs = [
            LED(wifi, [center, 65], convert=False, alt=wifi2),
            
            LED(wifi, [center - 100, 80], convert=False, alt=wifi2),
            LED(wifi, [center + 100, 80], convert=False, alt=wifi2),
            
            LED(wifi, [center - 250, 150], convert=False, alt=wifi2),
            LED(wifi, [center - 150, 170], convert=False, alt=wifi2),
            LED(wifi, [center + 150, 170], convert=False, alt=wifi2),
            LED(wifi, [center + 250, 150], convert=False, alt=wifi2),

            LED(wifi, [center - 300, 280], convert=False, alt=wifi2),
            LED(wifi, [center - 140, 330], convert=False, alt=wifi2),
            LED(wifi, [center + 140, 330], convert=False, alt=wifi2),
            LED(wifi, [center + 300, 280], convert=False, alt=wifi2),
            ]

        self.images = [self.gwLEDs, self.wifiLEDs, ]
        self.reset()
        
    def reset(self):
        self.current = 0
        self.timer = 1100
        self.wifi_level = 0
        self.correct_lane = random.randint(0, 3)
        
    def update(self, input, tick):
        self._iterate_all(self.images, "update", {"input": input, "tick": tick})

        if input.left:
            self.current -= 1
            if self.current < 0:
                self.current = 3

        if input.right:
            self.current += 1
            if self.current > 3:
                self.current = 0

        self.timer -= tick
        if self.timer <= 0:
            self.timer = random.randint(700, 1000)
            self.wifi_level += 1

        for gw in self.gwLEDs:
            gw.active = False
        self.gwLEDs[self.current].active = True
        
        for wifi in self.wifiLEDs:
            wifi.active = False
        if self.wifi_level == 0:
            self.wifiLEDs[0].active = True
        elif self.wifi_level == 1:
            if self.correct_lane < 2:
                self.wifiLEDs[1].active = True
            else:
                self.wifiLEDs[2].active = True
        elif self.wifi_level == 3:
            self.wifiLEDs[3 + self.correct_lane].active = True
        elif self.wifi_level == 4:
            self.wifiLEDs[7 + self.correct_lane].active = True

        if self.wifi_level == 5:
            if self.correct_lane == self.current:
                return True

        if self.wifi_level > 5:
            self.reset()

    def draw(self, screen):
        screen.fill((128, 128, 128))
        super().draw(screen)      
                        
        self._iterate_all(self.images, "draw", {"screen": screen})