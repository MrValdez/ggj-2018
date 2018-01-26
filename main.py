import pygame

pygame.init()
resolution = [640, 480]
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

GameIsRunning = True

class Input:
    def __init__(self):
        self.left = self.right = self.up = self.down = False
        self.button1 = self.button2 = False
        self.prev_keys = pygame.key.get_pressed()

    def update(self):
        self._update_keyboard()
        self._update_joystick()

    def _update_keyboard(self):
        keys = pygame.key.get_pressed()

        def check_key(key):
            return keys[key] and not self.prev_keys[key]

        self.left = check_key(pygame.K_LEFT)
        self.right = check_key(pygame.K_RIGHT)
        self.up = check_key(pygame.K_UP)
        self.down = check_key(pygame.K_DOWN)
        self.button1 = check_key(pygame.K_q)
        self.button2 = check_key(pygame.K_w)

        self.prev_keys = keys

    def _update_joystick(self):
        pass

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

input = Input()
stage1 = Stage()

while GameIsRunning:
    pygame.display.flip()
    tick = clock.tick(60)
    screen.fill([0, 0, 0])

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                GameIsRunning = False

        if event.type == pygame.QUIT:
            GameIsRunning = False

    if not GameIsRunning:
        pygame.quit()
        break

    input.update()
    stage1.update(input)

    stage1.draw(screen)