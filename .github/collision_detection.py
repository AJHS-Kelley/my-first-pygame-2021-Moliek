# PyGame Collision Dtection Pratice, Ryan Kelley, January 04, 2022, 1:49, v0.2

import pygame, sys, random
from pygame.locals import *

# Setup PyGame
pygame.int()
mainClock= pygame.time.Clock()

# Setup the PyGame window
WINDOWWIDTH = 400
WINDOWNFIGHT= 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDIWHEIGHT), 0, 32)
pygame.display.set_caption('Collision Detection 2022')