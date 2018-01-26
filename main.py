import pygame

pygame.init()
resolution = [640, 480]
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

GameIsRunning = True

while GameIsRunning:
    screen.fill([0, 0, 0])

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                GameIsRunning = False
                pygame.quit()

        if event.type == pygame.QUIT:
            GameIsRunning = False

    clock.tick(60)
    pygame.display.flip()
    
