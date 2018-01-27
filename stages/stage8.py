# Two Auth factor

import pygame
import pyganim
import random
from .stage import Stage, Text

class Stage8(Stage):
    def _next_line_text(self, pos, line_number):
        pos.x = (self.resolution[0] / 2) - 100
        pos.y = 100

        pos.move_ip(0, 18 * line_number)
        return pos

    def __init__(self, resolution):
        super().__init__(resolution)
        self.texts = [Text("Enter the two-auth factor", (255, 255, 255), self._center_text),
                      Text("*Login details*", (255, 255, 255), lambda x: self._next_line_text(x, 1)),
                      Text("Username: root", (255, 255, 255), lambda x: self._next_line_text(x, 2)),
                      Text("Password: hunter2", (255, 255, 255), lambda x: self._next_line_text(x, 3))]

        self.phone = pyganim.PygAnimation([("images/phone_white.png", 10)])
        self.phone.play()

        self.up = pyganim.PygAnimation([("images/up.png", 10)])
        self.left = self.up.getCopy()
        self.down = self.up.getCopy()
        self.right = self.up.getCopy()
        self.left.rotate(90)
        self.down.rotate(180)
        self.right.rotate(-90)
        self.up.play()
        self.left.play()
        self.down.play()
        self.right.play()

        self.reset()
        
    def reset(self):
        self.password = [self.up,
                         self.up,
                         self.down,
                         self.down,
                         self.left,
                         self.right,
                         self.left,
                         self.right,]
        self.password = [[dir, False] for dir in self.password]
        self.current_entry = 0

    def update(self, input, tick):
        for input_press, password in ((input.up, self.up),
                                      (input.down, self.down),
                                      (input.left, self.left),
                                      (input.right, self.right),):
            if input_press and self.password[self.current_entry][0] == password:
                self.password[self.current_entry][1] = True
                self.current_entry += 1
                valid_password = True
                break

        if self.current_entry >= len(self.password):
            return True

    def draw(self, screen):
        super().draw(screen)

        monitor = pygame.Rect(10, 10, self.resolution[0] - 10, 200)
        pygame.draw.rect(screen, [255, 255, 255], monitor, 1)

        phone_rect = self.phone.getRect()
        phone_rect.centerx = self.resolution[0] / 2
        phone_rect.bottom = self.resolution[1] - 100
        self.phone.blit(screen, phone_rect)

        dir = self.password[self.current_entry][0]

        next_button_rect = dir.getRect()
        next_button_rect.centerx = phone_rect.centerx
        next_button_rect.top = phone_rect.top + 30
        dir.blit(screen, next_button_rect)
                    
        # successful inputs
        rect = self.up.getRect()
        rect.x = 20
        rect.centery = self.resolution[1] / 2
        rect.y -= 90

        for dir, active in self.password:
            rect.x += rect.width + 10
            if active:
                color = (255, 255, 128)
                dir.blit(screen, rect)
                pygame.draw.rect(screen, color, rect, 1)
