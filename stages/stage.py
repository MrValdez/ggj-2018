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
        self.texts = [Text("Hello World", (255, 255, 255), self._center_text)]
        self.resolution = resolution

        example = Text("h", (0, 0, 0), lambda x: x)
        self.texts.append(example)

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
        self._draw_texts(screen)

    def _draw_texts(self, screen):
        for text in self.texts:
            text.draw(screen)