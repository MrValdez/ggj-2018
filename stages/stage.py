class Stage:
    def update(self, input):
        if input.left: print("left")
        if input.right: print("right")
        if input.up: print("up")
        if input.down: print("down")
        if input.button1: print("button1")
        if input.button2: print("button2")

    def draw(self, screen):
        pass