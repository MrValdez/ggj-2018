import pygame
import random
from .stage import Stage, Text

class Stage_transition(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)

        self.texts = [Text("You won!", (255, 255, 255), self._center_text)]

        self.lines = []

        for i in range(500):
            x = random.randint(int(resolution[0] * 0.25), resolution[0])
            y = random.randint(0, resolution[1])
            length = random.randint(400, 3000)
            start_pos = [x, y]
            end_pos = [x + length, y]
            color = (255, 128, 128)
            width = random.randint(1, 30)
            self.lines.append((color, start_pos, end_pos, width))

        self.timer = 0

    def update(self, input, tick):
        self.timer += tick
        if self.timer > 1000:
            return True

    def draw(self, screen):
        super().draw(screen)
        screen.fill([0, 0, 0])
        
        speed = 100
        for color, start_pos, end_pos, width in self.lines:
            pygame.draw.line(screen, color, start_pos, end_pos, width)
            start_pos[0] -= speed + random.randint(-10, 10)
            end_pos[0] -= speed  + random.randint(-10, 10)