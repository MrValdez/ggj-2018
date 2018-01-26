from .stage import Stage, Text

class Stage1(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)

        self.texts.append(Text("h", (0, 0, 0), lambda x: x.get_rect()))

    def draw(self, screen):
        screen.fill([255,128,128])
        super().draw(screen)