import pygame, sys
from pygame.locals import *
import maze

pygame.init()
screen = pygame.display.set_mode((600,600))

MAZE= maze.Maze(120,120)

print(MAZE)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)
        else:
            pass
