# Have you tried turning it on and off again?

import pygame
import pyganim
from .stage import Stage, Text

class Stage2(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)

        self.texts = [Text("Have you tried turning it on and off again?", (255, 255, 255), self._center_text)]

        self.pc = pyganim.PygAnimation([("images/computer.png", 10)])
        self.poop = pyganim.PygAnimation([("images/poop.png", 10)])
        self.pc.play()
        self.poop.play()

        switch = pyganim.PygAnimation([("images/button1.png", 10),         # off
                                       ("images/button 2.png", 10)])        # on
        self.switches = []
        self.switch_status = []
        self.switches.append(switch)
        self.switches.append(switch.getCopy())
        for switch in self.switches:
            switch.play()
            switch.pause()
            self.switch_status.append(False)

        self.pos = [[150, 400],
                    [650, 400]]
        self.current_switch = 0

    def update(self, input, tick):
        speed = 10
        if input.left:  self.current_switch = self.current_switch - 1
        if input.right:  self.current_switch = self.current_switch + 1
        self.current_switch %= len(self.pos)

        if input.button:
            self.switches[self.current_switch].nextFrame()
            self.switch_status[self.current_switch] = True

        return all(self.switch_status)

    def draw(self, screen):
        super().draw(screen)

        self.pc.blit(screen, [200, 300])
        self.poop.blit(screen, [350, 400])

        for switch, pos in zip(self.switches, self.pos):
            switch.blit(screen, pos)
        
        rect = self.switches[self.current_switch].getRect()
        rect.move_ip(self.pos[self.current_switch])
        pygame.draw.rect(screen, (255, 128, 128), rect, 2)