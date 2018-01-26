import pygame

class Text:
    def __init__(self, text, color, update_pos, font_name = None):
        self.text = text
        self.color = color
        self.font = pygame.font.Font(font_name, 30)
        self.update_pos = update_pos

    def draw(self, screen):
        text = self.font.render(self.text, True, self.color)
        pos = text.get_rect()
        pos = self.update_pos(pos)

        screen.blit(text, pos)

class Stage:
    def __init__(self, resolution):
        self.resolution = resolution

    def _center_text(self, pos):
        pos.centerx = self.resolution[0] / 2
        pos.centery = 50
        return pos

    def update(self, input):
        if input.left: print("left")
        if input.right: print("right")
        if input.up: print("up")
        if input.down: print("down")
        if input.button1: print("button1")
        if input.button2: print("button2")

    def draw(self, screen):
        pass