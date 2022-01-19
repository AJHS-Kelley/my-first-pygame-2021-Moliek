# PyGame Collision Dtection Pratice, Ryan Kelley, January 04, 2022, 1:36, v0.5

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

# Setup colors.
BLACK = (0, 0, 0)
GREEN =(0, 255, 0)
WHITE = (255, 255, 255)

# Setup the player and food data structres.
foodCountyer = 0
NEWFOOD = 40
FOODSIZE = 20
player = pygame.Rect(300,100, 50, 50)
foods = []

for i in range(20):
    foods.append(pygame.Rect(random.randict(0, WINDOWWIDTH - FOODSIZE), random.randict(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

# Movement Variables
moveLeft = False
moveRight = False 
moveUp = False
moveDown = False

MOVESPEEDF = 6