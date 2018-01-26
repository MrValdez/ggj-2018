from .stage import Stage, Text

class Stage1(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)

        self.texts = [Text("Remove interference", (255, 255, 255), self._center_text)]

    def draw(self, screen):
        super().draw(screen)