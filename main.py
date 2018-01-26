import os
import pygame
from stages.stage import Stage
from stages.stage_example import StageExample
from stages.stage1 import Stage1
from input import Input

#os.environ['SDL_VIDEO_WINDOW_POS'] = "1, 0"
os.environ['SDL_VIDEO_WINDOW_POS'] = "100, 0"     #debug
resolution = [1024, 768]

pygame.init()
pygame.display.set_caption("32 bits delivery")
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

GameIsRunning = True
input = Input()
stages = [
    StageExample(resolution),
    Stage1(resolution),
    ]

currentStage = stages[0]
currentStage = stages[1]

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
    currentStage.update(input)

    currentStage.draw(screen)