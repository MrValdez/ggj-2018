import pygame

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
