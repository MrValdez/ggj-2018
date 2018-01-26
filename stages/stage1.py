import pyganim
from .stage import Stage, Text

class Stage1(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)

        self.texts = [Text("Remove interference", (255, 255, 255), self._center_text)]

        self.sprite = pyganim.PygAnimation([("images/spam.png", 10)])
        self.sprite.play()
        self.sprite_size = self.sprite.getMaxSize()
        
        self.pos = [0, 0]

    def update(self, input, tick):
        speed = 10
        if input.left:  self.pos[0] -= speed
        if input.right: self.pos[0] += speed
        if input.up:    self.pos[1] -= speed
        if input.down:  self.pos[1] += speed
        
        self.pos[0] = max(0, min(self.pos[0], self.resolution[0] - self.sprite_size[0]))
        self.pos[1] = max(0, min(self.pos[1], self.resolution[1] - self.sprite_size[1]))

    def draw(self, screen):
        screen.fill([255,128,128])
        super().draw(screen)

        self.sprite.blit(screen, self.pos)
        self.button.blit(screen, self.pos)