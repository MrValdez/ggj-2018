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
        
        return rect1.colliderect(rect2)

    def update(self, input, tick):
        pass

    def draw(self, screen):
        self.anim.blit(screen, self.pos)


class Avatar(Collidable):
    def __init__(self, speed, pos, facing, animation_files = None):
        if animation_files is None:
            animation_files = [("images/button1.png", 200),
                               ("images/button 2.png", 200)]

        self.avatar_original = pyganim.PygAnimation(animation_files)
        self.avatar_up = self.avatar_original.getCopy()
        self.avatar_down = self.avatar_original.getCopy()
        self.avatar_down.rotate(180)
        self.avatar_left = self.avatar_original.getCopy()
        self.avatar_left.rotate(90)
        self.avatar_right = self.avatar_original.getCopy()
        self.avatar_right.rotate(-90)
        self.avatar_up.play()
        self.avatar_down.play()
        self.avatar_left.play()
        self.avatar_right.play()

        self.anim = self.avatar_up
        self.anim.play()
        self.pos = pos[:]
        self.facing = facing[:]
        self.speed = speed
        
    def update(self, input, tick):
        speed = self.speed
        
        if input.left_hold:
            self.anim = self.avatar_left
            self.pos[0] -= speed
            self.facing = [-1, 0]
        if input.right_hold:
            self.anim = self.avatar_right
            self.pos[0] += speed
            self.facing = [+1, 0]
        if input.down_hold:
            self.anim = self.avatar_down
            self.pos[1] += speed
            self.facing = [0, +1]
        if input.up_hold:
            self.anim = self.avatar_up
            self.pos[1] -= speed
            self.facing = [0, -1]


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

    def update(self, input, tick):
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

class UpdatingText:
    def __init__(self, text, color, pos, size=30, font_name = None):
        self.text = text
        self.color = color
        self.pos = pos
        self.font = pygame.font.Font(font_name, size)

    def update(self, input, tick):
        pass

    def draw(self, screen):
        text = self.font.render(self.text, True, self.color)

        screen.blit(text, self.pos)
        return text.get_rect()

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

    def _iterate_all(self, objects, func, kwargs):
        for obj in objects:
            if type(obj) is list:
                self._iterate_all(obj, func, kwargs)
            else:
                getattr(obj, func)(**kwargs)
                
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