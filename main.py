import pygame
from stages.stage import Stage
from stages.stage_example import StageExample
from stages.stage1 import Stage1
from input import Input

pygame.init()
resolution = [640, 480]
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