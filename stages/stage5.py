# crowd surfing game

import pygame
import pyganim
import random
from .stage import Stage, Text

class Stage5(Stage):            
    def __init__(self, resolution):
        super().__init__(resolution)

        self.texts = [Text("CROWD SURFING", (255, 255, 255), self._center_text)]

        self.crowd = pyganim.PygAnimation([("images/button1.png", 10),
                                               ("images/button 2.png", 10)])
        self.player = pyganim.PygAnimation([("images/button1.png", 10),
                                               ("images/button 2.png", 10)])
        rects = [
                 [64 * 1, 0, 64, 64],
                 [64 * 2, 0, 64, 64],
                 [64 * 3, 0, 64, 64],
                 [64 * 0, 0, 64, 64],
                 ]
        exit = pyganim.getImagesFromSpriteSheet("images/door2.png", rects=rects)
        frames = list(zip(exit, [1000, 400, 400, 400]))
        self.exit = pyganim.PygAnimation(frames)
        
        self.crowd.play()
        self.player.play()
        self.exit.play()
        
        self.reset()
        
    def reset(self):
        self.crowds = []
        x = 100
        for i in range(100):
            crowd = self.crowd.getCopy()
            crowd.play()
            pos = (x, random.randint(100, self.resolution[1] - 100))
            if i % 2:
                x += random.randint(0, 40)
            self.crowds.append((crowd, pos))
        
        self.exit_pos = (700, random.randint(100, 400))
        self.player_pos = [100, random.randint(100, 450)]

    def update(self, input, tick):
        speed = 30
        if input.right: self.player_pos[0] += speed
        if input.left: self.player_pos[0] -= speed
        if input.up: self.player_pos[1] -= speed
        if input.down: self.player_pos[1] += speed

#        if input.right_hold: self.player_pos[0] += speed
#        if input.left_hold: self.player_pos[0] -= speed
#        if input.up_hold: self.player_pos[1] -= speed
#        if input.down_hold: self.player_pos[1] += speed
        
        self.player_pos[0] += random.randint(-2, 1)
        self.player_pos[1] += random.randint(-2, 1)

        self.player_pos[0] = max(130, min(self.player_pos[0], self.exit_pos[0] + 100))
        self.player_pos[1] = max(130, min(self.player_pos[1], self.exit_pos[1] + 300))
        
        player = self.player.getRect().move(self.player_pos)
        exit = self.exit.getRect().move(self.exit_pos)
        if player.colliderect(exit):
            return True

    def draw(self, screen):
        super().draw(screen)

        for crowd, pos in self.crowds:
            crowd.blit(screen, pos)
        
        self.exit.blit(screen, self.exit_pos)
        self.player.blit(screen, self.player_pos)