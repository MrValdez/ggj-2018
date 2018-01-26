import pygame

class Stage:
    def __init__(self, resolution):
        self.instruction_text = "Hello World"
        self.font = pygame.font.Font(None, 30)
        self.font.set_bold(True)
        self.resolution = resolution

    def update(self, input):
        if input.left: print("left")
        if input.right: print("right")
        if input.up: print("up")
        if input.down: print("down")
        if input.button1: print("button1")
        if input.button2: print("button2")

    def draw(self, screen):
        self._draw_instruction(screen)

    def _draw_instruction(self, screen):
        text = self.font.render(self.instruction_text, True, (255, 255, 255))

        pos = text.get_rect()
        pos.centerx = (self.resolution[0] / 2)
        pos.centery = (self.resolution[1] / 2)
        screen.blit(text, pos)
