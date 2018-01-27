import os
import pygame

from input import Input

from stages.stage import Stage
from stages.stage_example import StageExample
from stages.stage1 import Stage1
from stages.stage2 import Stage2
from stages.stage3 import Stage3
from stages.stage4 import Stage4
from stages.stage5 import Stage5
from stages.stage6 import Stage6
from stages.stage7 import Stage7
from stages.stage8 import Stage8
from stages.stage9 import Stage9
from stages.stage10 import Stage10
from stages.stage11 import Stage11
from stages.stage12 import Stage12
from stages.stage13 import Stage13
from stages.stage14 import Stage14
from stages.stage15 import Stage15
from stages.stage16 import Stage16
from stages.stage17 import Stage17
from stages.stage_end import Stage_end
from stages.stage_transition import Stage_transition

#os.environ['SDL_VIDEO_WINDOW_POS'] = "1, 0"
os.environ['SDL_VIDEO_WINDOW_POS'] = "100, 0"     #debug
resolution = [800, 600]

pygame.init()
pygame.display.set_caption("32 bits delivery")
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

GameIsRunning = True
input = Input()
stages = [
#    StageExample(resolution),
#    Stage1(resolution),
    Stage17(resolution),        # Buy coffee
    Stage16(resolution),        # Poop
    Stage15(resolution),        # Clap to transmit noise
    Stage14(resolution),        # Find the strongest transmission
    Stage13(resolution),        # Love transmission!
    Stage12(resolution),        # Charge!
    Stage11(resolution),        # Space Defender
    Stage10(resolution),        # Ninja Turtle Van
    Stage9(resolution),         # Dancing
    Stage8(resolution),         # Two auth factor
    Stage7(resolution),         # USB connection
    Stage6(resolution),         # energize with coffee
    Stage5(resolution),         # crowd surfing game
    Stage4(resolution),         # punching game
    Stage3(resolution),         # chrome game
    Stage2(resolution),         # have you tried turning it on and off again?
    Stage_end(resolution),
    ]

# add transtitions
updated_stages = []
for stage in stages:
    updated_stages.append(stage)
    updated_stages.append(Stage_transition(resolution))
stages = updated_stages

currentStage = 0
#currentStage = -2

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

    complete = stages[currentStage].update(input, tick)
    if complete:
        currentStage = (currentStage + 1) % len(stages)
        stages[currentStage].__init__(resolution)
        
    
    stages[currentStage].draw(screen)