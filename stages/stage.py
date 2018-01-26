import pygame

class Text:
    def __init__(self, text, color, update_pos, font_name = None):
        self.text = text
        self.color = color
        self.font = pygame.font.Font(font_name, 30)
        self.update_pos = update_pos

    def draw(self, screen):
        text = self.font.render(self.text, True, self.color)
        pos = self.update_pos(text)

        screen.blit(text, pos)

class Stage:
    def __init__(self, resolution):
        def send_to_center(text):
            pos = text.get_rect()
            pos.centerx = self.resolution[0] / 2
            pos.centery = 50
            return pos

        self.texts = [Text("Hello World", (255, 255, 255), send_to_center)]
        self.resolution = resolution

    def update(self, input):
        if input.left: print("left")
        if input.right: print("right")
        if input.up: print("up")
        if input.down: print("down")
        if input.button1: print("button1")
        if input.button2: print("button2")

    def draw(self, screen):
        self._draw_texts(screen)

    def _draw_texts(self, screen):
        for text in self.texts:
            text.draw(screen)