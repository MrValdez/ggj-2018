from .stage import Stage

class Stage1(Stage):
    def draw(self, screen):
        screen.fill([255,128,128])
        super().draw(screen)