import pygame
import pyganim

class Collidable:
    def __init__(self, anim, pos):
        self.anim = anim.getCopy()
        self.anim.play()
        self.pos = pos[:]

    def has_collide(self, obj):
        """ Returns True if collides """
        rect1 = self.anim.getRect()
        rect2 = obj.anim.getRect()
        
        rect1.move_ip(self.pos)
        rect2.move_ip(obj.pos)
        
        return rect1.colliderect(rect2):

    def update(self, tick):
        pass

    def draw(self, screen):
        self.anim.blit(screen, self.pos)


class Projectile(Collidable):
    def __init__(self, original_anim, pos, facing, speed, resolution):
        self.anim = original_anim.getCopy()
        self.anim.play()
        self.pos = pos[:]
        self.facing = facing[:]
        self.speed = speed
        self.resolution = resolution

        if self.facing == [+1, 0]:
            self.anim.rotate(-90)
        elif self.facing == [-1, 0]:
            self.anim.rotate(90)
        elif self.facing == [0, 1]:
            self.anim.rotate(180)

    def update(self, tick):
        self.pos[0] += self.facing[0] * self.speed
        self.pos[1] += self.facing[1] * self.speed
        if (-100 < self.pos[0] > self.resolution[0] or
            -100 < self.pos[1] > self.resolution[1]):
            return True


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
        self.resolution = resolution

        self.button = pyganim.PygAnimation([("images/button1.png", 700),
                                            ("images/button 2.png", 600)])
        self.button.scale2x()
        self.button.play()

    def _center_text(self, pos):
        pos.centerx = self.resolution[0] / 2
        pos.centery = 50
        return pos

    def update(self, input, tick):
        """ if update returns True, change stage """
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