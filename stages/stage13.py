# Send the love letter

import math
import pygame
import pyganim
import random
from .stage import Stage, Text, Projectile, Collidable, Avatar
from input import Input

class Player(Avatar):
    def __init__(self, speed, pos, animation_files):
        Avatar.__init__(self, speed=speed, pos=pos, facing=[1, 0], animation_files=animation_files)

    def update(self, input, tick):
        speed = self.speed
        if input.left_hold:
            self.pos[0] -= speed
        if input.right_hold:
            self.pos[0] += speed
        if input.up_hold:
            self.pos[1] -= speed
        if input.down_hold:
            self.pos[1] += speed


class Obstacle(Collidable):
    def __init__(self, pos):
        anim = pyganim.PygAnimation([("images/obstacle.png", 200)])
        anim.play()

        Collidable.__init__(self, anim, pos)


class Stage13(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)
        self.texts = [Text("Transmit the love letter", (255, 255, 255), self._center_text)]

        self.reset()
        
    def reset(self):
        pos1 = [0, 0]
        pos2 = [500, 550]
        speed = 3
        self.avatar1 = Player(speed=speed, pos=pos1, animation_files = [("images/maze_player.png", 200)])
        self.avatar2 = Player(speed=-speed, pos=pos2, animation_files = [("images/maze_player2.png", 200)])
        
        self.maze = []
        self.objects = [self.avatar1, self.avatar2, self.maze]
        
        
        map = """
xooxxxxxoxxxxxoxx
xxoxxooooxxxxooxx
xxoxxoxxoxxooooxx
xooxxoxxooooxxoxx
xoxxxoxoxxxxxooxx
xooxxoxxoxxxxoxxx
xxooooxxoxxxxooxx
xxxxxxxxxxxxxoxxx""".strip()
        pos_y = 100
        for line in map.split("\n"):
            tiles_per_line = len(line)
            pos_x = 0
            max_line_height = 0
            for tile in line:
                if tile == "x":
                    obstacle = Obstacle([pos_x, pos_y])
                    self.maze.append(obstacle)
                size = obstacle.anim.getRect().size
                pos_x += size[0]
                max_line_height = max(max_line_height, size[1])
            pos_y += max_line_height
            

    def update(self, input, tick):
        for avatar in [self.avatar1, self.avatar2]:
#        for avatar in [self.avatar1, ]:
            prev_pos = avatar.pos[:]
            avatar.update(input, tick)
            
            avatar.pos[0] = max(10, min(self.resolution[0] - avatar.anim.getRect().width, avatar.pos[0]))
            avatar.pos[1] = max(10, min(self.resolution[1] - avatar.anim.getRect().height, avatar.pos[1]))
            
            for obstacle in self.maze:
                if avatar.has_collide(obstacle):
                    avatar.pos = prev_pos
                    rect_avatar = avatar.anim.getRect()
                    rect_obstacle = obstacle.anim.getRect()
                    rect_avatar.move_ip(avatar.pos)
                    rect_obstacle.move_ip(obstacle.pos)
                    
                    
                    
                    #if rect_avatar[1] < rect_obstacle.center[1] - 10:
                    #    avatar.pos[1] = rect_obstacle.y - rect_avatar.height
#                    else:
#                        avatar.pos[1] = rect_obstacle.bottom + abs(avatar.speed)
                        
                    break
        if input.button:
            self.reset()

        if self.avatar1.has_collide(self.avatar2):
            return True

    def draw(self, screen):
        super().draw(screen)

        self._iterate_all(self.objects, "draw", {"screen": screen})