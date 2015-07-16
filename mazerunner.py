import pygame, sys
from pygame.locals import *
import maze

pygame.init()
screen = pygame.display.set_mode((600,600))


MAZE= maze.matriz
print(len(MAZE[0]))
for x in MAZE:
    pass
    print(x)   

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)
        else:
            pass
