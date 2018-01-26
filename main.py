import pygame
from stage import Stage
from input import Input

pygame.init()
resolution = [640, 480]
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

GameIsRunning = True
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