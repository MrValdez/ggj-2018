import pygame
import pyganim
from .stage import Stage, Text

class Stage2(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)

        self.texts = [Text("Have you tried turning it on and off again?", (255, 255, 255), self._center_text)]

        switch = pyganim.PygAnimation([("images/button1.png", 10),         # off
                                       ("images/button 2.png", 10)])        # on
        self.switches = []
        self.switches.append(switch)
        self.switches.append(switch.getCopy())
        for switch in self.switches:
            switch.play()
            switch.pause()

        self.pos = [[100, 200],
                    [400, 200]]
        self.current_switch = 0

    def update(self, input):
        speed = 10
        if input.left:  self.current_switch = self.current_switch - 1
        if input.right:  self.current_switch = self.current_switch + 1
        self.current_switch %= len(self.pos)

        if input.button:
            self.switches[self.current_switch].nextFrame()
        
    def draw(self, screen):
        super().draw(screen)

        for switch, pos in zip(self.switches, self.pos):
            switch.blit(screen, pos)
        
        rect = self.switches[self.current_switch].getRect()
        rect.move_ip(self.pos[self.current_switch])
        pygame.draw.rect(screen, (255, 128, 128), rect, 2)